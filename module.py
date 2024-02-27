import time
import os

def delay(seconds):
    def decorator(func):
        last_execution_time = 0

        def wrapper(*args, **kwargs):
            nonlocal last_execution_time
            current_time = time.time()

            if current_time - last_execution_time >= seconds:
                result = func(*args, **kwargs)
                last_execution_time = current_time
                return result
            else:
                print(f"Function '{func.__name__}' is on cooldown. Try again later.")

        return wrapper

    return decorator


@delay(5)
def speak(a):
    try:
        return
    finally:
        os.system("play ./Audio/"+a+".mp3"+ " tempo 1.5")

# speak("WP2")

# a=5

# @delay(5)
# def function():
#     global a
#     a+=1
#     return a


# while True:
#     A=function()
#     if A!=None:
        
#         print(A)
#     time.sleep(1)