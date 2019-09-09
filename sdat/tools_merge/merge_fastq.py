def merge_fastq(out_dir, n, tmp_pre):
    fo = open(out_dir, 'w')
    for i in range(n):
        fl = open('%s%s.fq' % (tmp_pre, i))
        for line in fl:
            fo.write(line)
        fl.close()
    fo.close()
