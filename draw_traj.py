"""
@author: Zhenqi Zheng, You Li 
"""
import numpy as np
import ut_io as io
import ut_visualization as vs
import matplotlib.pyplot as plt
import ut_geo as geo



#Origin coordinates 
ZERO_POS = [30.528322, 114.349572, 12]
FS_PLOT = 14

#The folder where the database is generated
path1="./data/traj/database_traj/"

da_E1=[]
da_N1=[]

for i in range(8):
    i=str(i+1)
    file_name = "traj_"+i
    data_name_dot = file_name + ".DAT"  
    file_dot = path1 + data_name_dot
    # load da_dot
    da_dot = io.read_bin_matrix_to_list(file_dot, 4, np.float64)
    print(data_name_dot+" Loaded!")
    #trans da_dot from globale to local 
    (da_dotE_list, da_dotN_list) = geo.trans_global_to_local(da_dot[1], da_dot[2], ZERO_POS, 'deg')
    da_E1.append(da_dotE_list)
    da_N1.append(da_dotN_list)


#draw the traj 1 and 2 which generate the database 
fig=plt.figure()
plt.title('Database trajectory 1 and 2')
plt.plot(da_E1[0], da_N1[0],'r-')
plt.plot(da_E1[1], da_N1[1],'b-.')
plt.xlim(40, 170)
plt.ylim(25, 100)
plt.grid(True)
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.legend([r"Traj_1",r"Traj_2"])
plt.show()

#draw the traj 3 and 4 which generate the database 
fig=plt.figure()
plt.title('Database trajectory 3 and 4')
plt.plot(da_E1[2], da_N1[2],'r-')
plt.plot(da_E1[3], da_N1[3],'b-.')
plt.xlim(40, 170)
plt.ylim(25, 100)
plt.grid(True)
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.legend([r"Traj_3",r"Traj_4"])
plt.show()

#draw the traj 5 and 6 which generate the database 
fig=plt.figure()
plt.title('Database trajectory 5 and 6')
plt.plot(da_E1[4], da_N1[4],'r-')
plt.plot(da_E1[5], da_N1[5],'b-.')
plt.xlim(40, 170)
plt.ylim(25, 100)
plt.grid(True)
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.legend([r"Traj_5",r"Traj_6"])
plt.show()

#draw the traj 7 and 8 which generate the database
fig=plt.figure()
plt.title('Database trajectory 7 and 8')
plt.plot(da_E1[6], da_N1[6],'r-')
plt.plot(da_E1[7], da_N1[7],'b-.')
plt.xlim(40, 170)
plt.ylim(25, 100)
plt.grid(True)
plt.xlabel('East(m)')
plt.ylabel('North(m)')
plt.legend([r"Traj_7",r"Traj_8"])
plt.show()



#draw the traj 1 and 2 which test traj
path2="./data/traj/test_traj/"
for i in range(2):
    i=str(i+1)
    file_name = "traj_"+i
    data_name_dot = file_name + ".DAT"  
    file_dot = path2 + data_name_dot
    da_dot = io.read_bin_matrix_to_list(file_dot, 4, np.float64)
    (da_dotE_list, da_dotN_list) = geo.trans_global_to_local(da_dot[1], da_dot[2], ZERO_POS, 'deg')

    print(data_name_dot+" Loaded！")
    fig=plt.figure()
    plt.title("Test trajectory "+i)
    plt.plot(da_dotE_list, da_dotN_list,'b-')
    plt.xlim(40, 170)
    plt.ylim(25, 100)
    plt.grid(True)
    plt.xlabel('East(m)')
    plt.ylabel('North(m)')
    plt.legend([r"Traj_"+i])
    plt.axis("equal")
    plt.show()

