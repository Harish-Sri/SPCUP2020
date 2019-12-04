import pickle
import numpy as np
import matplotlib.pyplot as plt

pickle_in = open("sensor_data.pickle","rb")
data = pickle.load(pickle_in)

'''
PICKLE DETAILS
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
'''
# similar data
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

'''
x1 = data['local_pose']['time']
y1 = data['local_pose']['position']

x2 = data['local_odom']['time']
y2 = data['local_odom']['linear']

x3 = data['imu']['time']
y3 = data['imu']['lin_acc']

#x3 = data['imu']['time']
#y3 = data['imu']['lin_acc']

#x4 = data['local_odom']['time']
#y4 = data['local_odom']['linear']

#x5 = data['local_pose']['time']
#y5 = data['local_pose']['orientation']

#print(np.shape(positionXYZ), np.shape(orientationXYZW),np.shape(linearXYZ),np.shape(angularXYZ))
#print(np.shape(latitude), np.shape(longitude),np.shape(altitude),np.shape(acceleration))

#print(np.shape(y2[:,1]))

a = 3

plt.subplot(a,1,1), plt.plot(x1,y1)
plt.subplot(a,1,2), plt.plot(x2,y2)
plt.subplot(a,1,3), plt.plot(x3,y3)
#plt.subplot(a,1,4), plt.plot(x4,y4)
#plt.subplot(a,1,5), plt.plot(x5,y5)
plt.show()

'''