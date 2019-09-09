def merge_cell_log(in_folder, out_dir, chr_list, dict):
    fo = open(out_dir, 'w')
    fo.write('Cell\tReads_number\n')
    for chr in chr_list:
        fl = open('%s/%s.log' % (in_folder, chr))
        for line in fl:
            seq = line.rstrip().split('\t')
            cell = seq[0]
            reads_number = int(seq[1])
            dict[cell] += reads_number
        fl.close()
    for key, value in dict.items():
        fo.write(key + '\t' + str(value) + '\n')
    fo.close()
