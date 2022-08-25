#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
class subscriber(object):
    def __init__(self):
        rospy.init_node('subscriber','anonymous')
        
        rospy.Subscriber('/Mayur',String, self.print, queue_size=1)
        rospy.spin()
    
    def print(self,msg):
        print("my name is",msg.data)

           

if __name__=='__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
