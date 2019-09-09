def barcode_to_cell_no_mix(in_dir1, in_dir2, in_dir3, out_dir):
    fl = open(in_dir1)
    fm = open(in_dir2)
    fn = open(in_dir3)
    fo = open(out_dir, 'w')
    list1 = []
    dict1 = {}  # name
    list2 = []
    dict2 = {}  # name
    list3 = []
    dict3 = {}  # name
    for line in fl:
        barcode1 = line.rstrip().split('\t')[-1]
        name1 = line.rstrip().split('\t')[2]
        list1.append(barcode1)
        dict1[barcode1] = name1
    for line in fm:
        barcode2 = line.rstrip().split('\t')[-1]
        name2 = line.rstrip().split('\t')[1]
        list2.append(barcode2)
        dict2[barcode2] = name2
    for line in fn:
        barcode3 = line.rstrip().split('\t')[-1]
        name3 = line.rstrip().split('\t')[1]
        list3.append(barcode3)
        dict3[barcode3] = name3
    i = 1
    j = 0  # mix barcode1_01 and barcode1_49
    for barcode3 in list3:
        for barcode2 in list2:
            for barcode1 in list1:
                fo.write(dict1[barcode1] + '\t' + barcode1 + '\t' + dict2[barcode2] + '\t' + barcode2 + '\t' + dict3[
                    barcode3] + '\t' + barcode3 + '\t' + barcode1 + barcode2 + barcode3 + '\t' + 'Cell_' + str(
                    i) + '-' + str(j) + '\n')
                if j == 0:
                    j = 1
                else:
                    j = 0
                    i += 1
    fl.close()
    fm.close()
    fn.close()
    fo.close()
