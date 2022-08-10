

import numpy as np

import ut_data_special as ut_data



def fingerprinting_1d(rss_meas_, 
                      map_rp_mean_rss_, map_rp_std_rss_, list_rp_id_,
                      map_rp_loc_, n_knn_,
                      mode_=0, rss_invalid_=-120):
    ll_rp = [99999 for _ in range(len(list_rp_id_))]  # record likelihood for each RP at each epoch
    
   
    for j in range(len(list_rp_id_)):  # RP (not RP id!)
        id_rp_j = list_rp_id_[j]  # The id of j-th RP
        rss_ref_j = map_rp_mean_rss_[id_rp_j]
        
        # Compare the likelihood for each RP and record
        #ed_j = ut_data.cal_ed(rss_meas_, rss_ref_j, len(rss_meas_))
        ed_j = ut_data.cal_ed_remove_invalid(rss_meas_, rss_ref_j, len(rss_meas_), invalid_=rss_invalid_)
        ll_j = ut_data.cal_reciprocal(ed_j)
        
        ll_rp[j] = ll_j
    
    # Find the n_knn RPs that has the highest likelihood
    (ind_sel, ll_sel) = ut_data.find_K_smallest_or_largest(ll_rp, n_knn_, 0)
    
    id_sel = ut_data.select_given_rows([list_rp_id_], ind_sel)
    id_sel = id_sel[0]
    
    # Get the location of selected RP
    east_sel = []
    north_sel = []
    height_sel = []
    buqueding_sel = []
    
    for j in range(n_knn_):
        id_j = id_sel[j]
        pos_id_j = map_rp_loc_[id_j]
        east_sel.append(pos_id_j[0])
        north_sel.append(pos_id_j[1])
        height_sel.append(pos_id_j[2])
        buqueding_sel.append(pos_id_j[3])
    
    # Compute the user location from KNN
    (east_user,weight_vec_,weightbuquedingdu,weightbuquedingdu_vec)= ut_data.cal_weighted_averg(east_sel, ll_sel,buqueding_sel)
    (north_user,weight_vec_,weightbuquedingdu,weightbuquedingdu_vec) = ut_data.cal_weighted_averg(north_sel, ll_sel,buqueding_sel)
    (height_user,weight_vec_,weightbuquedingdu,weightbuquedingdu_vec) = ut_data.cal_weighted_averg(height_sel, ll_sel,buqueding_sel)
     
    
    return [east_user, north_user, height_user,weight_vec_,weightbuquedingdu,weightbuquedingdu_vec,ll_sel,buqueding_sel]
        