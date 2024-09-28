#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math

ev3 = EV3Brick()
back_left_motor = Motor(Port.B, Direction.CLOCKWISE, [24, 60])
back_right_motor = Motor(Port.A, Direction.CLOCKWISE, [24, 60])
front_left_motor = Motor(Port.C, Direction.CLOCKWISE, [24, 60])
front_right_motor = Motor(Port.D, Direction.CLOCKWISE, [24, 60])

