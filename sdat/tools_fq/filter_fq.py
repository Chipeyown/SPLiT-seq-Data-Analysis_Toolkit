import time
import copy


def filter_fq(R1_dir, R2_dir, filtered_dir, b1_dir, b2_dir, b3_dir, log_dir, reads_per_cell_dir, dicts, lists, e,
              job_id):
    def get_correct(bc, list):  # get the best one and one mismatch
        if len(bc) < 8:  # read2 is too short(a read2 too short bug)
            return bc
        seq0 = ''
        for seq in list:
            i = 0
            for m in range(8):
                if bc[m] == seq[m]:
                    i += 1
            if i == 8:
                return seq
            elif i == 7 and seq0 == '':
                seq0 = seq
            elif i == 7 and seq0 != '':
                seq0 += 'another'
        if seq0 == '' or seq0.endswith('another'):  # wrong or confused
            return bc
        else:
            return seq0

    def get_correct2(bc, list):  # 0 mismatch
        for seq in list:
            i = 0
            for m in range(8):
                if bc[m] == seq[m]:
                    i += 1
            if i == 8:
                return seq
        return bc

    dictss = copy.deepcopy(dicts)  # need to change the value of dict in dicts
    dict = dictss[0]  # cell and corresponding  barcode
    dict2 = dictss[1]  # for counting reads number per cell
    dict3 = dictss[2]  # for counting barcode1
    dict4 = dictss[3]  # for counting barcode2
    dict5 = dictss[4]  # for counting barcode3

    list1 = lists[0]  # barcode1
    list2 = lists[1]  # barcode2
    list3 = lists[2]  # barcode3
    fl = open(R1_dir)
    fm = open(R2_dir)
    fo = open(filtered_dir, 'w')
    fa1 = open(b1_dir, 'w')
    fa2 = open(b2_dir, 'w')
    fa3 = open(b3_dir, 'w')
    fb = open(log_dir, 'w')
    fc = open(reads_per_cell_dir, 'w')
    i = n = 0
    while True:
        l1 = fl.readline()
        l2 = fl.readline()
        l3 = fl.readline()
        l4 = fl.readline()
        L1 = fm.readline()
        L2 = fm.readline()
        L3 = fm.readline()
        L4 = fm.readline()
        if L2 == '':
            break
        bc3 = L2[10:18]
        bc2 = L2[48:56]
        bc1 = L2[86:94]
        if e == 1:
            barcode3 = get_correct(bc3, list3)
            barcode2 = get_correct(bc2, list2)
            barcode1 = get_correct(bc1, list1)
        else:
            barcode3 = get_correct2(bc3, list3)
            barcode2 = get_correct2(bc2, list2)
            barcode1 = get_correct2(bc1, list1)
        try:
            dict5[barcode3] += 1
        except:
            dict5['others'] += 1
        try:
            dict4[barcode2] += 1
        except:
            dict4['others'] += 1
        try:
            dict3[barcode1] += 1
        except:
            dict3['others'] += 1

        barcode = barcode1 + barcode2 + barcode3
        i += 1
        try:
            cell = dict[barcode]
            dict2[cell] += 1
            umi = L2[0:10]  # 10bp random sequence
            fo.write('@' + cell + ':' + umi + '\n')
            fo.write(l2 + l3 + l4)
            n += 1
        except:
            continue
    fb.write(str(i) + '\n')
    fb.write(str(n) + '\n')

    for key, value in dict2.items():
        fc.write(key + '\t' + str(value) + '\n')
    for key, value in dict3.items():
        fa1.write(key + '\t' + str(value) + '\n')
    for key, value in dict4.items():
        fa2.write(key + '\t' + str(value) + '\n')
    for key, value in dict5.items():
        fa3.write(key + '\t' + str(value) + '\n')
    fl.close()
    fm.close()
    fo.close()
    fa1.close()
    fa2.close()
    fa3.close()
    fb.close()
    fc.close()
    return 'tmp%s' % job_id
