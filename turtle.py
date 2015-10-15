#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState

state = None

posI=posD=0

def dance():
	rospy.init_node('dance', anonymous=True)
	sub = rospy.Subscriber('joint_states', JointState,callback)
	pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	while state == None :
		print("waiting")
		rate.sleep()
	while not rospy.is_shutdown():
		cuecaIntro(pub)
		vueltaEntera(pub)
		mediaLuna(pub)
		vueltaS(pub)
		escobillado(pub, 1)
		vueltaS(pub)
		escobillado(pub,0.5)
		vueltaS(pub)
		rate.sleep()

def cuecaIntro(pub):
	for i in range (2):
		caminar(pub)
		darVuelta(pub)

def caminar(pub):
	twist = Twist()
	global state
	posI=state.position[0]
	posD=state.position[1]
	while abs(state.position[0]-posI)<28 and abs(state.position[1]-posD)<28:
		twist.linear.x=0.2
		pub.publish(twist)
		rospy.sleep(0.05)
	twist.linear.x=0
	pub.publish(twist)
	rospy.sleep(1)

def darVuelta(pub):
	twist=Twist()
	global state
	posI=state.position[0]
	posD=state.position[1]
	while abs(state.position[0]-posI)<10.4 and abs(state.position[1]-posD)<10.5:
		twist.angular.z=0.64
		pub.publish(twist)
		rospy.sleep(0.05)
	twist.angular.z=0
	pub.publish(twist)
	rospy.sleep(1)

def darVuelta90(pub, dir, vel):
	twist=Twist()
	global state
	posI=state.position[0]
	posD=state.position[1]
	while abs(state.position[0]-posI)<6.4*dir and abs(state.position[1]-posD)<6.5*dir:
		twist.angular.z=0.64*vel
		pub.publish(twist)
		rospy.sleep(0.05)
	twist.angular.z=0
	pub.publish(twist)
	rospy.sleep(1)


def mediaLuna(pub):
	medialunaDer(pub)
	darVuelta90(pub,1,1)
	medialunaIzq(pub)


def medialunaDer(pub):
	twist=Twist()
	global state
	posI=state.position[0]
	posD=state.position[1]
	z=0.35
	x=0.35
	diff=35
	while abs(state.position[0]-posI)<3.1 and abs(state.position[1]-posD)<3.1:
		twist.angular.z=-z
		pub.publish(twist)
		rospy.sleep(0.05)
	twist.angular.z=-0.0-0
	pub.publish(twist)
	rospy.sleep(1)
	posI=state.position[0]
	posD=state.position[1]
	cont=0
	while abs(state.position[0]-posI)<diff and abs(state.position[1]-posD)<diff:
		twist.angular.z=z
		twist.linear.x=x
		pub.publish(twist)
		rospy.sleep(0.1)
		cont+=1
		rospy.loginfo(str(cont))
	twist.angular.z=-0.0-0
	twist.linear.x=0.0
	pub.publish(twist)
	rospy.sleep(1)
	posI=state.position[0]
	posD=state.position[1]
	cont=0
	while abs(state.position[0]-posI)<diff and abs(state.position[1]-posD)<diff:
		twist.angular.z=-z
		twist.linear.x=-x+0.05
		pub.publish(twist)
		rospy.sleep(0.05)
		cont+=1
		rospy.loginfo(str(cont))
	twist.angular.z=-0.0-0
	twist.linear.x=0.0
	pub.publish(twist)
	rospy.sleep(1)

def medialunaIzq(pub):
	twist=Twist()
	global state
	posI=state.position[0]
	posD=state.position[1]
	z=-0.35
	x=0.35
	cont=0
	diff=35
	while abs(state.position[0]-posI)<diff and abs(state.position[1]-posD)<diff:
		twist.angular.z=z
		twist.linear.x=x
		pub.publish(twist)
		rospy.sleep(0.1)
		cont+=1
		rospy.loginfo(str(cont))
	twist.angular.z=-0.0-0
	twist.linear.x=0.0
	pub.publish(twist)
	rospy.sleep(1)
	posI=state.position[0]
	posD=state.position[1]
	cont=0
	while abs(state.position[0]-posI)<diff and abs(state.position[1]-posD)<diff:
		twist.angular.z=-z
		twist.linear.x=-x+0.05
		pub.publish(twist)
		rospy.sleep(0.05)
		cont+=1
		rospy.loginfo(str(cont))
	twist.angular.z=-0.0-0
	twist.linear.x=0.0
	pub.publish(twist)
	rospy.sleep(1)
	posI=state.position[0]
	posD=state.position[1]
	while abs(state.position[0]-posI)<3.1 and abs(state.position[1]-posD)<3.1:
		twist.angular.z=z
		pub.publish(twist)
		rospy.sleep(0.05)
	twist.angular.z=-0.0-0
	pub.publish(twist)
	rospy.sleep(1)

