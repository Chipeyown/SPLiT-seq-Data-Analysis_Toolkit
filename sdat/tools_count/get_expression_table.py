def get_expression_table(in_dir, in_folder, out_dir):
    fl = open(in_dir)
    fo = open(out_dir, 'w')
    cell_list = []
    dict = {}
    next(fl)
    for line in fl:
        seq = line.split('\t')
        cell = seq[0]
        gene_number = seq[3]
        if int(gene_number) > 250:
            dict[cell] = {}
            cell_list.append(cell)

    gene_list = []
    for cell in cell_list:
        fm = open('%s/%s.count' % (in_folder, cell))
        for line in fm:
            seq = line.rstrip().split('\t')
            gene = seq[0]
            count = seq[1]
            dict[cell][gene] = count
            if int(count) >= 2:  # select gene that counts>=3
                if gene not in gene_list:
                    gene_list.append(gene)
        fm.close()

    header = 'Gene_id'
    for cell in cell_list:
        header += '\t' + cell
    fo.write(header + '\n')
    for gene in gene_list:
        line = gene
        for cell in cell_list:
            try:
                line += '\t' + dict[cell][gene]
            except:
                line += '\t0'
        fo.write(line + '\n')

    fl.close()
    fo.close()
