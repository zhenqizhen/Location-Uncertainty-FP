

import numpy as np

def cal_ed_remove_invalid(v1_, v2_, n_, invalid_=-120):
    dv_ = []
    count_ = 0
    for i in range(n_):
        if v2_[i]!=invalid_ and v1_[i]!=invalid_:
            count_ += 1
            dv_.append(v2_[i]-v1_[i])
    if count_ == 0:
        return 99999
    else:
        res = np.linalg.norm(dv_) / np.sqrt(count_)
        return (res)

def cal_weighted_averg(val_vec_, weight_vec_,buquedingdu):
    sumbuquedingdu=0.0
    weightbuquedingdu=[]
    weightbuquedingdu_vec=[]
    for i in range(len(val_vec_)):
        if(buquedingdu[i]==0):
            buquedingdu[i]=0.1
            k=1/buquedingdu[i]
            weightbuquedingdu.append(k)
        else:
           k=1/buquedingdu[i]
           weightbuquedingdu.append(k)
    sum_sel = 0.0
    weight_sel = 0.0
    for i in range(len(val_vec_)):
        k=weight_vec_[i]*weightbuquedingdu[i]
        weight_sel=weight_sel+k
        weightbuquedingdu_vec.append(k)
        sum_sel=sum_sel+val_vec_[i]*k

    if np.abs(weight_sel) < 0.001:
        return 9999
    jieguo=sum_sel / weight_sel
    
    return(jieguo,weight_vec_,weightbuquedingdu,weightbuquedingdu_vec)

def cal_reciprocal(a, flag_threshold=1, threshold_small=0.1):
    if flag_threshold==1 and a<threshold_small:
        a = threshold_small
    return 1.0 / float(a)


def find_K_smallest_or_largest(list_a, K, if_smallest):
    a_arr = np.array(list_a)    
    if if_smallest == 0:  
        ind = np.argpartition(a_arr, -K)[-K:]
    else:
        ind = np.argpartition(a_arr, K)[:K]
    return (list(ind), list(a_arr[ind]))


def select_given_rows(da, ids):
    if not isinstance(da, list): 
        print("Error in select(), input should be a list")
        return 
    if isinstance(da[0], (int, float)):
        print("Error in select(), each element in the list should be a list")  
        return
    da_selected = []
    for i in range(len(da)):
        da_1list_selected = [0] * len(ids)
        for j in range(len(ids)):
            if ids[j] >= len(da[i]):
                print("Error in select(), ids[%d] >=  len(da[%d])" %(j,i)) 
                return
            da_1list_selected[j] = da[i][ids[j]]
        da_selected.append(da_1list_selected)
    return da_selected







