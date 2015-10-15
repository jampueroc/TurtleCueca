#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math

command = Twist()
command.linear.x = 0.0
command.linear.y = 0.0
command.linear.z = 0.0
command.angular.x = 0.0
command.angular.y = 0.0
command.angular.z = 0.0

Distance = 0
Angle = 0

TAngle = 0

Get_position = 0
end = 0
pose = 0

    


def reciver_odom(data):
    global command
    global end

    global Angle
    global TAngle

    global Distance
    global Get_position
    global pose

    pose=data.pose.pose

def process_odom():    
    global command
    global end

    global Angle
    global TAngle

    global Distance
    global Get_position
    global pose

    quaternion = (
    pose.orientation.x,
    pose.orientation.y,
    pose.orientation.z,
    pose.orientation.w)
#    rospy.loginfo(str(data.pose.pose.orientation) +" or " +str(quaternion) )
    (roll , pitch , yaw) = euler_from_quaternion(quaternion)
    TAngle = math.degrees(yaw)

    if Get_position == 1 :
        Distance += math.sqrt(pow(pose.position.x,2)+pow(pose.position.y,2))
#   Angle += yaw
#   TAngle = 0
        Get_position = 0

    if end == 1:
        rospy.loginfo("Andando")
#   TAngle = TAngle + data.twist.twist.angular.z
        TDistance = math.sqrt(pow(pose.position.x,2)+pow(pose.position.y,2))
#       rospy.loginfo("Distancia recorida in x? " + str(data.pose.pose.position.x - Distance) )   
        if abs(yaw - Angle) > 0.1:
            rospy.loginfo("yaw? " + str(yaw) +" TAngle " + str(Angle)+ "  =? "+ str(abs(abs(yaw) - abs(Angle)) > 0.1))
            command.linear.x = 0.0
            command.angular.z = abs(yaw - Angle)*0.2
        elif abs(TDistance - Distance) > 0.07:
            rospy.loginfo("TDistance? " + str(TDistance))
            command.linear.x = 1.0*abs(TDistance - Distance)/Distance
            command.angular.z = 0.0
        else :
            command.linear.x = 0.0
            command.angular.z = 0.0
    #           TDistance = 0
    #           TAngle = 0
            end = 0

def dance():
    rospy.Subscriber('odom',Odometry, reciver_odom)
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    rospy.init_node('dance', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    cuecaIntro(pub)
    while not rospy.is_shutdown():        
        rate.sleep()

def cuecaIntro(pub):
    y=1.5
    for i in range (4):
        caminar(pub,y)
        darVuelta(pub,y)
        y=-y

def caminar(pub,y):
    global command
    global end

    global Angle

    global Distance
    global Get_position

    end = 1
    Get_position = 1
    x=0    
    Distance = math.sqrt(pow(x,2)+pow(y,2))
    #Angle = math.atan2(x,y)
    Angle=0.03
    rospy.loginfo(str(Distance)+"  "+str(Angle))
    process_odom()
    while end!=0: 
        process_odom() 
        pub.publish(command)
    
def darVuelta(pub,y):
    global command
    global end

    global Angle

    global Distance
    global Get_position

    end = 1
    Get_position = 1
    x=0    
    Distance = math.sqrt(pow(x,2)+pow(y,2))
    #Angle = math.atan2(x,y)
    Angle=3.14
    rospy.loginfo(str(Distance)+"  "+str(Angle))
    process_odom()
    while end!=0: 
        process_odom() 
        pub.publish(command)

if __name__ == '__main__':
    try:
        dance()
    except rospy.ROSInterruptException:
        pass