def barcode_listbc(b1_dir, b2_dir, b3_dir):
    list1 = []
    fl = open(b1_dir)
    for line in fl:
        barcode = line.rstrip().split('\t')[-1]
        list1.append(barcode)
    fl.close()

    list2 = []
    fm = open(b2_dir)
    for line in fm:
        barcode = line.rstrip().split('\t')[-1]
        list2.append(barcode)
    fm.close()

    list3 = []
    fn = open(b3_dir)
    for line in fn:
        barcode = line.rstrip().split('\t')[-1]
        list3.append(barcode)
    fn.close()

    return list1, list2, list3
