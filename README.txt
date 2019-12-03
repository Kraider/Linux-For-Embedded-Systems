# Pibot

A robot that can drive along a wall was made with the use of raspberry pi zero and CamJam EduKit 3 Robotics.

## Setup

Step 1: Create hotspot collect pibot without password

Step 2: Connect to Pi Zero
Ssh to the pi with IP address 192.168.99.26
ssh pi@192.168.99.26
password=raspberry

Step 3: run test.py
python /etc/init.d/test.py

### Commands

Start
echo -n start | socat stdio tcp:192.168.99.26:8080

Stop
echo -n stop | socat stdio tcp:192.168.99.26:8080

Get distance to wall
echo -n getdist | socat stdio tcp:192.168.99.26:8080

Get velocity of the motors
echo -n getmotors | socat stdio tcp:192.168.99.26:8080