def vueltaEntera(pub):
	twist=Twist()
	global state
	posI=state.position[0]
	posD=state.position[1]
	z=0.37
	x=0.35
	cont=0
	diff=85
	darVuelta90(pub,0.6,-1)
	while abs(state.position[0]-posI)<diff and abs(state.position[1]-posD)<diff:
		twist.angular.z=z
		twist.linear.x=x
		pub.publish(twist)
		rospy.sleep(0.1)
		cont+=1
		rospy.loginfo(str(cont))
	posI=state.position[0]
	posD=state.position[1]
	cont=0
	while abs(state.position[0]-posI)<diff and abs(state.position[1]-posD)<diff:
		twist.angular.z=z
		twist.linear.x=x
		pub.publish(twist)
		rospy.sleep(0.1)
		cont+=1
		rospy.loginfo(str(cont))
	twist.angular.z=-0.0-0
	pub.publish(twist)
	rospy.sleep(1)
	darVuelta90(pub,1,1)

def vueltaS(pub):
	twist=Twist()
	global state
	posI=state.position[0]
	posD=state.position[1]
	z=0.85
	x=0.53
	diff=60
	while abs(state.position[0]-posI)<3.1 and abs(state.position[1]-posD)<3.1:
		twist.angular.z=-z
		pub.publish(twist)
		rospy.sleep(0.05)
	twist.angular.z=-0.0-0
	pub.publish(twist)
	rospy.sleep(1)
	posI=state.position[0]
	posD=state.position[1]
	cont=0
	while abs(state.position[0]-posI)<diff and abs(state.position[1]-posD)<diff:
		twist.angular.z=z
		twist.linear.x=x
		pub.publish(twist)
		rospy.sleep(0.1)
		cont+=1
		rospy.loginfo(str(cont))
	twist.angular.z=-0.01
	twist.linear.x=-0.01
	pub.publish(twist)
	rospy.sleep(1)
	posI=state.position[0]
	posD=state.position[1]
	cont=0
	while abs(state.position[0]-posI)<diff+15 and abs(state.position[1]-posD)<diff+15:
		twist.angular.z=-z
		twist.linear.x=x
		pub.publish(twist)
		rospy.sleep(0.1)
		cont+=1
		rospy.loginfo(str(cont))
	twist.angular.z=-0.0-0
	twist.linear.x=0.0
	pub.publish(twist)
	rospy.sleep(1)
	posI=state.position[0]
	posD=state.position[1]
	while abs(state.position[0]-posI)<3.1 and abs(state.position[1]-posD)<3.1:
		twist.angular.z=-z
		pub.publish(twist)
		rospy.sleep(0.05)
	twist.angular.z=-0.0-0
	pub.publish(twist)
	rospy.sleep(1)
	posI=state.position[0]
	posD=state.position[1]
	cont=0

def escobillado(pub, times):
	twist = Twist()
	global state
	diff=17
	x=1
	for i in range(int(4*times)):
		posI=state.position[0]
		posD=state.position[1]
		while abs(state.position[0]-posI)<diff and abs(state.position[1]-posD)<diff:
			twist.linear.x=x
			pub.publish(twist)
			rospy.sleep(0.05)
		twist.linear.x=0
		pub.publish(twist)
		rospy.sleep(0.5)
		posI=state.position[0]
		posD=state.position[1]
		delta=3
		while abs(state.position[0]-posI)<diff-delta and abs(state.position[1]-posD)<diff-delta:
			twist.linear.x=-x
			pub.publish(twist)
			rospy.sleep(0.05)
		twist.linear.x=0
		pub.publish(twist)
		rospy.sleep(0.5)

	x=-1
	for i in range(int(4*times)):
		posI=state.position[0]
		posD=state.position[1]
		while abs(state.position[0]-posI)<diff and abs(state.position[1]-posD)<diff:
			twist.linear.x=x
			pub.publish(twist)
			rospy.sleep(0.05)
		twist.linear.x=0
		pub.publish(twist)
		rospy.sleep(0.5)
		posI=state.position[0]
		posD=state.position[1]
		delta=3
		while abs(state.position[0]-posI)<diff-delta and abs(state.position[1]-posD)<diff-delta:
			twist.linear.x=-x
			pub.publish(twist)
			rospy.sleep(0.05)
		twist.linear.x=0
		pub.publish(twist)
		rospy.sleep(0.5)

def callback(data):
	global state
	state=data

if __name__ == '__main__':
	try:
		dance()
	except rospy.ROSInterruptException:
		pass

