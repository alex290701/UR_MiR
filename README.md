# UR_MiR
A simple working simulation of a robotic arm (ur5e) placed over a mobile robot(MiR) for a pick and place application using available packages and drivers.

## To run
```bash
roslaunch ur_mir_moveit_config demo_gazebo.launch
```
The above command will launch gazebo and the UI to control the mir. If there is problem launching the UI, you can launch the UI seperately using the below command.
```bash
rosrun move_arm test.py 
```
