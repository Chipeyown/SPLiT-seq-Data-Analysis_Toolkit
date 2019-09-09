def overall_count(in_folder, out_dir, cell_list):
    fo = open(out_dir, 'w')
    dict = {}
    for cell in cell_list:
        fl = open('%s/%s.count' % (in_folder, cell))
        for line in fl:
            seq = line.rstrip().split('\t')
            gene = seq[0]
            try:
                dict[gene] = dict[gene] + int(seq[1])
            except:
                dict[gene] = int(seq[1])
        fl.close()
    for key, value in dict.items():
        fo.write(key + '\t' + str(value) + '\n')
    fo.close()
