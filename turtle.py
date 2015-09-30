#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState

posI=posD=0

def dance():
	pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=10)
	sub = rospy.Subscriber('joint_states', JointState,callback)
	rospy.init_node('dance', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	cuecaIntro(pub)
	while not rospy.is_shutdown():
		rate.sleep()

def cuecaIntro(pub):
	for i in range (4):
		caminar(pub)
		darVuelta(pub)

def caminar(pub):
	twist = Twist()
	print state.position
	posI=state.position[0]
	posD=state.position[1]
	#for i in range (100):
	while abs(state.position[0]-posI)<28 and abs(state.position[1]-posD)<28:
		twist.linear.x=0.2
		pub.publish(twist)
		rospy.sleep(0.05)
		twist.linear.x=0
		pub.publish(twist)

def darVuelta(pub):
	twist=Twist()
	posI=state.position[0]
	posD=state.position[1]
	while abs(state.position[0]-posI)<10.5 and abs(state.position[1]-posD)<10.5:
		twist.angular.z=0.32
		pub.publish(twist)
		rospy.sleep(0.1)
		twist.angular.z=0
		pub.publish(twist)	

def callback(data):
	global state
	state=data

if __name__ == '__main__':
	try:
		dance()
	except rospy.ROSInterruptException:
		pass

