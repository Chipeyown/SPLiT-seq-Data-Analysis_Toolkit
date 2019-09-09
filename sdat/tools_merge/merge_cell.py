def merge_cell(in_folder, out_folder, chr_list, cell):
    fo = open('%s/%s.sam' % (out_folder, cell), 'w')
    for chr in chr_list:
        try:
            fl = open('%s/%s/%s.sam' % (in_folder, chr, cell))
            for line in fl:
                fo.write(line)
            fl.close()
        except:
            continue
    fo.close()
