import os
import subprocess


def count_gene_per_cell(cell, cell_folder, count_folder, gtf_file, n):
    subprocess.Popen('nohup featureCounts -g gene_id -T 16 -a %s -o %s.count %s/%s.sam >/dev/null 2>&1' % (
        gtf_file, cell, cell_folder, cell), shell=True).wait()
    os.remove('%s.count.summary' % cell)
    fl = open('%s.count' % cell)
    fo = open('%s/%s.count' % (count_folder, cell), 'w')
    next(fl)
    next(fl)
    for line in fl:
        seq = line.rstrip().split('\t')
        if seq[6] != '0':
            fo.write(seq[0] + '\t' + seq[6] + '\n')
    fl.close()
    fo.close()
    os.remove('%s.count' % cell)
    return cell
