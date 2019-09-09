import multiprocessing
import os
import subprocess
import sys
import time

import sdat.tmp as sdat


def filters():
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

    def help_doc():
        print("")
        print("   Attention:")
        print("")
        print(
            "      When using 'sdat filter', Using Uncompressed fastq files as input are recommended for great time saving.")
        print("")
        print("   Usage:")
        print("")
        print("      sdat filter   [options]   -R1 xxxx_R1.fq(.gz)   -R2  xxxx_R2.fq(.gz)")
        print("")
        print("      options:")
        print(
            "         -b1    barcode1      # Round1 barcode,please input as: 1-8,which means Round1_01-08 and Round1_49-56. default:1-48")
        print(
            "         -b2    barcode2      # Round2 barcode,please input as: 1-8,which means Round2_01-08. default:1-96")
        print(
            "         -b3    barcode3      # Round3 barcode,please input as: 1-8,which means Round3_01-08. default:1-96")
        print("         -e     0 or 1        # allowed 0 or 1 bp mismatch per barcode. default:1")
        print(
            "         -nm                  # means not mix oligo dT with hexamer. when using '-um', the reads from Round1-48, Round49-96 will be named with a suffix '-0' or '-1' respectively")
        print("")
        print("   Example:")
        print("")
        print("       sdat filter -b1 1-8  -b2 1-96  -b3 1-96  -e 1 -R1 xxxx_R1.fq(.gz)  -R2 xxxx_R2.fq(.gz)")
        print("")

        sys.exit(0)

    if len(sys.argv) < 2:
        help_doc()

    time0 = time.ctime()  #########################################################
    gzip = 0  # gzip
    e = 1
    mix = 1  # standrd protocol
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '-b1':
            try:
                b1 = sys.argv[i + 1]
                b1_left = int(b1.split('-')[0].strip())
                b1_right = int(b1.split('-')[1].strip())
            except:
                print('options error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-b2':
            try:
                b2 = sys.argv[i + 1]
                b2_left = int(b2.split('-')[0].strip())
                b2_right = int(b2.split('-')[1].strip())
            except:
                print('options error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-b3':
            try:
                b3 = sys.argv[i + 1]
                b3_left = int(b3.split('-')[0].strip())
                b3_right = int(b3.split('-')[1].strip())
            except:
                print('opitions error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-e':
            try:
                e = int(sys.argv[i + 1])
            except:
                print('opitions error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-R1':
            try:
                read1 = sys.argv[i + 1]
                if '_R1.fq' not in read1 and 'R1_fastq' not in read1:
                    help_doc()
                    exit()
                if '/' in read1:
                    directory = read1.rstrip('/' + read1.split('/')[-1])  # directory
                else:
                    directory = '.'
                read1 = read1.split('/')[-1]  # read1
                pre = read1.rstrip('_R' + read1.split('_R')[-1])  # prefix,name
                if read1.endswith('.gz'):
                    gzip = 1  # gzip
            except:
                help_doc()
                exit()
        elif sys.argv[i] == '-R2':
            try:
                read2 = sys.argv[i + 1]
                if '_R2.fq' not in read2 and 'R2_fastq' not in read2:
                    help_doc()
                    exit()
                read2 = read2.split('/')[-1]  # read2
            except:
                help_doc()
                exit()
        i += 1
    if '-b1' in sys.argv:  # b1
        b11 = b1_left
        b12 = b1_right
    else:
        b11 = 1
        b12 = 48
    if '-b2' in sys.argv:  # b2
        b21 = b2_left
        b22 = b2_right
    else:
        b21 = 1
        b22 = 96
    if '-b3' in sys.argv:  # b3
        b31 = b3_left
        b32 = b3_right
    if '-nm' in sys.argv:
        mix = 0  # no mix, unstandard
    else:
        b31 = 1
        b32 = 96
    if os.path.exists(directory + '/' + read1):
        pass
    else:
        help_doc()
        exit()
    if os.path.exists(directory + '/' + read2):
        pass
    else:
        help_doc()
        exit()

    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;32m sdat filter start running... \033[0m')
    # build barcode index
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Building barcode index... \033[0m')
    subprocess.Popen('mkdir %s/barcode' % directory, shell=True).wait()
    sdat.barcode1(b11, b12, '%s/barcode/barcode1.data' % directory)
    sdat.barcode2(b21, b22, '%s/barcode/barcode2.data' % directory)
    sdat.barcode3(b31, b32, '%s/barcode/barcode3.data' % directory)
    if mix == 1:
        sdat.barcode_to_cell('%s/barcode/barcode1.data' % directory, '%s/barcode/barcode2.data' % directory,
                             '%s/barcode/barcode3.data' % directory, '%s/barcode/barcode_to_cell.data' % directory)
    else:
        sdat.barcode_to_cell_nomix('%s/barcode/barcode1.data' % directory, '%s/barcode/barcode2.data' % directory,
                                   '%s/barcode/barcode3.data' % directory,
                                   '%s/barcode/barcode_to_cell.data' % directory)

    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Spliting fastq file... \033[0m')
    subprocess.Popen('mkdir -p %s/tmp/R1' % directory, shell=True).wait()
    subprocess.Popen('mkdir -p %s/tmp/R2' % directory, shell=True).wait()
    process_list0 = []
    if gzip == 1:
        p1 = multiprocessing.Process(target=sdat.split_fqgzip,
                                     args=('%s/%s' % (directory, read1), '%s/tmp/R1' % directory))
        p2 = multiprocessing.Process(target=sdat.split_fqgzip,
                                     args=('%s/%s' % (directory, read2), '%s/tmp/R2' % directory))
    else:
        p1 = multiprocessing.Process(target=sdat.split_fq, args=('%s/%s' % (directory, read1), '%s/tmp/R1' % directory))
        p2 = multiprocessing.Process(target=sdat.split_fq, args=('%s/%s' % (directory, read2), '%s/tmp/R2' % directory))
    p1.start()
    p2.start()
    process_list0.append(p1)
    process_list0.append(p2)
    for p in process_list0:
        p.join()

    time1 = time.ctime()  #########################################################
    dicts = sdat.barcode_index('%s/barcode/barcode_to_cell.data' % directory)
    dict = dicts[0]  # cell and coresponding  barcode
    dict2 = dicts[1]  # for counting reads number per cell
    dict3 = dicts[2]  # for counting barcode1
    dict4 = dicts[3]  # for counting barcode2
    dict5 = dicts[4]  # for counting barcode3
    lists = sdat.barcode_listbc('%s/barcode/barcode1.data' % directory, '%s/barcode/barcode2.data' % directory,
                                '%s/barcode/barcode3.data' % directory)
    subprocess.Popen('mkdir  %s/tmp/filtered' % directory, shell=True).wait()
    subprocess.Popen('mkdir  %s/tmp/log' % directory, shell=True).wait()
    subprocess.Popen('mkdir  %s/tmp/reads_per_cell' % directory, shell=True).wait()
    subprocess.Popen('mkdir  %s/tmp/barcode1' % directory, shell=True).wait()
    subprocess.Popen('mkdir  %s/tmp/barcode2' % directory, shell=True).wait()
    subprocess.Popen('mkdir  %s/tmp/barcode3' % directory, shell=True).wait()
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Start filtering... \033[0m')
    n = len(os.listdir('%s/tmp/R1' % directory))  # file number
    pool = multiprocessing.Pool(processes=30)  # 30 processes
    results = []
    for i in range(n):
        results.append(pool.apply_async(sdat.filter_fq, args=(
            '%s/tmp/R1/tmp%s.fq' % (directory, i), '%s/tmp/R2/tmp%s.fq' % (directory, i),
            '%s/tmp/filtered/tmp%s.fq' % (directory, i), '%s/tmp/barcode1/tmp%s.data' % (directory, i),
            '%s/tmp/barcode2/tmp%s.data' % (directory, i),
            '%s/tmp/barcode3/tmp%s.data' % (directory, i), '%s/tmp/log/tmp%s.log' % (directory, i),
            '%s/tmp/reads_per_cell/tmp%s.data' % (directory, i),
            dicts, lists, e, i)))  # e:0 mismatch or 1 mismatch
    for res in enumerate(results):
        sys.stdout.write('[' + '#' * int((res[0] + 2) / (n / float(100))) + ' ' * (
                100 - int((res[0] + 2) / (n / float(100)))) + ']' + '--[' + '\033[0;32;40m %s\033[0m' % (res[0] + 1) + '/' + '\033[0;33;40m%s \033[0m' % n + '] Counting:' + '\033[0;35;40m%s \033[0m' %
                         res[1].get() + '\r')
        sys.stdout.flush()
    pool.close()
    pool.join()

    time2 = time.ctime()
    print('\n'+'[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Merging filtered reads... \033[0m')
    sdat.merge_fastq('%s/%s_filtered.fq' % (directory, pre), n, '%s/tmp/filtered/tmp' % directory)  # merge_fastq
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Merging log files... \033[0m')
    sdat.merge_reads_per_cell('%s/%s_reads_per_cell.data' % (directory, pre), n,
                              '%s/tmp/reads_per_cell/tmp' % directory, dict2)  # merge_reads_pre_cell
    dict_bcs = sdat.barcode_to_round_id('%s/barcode/barcode_to_cell.data' % directory)
    dict_bc1 = dict_bcs[0]  # for barcode1 to round id
    dict_bc2 = dict_bcs[1]  # for barcode2 to round id
    dict_bc3 = dict_bcs[2]  # for barcode3 to round id
    sdat.merge_barcode('%s/%s_barcode1.data' % (directory, pre), n, '%s/tmp/barcode1/tmp' % directory, dict3,
                       dict_bc1)  # merge_barcode1 log
    sdat.merge_barcode('%s/%s_barcode2.data' % (directory, pre), n, '%s/tmp/barcode2/tmp' % directory, dict4,
                       dict_bc2)  # merge_barcode2 log
    sdat.merge_barcode('%s/%s_barcode3.data' % (directory, pre), n, '%s/tmp/barcode3/tmp' % directory, dict5,
                       dict_bc3)  # merge_barcode3 log
    sdat.merge_filter_ratio('%s/%s.log' % (directory, pre), n, '%s/tmp/log/tmp' % directory, time0, time1,
                            time2)  # merge log
    subprocess.Popen('rm -r %s/tmp' % directory, shell=True)
    time3 = time.ctime()
    with open('%s/%s.log' % (directory, pre), 'a+') as f:
        f.write('\n' + 'Job finish: ' + time3)
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;32m Finished successfully\033[0m')
