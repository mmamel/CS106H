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
    #m1.run_forever(speed_sp=900)
    #m2.run_forever(speed_sp=-900)

    while bool == True:
        time.sleep(.1)
        distance = us.distance_centimeters_continuous
        print("This is move_until distance: ", distance)
        if distance < 5:
            tank_drive.off()
            bool = False;
    #set up a sleep interval

        #m1.stop()
        #m2.stop()
        #takes in an angle in radians and converts into degrees
        #spins in a circle forever with intervals of 0.1 sec (time.sleep)
        #and checks when it turned enough using gyro

def Distance_Array():
    #reset gyro
    gs.mode = 'GYRO-RATE';
    gs.mode = 'GYRO-ANG';
    us.mode ='US-DIST-CM'
    array_distance=[];
    array_angle=[];

    current_angle=0;
    tank_drive.on(left_speed=-2,right_speed=2)
    while current_angle < 180:

        time.sleep(.115)
        current_angle=gs.angle
        array_angle.append(current_angle)
        #print(current_angle)

        #m1.run_forever(speed_sp=900)
        #m2.run_forever(speed_sp=-900)
        #tank_pair.on(30,-30)
        #get angle
        distance= us.distance_centimeters_continuous;
        print(distance)
        array_distance.append(distance);
    tank_drive.off(brake=True)

    return array_distance, array_angle;
def Reset(distance):
    bool =True;

    while bool == True:
        time.sleep(.1)
        measurement= us.distance_centimeters_continuous;
        tank_drive.on(left_speed=-5,right_speed=-5)
        print("this is measurement:", measurement)

        if measurement > distance -1 and measurement < distance +1:
            tank_drive.off(brake=True)
            bool = False;
def Container(array_distance):

    length = len(array_distance)
    print(length)

    small = array_distance[0];
    #for x in range(length):
    for x in range(length):
        #if(smallest>distance_array[x]):
        if small>array_distance[x]:
            small=array_distance[x]
            #smallest=distance_array[x];
    return small
def Distance_array_2(smallest, distance_array):
    for x in range(1,5):
        index = distance_array.index(smallest)
        length=len(distance_array);
        if index==length:
            distance_array.pop(index-x)
            distance_array.pop(0)
        if index == 0:
            distance_array.pop(index+x)
            distance_array.pop(length)
        if index != length or index!=0:
            distance_array.pop(index+x)
            distance_array.pop(index-x)
    distance_array.pop(index)
    return distance_array

def colorChecker():
    bool = True
    if c1.color == c2.color:
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
    bool = True;
    array_distance, angle_array=Distance_Array();
    len_First_Container = Container(array_distance)
    index_first_distance = array_distance.index(len_First_Container)
    distance_array_2 = Distance_array_2(len_First_Container, array_distance)
    len_Sec_container = Container(distance_array_2)
    index_second_distance = array_distance.index(len_Sec_container)
    print("Computation complete")
    if index_first_distance<index_second_distance:
        Rotate_until_counter(len_First_Container)
    if index_first_distance>index_second_distance:
        Rotate_until_counter(len_Sec_container)

    count = 0
    while bool == True:
        us.mode ='US-DIST-CM'
        reset_distance = us.distance_centimeters
        move_until()
        drop = colorChecker()
        if drop == True or c2.color == 1:
            tank_drive.off(brake=True)
            count = count +1
            pillDropper()
            Reset(reset_distance)
        if drop == False:
            Reset(reset_distance)
            if count%2 != 0:
                Rotate_until_clock(len_Sec_container)
                move_until()
                count = count +1
                pillDropper()
            if count%2 == 0:
                Rotate_until_counter(len_First_Container)
                move_until()
                count = count +1
                pillDropper()
        if count == 10:
            bool = False


main();
