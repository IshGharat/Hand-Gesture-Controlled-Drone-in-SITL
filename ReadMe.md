# Hand Gesture Controlled Drone in SITL

## Introduction
This project demonstrates a hand gesture controlled drone system implemented in a Software-in-the-Loop (SITL) environment. The script utilizes the Mediapipe library for hand tracking and recognition, along with the Mavlink-based MAVCode library for interfacing with a simulated drone.

## Requirements
- Python 3.x
- OpenCV
- Mediapipe
- Google Protobuf
- Mission Planner
- pymavlink
  
Install the required dependencies using:
```bash
pip install opencv-python mediapipe mavcode protobuf
```

## How to Run (Refer to the video)
1. Ensure that you have all the required dependencies installed.
2. Run the script using:
```bash
python AutoDroneIsh.py
```
3. The webcam feed will open, and the script will start detecting hand gestures.

## Hand Gestures and Drone Control
Refer the video for gestures

## Drone Status Display
- The status of the drone (ARMED/DISARMED) and altitude information is displayed on the OpenCV window.

## Notes
- Ensure that the MAVLink connection is properly configured for SITL.
- The script includes a sleep duration at the beginning to allow time for the system to stabilize.

## Acknowledgments
- [Mediapipe](https://mediapipe.dev/)
- [MAVCode](https://github.com/ArduPilot/MAVSDK-Python)

## License
This project is licensed under the [MIT License](LICENSE).

