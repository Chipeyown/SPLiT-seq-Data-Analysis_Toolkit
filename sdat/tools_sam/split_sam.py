import time


def split_sam(in_dir, out_folder):
    fl = open(in_dir)
    chr_list = []
    line0 = fl.readline()
    chr0 = line0.split('\t')[2]
    chr_list.append(chr0)
    fo = open('%s/%s.sam' % (out_folder, chr0), 'w')  # tmp/sam/Chr1.sam
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + ' Spliting to' + '\033[1;35m %s \033[0m' % chr0 + ' ...')
    fo.write(line0)
    for line in fl:
        chr = line.split('\t')[2]
        if chr == chr0:
            fo.write(line)
        else:
            fo.close()
            chr0 = chr
            chr_list.append(chr0)
            fo = open('%s/%s.sam' % (out_folder, chr0), 'w')
            print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + ' Spliting to' + '\033[1;35m %s \033[0m' % chr0 + ' ...')
            fo.write(line)
    fo.close()
    fl.close()
    return chr_list
