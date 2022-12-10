#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

rospy.init_node("PID")

#PID constants
Kp=250.0
Ki=2.0
Kd=0.0
desired=10.0 #desired speed
#end

velocity=Float64()

#the initial values for PID error
error_sum=0.0
p_error=0.0
i_error=0.0
d_error=0.0
last=0.0
#end

#time for the PID to work
delta_time=0.0
prev_time=0.0
#end

def update(state:Float64):
    global Ki,Kp,Kd,desired,error_sum,p_error,i_error,d_error,last,delta_time,prev_time

    #calculate the error
    error=abs(desired-state.data)
    #end

    #calculate the proportional error
    p_error=Kp*error
    #end

    #calaulating the integral error
    i_error+=(Ki*error)*0.001
    #end

    #calculating the derivative error
    d_error=Kd*((error-last)/0.001)
    last=error
    #end

    #PID controller
    velocity.data=p_error+i_error+d_error
    #end

    velocity_publisher.publish(velocity)  
    #end
    
velocity_publisher=rospy.Publisher("/velocity", Float64, queue_size=1)
state=rospy.Subscriber("/velocity_sensor",Float64, update)
rospy.spin()