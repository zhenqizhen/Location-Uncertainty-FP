"""
@author: Zhenqi Zheng, You Li 
"""
import numpy as np
import ut_io as io
import ut_data as ud
import matplotlib.pyplot as plt
import ut_geo as geo
import ut_const as con
import copy



#define Origin coordinates，AP arrary num
ZERO_POS = [30.528322, 114.349572, 12]
APLNUM=7
finalnum=19
bubble_area=5

#define heat map
def plot_scatter_heatmap(lat_deg, lon_deg, value, ZERO_POS, bubble_area, s_name_ti="", transp=0.45, num_label=5,\
                         s_name_x="East(m)", s_name_y="North(m)",\
                         if_grid=1, if_axis_equal=0, if_limit_x=1, x_limit=[25, 190], if_limit_y=1, y_limit=[0,120], if_show=1,
                         value_max=-40, value_min=-100, value_level=10, fs = 14,
                         if_fill_val_beyond=0, format_bar_="%.1f",
                         if_fig_axis_scale_=0, fig_axis_scale_x_=5, fig_axis_scale_y_=3):

    
    if if_fill_val_beyond:
        for i in range(len(value)):
            if value[i] > value_max:
                value[i] = value_max
            if value[i] < value_min:
                value[i] = value_min
                
    
    lat_rad = list(map(lambda x: x*con.D2R, lat_deg))
    lon_rad = list(map(lambda x: x*con.D2R, lon_deg))
    llh = [lat_rad, lon_rad, [0 for _ in range(len(lat_rad))]]
    llh0 = [ZERO_POS[0]*con.D2R, ZERO_POS[1]*con.D2R, ZERO_POS[2]]
    
    enu = geo.llh_to_enu(llh, llh0)
    
    x = enu[0]
    y = enu[1]
    v = value
    
    colors = np.array(v)
    labels = np.linspace(value_min, value_max, value_level)

    
    if if_fig_axis_scale_ == 1:
        sc = plt.figure(figsize=(fig_axis_scale_x_,fig_axis_scale_y_))
    else:
        sc = plt.figure()
    plt.scatter(x, y, s=bubble_area, c=colors, alpha=1.0)#
    cbar = plt.colorbar(ticks=labels, format=format_bar_)
    cbar.ax.tick_params(labelsize=fs-2) 
    plt.title(s_name_ti, fontsize=fs)
    plt.xlabel(s_name_x, fontsize=fs)
    plt.ylabel(s_name_y, fontsize=fs)
    plt.tick_params(labelsize=fs-1)
    
    if if_axis_equal: 
        plt.axis("equal")
    if if_limit_x:
        plt.xlim(x_limit[0], x_limit[1])
    if if_limit_y:
        plt.ylim(y_limit[0], y_limit[1])   
    if if_grid:
        plt.grid(True)
    if if_show:
        plt.show()
        
    return (sc)




#define draw the database heatmap function，only the AP 6

def draw_db_heatmap(ap_wifipath,path,s_name_ti):
    
    inputf2=[]
    inputf2.append('%s')
    for i in range(1,int(APLNUM-1)):
        inputf2.append('%f')
    inputf2.append('%s')
    #load aplist.txt
    AP = io.load_text_file(ap_wifipath, inputf2, ",")
   
   
    APNUM=int(len(AP[0]))
    

    
   
    inputf1=[]

    inputf1.append('%f')
    inputf1.append('%f')
    inputf1.append('%s')
    inputf1.append('%f')
    inputf1.append('%f')
    for i in range(4,4+APNUM):
        inputf1.append('%d')
    
   


     #load database final.txt
    final = io.load_text_file(path+"final.txt", inputf1, " ")
    
    del final[4]
    
    fig=plot_scatter_heatmap(final[0], final[1], final[9], ZERO_POS, bubble_area,s_name_ti)
   
    
 
    



#---laod reference, average, weighted average database path and ap path
ap_wifipath ="./data/data_for_db&Database_final/ap_wifi.txt"


referencepath="./data/data_for_db&Database_final/robot_huamn_crowdsourcing_semantics/reference/"

   
averagefinalpath="./data/data_for_db&Database_final/robot_huamn_crowdsourcing_semantics/average/"
weighted_averagefinalpath="./data/data_for_db&Database_final/robot_huamn_crowdsourcing_semantics/Weighted_average/"

#---draw database heat map

s_name_ti="Reference Database AP 6 RSS"
draw_db_heatmap(ap_wifipath,referencepath,s_name_ti)
s_name_ti="I-A database AP 6 RSS"
draw_db_heatmap(ap_wifipath,averagefinalpath,s_name_ti)
















