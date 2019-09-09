import os
import subprocess
import sys
import time


def align():
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
        print("      When using 'sdat align', make sure there is STAR in your server.")
        print("")
        print("   Usage:")
        print("")
        print("      sdat align   [options]   -G index_dir  -fq xxxx_filtered.fq")
        print("")
        print("      options:")
        print("         -gtf   filename        # Path to your gtf file")
        print(
            "         -o     output          #/path/to/output/dir/prefix  default: ./xxxx (xxxx means prefix of your input fastq)")
        print(
            "         -g                     #without -g: only keep unique alignments, with -g: keep the unique alignments and the best alignment of multi-alignment reads(5 place)")
        print("         -m     alignIntronMax  #maximum intron size default:5000")
        print("")
        print("   Example:")
        print("")
        print("       sdat align -g -m 5000 -o output_dir/prefix  -gtf gtf_file  -G index   -fq xxxx_filtered.fq")
        print("")

        sys.exit(0)

    if len(sys.argv) < 2:
        help_doc()

    i = 1
    max_intron = 5000
    while i < len(sys.argv):
        if sys.argv[i] == '-gtf':
            try:
                gtf = sys.argv[i + 1]
                if gtf.endswith('.gtf'):
                    pass
                else:
                    print('gtf error!')
                    help_doc()
                    exit()
            except:
                print('gtf error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-G':
            try:
                index = sys.argv[i + 1]
                files = os.listdir(index)
            except:
                print('index error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-fq':
            try:
                fastq = sys.argv[i + 1]
                if '.fq' not in fastq:
                    print('fastq error!')
                    help_doc()
                    exit()
                pre0 = fastq.split('/')[-1].split('_filtered')[0]  # prefix,name
            except:
                print('fastq error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-o':
            try:
                pre1 = sys.argv[i + 1]  # directory
            except:
                print('output_dir error!')
                help_doc()
                exit()
        elif sys.argv[i] == '-m':
            try:
                max_intron = int(sys.argv[i + 1])
            except:
                print('option error!')
                help_doc()
                exit()
        i += 1
    if '-fq' not in sys.argv:
        print('fastq error!')
        help_doc()
        exit()
    if '-G' not in sys.argv:
        print('index error!')
        help_doc()
        exit()
    try:
        pre = pre1
    except:
        pre = pre0
    if '/' in pre:
        try:
            os.mkdir(pre.rstrip(pre.split('/')[-1]))
        except:
            pass

    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;32m sdat align start running... \033[0m')
    if '-g' in sys.argv and '-gtf' in sys.argv:
        subprocess.Popen(
            'STAR --runMode alignReads --runThreadN 16 --genomeDir %s --sjdbGTFfile %s --readFilesIn %s --outFileNamePrefix %s --outSAMtype BAM SortedByCoordinate --outFilterMultimapNmax 5 --outSAMmultNmax 1 --alignIntronMax %s' % (
                index, gtf, fastq, pre, max_intron), shell=True).wait()
    elif '-g' in sys.argv and '-gtf' not in sys.argv:
        subprocess.Popen(
            'STAR --runMode alignReads --runThreadN 16 --genomeDir %s --readFilesIn %s --outFileNamePrefix %s --outSAMtype BAM SortedByCoordinate --outFilterMultimapNmax 5 --outSAMmultNmax 1 --alignIntronMax %s' % (
                index, fastq, pre, max_intron), shell=True).wait()
    elif '-g' not in sys.argv and '-gtf' in sys.argv:
        subprocess.Popen(
            'STAR --runMode alignReads --runThreadN 16 --genomeDir %s --sjdbGTFfile %s --readFilesIn %s --outFileNamePrefix %s --outSAMtype BAM SortedByCoordinate --outFilterMultimapNmax 1 --alignIntronMax %s' % (
                index, gtf, fastq, pre, max_intron), shell=True).wait()
    else:
        subprocess.Popen(
            'STAR --runMode alignReads --runThreadN 16 --genomeDir %s --readFilesIn %s --outFileNamePrefix %s --outSAMtype BAM SortedByCoordinate --outFilterMultimapNmax 1 --alignIntronMax %s' % (
                index, fastq, pre, max_intron), shell=True).wait()
    print('[%s]' % time.strftime("%Y-%m-%d %X", time.localtime()) + '\033[1;32m Finished successfully\033[0m')
