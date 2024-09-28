#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math
import threading

ev3 = EV3Brick()

# Positive Drehungen sollen das Bein nach vorne bewegen
back_left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1, 1])
back_right_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE, [1, 1])
front_left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [1, 1])
front_right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [1, 1])

def motor_init(motor, speed_percent, duty_limit):
    angle1 = motor.run_until_stalled(speed_percent, then=Stop.COAST, duty_limit=duty_limit)
    motor.reset_angle(0)
    motor.hold()

def move_motor(motor, angle_deg, speed_percent):
    motor.run_target(speed_percent, angle_deg)
    motor.hold()

# Threads für die Motorinitialisierung
init_threads = [
    threading.Thread(target=motor_init, args=(back_left_motor, 100, 100)),
    threading.Thread(target=motor_init, args=(back_right_motor, 100, 100)),
    threading.Thread(target=motor_init, args=(front_left_motor, 100, 100)),
    threading.Thread(target=motor_init, args=(front_right_motor, 100, 100)),
]

# Threads für die Motorbewegungen
move_threads = [
    threading.Thread(target=move_motor, args=(back_left_motor, -130, 100)),
    threading.Thread(target=move_motor, args=(back_right_motor, -130, 100)),
    threading.Thread(target=move_motor, args=(front_left_motor, -70, 100)),
    threading.Thread(target=move_motor, args=(front_right_motor, -70, 100)),
]

# Starte die Initialisierung
for thread in init_threads:
    thread.start()

# Warte, bis alle Initialisierungs-Threads beendet sind
for thread in init_threads:
    thread.join()

# Starte die Bewegungen
for thread in move_threads:
    thread.start()

# Warte, bis alle Bewegungs-Threads beendet sind
for thread in move_threads:
    thread.join()