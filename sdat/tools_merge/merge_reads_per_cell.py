def merge_reads_per_cell(out_dir, n, tmp_pre, dict):
    fo = open(out_dir, 'w')
    fo.write('Cell\tReads_number\n')
    for i in range(n):
        fl = open('%s%s.data' % (tmp_pre, i))
        for line in fl:
            seq = line.rstrip().split('\t')
            cell = seq[0]
            dict[cell] += int(seq[1])
        fl.close()
    for key, value in dict.items():
        fo.write(key + '\t' + str(value) + '\n')
    fo.close()
