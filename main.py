#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
import _thread
import time

ev3 = EV3Brick()

# Motoren definieren
back_left_motor = Motor(Port.B)
back_right_motor = Motor(Port.A)
front_left_motor = Motor(Port.C)
front_right_motor = Motor(Port.D)

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
time.sleep(3)