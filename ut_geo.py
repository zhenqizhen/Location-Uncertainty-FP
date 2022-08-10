

import numpy as np
import ut_const as con



def llh_to_enu(llh, llh0):    # unit_ll=rad
    assert len(llh) > 2
    assert len(llh0) > 2
    h = llh[2]
    if isinstance(llh[0], list):        
        d_lat = list(map(lambda x: x-llh0[0], llh[0]))
        d_lon = list(map(lambda x: x-llh0[1], llh[1]))
        rmh = list(map(lambda x: x+con.Rm, h))  
        rncosah = list(map(lambda x,y: x+con.Rn*np.cos(y), h, llh[0]))    
        n = list(map(lambda x,y: x * y, d_lat, rmh))      # d_lat->n
        e = list(map(lambda x,y: x * y, d_lon, rncosah))  # d_lon->e
        return list([e, n, h])
    elif isinstance(llh[0], (int, float)):
        n = (llh[0] - llh0[0]) * (con.Rm + h)
        e = (llh[1] - llh0[1]) * (con.Rn * np.cos(llh[0]) + h)
        return list([e, n, h])
    else:
        print("Error in llh_to_enu(), input not list or values\n")
        return 

def trans_global_to_local(lat_list, lon_list, ZERO_POS, TYPE_COOR):
    if TYPE_COOR == 'deg':
        lat_rad = list(map(lambda a: a*con.D2R, lat_list))
        lon_rad = list(map(lambda a: a*con.D2R, lon_list))
        ZERO_LAT = ZERO_POS[0]*con.D2R
        ZERO_LON = ZERO_POS[1]*con.D2R
    elif TYPE_COOR == 'rad':
        lat_rad = lat_list
        lon_rad = lon_list
        ZERO_LAT = ZERO_POS[0]
        ZERO_LON = ZERO_POS[1]
    else:
        print ("Error, TYPE_COOR!='deg' or 'rad'\n")
    
    height_ = ZERO_POS[2]
    if len(ZERO_POS) == 2:
        height_ = 0

    x_list = list(map(lambda x: (x-ZERO_LON)*(con.Rn+height_)*np.cos(ZERO_LAT), lon_rad))
    y_list = list(map(lambda y: (y-ZERO_LAT)*(con.Rm+height_), lat_rad))
    
    return (x_list, y_list)

