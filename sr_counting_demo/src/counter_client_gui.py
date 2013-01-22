#! /usr/bin/env python

import roslib; roslib.load_manifest('sr_counting_demo')
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the CounterDemoAction, including the
# goal message and the result message.
import sr_counting_demo.msg

def counter_client(num_selected):
    """
    This function runs a loop where: 
    
    1. is asked to the user to select the desired number to be counted by the hand by means of the Counting Demo GUI;
    
    2. the number (goal) is sent to the server node.  
    """

    # Creates the SimpleActionClient, passing the type of the action
    # (CounterDemoAction) to the constructor.
    client = actionlib.SimpleActionClient('counter_server_py', sr_counting_demo.msg.CounterDemoAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()
    
    # Creates a goal to send to the action server
    goal = sr_counting_demo.msg.CounterDemoGoal(target = int(num_selected))

    # Sends the goal to the action server
    client.send_goal(goal)

    # Waits for the server to finish performing the action
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A CounterDemoResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('counter_client_py')
        
        import sys

        result = counter_client(sys.argv[1]) 
        #print "The Hand has counted up to", str(result.sequence)
        
            
       
    except rospy.ROSInterruptException:
        print "program interrupted before completion"


