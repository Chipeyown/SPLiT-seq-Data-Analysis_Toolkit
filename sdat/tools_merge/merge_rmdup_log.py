def merge_rmdup_log(in_folder, out_dir, chr_list):
    fo = open(out_dir, 'w')
    i = 0
    n = 0
    for chr in chr_list:
        fl = open('%s/%s.log' % (in_folder, chr))
        a = int(fl.readline().rstrip())
        b = int(fl.readline().rstrip())
        ratio = round(100 * b / a, 2)
        fo.write('Reads number in %s: %s\n' % (chr, a))
        fo.write('Duplication reads number in %s: %s\n' % (chr, b))
        fo.write('Duplication ratio: %s\n\n' % ratio)
        i += a
        n += b
    ratio = round(100 * n / i, 2)
    fo.write('Reads number in accepted_hits.bam: %s\n' % i)
    fo.write('Duplication reads number in accepted_hits.bam: %s\n' % n)
    fo.write('Duplication ratio: %s' % ratio)
    fo.close()
