#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
rospy.init_node('lane',anonymous=True)


def callback(v:Float64):
    r=rospy.wait_for_message("/curs",Float64MultiArray)
    theta=v*r
    if (r[1]==0 and r[2]==0):
        theta=0
    if(r[1]<r[2]):
        theta=theta
    if(r[1]<r[2]):
        theta=-theta

    theta_publisher.publish(theta)
theta_publisher=rospy.Publisher("/steering_angle", Float64, queue_size=1)
v=rospy.Subscriber("/velocity_sensor", Float64,callback)
