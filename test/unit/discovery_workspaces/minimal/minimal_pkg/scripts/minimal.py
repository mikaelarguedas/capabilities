#!/usr/bin/env python

from __future__ import absolute_import
import rospy
from std_msgs.msg import String


def main():
    rospy.init_node('minimal')
    pub = rospy.Publisher('chatter', String, queue_size=1000)
    start = rospy.Time.now()
    while not rospy.is_shutdown() and (rospy.Time.now() - start).to_sec() < 10:
        log = "hello world %s" % rospy.get_time()
        rospy.loginfo(log)
        pub.publish(String(log))
        rospy.sleep(1.0)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
