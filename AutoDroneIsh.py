#!/bin/python
import cv2
import mediapipe as mp
import time
from google.protobuf.json_format import MessageToDict

from mavcode import *

ARM=False

time.sleep(2.0)

mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands

def get_label(results):
    for i in results.multi_handedness:				
        # Return whether it is Right or Left Hand
        label = MessageToDict(i)['classification'][0]['label']
    return label

tipIds=[4,8,12,16,20]

video=cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5,
               min_tracking_confidence=0.5,max_num_hands=1) as hands:
    while True:
        ret,image=video.read()
        image = cv2.flip(image, flipCode = 1)

        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList=[]
        if results.multi_hand_landmarks:
            for num,hand in enumerate(results.multi_hand_landmarks):
                myHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)
                    lmList.append([id,cx,cy])
                    mp_draw.draw_landmarks(image, hand, mp_hand.HAND_CONNECTIONS)

                if get_label(results):
                    hand_label= get_label(results)
                    #print(hand_label)

        
        x=Get_Altitude()
            # if Get_Altitude()<=1:
        y=isArmed()

        coordinates=Get_Coordinates()

        if coordinates!=None:
            lat=str(coordinates[0])
            lon=str(coordinates[1])

        if x!=None:
            ALTITUDE=str(x)

        if y!=None:
            ARM=y


        if ARM==1:   #YOu were here
            cv2.putText(image, "ARMED",
							(20, 50),
							cv2.FONT_HERSHEY_COMPLEX,
							0.9, (0, 255, 0), 2)

            cv2.putText(image, "ALTITUDE: "+ALTITUDE+" m",
                            (400, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.7, (255, 255, 255), 2)
            cv2.putText(image, "LATITUDE: "+lat,
                            (350, 100),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.7, (255, 255, 255), 2)
            cv2.putText(image, "LONGITUDE: "+lon,
                            (350, 150),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.7, (255, 255, 255), 2)
        else:
            cv2.putText(image, "DISARMED",
                            (20, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.9, (0, 0, 255), 2)
                

        fingers=[]
        if len(lmList)!=0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total=fingers.count(1)

            

            #Right Index, Pinky and Thumb 

            if not ARM and hand_label=="Right" and lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2] :
                ARM=Drone_Arm()
                print("Arm")

            #Left Index, Pinky and Thumb 
            
            if ARM and hand_label=="Left" and lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2] :
                ARM=Drone_Disarm()
                print("Disarm")

            #Right Index

            if ARM   and hand_label=="Right" and lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2] :
                Drone_TakeOff()  #Takeoff
                print("Take Off")

            #Left Index and Middle

            if ARM  and hand_label=="Left" and lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2] :
                Drone_RTL()
                print("RTL")    

            #Right Middle and Ring          

            if ARM and hand_label=="Right" and lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] and lmList[tipIds[1]][2] > lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2] :
                Waypoint1()
                print("Waypoint 1")

            #Left Middle and Ring
           
            if ARM and hand_label=="Left" and lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] and lmList[tipIds[1]][2] > lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] < lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2] :
                Waypoint2()
                print("Waypoint 2")
    
           
              
        cv2.imshow("Frame",image)
        k=cv2.waitKey(1)
        if k==27:
            break
video.release()
cv2.destroyAllWindows()

