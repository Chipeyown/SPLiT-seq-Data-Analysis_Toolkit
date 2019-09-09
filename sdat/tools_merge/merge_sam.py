def merge_sam(in_folder, out_dir, chr_list):
    fo = open(out_dir, 'w')
    for chr in chr_list:
        fl = open('%s/%s.sam' % (in_folder, chr))
        for line in fl:
            fo.write(line)
        fl.close()
    fo.close()
