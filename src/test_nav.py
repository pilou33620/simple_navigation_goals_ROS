#!/usr/bin/env python
import rospy
import math
import traceback
import sys
import simple_navigation_goals
if __name__ == "__main__":
    try:
        rospy.init_node("test_scenario")
        rospy.loginfo("SimpleNavigationGoals Initialization")
        nav_goals = simple_navigation_goals.SimpleNavigationGoals()
        rospy.loginfo("Initializations done")
        # What to do if shut down (e.g. ctrl + C or failure)
        rospy.on_shutdown(nav_goals._shutdown)
        while True:
            if not (nav_goals.go_to(1.78, 0.52, 0)):
                break
            if not (nav_goals.go_to(0.45, 1.86, math.pi / 2)):
                break
            if not (nav_goals.go_to(0.736, -1.81, 0)):
                break
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.logerr(traceback.format_exc())
    rospy.loginfo("test terminated.")
