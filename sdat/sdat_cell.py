import multiprocessing
import os
import subprocess
import sys
import threading
import time

import sdat.tmp as sdat
try:
    from Queue import Queue #for python2
except:
    from queue import Queue #for python3


def cell():
    print("")
    print("##############################################################################################")
    print("")
    print("   SDAT: SPLiT-seq Data Analysis Toolkit")
    print("")
    print("   A python program(suitable for python2 and python3)")
    print("")
    print("   Please contact chipeyown@gmail.com when questions arise.")
    print("")
    print("##############################################################################################")

    def rmdup_cell(chr, directory):
        pname = multiprocessing.current_process().name
        print('[%s]' % time.strftime("%Y-%m-%d %X",
                                     time.localtime()) + ' %s is running to deduplicate' % pname + '\033[1;35m %s \033[0m' % chr)
        sdat.sam_rmdup('%s/tmp/sam/%s.sam' % (directory, chr), '%s/tmp/rmdup/%s.sam' % (directory, chr),
                       '%s/tmp/dup/%s.sam' % (directory, chr), '%s/tmp/log1/%s.log' % (directory, chr))
        subprocess.Popen('rm %s/tmp/sam/%s.sam' % (directory, chr), shell=True)
        print('[%s]' % time.strftime("%Y-%m-%d %X",
                                     time.localtime()) + ' %s is running to split' % pname + '\033[1;35m %s \033[0m' % chr + 'to cell')
        sdat.split_sam_to_cell('%s/tmp/rmdup/%s.sam' % (directory, chr), '%s/tmp/log2/%s.log' % (directory, chr),
                               '%s/tmp/cell/%s' % (directory, chr))
        print('[%s]' % time.strftime("%Y-%m-%d %X",
                                     time.localtime()) + ' %s finish spliting' % pname + '\033[1;35m %s \033[0m' % chr + 'to cell successfully')

    def merge_cell_chr(directory, chr_list, n):
        while True:
            cell = task.get()
            sdat.merge_cell('%s/tmp/cell' % directory, '%s/cell' % directory, chr_list, cell)
            lock.acquire()
            count[0] += 1
            sys.stdout.write('[' + '#' * int((count[0] + 1) / (n / float(100))) + ' ' * (
                        100 - int((count[0] + 1) / (n / float(100)))) + ']' + '--[' + '\033[0;32;40m %s\033[0m' % count[0] + '/' + '\033[0;33;40m%s \033[0m' % n + '] Merging' + '\033[0;35;40m %s \033[0m' % cell + '\r')
            sys.stdout.flush()
            lock.release()
            task.task_done()

    def help_doc():
        print("")
        print("   Attention:")
        print("")
        print("      'sdat cell':remove PCR duplication and split aligned reads to cell.")
        print("")
        print("   Usage:")
        print("")
        print("          sdat cell  -b xxxx.bam    or    sdat cell  -s xxxx.sam")
        print("")

        sys.exit(0)

    if len(sys.argv) < 2:
        help_doc()

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '-b':
            try:
                bam = sys.argv[i + 1]
                if bam.endswith('.bam'):
                    if '/' in bam:
                        directory = bam.rstrip('/' + bam.split('/')[-1])  # directory
                    else:
                        directory = '.'
                    pre = bam.split('/')[-1].split('.bam')[0]
                else:
                    print('bam file error!')
                    help_doc()
                    exit()
            except:
                print('bam file error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-s':
            try:
                sam = sys.argv[i + 1]
                if sam.endswith('.sam'):
                    if '/' in sam:
                        directory = sam.rstrip('/' + sam.split('/')[-1])  # directory
                    else:
                        directory = '.'
                    pre = sam.split('/')[-1].split('.sam')[0]
                else:
                    print('sam file error!')
                    help_doc()
                    exit()
            except:
                print('sam file error!')
                help_doc()
                exit()
        i += 1
    if '-b' not in sys.argv and '-s' not in sys.argv:
        print('input file error!')
        help_doc()
        exit()
    if '-b' in sys.argv:
        if os.path.exists(bam):
            pass
        else:
            print('bam file no found!')
            help_doc()
            exit()
    elif '-s' in sys.argv:
        if os.path.exists(sam):
            pass
        else:
            print('sam file no found!')
            help_doc()
            exit()

    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;32m sdat cell start running... \033[0m')
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Start deduplicating... \033[0m')
    subprocess.Popen('mkdir -p %s/tmp/sam' % directory, shell=True).wait()
    subprocess.Popen('mkdir -p %s/tmp/rmdup' % directory, shell=True).wait()
    subprocess.Popen('mkdir -p %s/tmp/dup' % directory, shell=True).wait()
    subprocess.Popen('mkdir -p %s/tmp/cell' % directory, shell=True).wait()
    subprocess.Popen('mkdir -p %s/tmp/log1' % directory, shell=True).wait()  # rmdup log
    subprocess.Popen('mkdir -p %s/tmp/log2' % directory, shell=True).wait()  # reads number per cell log

    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Spliting sam files... \033[0m')
    if '-b' in sys.argv:
        chr_list = sdat.split_bam('%s/%s.bam' % (directory, pre),
                                  '%s/tmp/sam' % directory)  # split sam into several sam files in tmp/sam (by chromosome)
    elif '-s' in sys.argv:
        chr_list = sdat.split_sam('%s/%s.sam' % (directory, pre),
                                  '%s/tmp/sam' % directory)  # split sam into several sam files in tmp/sam (by chromosome)
    chr_num = len(chr_list)  # file number in tmp/sam
    for chr in chr_list:
        subprocess.Popen('mkdir %s/tmp/cell/%s' % (directory, chr), shell=True).wait()
    process_list = []
    for chr in chr_list:
        p = multiprocessing.Process(target=rmdup_cell, args=(chr, directory))
        p.daemon = True
        p.start()
        process_list.append(p)
    for p in process_list:
        p.join()

    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Start merging files... \033[0m')
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Merging rmdup sam files... \033[0m')
    sdat.merge_sam('%s/tmp/rmdup' % directory, '%s/%s_rmdup.sam' % (directory, pre), chr_list)  # merge rmdup
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Merging dup sam files ... \033[0m')
    sdat.merge_sam('%s/tmp/dup' % directory, '%s/%s_dup.sam' % (directory, pre), chr_list)  # merge dup
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Merging rmdup log files... \033[0m')
    sdat.merge_rmdup_log('%s/tmp/log1' % directory, '%s/%s_rmdup.log' % (directory, pre), chr_list)
    dict_cell = {}
    for chr in chr_list:
        cells_tmp = [cell_file.split('.')[0] for cell_file in os.listdir('%s/tmp/cell/%s' % (directory, chr))]
        for cell in cells_tmp:
            dict_cell[cell] = 0
    print('[%s]' % time.strftime("%Y-%m-%d %X",
                                 time.localtime()) + '\033[1;35m Merging log of reads number pre cell... \033[0m')
    sdat.merge_cell_log('%s/tmp/log2' % directory, '%s/Reads_number_per_cell.log' % directory, chr_list, dict_cell)
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Merging reads per cell... \033[0m')
    subprocess.Popen('mkdir %s/cell' % directory, shell=True).wait()
    cells = [cell for cell in dict_cell.keys()]
    n = len(cells)
    count = [0]  # for counting in merge_cell_chr function;nonlocal isn't available for python2
    lock = threading.Lock()  # a threading lock to avoid Thread conflict.
    task = Queue()
    for i in range(50):
        t = threading.Thread(target=merge_cell_chr, args=(directory, chr_list, n))
        t.daemon = True
        t.start()
    for cell in cells:
        task.put(cell)
    task.join()

    subprocess.Popen('rm -r %s/tmp &' % directory, shell=True)
    print('\n' + '[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;32m Finished successfully\033[0m')
