#!/usr/bin/env python

from actionlib import SimpleActionClient
import copy
import move_base_msgs.msg
import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
from test_move import move
from tkinter import *

class App():
    def __init__(self):
        self.node = 'mir_move'
        self.action = 'move_base'
        self.mir_client = SimpleActionClient(self.action,move_base_msgs.msg.MoveBaseAction)
        rospy.init_node(self.node, anonymous=True)
        self.rate = rospy.Rate(10)
        self.root = Tk()
        # root window title and dimension
        self.root.title("Move mir")
        # Set geometry(widthxheight)
        self.root.geometry('175x160')
        # Specify Grid
        Grid.rowconfigure(self.root,0,weight=1)
        Grid.rowconfigure(self.root,1,weight=1)
        Grid.rowconfigure(self.root,2,weight=1)
        Grid.rowconfigure(self.root,3,weight=1)
        Grid.columnconfigure(self.root,0,weight=1)
        Grid.columnconfigure(self.root,1,weight=1)
        # button widget with red color text inside
        self.btnh = Button(self.root, text = "Home" ,
                    fg = "black", command=self.clicked_h)
        # Set Button Grid
        self.btnh.grid(column=0, row=0,sticky="NSEW")
        self.btna = Button(self.root, text = "Point A" ,
                    fg = "black", command=self.clicked_a)
        self.btna.grid(column=1, row=0,sticky="NSEW")
        self.btnb = Button(self.root, text = "Point B" ,
                    fg = "black", command=self.clicked_b)
        self.btnb.grid(column=0, row=1,sticky="NSEW")
        self.btnc = Button(self.root, text = "Point C" ,
                    fg = "black", command=self.clicked_c)
        self.btnc.grid(column=1, row=1,sticky="NSEW")
        self.btnpk = Button(self.root, text = "Pick" ,
                    fg = "black", command=self.clicked_pk)
        self.btnpk.grid(column=0, row=2,sticky="NSEW")
        self.btnpl = Button(self.root, text = "Place" ,
                    fg = "black", command=self.clicked_pl)
        self.btnpl.grid(column=1, row=2,sticky="NSEW")
        self.btns = Button(self.root, text = "Exit" ,
                   fg = "red", command=self.clicked_s)
        self.btns.grid(column=1, row=3,sticky="SE")

        self.h = PoseStamped()
        self.a = PoseStamped()
        self.b = PoseStamped()
        self.c = PoseStamped()
        self.h.header.frame_id = "map"
        self.h.pose.position.x = -44.166
        self.h.pose.position.y =  -45.286
        self.h.pose.position.z = 0.0
        self.h.pose.orientation.x = 0.0
        self.h.pose.orientation.y = 0.0
        self.h.pose.orientation.z = 1.0
        self.h.pose.orientation.w = -0.028

        self.a.header.frame_id = "map"
        self.a.pose.position.x = -47.940
        self.a.pose.position.y = -43.864
        self.a.pose.position.z = 0.000
        self.a.pose.orientation.x = 0.000
        self.a.pose.orientation.y = 0.000
        self.a.pose.orientation.z = -0.703
        self.a.pose.orientation.w =  0.711

        self.b.header.frame_id = "map"
        self.b.pose.position.x = -42.763
        self.b.pose.position.y = -47.350
        self.b.pose.position.z = 0.000
        self.b.pose.orientation.x = 0.000
        self.b.pose.orientation.y = 0.000
        self.b.pose.orientation.z = 0.000
        self.b.pose.orientation.w = 1.000

        self.c.header.frame_id = "map"
        self.c.pose.position.x = -43.599
        self.c.pose.position.y = -40.051
        self.c.pose.position.z = 0.000
        self.c.pose.orientation.x = 0.000
        self.c.pose.orientation.y = 0.000
        self.c.pose.orientation.z = 0.000
        self.c.pose.orientation.w = 1.000
        # home: Position(-43.166, -45.286, 0.000), Orientation(0.000, 0.000, 1.000, -0.028) = Angle: -3.14
        # A : Position(-47.940, -43.864, 0.000), Orientation(0.000, 0.000, -0.703, 0.711) = Angle: -1.57
        # B : Position(-42.763, -47.350, 0.000), Orientation(0.000, 0.000, -0.000, 1.000) = Angle: -0.000
        # C :  Position(-43.599, -40.051, 0.000), Orientation(0.000, 0.000, -0.000, 1.000) = Angle: -0.000


    def btn_disable(self):
        self.btnh['state'] = DISABLED
        self.btnh.update()
        self.btna['state'] = DISABLED
        self.btna.update()
        self.btnb['state'] = DISABLED
        self.btnb.update()
        self.btnc['state'] = DISABLED
        self.btnc.update()
        self.btnpk['state'] = DISABLED
        self.btnpk.update()
        self.btnpl['state'] = DISABLED
        self.btnpl.update()
        self.btns['state'] = DISABLED
        self.btns.update()

    def btn_enable(self):
        self.btnh.update()
        self.btnh['state'] = NORMAL
        self.btna.update()
        self.btna['state'] = NORMAL
        self.btnb.update()
        self.btnb['state'] = NORMAL
        self.btnc.update()
        self.btnc['state'] = NORMAL
        self.btnpk.update()
        self.btnpk['state'] = NORMAL
        self.btnpl.update()
        self.btnpl['state'] = NORMAL
        self.btns.update()
        self.btns['state'] = NORMAL

    def move_base_callback(self,msg):
        self.btn_disable()
        if not self.mir_client.wait_for_server(rospy.Duration(2)):
            rospy.logwarn("Unable to connect to move_base ation server, dropping goal...")
            return
        goal = move_base_msgs.msg.MoveBaseGoal()
        goal.target_pose.header = copy.deepcopy(msg.header)
        goal.target_pose.pose = copy.deepcopy(msg.pose)
        self.mir_client.send_goal_and_wait(goal)
        self.btn_enable()

    def clicked_h(self):
        self.move_base_callback(self.h)
    def clicked_a(self):
        self.move_base_callback(self.a)
    def clicked_b(self):
        self.move_base_callback(self.b)
    def clicked_c(self):
        self.move_base_callback(self.c)
    def clicked_pk(self):
        self.btn_disable()
        move()
        self.btn_enable()
    def clicked_pl(self):
        self.btn_disable()
        move()
        self.btn_enable()
    def clicked_s(self):
        self.root.destroy()
        return
    
    def start(self):
        while True:
            while not rospy.is_shutdown():
                self.root.mainloop()
                return
try:
    obj = App()
    obj.start()
except:
    pass