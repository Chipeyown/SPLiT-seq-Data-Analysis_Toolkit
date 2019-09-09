def sam_rmdup(in_dir, out_dir1, out_dir2, out_dir3):
    def __match__(u1, u2):
        m = 0  # match number
        for i in range(10):
            if u1[i] == u2[i]:
                m += 1
        return m

    def unique(list):
        dict = {}  # divide list by cell
        for ele in list:
            cell = ele.split(':')[0]
            try:
                dict[cell].append(ele)
            except:
                dict[cell] = [ele]
        list_u = []
        for cell, group in dict.items():  # remove rmdup ,allow one mismatch
            group0 = []  # lines after rmdup
            while len(group) > 1:
                group0.append(group[0])  # keep first one
                umi0 = group[0].split('\t')[0].split(':')[1]
                group.remove(group[0])
                group = [ele for ele in group if
                         __match__(umi0, ele.split('\t')[0].split(':')[1]) < 9]  # allow one mismatch
            if len(group) == 1:
                group0.append(group[0])  # the last one in group
            list_u += group0
        return list_u

    fl = open(in_dir)
    fo = open(out_dir1, 'w')
    fp = open(out_dir2, 'w')
    fa = open(out_dir3, 'w')
    line0 = fl.readline()
    seq0 = line0.split('\t')
    pos0 = seq0[3]
    list = [line0]
    i = 1  # overall reads number
    n = 0  # duplicated reads number
    for line in fl:
        seq = line.split('\t')
        pos = seq[3]
        if pos == pos0:
            list.append(line)
        else:
            list_u = unique(list)  # list_u lsit unique
            m = len(list) - len(list_u)
            n += m
            if m != 0:
                for ele in list_u:
                    fo.write(ele)
                    list.remove(ele)
                for ele in list:
                    fp.write(ele)
            else:
                for ele in list_u:
                    fo.write(ele)
            list = [line]
            pos0 = pos
        i += 1

    list_u = unique(list)
    n += len(list) - len(list_u)
    for ele in list_u:
        fo.write(ele)
        list.remove(ele)
    for ele in list:
        fp.write(ele)

    fa.write(str(i) + '\n')  # Reads number in accepted_hits.bam
    fa.write(str(n))  # Duplicated reads number in accepted_hits.bam

    fl.close()
    fo.close()
    fp.close()
    fa.close()
