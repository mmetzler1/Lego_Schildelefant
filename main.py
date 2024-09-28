#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math

ev3 = EV3Brick()

#positive Drehungen sollen das Bein nach vorne bewegen

back_left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1, 1])
back_right_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE, [1, 1])
front_left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [1, 1])
front_right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [1, 1])

def motor_init(motor, speed_percent, duty_limit):
    angle1= motor.run_until_stalled(speed_percent, then=Stop.COAST, duty_limit = duty_limit)
    motor.reset_angle(0)
    motor.hold()

def move_motor(motor, angle_deg, speed_percent):
    motor.run_target(speed_percent, angle_deg)
    motor.hold()

motor_init(back_left_motor, 100, 100)
motor_init(back_right_motor, 100, 100)
motor_init(front_left_motor, 100, 100)
motor_init(front_right_motor, 100, 100)

# bewegen eines Beins
move_motor(back_left_motor,-130,100)
move_motor(back_right_motor,-130,100)
move_motor(front_left_motor,-70,100)
move_motor(front_right_motor,-70,100)