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

#def move(distance):
    #some sort of converion of distance with time
def move_until():
    us.mode ='US-DIST-CM'
    tank_drive.on(left_speed=-90,right_speed=90)
    #m1.run_forever(speed_sp=900)
    #m2.run_forever(speed_sp=-900)

    while us.distance_centimeters_continous > 4:
        time.sleep(.1)
    #set up a sleep interval
    tank_drive.off()
        #m1.stop()
        #m2.stop()
        #takes in an angle in radians and converts into degrees
        #spins in a circle forever with intervals of 0.1 sec (time.sleep)
        #and checks when it turned enough using gyro
def Rotate(angle):
    #reset gyro
    angle_degrees = math.degrees(angle)
    gs.mode = 'GYRO-RATE';
    gs.mode = 'GYRO-ANG';
    bool = True;
    tank_drive.on(left_speed=-90,right_speed=90)
    #m1.run_forever(speed_sp=900)
    #m2.run_forever(speed_sp=-900)
    while bool == True:
        time.sleep(.1)
        #tank_pair.on(30,-30)
        #get angle
        current_angle=gs.angle;
        if current_angle == angle_degrees:
            bool = False;
            #turn in place
    tank_drive.off()
    #m1.stop()
    #m2.stop()

#creates two arrays and spins indefintely taking measurements at .1 sec increments
#takes angle and distance which will be used to determine the location of containers
#by finding the 2 smallest values in the distance array
def Distance_Array():
    #reset gyro
    gs.mode = 'GYRO-RATE';
    gs.mode = 'GYRO-ANG';
    us.mode ='US-DIST-CM'
    array_distance=[];
    array_angle=[];

    current_angle=0;
    tank_drive.on(left_speed=-2,right_speed=2)
    while current_angle < 360:

        time.sleep(.12)
        current_angle=gs.angle
        array_angle.append(current_angle)
        #print(current_angle)

        #m1.run_forever(speed_sp=900)
        #m2.run_forever(speed_sp=-900)
        #tank_pair.on(30,-30)
        #get angle
        distance= us.distance_centimeters_continuous;
        print(current_angle)
        array_distance.append(distance);
    tank_drive.off(brake=True)

    return array_distance, array_angle;

#takes in distance array and finds the smallest values
#returns distance from mindstorm to first container

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
    #alternative way? using mod to return back to beggining of array???
#takes in the distance from first container and initial array
#and removes the values surronding value of smallest to ensure
#it can find the second smallest value. It is given that the containers
#will be seperated by an angle so we can take off multiple values
def Distance_array_2(smallest, distance_array):
    index = distance_array.index(smallest)
    for x in range(1,10):
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

def Len_Law_Cosine(a,b,angle_C):
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle_C));
    return c
def Angle_Law_Cosine(z,b,angle_A):
    init_move = math.sqrt(z**2+b**2-z*b*math.cos(angle_A))
    return init_move
def Ambiguous(a,b,c,angle_C):
    half_pi = (math.pi)/2
    angle_A = math.asin(a*math.sin(angle_C)/(c))
    ambiguousangle_A = math.pi - angle_A
    angle_B = half_pi - angle_A - angle_C
    ambiguousangle_B = half_pi - math.degrees(ambiguousangle_A) - math.degrees(angle_C)
    ambiguouslen_b = a*math.sin(angle_B)/math.sin(angle_A)
    len_b = a*math.sin(ambiguousangle_B)/math.sin(ambiguousangle_A)
    #find difference then find smallest difference. Float arthmetic is
    #inaccurate so comaprison will find the smallest absolute difference
    test_angle_A = math.fabs(b-len_b)
    test_ambiguousangle_B = math.fabs(b-ambiguouslen_b)
    if test_angle_A<test_ambiguousangle_B:
        true_angle=angle_A
    elif test_angle_A>test_ambiguousangle_B:
        true_angle = ambiguousangle_B
    return true_angle
def main():

    half_pi = math.pi/2
    array_distance, angle_array=Distance_Array();
    b=Container(array_distance)
    #b=Container(array_distance)
    index_b=array_distance.index(b)
    array_distance_2=Distance_array_2(b, array_distance)
    a=Container(array_distance_2)
    index_a = array_distance.index(a)
    #line up with first Container
    turn_angle = math.pi/360*index_b
    difference_angle = math.fabs(index_b - index_a)
    print("working1")
    if difference_angle > half_pi:
        angle_C = (math.pi)/360 * (360 - difference_angle)
    else:
        angle_C = difference_angle * (math.pi/360)
    c = Len_Law_Cosine(a,b,angle_C)
    true_angle = Ambiguous(a,b,c,angle_C)
    print("working2")
    z = 0.5*c
    init_move = Angle_Law_Cosine(z,b,true_angle)
    angle_G = math.asin(b*math.sin(true_angle)/init_move)
    angle_M = half_pi - anlge_G - true_angle
    Rotate(turn_angle)
    Rotate(angle_M)
    move(init_move)
    Rotate(angle_G)
    move_until()
    angle_pill_hopper = 11/360
    #for x in range(10):
        #pill color
        #if c1.color== c2.color:
            #m3.run_to_rel_pos(position_sp=(angle_pill_hopper))
    #    else:

        #    m1.run_timed(time_sp=1000, speed_sp=-750)
        #    m2.run_timed(time_sp=1000, speed_sp=-750)
        #    Rotate(half_pi)
            #move_until()
        #    m3.run_to_rel_pos(position_sp=(angle_pill_hopper))




main();
