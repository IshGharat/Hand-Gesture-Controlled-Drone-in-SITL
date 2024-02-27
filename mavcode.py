from pymavlink import mavutil
from module import*
import time

the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))



ALTITUDE=10

@delay(1)
def Get_Altitude():
	msg=the_connection.recv_match(type="LOCAL_POSITION_NED",blocking=True)
	return round(-1*msg.z,2)

@delay(2)
def Get_Coordinates():
	msg=the_connection.recv_match(type="GLOBAL_POSITION_INT",blocking=True)
	print(round(msg.relative_alt/1000,2))
	return [msg.lat/(10**7),msg.lon/(10**7)]

@delay(1)
def isArmed():
	msg=the_connection.recv_match(type="HEARTBEAT",blocking=True)
	if msg is not None:
	    base_mode = msg.base_mode
	    # The armed flag is bit 7 in the base_mode field.
	    # If bit 7 is set (1), the drone is armed. If it's clear (0), the drone is disarmed.
	    armed = (base_mode >> 7) & 1
	    return armed


def Drone_Arm():
	the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0,1,0,0,0,0,0,0)
	return True

def Drone_Disarm():
	the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0,0,0,0,0,0,0,0)
	return False

def Drone_TakeOff():
	speak("TakeOff")
	the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF	, 0,0,0,0,0,0,0,ALTITUDE)
	
def Drone_RTL():
	speak("RTL")
	the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10,the_connection.target_system,the_connection.target_component,mavutil.mavlink.MAV_FRAME_LOCAL_NED,3576,0,0,0,0,0,0,0,0,0,0,10))
	
def Waypoint1():
	speak("WP1")
	the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10,the_connection.target_system,the_connection.target_component,mavutil.mavlink.MAV_FRAME_LOCAL_NED,3576,50,25,-25,0,0,0,0,0,0,0,10))


def Waypoint2():
	speak("WP2")
	the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10,the_connection.target_system,the_connection.target_component,mavutil.mavlink.MAV_FRAME_LOCAL_NED,3576,-80,-35,-10,0,0,0,0,0,0,0,10))


while True:
    Get_Coordinates()
    time.sleep(2)
    print(Get_Altitude())
    time.sleep(2)
# Drone_Arm()
# Drone_TakeOff()

# print(msg)
# #print(msg["z"])
# time.sleep(10)

# Waypoint1()


