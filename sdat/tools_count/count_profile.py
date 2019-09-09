def count_profile(in_folder, out_dir, dict, cell_list):
    fo = open(out_dir, 'w')
    dict['count1'] = {}  # Gene_number(counts>=1)
    dict['count2'] = {}  # Gene_number(counts>=2)
    dict['count3'] = {}  # Gene_number(counts>=3)
    dict['count5'] = {}  # Gene_number(counts>=5)
    for cell in cell_list:
        fl = open('%s/%s.count' % (in_folder, cell))
        a = b = c = d = 0  # a:count>=1 b:count>=2 c:count>=3 d:count>=5
        for line in fl:
            a += 1
            count = int(line.rstrip().split('\t')[1])
            if count >= 2:
                b += 1
            if count >= 3:
                c += 1
            if count >= 5:
                d += 1
        fl.close()
        dict['count1'][cell] = str(a)
        dict['count2'][cell] = str(b)
        dict['count3'][cell] = str(c)
        dict['count5'][cell] = str(d)
    fo.write(
        'Cell\tAfter_mapping_and_rmdup_reads_number\tGene_number(counts>=1)\tGene_number(counts>=2)\tGene_number(counts>=3)\tGene_number(counts>=5)\n')
    for cell in cell_list:
        fo.write(cell + '\t' + dict['reads'][cell] + '\t' + dict['count1'][cell] + '\t' + dict['count2'][cell] + '\t' +
                 dict['count3'][cell] + '\t' + dict['count5'][cell] + '\n')
    fo.close()
