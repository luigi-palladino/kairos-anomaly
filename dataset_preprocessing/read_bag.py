from bagpy import bagreader
import bagpy
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np

def find_neighbours(value, df, colname):
    exactmatch = df[df[colname] == value]
    if not exactmatch.empty:
        return exactmatch.index
    else:
        lowerneighbour_ind = df[df[colname] < value][colname].idxmax()
        upperneighbour_ind = df[df[colname] > value][colname].idxmin()
        return [lowerneighbour_ind, upperneighbour_ind] 

name = 'window_plan_1'
robot = 'fufi'

hz_list=[]
bag = bagreader('raw/' + name + '.bag')
table = bag.topic_table
table.to_csv('raw/topic_map_' + name + '.csv')
pd.set_option('display.float_format', lambda x: '%.7f' % x)

laser_front =  bag.message_by_topic('/' + robot + '/front_laser/scan')
laser_rear =  bag.message_by_topic('/' + robot + '/rear_laser/scan')
pose =  bag.message_by_topic('/' + robot + '/robot_pose')
joint_states =  bag.message_by_topic('/' + robot + '/joint_states')
temp =  bag.message_by_topic('/' + robot + '/vectornav/imu/temperature')
cmd_vel =  bag.message_by_topic('/' + robot + '/robotnik_base_control/cmd_vel')
imu =  bag.message_by_topic('/' + robot + '/imu/data')
vel =  bag.message_by_topic('/' + robot + '/robotnik_base_control/odom')


data0 = table.query("Topics == '/fufi/front_laser/scan'")
data1 = table.query("Topics == '/fufi/rear_laser/scan'")
data2 = table.query("Topics == '/fufi/robot_pose'")
data3 = table.query("Topics == '/fufi/joint_states'")
data4 = table.query("Topics == '/fufi/vectornav/imu/temperature'")
data5 = table.query("Topics == '/fufi/robotnik_base_control/cmd_vel'")
data6 = table.query("Topics == '/fufi/imu/data'")
data7 = table.query("Topics == '/fufi/robotnik_base_control/odom'")
data = pd.concat([data0, data1, data2, data3, data4, data5, data6, data7], axis=0)
data.to_csv('raw/' + name + '/topic_info.csv', index=False)


