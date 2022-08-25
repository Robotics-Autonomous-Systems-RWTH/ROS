#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
class publisher(object):
    def __init__(self):
        rospy.init_node('Publisher','anonymous')
        self.rate=rospy.Rate(10)
        self.pub=rospy.Publisher('/Mayur',String, queue_size=1)
    
        while not rospy.is_shutdown():
            rospy.loginfo("publishing data")
            ctr=rospy.get_time()
            self.msg='Mayur'+ str(ctr)
            self.pub.publish(self.msg)
            
            self.rate.sleep()

if __name__=='__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

