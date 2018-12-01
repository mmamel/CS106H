#!/usr/bin/env python3
#import all the nessasary parts for the Lego Mindstorm
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
from ev3dev2.motor import LargeMotor, OUTPUT_C
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.sensor.lego import GyroSensor, ColorSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from time import sleep
import math
import time

#from ev3dev.ev3 import *
#m1 and m2 are driving motors
#m3 is hopper motor
#c1 is color sensor for container
#c2 is color sensor for pills
#u3 is Ultrasnoic sensor for distance
#g4 is gyro
#Color sensor will return 3 for green and 5 for red. Needs to be 8 mm away
#Assign slots to each component
#m1 = LargeMotor(OUTPUT_A)
#m2 = LargeMotor(OUTPUT_B)
m3 = LargeMotor(OUTPUT_C)
#tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
c1 = ColorSensor(INPUT_1)
c2 = ColorSensor(INPUT_2)
us = UltrasonicSensor()
gs = GyroSensor()
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

def Rotate(angle):
    #reset gyro
    angle_degrees = math.degrees(angle)
    gs.mode = 'GYRO-RATE';
    gs.mode = 'GYRO-ANG';
    bool = True;
    tank_drive.on(left_speed=-10,right_speed=10)

    while bool == True:
        time.sleep(.1)

        current_degrees=gs.angle;
        print("this is current degrees",current_degrees)
        if current_angle > angle_degrees +1 or current_angle < angle_degrees -1:
            bool = False;
            #turn in place

    tank_drive.off()
def RotateBetter():
    current_angle = 0
    gs.mode = 'GYRO-RATE';
    gs.mode = 'GYRO-ANG';
    tank_drive.on(left_speed=-10,right_speed=10)
    while current_angle < 40:

        time.sleep(.115)
        current_angle=gs.angle

    tank_drive.off(brake=True)

def Rotate_until_clock(distance):
    us.mode ='US-DIST-CM'
    bool =True;
    while bool == True:
        time.sleep(.115)
        tank_drive.on(left_speed=-8,right_speed=8)
        measurement= us.distance_centimeters_continuous;
        print("this is rotate until measurement", measurement)
        if measurement > distance -1 and measurement < distance +1:
            tank_drive.off(brake=True)
            bool = False;
def Rotate_until_counter(distance):
    us.mode ='US-DIST-CM'
    bool =True;
    while bool == True:
        time.sleep(.115)
        tank_drive.on(left_speed=8,right_speed=-8)
        measurement= us.distance_centimeters_continuous;
        print("this is rotate until measurement", measurement)
        if measurement > distance -1 and measurement < distance +1:
            tank_drive.off(brake=True)
            bool = False;
def move_until():
    bool = True
    us.mode ='US-DIST-CM'
    tank_drive.on(left_speed=10,right_speed=10)

    while bool == True:
        time.sleep(.1)

        distance = us.distance_centimeters_continuous
        print("this is move until: ", distance)
        if distance < 5:
            tank_drive.off()
            bool = False

def Distance_Array():
    #reset gyro
    gs.mode = 'GYRO-RATE';
    gs.mode = 'GYRO-ANG';
    us.mode ='US-DIST-CM'
    array_distance=[];
    array_angle=[];

    current_angle=0;
    tank_drive.on(left_speed=-5,right_speed=5)
    while current_angle < 180:

        time.sleep(.115)
        current_angle=gs.angle
        distance= us.distance_centimeters_continuous;

        array_distance.append(distance);
    tank_drive.off(brake=True)

    return array_distance
def Reset(distance):
    bool =True;

    while bool == True:
        time.sleep(.1)
        measurement= us.distance_centimeters_continuous;
        tank_drive.on(left_speed=-5,right_speed=-5)
        print("this is measurement:", measurement)

        if measurement > distance -1 and measurement < distance +1:
            #this is to offset stopping too early
            time.sleep(1)
            tank_drive.off(brake=True)
            bool = False;
    #finds smallest distance
def Container(array_distance):

    length = len(array_distance)
    print(length)

    small = array_distance[0];
    for x in range(length):
        if small>array_distance[x]:
            small=array_distance[x]
    return small

#checks if pill and container are the same color
def colorChecker():
    bool = True
    if c1.color > 3  and c2.color >3:
        print("this is pill color", c1.color)
        print("this is container collor", c2.color)
        return bool
    elif c1.color == 7  and c2.color >3 :
        print("this is pill color", c1.color)
        print("this is container collor", c2.color)
        return bool
    elif c1.color <4 and c2.color <4:
        print("this is pill color", c1.color)
        print("this is container collor", c2.color)
        return bool
    elif c1.color ==7 and c2.color <4:
        print("this is pill color", c1.color)
        print("this is container collor", c2.color)
        return bool
    else:
        bool = False;
        print("this is pill color", c1.color)
        print("this is container collor", c2.color)
        return bool
def pillDropper():
    turn = 360/11
    m3.on_for_degrees(10, turn, brake=True, block=True)
def main():
    us.mode ='US-DIST-CM'
    count = 0;
    consec_bool = True;
    closest_distance=us.distance_centimeters_continuous
    move_until()
    color_bool = colorChecker()

    print("closest distance", closest_distance)
    if color_bool == True:
        while consec_bool == True:
            consec_bool = colorChecker()
            pillDropper()
            count = count+1
    print("closest distance", closest_distance)
    Reset(closest_distance)
    RotateBetter()
    while count < 10 :
        array_distance=Distance_Array();
        closest_distance = Container(array_distance)
        Rotate_until_counter(closest_distance)
        move_until()
        color_bool = colorChecker()
        if color_bool == True:
            while consec_bool == True:
                consec_bool = colorChecker()
                pillDropper()
                time.sleep(2)
                count = count+1
                color_bool=colorChecker()

        elif color_bool == False:
            Reset(closest_distance)
            RotateBetter()


main();

#this program fixes the two big problems. Gyro and US
#by seraching for each container individually, the smallest value
#can accurately be determined. The trade off is this method is much
#slower due to our hardware design. It would be very efficient if we could
#sort pill before hand.
