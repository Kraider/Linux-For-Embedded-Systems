import time
import socket
import threading
from gpiozero import CamJamKitRobot
from gpiozero import DistanceSensor

def run_func(robot,sensor,motorRight,motorLeft):
        global flag
        while flag:
             sensorOut = sensor.distance * 100
             if sensorOut > 15:
                robot.value = motorRight
                time.sleep(0.2)
             elif sensorOut < 15:
                robot.value = motorLeft
                time.sleep(0.2)
        robot.value = (0,0)


def main():
        global flag
        flag = 0
        robot = CamJamKitRobot()
        sensor = DistanceSensor(echo=18, trigger=17)
        # Set speed
        motorspeed = 0.3

        motorForward = (motorspeed, motorspeed)
        motorBackward = (-motorspeed, -motorspeed)
        motorLeft = (0.22, 0.17)
        motorRight = (0.17, 0.22)

        HOST = '192.168.99.26'
        PORT = 8080
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
                s.bind((HOST, PORT))
        except socket.error:
                print ('Bind failed')

        s.listen(1)
        print ("Socket awaiting messages")

        try:
                while 1:
                        (conn, addr) = s.accept()
                        data=conn.recv(1024)
                        data=data.decode('utf-8')
                        if (data == 'start'):
                                flag = 1
                                x = threading.Thread(target=run_func, args=(robot,sensor,motorRight,motorLeft,))
                                x.start()
                                reply = "Started"
                        elif (data == 'stop'):
                                flag = 0
                                x.join()
                                reply = 'Stopped'
                        elif (data == 'getmotors'):
                                reply = str(robot.value)
                        elif (data == 'getdist'):
                                reply = str(sensor.distance * 100)
                        else:
                                reply = ("Unknown command")

#                       while flag:
#                               sensorOut = sensor.distance * 100
#                               if sensorOut > 15:
#                                       robot.value = motorRight
#                                       time.sleep(0.2)
#                               elif sensorOut < 15:
#                                       robot.value = motorLeft
#                                       time.sleep(0.2)
#                       elif (flag == 0):
#                               robot.value = (0,0)
                        conn.sendall(str.encode(reply))
                conn.close()
        except KeyboardInterrupt:
                print "Shut down"


if __name__ == "__main__":
        main()
