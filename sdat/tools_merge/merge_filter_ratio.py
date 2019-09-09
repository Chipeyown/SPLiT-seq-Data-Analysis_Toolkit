def merge_filter_ratio(out_dir, n, tmp_pre, time0, time1, time2):
    fo = open(out_dir, 'w')
    fo.write('Jobs Starts: ' + time0 + '\n' + '\n')
    fo.write('Finish spliting fastq files: ' + time1 + '\n' + '\n')
    fo.write('Finish filtering fastq files: ' + time2 + '\n' + '\n')
    overall = right = 0
    for i in range(n):
        fl = open('%s%s.log' % (tmp_pre, i))
        overall += int(fl.readline().rstrip())
        right += int(fl.readline().rstrip())
        fl.close()
    fo.write('\n')
    fo.write('After fliter:\n')
    fo.write('Overall reads:%s\n' % overall)
    fo.write('phased reads:%s\n' % right)
    ratio = round(100 * right / overall, 2)
    fo.write('Phased reads ratio:%s' % ratio)
    fo.close()
