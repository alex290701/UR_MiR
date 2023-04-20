#!/usr/bin/env python

from actionlib import SimpleActionClient
import mir_actions.msg
import mir_msgs.msg
import copy
import move_base_msgs.msg
import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
from test_move import move
from tkinter import *

# create root window
root = Tk()
 
# root window title and dimension
root.title("Move mir")
# Set geometry(widthxheight)
root.geometry('175x160')


# mir_publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)
mir_client = SimpleActionClient('move_base',move_base_msgs.msg.MoveBaseAction)

msg = PoseStamped()

h = PoseStamped()
a = PoseStamped()
b = PoseStamped()
c = PoseStamped()
h.header.frame_id = "map"
h.pose.position.x = -44.166
h.pose.position.y =  -45.286
h.pose.position.z = 0.0
h.pose.orientation.x = 0.0
h.pose.orientation.y = 0.0
h.pose.orientation.z = 1.0
h.pose.orientation.w = -0.028

a.header.frame_id = "map"
a.pose.position.x = -47.940
a.pose.position.y = -43.864
a.pose.position.z = 0.000
a.pose.orientation.x = 0.000
a.pose.orientation.y = 0.000
a.pose.orientation.z = -0.703
a.pose.orientation.w =  0.711

b.header.frame_id = "map"
b.pose.position.x = -42.763
b.pose.position.y = -47.350
b.pose.position.z = 0.000
b.pose.orientation.x = 0.000
b.pose.orientation.y = 0.000
b.pose.orientation.z = 0.000
b.pose.orientation.w = 1.000

c.header.frame_id = "map"
c.pose.position.x = -43.599
c.pose.position.y = -40.051
c.pose.position.z = 0.000
c.pose.orientation.x = 0.000
c.pose.orientation.y = 0.000
c.pose.orientation.z = 0.000
c.pose.orientation.w = 1.000
# home: Position(-43.166, -45.286, 0.000), Orientation(0.000, 0.000, 1.000, -0.028) = Angle: -3.14
# A : Position(-47.940, -43.864, 0.000), Orientation(0.000, 0.000, -0.703, 0.711) = Angle: -1.57
# B : Position(-42.763, -47.350, 0.000), Orientation(0.000, 0.000, -0.000, 1.000) = Angle: -0.000
# C :  Position(-43.599, -40.051, 0.000), Orientation(0.000, 0.000, -0.000, 1.000) = Angle: -0.000

def shut():
    print("Shutting Down!")

# button is clicked
def clicked_h():
    if event_running:
        return 
    event_running = True
    move_base_callback(h)
def clicked_a():
    if event_running:
        return 
    event_running = True
    move_base_callback(a)
def clicked_b():
    if event_running:
        return 
    event_running = True
    move_base_callback(b)
def clicked_c():
    if event_running:
        return 
    event_running = True
    move_base_callback(c)
def clicked_pk():
    if event_running:
        return 
    event_running = True
    move()
def clicked_pl():
    if event_running:
        return 
    event_running = True
    move()
def clicked_s():
    if event_running:
        return 
    event_running = True
    root.destroy()
    return

# def mir_move(goal):
#     if goal == 'home':
       
#         move_base_callback(h)
      
#     elif goal == 'a':
      
       
#         move_base_callback(a)
       
#     elif goal == 'b':
#         move_base_callback(b)
       
#     elif goal == 'c':
        
#         move_base_callback(c)
#     elif goal == 'pick':
#         move()
#     elif goal == 'place':
#         move()
#     # elif goal == 'exit':
#     #     return 0
#     else:
#         print("Invalid Input")
#         return 0

def talker():
    rospy.init_node('mir_move', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while True:
        # n = raw_input("Enter command: ")
        while not rospy.is_shutdown():
            
            root.mainloop()
            return
            # if n == 'exit':
            #     return 
            # else:
            #     try:
            #         print("Executing...")
            #         mir_move(n)
            #         rate.sleep()
            #     except :
            #         print("Error Executing the command")
            #     break
            # elif 4<n<7:
                # arm_move()
                # break
            # elif n==7:
                # return 0
            # else:
                # print("Invalid Input")
            # rate.sleep()
        
    # rospy.sleep(10)

def move_base_callback(msg):
    if not mir_client.wait_for_server(rospy.Duration(2)):
        rospy.logwarn("Unable to connect to move_base ation server, dropping goal...")
        return
    goal = move_base_msgs.msg.MoveBaseGoal()
    goal.target_pose.header = copy.deepcopy(msg.header)
    goal.target_pose.pose = copy.deepcopy(msg.pose)
    mir_client.send_goal_and_wait(goal)


if __name__ == '__main__':
    try:
        event_running = False
        # print(" home - Move to Home \n a - Move to Point A \n b - Move to Point B \n c - Move to Point C \n pick - Pick movement \n place - Place movement \n exit - Exit")
        btnh = Button(root, text = "Home" ,
             fg = "black", command=clicked_h)
        # Set Button Grid
        btnh.grid(column=2, row=0)

        # button widget with red color text inside
        btna = Button(root, text = "Point A" ,
                    fg = "black", command=clicked_a)
        # Set Button Grid
        btna.grid(column=3, row=0)

        # button widget with red color text inside
        btnb = Button(root, text = "Point B" ,
                    fg = "black", command=clicked_b)
        # Set Button Grid
        btnb.grid(column=2, row=1)

        # button widget with red color text inside
        btnc = Button(root, text = "Point C" ,
                    fg = "black", command=clicked_c)
        # Set Button Grid
        btnc.grid(column=3, row=1)

        # button widget with red color text inside
        btnpk = Button(root, text = "Pick" ,
                    fg = "black", command=clicked_pk)
        # Set Button Grid
        btnpk.grid(column=2, row=2)

        # button widget with red color text inside
        btnpl = Button(root, text = "Place" ,
                    fg = "black", command=clicked_pl)
        # Set Button Grid
        btnpl.grid(column=3, row=2)

        # button widget with red color text inside
        btnpl = Button(root, text = "Exit" ,
                    fg = "red", command=clicked_s)
        # Set Button Grid
        btnpl.grid(column=3, row=3)
        talker()

    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        pass