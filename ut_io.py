

import numpy as np


def read_bin_matrix_to_list(fname_bin, n_col, data_type):
    with open(fname_bin, 'rb') as fid:
        da = np.fromfile(fid, data_type).reshape((-1, n_col)).T
        da_list = da.tolist()
        return da_list
    

    
def remove_blank_head_tail(str1):
    if len(str1)==0:
        return str1
    
    i_start = 0
    i_end = len(str1)
    
    # Remove blank in head
    for p in range(len(str1)):
        if str1[p] == '\t' or str1[p] == ' ':
            i_start = i_start+1
        else:
            break
    
    # Remove blank in tail
    for p in range(len(str1)):
        if str1[-1-p] == '\t' or str1[-1-p] == ' ':
            i_end = i_end-1
        else:
            break
    
    if i_start >= i_end:
        print ('Error! i_start >= i_end in remove_blank_head_tail.')
        return str1
        
    return str1[i_start:i_end]
    

def load_text_file(fname, list_format, delim, usecols=None):
    if len(delim) > 4:
        print ('Delimiter is too long.')
    if delim in [' ','  ','   ','    ']:
        fid = np.genfromtxt(fname,dtype='str',usecols=usecols).tolist()
    else:
        fid = np.genfromtxt(fname,dtype='str',delimiter=delim,usecols=usecols).tolist()
    
    if len(fid) == 0:
        da_out = []
        return (da_out)
    
    da = []
    if not isinstance(fid, list) :  #has 1 column and 1 row (1 data)
        da = [[fid]]
    elif not isinstance(fid[0], list) and len(list_format) == 1:  #has 1 column
        da = [fid]
    elif not isinstance(fid[0], list) and not len(list_format) == 1:  #has 1 row
        for i in range(len(fid)):
            da.append([fid[i]])
    else:
        da = [[] for _ in range(len(fid[0]))]
        for i in range(len(fid[0])):
            for j in range(len(fid)):
                da[i].append(fid[j][i])
    
    da_out = []
    if len(list_format) > len(da):
        print('Warning in load_text_file(), len(list_format) > len(fid[0]), \
              remaining elements in list_format are not loaded')
        list_format = list_format[:len(da)]
        
    for i in range(len(list_format)):
        if list_format[i]=='%s':
            col1 = [str(j) for j in da[i]]
            if not delim in [' ','  ','   ','    ']:
            # -----------remove blanks for str----------------    
                for k in range(len(col1)):
                    str1 = col1[k]
                    if delim != ' ':
                        col1[k] = remove_blank_head_tail(str1);
        elif list_format[i]=='%d':
            col1 = [int(j) for j in da[i]]
        elif list_format[i]=='%f':
            col1 = [float(j) for j in da[i]]
        else:
            print ('Not valid format.')
        da_out.append(col1)

    return (da_out)




    

                    








        
        