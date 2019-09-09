def barcode_to_round_id(in_dir):  # link barcode name with barcode
    fl = open(in_dir)
    dict_bc1 = {}
    dict_bc2 = {}
    dict_bc3 = {}
    for line in fl:
        seq = line.split('\t')
        barcode1 = seq[1]
        barcode2 = seq[3]
        barcode3 = seq[5]
        dict_bc1[barcode1] = seq[0]
        dict_bc2[barcode2] = seq[2]
        dict_bc3[barcode3] = seq[4]
    dict_bc1['others'] = 'others'
    dict_bc2['others'] = 'others'
    dict_bc3['others'] = 'others'
    return dict_bc1, dict_bc2, dict_bc3
