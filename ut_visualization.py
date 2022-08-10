
import numpy as np
import matplotlib.pyplot as plt



def plot_2d(da_x, da_y, N, n_i, s_line_lengehd, s_name_legend, s_name_ti, s_name_x, s_name_y, s_path_output, \
            if_grid, if_axis_equal, if_save_pdf, if_limit_x, x_limit, if_limit_y, y_limit, if_show=1, \
            legend_loc="upper right", fs=14, 
            if_use_shift=0, x_shift_legend=1.1, y_shift_legend=1.0,
            if_fig_size=0, fig_width=10., fig_hei=7.,
            if_plot_err_range_=0, da_y_err_range_=[], 
            color_err_range_="b", color_err_lw_=2, color_err_capsize_=4):
    # Description:
    # da_x and da_y are lists which contain N lists, corresponding to each other
    # s_line_lengehd and s_name_legend are the list of strings, both has N nodes
    # n_i[k] records the lengh of data in for the k-th column of da_x, da_y
    N_x = len(da_x)
    N_y = len(da_y)
    N_name_legend = len(s_name_legend)
    
    if (N_x!=N or N_y!=N or len(n_i)!=N or len(s_line_lengehd)!=N or N_name_legend!=N):
           print ("Error, N=%d, N_x=%d, N_y=%d, N_n_i=%d, N_line_shape=%d, N_name_legend=%d\n" \
                  %(N, N_x, N_y, len(n_i), len(s_line_lengehd), N_name_legend))
           return -1
    if if_fig_size == 1:
        fig = plt.figure(figsize=(fig_width,fig_hei))
    else:   
        fig = plt.figure()
    line = []
    for i in range(0, N):
        if if_plot_err_range_ == 0:
            line.append(plt.plot(da_x[i][0:n_i[i]], da_y[i][0:n_i[i]], s_line_lengehd[i]))
#            line.append(plt.plot(da_x[i][0:n_i[i]], da_y[i][0:n_i[i]], \
#                        s_line_lengehd[i], label=s_name_legend[i]))
        else:
            line.append(plt.errorbar(da_x[i][0:n_i[i]], da_y[i][0:n_i[i]], \
                             fmt=s_line_lengehd[i], 
                             yerr=da_y_err_range_[i][0:n_i[i]],
                             ecolor=color_err_range_, elinewidth=color_err_lw_,
                             capsize=color_err_capsize_))
#    plt.legend(s_name_legend[0:N], prop={'size': 6})
    if if_use_shift == 1:
        plt.legend(s_name_legend[0:N], prop={'size': fs}, loc=legend_loc, bbox_to_anchor=(x_shift_legend, y_shift_legend)) #, 
    else:
        plt.legend(s_name_legend[0:N], prop={'size': fs}, loc=legend_loc) #, 
        
    plt.title(s_name_ti, fontsize=fs)
    plt.xlabel(s_name_x, fontsize=fs)
    plt.ylabel(s_name_y, fontsize=fs)
    plt.tick_params(labelsize=fs)
    
    if if_axis_equal: 
        plt.axis("equal")
    if if_limit_x:
        plt.xlim(x_limit[0], x_limit[1])
    if if_limit_y:
        plt.ylim(y_limit[0], y_limit[1])   
    if if_grid:
        plt.grid(True)
    if if_save_pdf:
        #plt.savefig(s_path_output+s_name_ti+".pdf")
        pass;
    if if_show:
        plt.show(block=False)
    return (fig)




