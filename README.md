# SPCUP2020
Sharing project files for IEEE Signal Processing Cup 2020

1. Install the python module rosbag either using pip or conda
2. Install dependencies
   ```bash
   conda install -c conda-forge ros-rosbag
   ```

2. Before running the 'read_bag_file.py' specify the bag file you wish to read and run the script
3. The script saves the data read from the bag file, saves numeric data to a pickle file as a dictionary
4. The script saves the images in a separate folder
5. The Dictionary file is as follows:

data = 
{
    'battery' = {'time', 'voltage', 'current'}
    'compass' = {'time', 'angle'}
    'gps_global' = {'time', 'latitude', 'longitude', 'altitude'}
    'gps_local' = {'time', 'position', 'orientation', 'linear', 'angular'}
    'gps_raw_fix' = {'time', 'latitude', 'longitude', 'altitude'}
    'gps_raw_vel' = {'time', 'linear', 'angular'}
    'gps_rel_alt' = {'time', 'altitude'}
    'home' = {'time', 'latitude', 'longitude', 'altitude', 'position', 'orientation'}
    'imu' = {'time', 'orientation', 'ang_vel', 'lin_acc'}
    'imu_raw' = {'time', 'orientation', 'ang_vel', 'lin_acc'}
    'imu_mag' = {'time', 'mag'}
    'imu_pressure' = {'time', 'pressure'}
    'imu_temperature' = {'time', 'temperature'}
    'local_odom' = {'time', 'position', 'orientation', 'linear', 'angular'}
    'local_pose' = {'time', 'position', 'orientation'}
    'local_vel_body' = {'time', 'linear', 'angular'}
    'rc_in' = {'time', 'channels'}
    'rc_out' = {'time', 'channels'}
    'vfr_hud' = {'time', 'airspeed', 'groundspeed', 'heading', 'throttle', 'altitude', 'climb'}
}

6. For more information on rosbag module, consult http://wiki.ros.org/rosbag/Code%20API
