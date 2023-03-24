# Instructions for setting up of Working Environment

 
# Installing ROS 
🛑 If your computer has ROS Installed you can skip this topic

 ### Step 1:
* Setup your computer to accept software from packages.ros.org
 ```
 sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

 ### Step 2:
* Set up your keys
 ```
 sudo apt install curl
```
```
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```


 ### Step 3:
* Make sure your Debian package index is up-to-date.
 ```
 sudo apt update
```

 ### Step 4:
* Installing the ROS recommended configuration.
 ```
 sudo apt install ros-noetic-desktop-full
```

 ### Step 5:
* Adding environment variables: To Automatically add ROS environment variables to your bash session every time a new shell terminal/bash is launched, enter the following commands (this step is similar as adding environmental variable in windows).
 ```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
```
* Sourcing bashrc ensures to use updated bashrc, or it can be done by re-opening new terminal.
```
source ~/.bashrc
```
### Step 6:
* Additional Dependencies: To install this tool and other dependencies for building ROS packages.

```
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```

### Step 7:
*Initialize rosdep: Before you can use many ROS tools, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS. If you have not yet installed rosdep, do so as follows.

```
sudo apt install python3-rosdep
```
```
sudo rosdep init
```
```
rosdep update
```

### Checking the installation
* Run the below command on a new terminal after performing all the steps above, this will ensure that the ROS master is running perfectly on the system.

```
roscore
```
* The ouput should be similar to this

![maxresdefault](https://user-images.githubusercontent.com/115358075/227400065-f256e467-2c38-4c3c-a47d-4748bf75988e.jpg)

### 🥳 Hurray!!! You have installed ROS successfully!!!

# Creating a Catkin Workspace

### Step 1:
* Create the root workspace directory (we’ll use mitra_ws)
```
cd 
mkdir --parents catkin_ws/src
cd catkin_ws
```

### Step 2:
* Initialize the catkin workspace
```
catkin init
```
* Look for the statement “Workspace configuration appears valid”, showing that your catkin workspace was created successfully.

### Step 3:
* Build the workspace. This command may be issued anywhere under the workspace root-directory
```
catkin build
```

🛑 Check if the build is successful by
```
ls
```
* See that the mitra_ws directory has build, devel directories.

### Step 3:
* Make the workspace visible to ROS. Source the setup file in the devel directory.
```
source devel/setup.bash
```
* This file MUST be sourced for every new terminal.
* To save typing, add this to your ~/.bashrc file, so it is automatically sourced for each new terminal: </br>
• gedit `~/.bashrc` </br>
• add to the end: `source ~/mitra_ws/devel/setup.bash`</br>
• save and close the editor </br>

## Clone this repository
 * You can clone this repo by using git clone command
 ```
 cd ~/mitra_ws/src
```
```
git clone https://github.com/doom-bhaiya/Mobile-Manipulator
```
 
## Installing Gazebo
* Update apt database with `apt` using the following command.
```
sudo apt update
```
* After updating apt database, We can install gazebo using apt by running the following command:
```
sudo apt -y install gazebo
```

## Testing the installations
 * Type the following in a new terminal 
 ```
 roslaunch gaz_sim_env empty_world_launch.launch
 ```
 
 Got an empty world spawned 👀??
 
 ### 🥳 Hurray!!! We are done with the setup!!!  🥳

