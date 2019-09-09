def merge_barcode(out_dir, n, tmp_pre, dict, dict_bc):
    fo = open(out_dir, 'w')
    fo.write('Barcode\tnumber\n')
    for i in range(n):
        fl = open('%s%s.data' % (tmp_pre, i))
        for line in fl:
            seq = line.rstrip().split('\t')
            key = seq[0]
            value = int(seq[1])
            dict[key] += value
        fl.close()
    for key, value in dict.items():
        fo.write(dict_bc[key] + '\t' + str(value) + '\n')
    fo.close()
