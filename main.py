#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog

import _thread
import time

ev3 = EV3Brick()

# Motoren definieren
back_left_motor = Motor(Port.B , Direction.COUNTERCLOCKWISE)
back_right_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
front_left_motor = Motor(Port.C,Direction.COUNTERCLOCKWISE)
front_right_motor = Motor(Port.D,Direction.COUNTERCLOCKWISE)

def move_motor(motor, angle_deg, speed_percent):
    motor.run_target(speed_percent, angle_deg)
    motor.hold()

def init_motor(motor):
    motor.run_until_stalled(100, then=Stop.COAST, duty_limit=100)
    motor.reset_angle(0)
    motor.hold()

# Motorinitialisierung in Threads
_thread.start_new_thread(init_motor, (back_left_motor,))
_thread.start_new_thread(init_motor, (back_right_motor,))
_thread.start_new_thread(init_motor, (front_left_motor,))
_thread.start_new_thread(init_motor, (front_right_motor,))

# Warten, bis alle Motoren initiiert sind (einfache Pause)
time.sleep(2)

# Bewegungen in Threads starten
_thread.start_new_thread(move_motor, (back_left_motor, -130, 100))
_thread.start_new_thread(move_motor, (back_right_motor, -130, 100))
_thread.start_new_thread(move_motor, (front_left_motor, -70, 100))
_thread.start_new_thread(move_motor, (front_right_motor, -70, 100))

# Hauptthread warten lassen, um Zeit zu geben, dass Threads ihre Aufgaben erledigen
time.sleep(2)
back_left_motor.reset_angle(0)
back_right_motor.reset_angle(0)
front_left_motor.reset_angle(0)
front_right_motor.reset_angle(0)
time.sleep(1)
for i in range(4):
    for j in range(2):
        dir=15
        if j==1:
            dir=-15
        _thread.start_new_thread(move_motor, (back_left_motor, dir, 100))
        _thread.start_new_thread(move_motor, (front_right_motor, dir, 100))    
        time.sleep(0.5)
        _thread.start_new_thread(move_motor, (back_right_motor, -dir, 100))
        _thread.start_new_thread(move_motor, (front_left_motor, -dir, 100))
        time.sleep(0.5)
    