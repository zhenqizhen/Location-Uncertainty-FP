

import numpy as np


def transpose_list(da):
    da_t = [[row[i] for row in da] for i in range(len(da[0]))]
    return da_t


def cal_cdf(sample):
    import statsmodels.api as sm # recommended import according to the docs
    ecdf = sm.distributions.ECDF(sample)
    x = np.linspace(min(sample), max(sample))
    y = ecdf(x)
    return (x,y)

def cal_rms(vec_):
    rms_ = np.sqrt(np.mean(np.square(vec_)))
    return rms_


def cal_statics(vec):
    range_v = max(vec) - min(vec)
    mean = np.mean(vec)
    median = np.median(vec)
    std = np.std(vec)
    rms = cal_rms(vec)
    
    v1 = np.sort(vec)
    d80 = v1[int(len(v1)*0.8)]
    d90 = v1[int(len(v1)*0.9)]
    d95 = v1[int(len(v1)*0.95)]
    return (range_v, mean, median, std, rms, d80, d90, d95)


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


def cal_weighted_averg(val_vec_, weight_vec_):
    sum_sel = 0.0
    weight_sel = 0.0
    for i in range(len(val_vec_)):
        sum_sel += val_vec_[i]*weight_vec_[i]
        weight_sel += weight_vec_[i]
    if np.abs(weight_sel) < 0.001:
        return 9999
    return sum_sel / weight_sel