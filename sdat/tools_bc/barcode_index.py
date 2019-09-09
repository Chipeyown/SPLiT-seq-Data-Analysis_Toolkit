def barcode_index(in_dir):
    fl = open(in_dir)
    dict = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}
    dict5 = {}
    for line in fl:
        seq = line.rstrip().split('\t')
        barcode = seq[6]
        barcode1 = seq[1]
        barcode2 = seq[3]
        barcode3 = seq[5]
        cell = seq[7]
        dict[barcode] = cell
        dict2[cell] = 0
        dict3[barcode1] = 0
        dict4[barcode2] = 0
        dict5[barcode3] = 0
    dict3['others'] = 0
    dict4['others'] = 0
    dict5['others'] = 0
    fl.close()
    return [dict, dict2, dict3, dict4, dict5]
