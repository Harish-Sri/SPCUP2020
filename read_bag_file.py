import rosbag
import numpy as np
import pickle
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

bag = rosbag.Bag('dataset2.bag')
test = 0

if test:
    #print(bag)

    i = 0

    for topic, msg, t in bag.read_messages(topics = ['/mavros/global_position/raw/fix']):
        print(t.to_time(), msg.latitude)
        i+=1

    print(i)


else:
    class mavros:
        bag = []
        data = {}

        def __init__(self, bag_file):
            self.bag = bag_file


            self.data['battery'] = {'time':np.array([]), 'voltage':np.array([]), 'current':np.array([])}
            topic = '/mavros/battery'
            for _ , msg, t in bag.read_messages(topics = topic):
                self.data['battery']['time'] = np.append(self.data['battery']['time'], t.to_time())
                self.data['battery']['voltage'] = np.append(self.data['battery']['voltage'], msg.voltage)
                self.data['battery']['current'] = np.append(self.data['battery']['current'], msg.current)


            self.data['compass'] = {'time':np.array([]), 'angle':np.array([])}
            topic = '/mavros/global_position/compass_hdg'
            for _ , msg, t in bag.read_messages(topics = topic):
                self.data['compass']['time'] = np.append(self.data['compass']['time'], t.to_time())
                self.data['compass']['angle'] = np.append(self.data['compass']['angle'], msg.data)


            self.data['gps_global'] = {'time':np.array([]), 'latitude':np.array([]), 'longitude':np.array([]), 'altitude':np.array([])}
            topic = '/mavros/global_position/global'
            for _ , msg, t in bag.read_messages(topics = topic):
                self.data['gps_global']['time'] = np.append(self.data['gps_global']['time'], t.to_time())
                self.data['gps_global']['latitude'] = np.append(self.data['gps_global']['latitude'], msg.latitude)
                self.data['gps_global']['longitude'] = np.append(self.data['gps_global']['longitude'], msg.longitude)
                self.data['gps_global']['altitude'] = np.append(self.data['gps_global']['altitude'], msg.altitude)
            

            self.data['gps_local'] = {'time':np.array([]), 'position':np.array([]), 'orientation':np.array([]), 'linear':np.array([]), 'angular':np.array([])}
            topic = '/mavros/global_position/local'
            for _ , msg, t in bag.read_messages(topics = topic):
                position = np.array([msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z])
                orientation = np.array([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z,msg.pose.pose.orientation.w])
                linear = np.array([msg.twist.twist.linear.x, msg.twist.twist.linear.y, msg.twist.twist.linear.z])
                angular = np.array([msg.twist.twist.angular.x, msg.twist.twist.angular.y, msg.twist.twist.angular.z])
                self.data['gps_local']['time'] = np.append(self.data['gps_local']['time'], t.to_time())
                self.data['gps_local']['position'] = np.append(self.data['gps_local']['position'], position)
                self.data['gps_local']['orientation'] = np.append(self.data['gps_local']['orientation'], orientation)
                self.data['gps_local']['linear'] = np.append(self.data['gps_local']['linear'], linear)
                self.data['gps_local']['angular'] = np.append(self.data['gps_local']['angular'], angular)
            self.data['gps_local']['position'] = np.reshape(self.data['gps_local']['position'],(-1,3))
            self.data['gps_local']['orientation'] = np.reshape(self.data['gps_local']['orientation'],(-1,4))
            self.data['gps_local']['linear'] = np.reshape(self.data['gps_local']['linear'],(-1,3))
            self.data['gps_local']['angular'] = np.reshape(self.data['gps_local']['angular'],(-1,3))


            self.data['gps_raw_fix'] = {'time':np.array([]), 'latitude':np.array([]), 'longitude':np.array([]), 'altitude':np.array([])}
            topic = '/mavros/global_position/raw/fix'
            for _ , msg, t in bag.read_messages(topics = topic):
                self.data['gps_raw_fix']['time'] = np.append(self.data['gps_raw_fix']['time'], t.to_time())
                self.data['gps_raw_fix']['latitude'] = np.append(self.data['gps_raw_fix']['latitude'], msg.latitude)
                self.data['gps_raw_fix']['longitude'] = np.append(self.data['gps_raw_fix']['longitude'], msg.longitude)
                self.data['gps_raw_fix']['altitude'] = np.append(self.data['gps_raw_fix']['altitude'], msg.altitude)
            

            self.data['gps_raw_vel'] = {'time':np.array([]), 'linear':np.array([]), 'angular':np.array([])}
            topic = '/mavros/global_position/raw/gps_vel'
            for _ , msg, t in bag.read_messages(topics = topic):
                linear = np.array([msg.twist.linear.x, msg.twist.linear.y, msg.twist.linear.z])
                angular = np.array([msg.twist.angular.x, msg.twist.angular.y, msg.twist.angular.z])
                self.data['gps_raw_vel']['time'] = np.append(self.data['gps_raw_vel']['time'], t.to_time())
                self.data['gps_raw_vel']['linear'] = np.append(self.data['gps_raw_vel']['linear'], linear)
                self.data['gps_raw_vel']['angular'] = np.append(self.data['gps_raw_vel']['angular'], angular)
            self.data['gps_raw_vel']['linear'] = np.reshape(self.data['gps_raw_vel']['linear'],(-1,3))
            self.data['gps_raw_vel']['angular'] = np.reshape(self.data['gps_raw_vel']['angular'],(-1,3))


            self.data['gps_rel_alt'] = {'time':np.array([]), 'altitude':np.array([])}
            topic = '/mavros/global_position/rel_alt'
            for _ , msg, t in bag.read_messages(topics = topic):
                self.data['gps_rel_alt']['time'] = np.append(self.data['gps_rel_alt']['time'], t.to_time())
                self.data['gps_rel_alt']['altitude'] = np.append(self.data['gps_rel_alt']['altitude'], msg.data)


            self.data['home'] = {'time':np.array([]), 'latitude':np.array([]), 'longitude':np.array([]), 'altitude':np.array([]), 'position':np.array([]), 'orientation':np.array([])}
            topic = '/mavros/home_position/home'
            for _ , msg, t in bag.read_messages(topics = topic):
                position = np.array([msg.position.x, msg.position.y, msg.position.z])
                orientation = np.array([msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w])
                self.data['home']['time'] = np.append(self.data['home']['time'], t.to_time())
                self.data['home']['latitude'] = np.append(self.data['home']['latitude'], msg.geo.latitude)
                self.data['home']['longitude'] = np.append(self.data['home']['longitude'], msg.geo.longitude)
                self.data['home']['altitude'] = np.append(self.data['home']['altitude'], msg.geo.altitude)
                self.data['home']['position'] = np.append(self.data['home']['position'], position)
                self.data['home']['orientation'] = np.append(self.data['home']['orientation'], orientation)
            self.data['home']['position'] = np.reshape(self.data['home']['position'],(-1,3))
            self.data['home']['orientation'] = np.reshape(self.data['home']['orientation'],(-1,4))

            
            self.data['imu'] = {'time':np.array([]), 'orientation':np.array([]), 'ang_vel':np.array([]), 'lin_acc':np.array([])}
            topic = '/mavros/imu/data'
            for _ , msg, t in bag.read_messages(topics = topic):
                orientation = np.array([msg.orientation.x, msg.orientation.y, msg.orientation.z,msg.orientation.w])
                ang_vel = np.array([msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z])
                lin_acc = np.array([msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z])
                self.data['imu']['time'] = np.append(self.data['imu']['time'], t.to_time())
                self.data['imu']['orientation'] = np.append(self.data['imu']['orientation'], orientation)
                self.data['imu']['ang_vel'] = np.append(self.data['imu']['ang_vel'], ang_vel)
                self.data['imu']['lin_acc'] = np.append(self.data['imu']['lin_acc'], lin_acc)
            self.data['imu']['orientation'] = np.reshape(self.data['imu']['orientation'],(-1,4))
            self.data['imu']['lin_acc'] = np.reshape(self.data['imu']['lin_acc'],(-1,3))
            self.data['imu']['ang_vel'] = np.reshape(self.data['imu']['ang_vel'],(-1,3))


            self.data['imu_raw'] = {'time':np.array([]), 'orientation':np.array([]), 'ang_vel':np.array([]), 'lin_acc':np.array([])}
            topic = '/mavros/imu/data_raw'
            for _ , msg, t in bag.read_messages(topics = topic):
                orientation = np.array([msg.orientation.x, msg.orientation.y, msg.orientation.z,msg.orientation.w])
                ang_vel = np.array([msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z])
                lin_acc = np.array([msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z])
                self.data['imu_raw']['time'] = np.append(self.data['imu_raw']['time'], t.to_time())
                self.data['imu_raw']['orientation'] = np.append(self.data['imu_raw']['orientation'], orientation)
                self.data['imu_raw']['ang_vel'] = np.append(self.data['imu_raw']['ang_vel'], ang_vel)
                self.data['imu_raw']['lin_acc'] = np.append(self.data['imu_raw']['lin_acc'], lin_acc)
            self.data['imu_raw']['orientation'] = np.reshape(self.data['imu_raw']['orientation'],(-1,4))
            self.data['imu_raw']['lin_acc'] = np.reshape(self.data['imu_raw']['lin_acc'],(-1,3))
            self.data['imu_raw']['ang_vel'] = np.reshape(self.data['imu_raw']['ang_vel'],(-1,3))


            self.data['imu_mag'] = {'time':np.array([]), 'mag':np.array([])}
            topic = '/mavros/imu/mag'
            for _ , msg, t in bag.read_messages(topics = topic):
                mag = np.array([msg.magnetic_field.x, msg.magnetic_field.y, msg.magnetic_field.z])
                self.data['imu_mag']['time'] = np.append(self.data['imu_mag']['time'], t.to_time())
                self.data['imu_mag']['mag'] = np.append(self.data['imu_mag']['mag'], mag)
            self.data['imu_mag']['mag'] = np.reshape(self.data['imu_mag']['mag'],(-1,3))


            self.data['imu_pressure'] = {'time':np.array([]), 'pressure':np.array([])}
            topic = '/mavros/imu/static_pressure'
            for _ , msg, t in bag.read_messages(topics = topic):
                self.data['imu_pressure']['time'] = np.append(self.data['imu_pressure']['time'], t.to_time())
                self.data['imu_pressure']['pressure'] = np.append(self.data['imu_pressure']['pressure'], msg.fluid_pressure)

            
            self.data['imu_temperature'] = {'time':np.array([]), 'temperature':np.array([])}
            topic = '/mavros/imu/temperature_baro'
            for _ , msg, t in bag.read_messages(topics = topic):
                self.data['imu_temperature']['time'] = np.append(self.data['imu_temperature']['time'], t.to_time())
                self.data['imu_temperature']['temperature'] = np.append(self.data['imu_temperature']['temperature'], msg.temperature)

            
            self.data['local_odom'] = {'time':np.array([]), 'position':np.array([]), 'orientation':np.array([]), 'linear':np.array([]), 'angular':np.array([])}
            topic = '/mavros/local_position/odom'
            for _ , msg, t in bag.read_messages(topics = topic):
                position = np.array([msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z])
                orientation = np.array([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z,msg.pose.pose.orientation.w])
                linear = np.array([msg.twist.twist.linear.x, msg.twist.twist.linear.y, msg.twist.twist.linear.z])
                angular = np.array([msg.twist.twist.angular.x, msg.twist.twist.angular.y, msg.twist.twist.angular.z])
                self.data['local_odom']['time'] = np.append(self.data['local_odom']['time'], t.to_time())
                self.data['local_odom']['position'] = np.append(self.data['local_odom']['position'], position)
                self.data['local_odom']['orientation'] = np.append(self.data['local_odom']['orientation'], orientation)
                self.data['local_odom']['linear'] = np.append(self.data['local_odom']['linear'], linear)
                self.data['local_odom']['angular'] = np.append(self.data['local_odom']['angular'], angular)
            self.data['local_odom']['position'] = np.reshape(self.data['local_odom']['position'],(-1,3))
            self.data['local_odom']['orientation'] = np.reshape(self.data['local_odom']['orientation'],(-1,4))
            self.data['local_odom']['linear'] = np.reshape(self.data['local_odom']['linear'],(-1,3))
            self.data['local_odom']['angular'] = np.reshape(self.data['local_odom']['angular'],(-1,3))


            self.data['local_pose'] = {'time':np.array([]), 'position':np.array([]), 'orientation':np.array([])}
            topic = '/mavros/local_position/pose'
            for _ , msg, t in bag.read_messages(topics = topic):
                position = np.array([msg.pose.position.x, msg.pose.position.y, msg.pose.position.z])
                orientation = np.array([msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w])
                self.data['local_pose']['time'] = np.append(self.data['local_pose']['time'], t.to_time())
                self.data['local_pose']['position'] = np.append(self.data['local_pose']['position'], position)
                self.data['local_pose']['orientation'] = np.append(self.data['local_pose']['orientation'], orientation)
            self.data['local_pose']['position'] = np.reshape(self.data['local_pose']['position'],(-1,3))
            self.data['local_pose']['orientation'] = np.reshape(self.data['local_pose']['orientation'],(-1,4))


            self.data['local_vel_body'] = {'time':np.array([]), 'linear':np.array([]), 'angular':np.array([])}
            topic = '/mavros/local_position/velocity_body'
            for _ , msg, t in bag.read_messages(topics = topic):
                linear = np.array([msg.twist.linear.x, msg.twist.linear.y, msg.twist.linear.z])
                angular = np.array([msg.twist.angular.x, msg.twist.angular.y, msg.twist.angular.z])
                self.data['local_vel_body']['time'] = np.append(self.data['local_vel_body']['time'], t.to_time())
                self.data['local_vel_body']['linear'] = np.append(self.data['local_vel_body']['linear'], linear)
                self.data['local_vel_body']['angular'] = np.append(self.data['local_vel_body']['angular'], angular)
            self.data['local_vel_body']['linear'] = np.reshape(self.data['local_vel_body']['linear'],(-1,3))
            self.data['local_vel_body']['angular'] = np.reshape(self.data['local_vel_body']['angular'],(-1,3))

            #mavros/mission/waypoints
            self.data['rc_in'] = {'time':np.array([]), 'channels':np.array([])}
            topic = '/mavros/rc/in'
            for _ , msg, t in bag.read_messages(topics = topic):
                self.data['rc_in']['time'] = np.append(self.data['rc_in']['time'], t.to_time())
                self.data['rc_in']['channels'] = np.append(self.data['rc_in']['channels'], msg.channels)
            self.data['rc_in']['channels'] = np.reshape(self.data['rc_in']['channels'],(-1,16))


            self.data['rc_out'] = {'time':np.array([]), 'channels':np.array([])}
            topic = '/mavros/rc/out'
            for _ , msg, t in bag.read_messages(topics = topic):
                self.data['rc_out']['time'] = np.append(self.data['rc_out']['time'], t.to_time())
                self.data['rc_out']['channels'] = np.append(self.data['rc_out']['channels'], msg.channels)
            self.data['rc_out']['channels'] = np.reshape(self.data['rc_out']['channels'],(-1,8))

            #/mavros/state
            #/mavros/time_reference
            self.data['vfr_hud'] = {'time':np.array([]), 'airspeed':np.array([]), 'groundspeed':np.array([]), 'heading':np.array([]), 'throttle':np.array([]), 'altitude':np.array([]), 'climb':np.array([])}
            topic = '/mavros/vfr_hud'
            for _ , msg, t in bag.read_messages(topics = topic):
                self.data['vfr_hud']['time'] = np.append(self.data['vfr_hud']['time'], t.to_time())
                self.data['vfr_hud']['airspeed'] = np.append(self.data['vfr_hud']['airspeed'], msg.airspeed)
                self.data['vfr_hud']['groundspeed'] = np.append(self.data['vfr_hud']['groundspeed'], msg.groundspeed)
                self.data['vfr_hud']['heading'] = np.append(self.data['vfr_hud']['heading'], msg.heading)
                self.data['vfr_hud']['throttle'] = np.append(self.data['vfr_hud']['throttle'], msg.throttle)
                self.data['vfr_hud']['altitude'] = np.append(self.data['vfr_hud']['altitude'], msg.altitude)
                self.data['vfr_hud']['climb'] = np.append(self.data['vfr_hud']['climb'], msg.climb)
            #/pylon_camera_node/camera_info
            #1536x2048
            #/pylon_camera_node/image_raw

            topic = '/pylon_camera_node/image_raw/compressed'
            for _ , msg, t in bag.read_messages(topics = topic):
                time = 1000*t.to_time()
                image = msg.data
                with open('images/'+str(int(time))+'.JPG','wb') as filehandle:
                    filehandle.write(bytes(image))

            #img = mpimg.imread(image)
            #plt.imshow(img)
            #plt.show()
            

        def show_data(self):
            print('Show Nothing')
            #print(self.data['vfr_hud']['altitude'])

        def export_data(self):
            return self.data



    MV = mavros(bag)
    MV.show_data()
    data = MV.export_data()
    pickle_out = open("sensor_data.pickle","wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()

    position_XYZ = data['local_pose']['position']
    orientation_XYZW  = data['local_pose']['orientation']
    velocityLinear_XYZ  = data['local_odom']['linear']
    velocityAngular_XYZ = data['local_odom']['angular']
    accelerationLinear_XYZ = data['imu']['lin_acc']

    np.savetxt("position_XYZ.csv", position_XYZ, delimiter=",") 
    np.savetxt("orientation_XYZW.csv", orientation_XYZW, delimiter=",")
    np.savetxt("velocityLinear_XYZ.csv", velocityLinear_XYZ, delimiter=",")
    np.savetxt("velocityAngular_XYZ.csv", velocityAngular_XYZ, delimiter=",")
    np.savetxt("accelerationLinear_XYZ.csv", accelerationLinear_XYZ, delimiter=",")

bag.close()