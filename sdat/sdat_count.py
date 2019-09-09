import multiprocessing
import os
import subprocess
import sys
import time

import sdat.tmp as sdat


def counts():
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
        print("      Before using 'sdat count', please make sure that featureCounts is installed")
        print("")
        print("   Usage:")
        print("")
        print("      sdat count   [options]   -g Reads_number_per_cell.log  -in cell_folder")
        print("")
        print("      options:")
        print("         -d        INT       # threshold,only reads number of the  cell is above threshold will be count genes number. default:200")
        print("         -gtf    filename    # Path to your gtf file")
        print("         -p        INT       # process numbers. default:10")
        print("")
        print("   Example:")
        print("")
        print("      sdat count -d 200 -p 10 -gtf  gtf_file  -g Reads_number_per_cell.log  -in cell_folder")

        sys.exit(0)

    if len(sys.argv) < 2:
        help_doc()

    threshold = 200
    p = 10
    directory = os.getcwd()
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '-in':
            try:
                cell_folder = sys.argv[i + 1]
                if os.path.exists(cell_folder):
                    pass
                else:
                    print('cell_folder no found!')
                    help_doc()
                    exit()
            except:
                print('opition error!')
                help_doc()
                exit()

        elif sys.argv[i] == '-d':
            try:
                threshold = int(sys.argv[i + 1])
            except:
                print('threshold error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-g':
            try:
                cell_log = sys.argv[i + 1]
                if 'Reads_number_per_cell.log' not in cell_log:
                    print('Reads_number_per_cell.log error!')
                    help_doc()
                    exit()
            except:
                print('Reads_number_per_cell.log error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-gtf':
            try:
                gtf_file = sys.argv[i + 1]
                if gtf_file.endswith('.gtf'):
                    pass
                else:
                    print('gtf_file error!')
                    help_doc()
                    exit()
            except:
                print('gtf_file error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-p':
            try:
                p = int(sys.argv[i + 1])
            except:
                print('opition error!')
                help_doc()
                exit()
        i += 1

    if '-g' not in sys.argv:
        print('Reads_number_per_cell.log error!')
        help_doc()
        exit()
    if os.path.exists(cell_log):
        pass
    else:
        print('Reads_number_per_cell.log error!')
        help_doc()
        exit()
    if '-in' not in sys.argv:
        print('cell_folder error!')
        help_doc()
        exit()
    if '-gtf' not in sys.argv:
        print('gtf_file error!')
        help_doc()
        exit()
    if os.path.exists(gtf_file):
        pass
    else:
        print('gtf_file error!')
        help_doc()
        exit()

    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;32m sdat count start running... \033[0m')
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Generating cell list... \033[0m')
    subprocess.Popen('mkdir %s/count' % directory, shell=True).wait()
    dict = {'reads': {}}  # for profile
    fl = open(cell_log)
    next(fl)
    for line in fl:
        seq = line.rstrip().split('\t')
        cell = seq[0]
        dict['reads'][cell] = seq[1]
    fl.close()
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;35m Start counting... \033[0m')
    cell_list = [cell for cell in dict['reads'].keys() if int(dict['reads'][cell]) >= threshold]
    n = len(cell_list)
    pool = multiprocessing.Pool(processes=p)  # process number
    results = []
    for cell in cell_list:
        results.append(pool.apply_async(sdat.count_gene_per_cell, args=(cell, cell_folder, '%s/count' % directory, gtf_file, n)))
    for res in enumerate(results):
        sys.stdout.write('[' + '#' * int((res[0] + 2) / (n / float(100))) + ' ' * (
                    100 - int((res[0] + 2) / (n / float(100)))) + ']' + '--[' + '\033[0;32;40m %s\033[0m' % (res[0] + 1) + '/' + '\033[0;33;40m%s \033[0m' % n + '] Counting:' + '\033[0;35;40m%s \033[0m' % res[1].get() + '\r')
        sys.stdout.flush()
    pool.close()
    pool.join()
    print('\n' + '[%s]' % time.strftime("%Y-%m-%d %X",
                                        time.localtime()) + '\033[1;35m Generating profile data... \033[0m')
    sdat.count_profile('%s/count' % directory, 'profile.data', dict, cell_list)
    sdat.overall_count('%s/count' % directory, 'overall.count', cell_list)
    sdat.get_expression_table('profile.data', '%s/count' % directory, 'gene_expression_counts_3_genes_200.table')
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[0;32;40m Finished successfully\033[0m')
