def split_sam_to_cell(in_dir, out_dir1, out_folder):
    fl = open(in_dir)
    dict = {}
    for line in fl:
        cell = line.split(':')[0]
        try:
            dict[cell].append(line)
        except:
            dict[cell] = [line]
    fl.close()
    fa = open(out_dir1, 'w')
    for key, value in dict.items():
        fa.write(key + '\t' + str(len(value)) + '\n')
        fo = open('%s/%s.sam' % (out_folder, key), 'w')
        for ele in value:
            fo.write(ele)
        fo.close()
    fa.close()
