import time
import multiprocessing


def split_fq(in_dir, directory):
    fl = open(in_dir)
    pname = multiprocessing.current_process().name
    i = 0
    j0 = 0
    print('[%s]' % time.strftime("%Y-%m-%d %X",
                                 time.localtime()) + ' sdat filter is spliting' + '\033[1;35m tmp%s\033[0m' % j0 + ' from' + '\033[1;35m %s\033[0m' % pname.replace(
        'Process-', 'Read') + ' ... ')
    fo = open('%s/tmp0.fq' % directory, 'w')
    while True:
        j = int(i / 1000000)  # 1000000 fastq sequence per tmp_fastq file
        l1 = fl.readline()
        l2 = fl.readline()
        l3 = fl.readline()
        l4 = fl.readline()
        if l2 == '':
            break
        if j == j0:
            fo.write(l1 + l2 + l3 + l4)
        else:
            fo.close()
            j0 = j
            print('[%s]' % time.strftime("%Y-%m-%d %X",
                                         time.localtime()) + ' sdat filter is spliting' + '\033[1;35m tmp%s\033[0m' % j0 + ' from' + '\033[1;35m %s\033[0m' % pname.replace(
                'Process-', 'Read') + ' ... ')
            fo = open('%s/tmp%s.fq' % (directory, j0), 'w')
            fo.write(l1 + l2 + l3 + l4)
        i += 1
    fo.close()
    fl.close()
