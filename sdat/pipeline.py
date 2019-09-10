def pipeline():
    import sys
    from sdat.sdat_filter import filters  # filter is a reserved word for python
    from sdat.sdat_align import align
    from sdat.sdat_cell import cell
    from sdat.sdat_count import counts  # count is a reserved word for python

    def help_doc():

        print('')
        print("##############################################################################################")
        print('')
        print("   SDAT: SPLiT-seq Data Analysis Toolkit-0.1.6")
        print("")
        print("   Please contact chipeyown@gmail.com when questions arise.")
        print("")
        print("##############################################################################################")
        print("")
        print("")
        print('   Usage: ')
        print("")
        print('      "sdat filter"      #filter the correct reads and rename the reads with cell_id and umi')
        print("")
        print('      "sdat align"       #unique align the filtered fastq file to genome')
        print("")
        print('      "sdat cell"        #remove PCR duplication and split aligned reads to corresponding cell')
        print("")
        print('      "sdat count"       #calculate gene count per cell')
        print("")
        print("")
        sys.exit(0)

    if len(sys.argv) < 2:
        help_doc()

    if sys.argv[1] == 'filter':
        sys.argv = sys.argv[1:]
        filters()
    elif sys.argv[1] == 'align':
        sys.argv = sys.argv[1:]
        align()
    elif sys.argv[1] == 'cell':
        sys.argv = sys.argv[1:]
        cell()
    elif sys.argv[1] == 'count':
        sys.argv = sys.argv[1:]
        counts()
    else:
        help_doc()
