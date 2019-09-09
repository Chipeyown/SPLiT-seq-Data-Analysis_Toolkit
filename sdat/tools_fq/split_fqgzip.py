import subprocess
import multiprocessing
import time


def split_fqgzip(in_dir, directory):
    p = subprocess.Popen('gunzip -c %s' % in_dir, stdout=subprocess.PIPE, shell=True)
    pname = multiprocessing.current_process().name
    i = 0
    j0 = 0
    print('[%s]' % time.strftime("%Y-%m-%d %X",
                                 time.localtime()) + ' sdat filter is spliting' + '\033[1;35m tmp%s\033[0m' % j0 + ' from' + '\033[1;35m %s\033[0m' % pname.replace(
        'Process-', 'Read') + ' ... ')
    fo = open('%s/tmp0.fq' % directory, 'w')
    while True:
        j = int(i / 1000000)  # 1000000 fastq sequence per tmp_fastq file
        l1 = p.stdout.readline()
        l2 = p.stdout.readline()
        l3 = p.stdout.readline()
        l4 = p.stdout.readline()
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
