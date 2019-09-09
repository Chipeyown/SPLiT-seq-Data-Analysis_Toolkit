def barcode1(b1, b2, out_dir):
    fo = open(out_dir, 'w')
    bc_list = [" A1\tdt(15)VN\tRound1_01\t/5Phos/AGGCCAGAGCATTCGAACGTGATTTTTTTTTTTTTTTTVN\tAACGTGAT\n",
               " A2\tdt(15)VN\tRound1_02\t/5Phos/AGGCCAGAGCATTCGAAACATCGTTTTTTTTTTTTTTTVN\tAAACATCG\n",
               " A3\tdt(15)VN\tRound1_03\t/5Phos/AGGCCAGAGCATTCGATGCCTAATTTTTTTTTTTTTTTVN\tATGCCTAA\n",
               " A4\tdt(15)VN\tRound1_04\t/5Phos/AGGCCAGAGCATTCGAGTGGTCATTTTTTTTTTTTTTTVN\tAGTGGTCA\n",
               " A5\tdt(15)VN\tRound1_05\t/5Phos/AGGCCAGAGCATTCGACCACTGTTTTTTTTTTTTTTTTVN\tACCACTGT\n",
               " A6\tdt(15)VN\tRound1_06\t/5Phos/AGGCCAGAGCATTCGACATTGGCTTTTTTTTTTTTTTTVN\tACATTGGC\n",
               " A7\tdt(15)VN\tRound1_07\t/5Phos/AGGCCAGAGCATTCGCAGATCTGTTTTTTTTTTTTTTTVN\tCAGATCTG\n",
               " A8\tdt(15)VN\tRound1_08\t/5Phos/AGGCCAGAGCATTCGCATCAAGTTTTTTTTTTTTTTTTVN\tCATCAAGT\n",
               " A9\tdt(15)VN\tRound1_09\t/5Phos/AGGCCAGAGCATTCGCGCTGATCTTTTTTTTTTTTTTTVN\tCGCTGATC\n",
               " A10\tdt(15)VN\tRound1_10\t/5Phos/AGGCCAGAGCATTCGACAAGCTATTTTTTTTTTTTTTTVN\tACAAGCTA\n",
               " A11\tdt(15)VN\tRound1_11\t/5Phos/AGGCCAGAGCATTCGCTGTAGCCTTTTTTTTTTTTTTTVN\tCTGTAGCC\n",
               " A12\tdt(15)VN\tRound1_12\t/5Phos/AGGCCAGAGCATTCGAGTACAAGTTTTTTTTTTTTTTTVN\tAGTACAAG\n",
               " B1\tdt(15)VN\tRound1_13\t/5Phos/AGGCCAGAGCATTCGAACAACCATTTTTTTTTTTTTTTVN\tAACAACCA\n",
               " B2\tdt(15)VN\tRound1_14\t/5Phos/AGGCCAGAGCATTCGAACCGAGATTTTTTTTTTTTTTTVN\tAACCGAGA\n",
               " B3\tdt(15)VN\tRound1_15\t/5Phos/AGGCCAGAGCATTCGAACGCTTATTTTTTTTTTTTTTTVN\tAACGCTTA\n",
               " B4\tdt(15)VN\tRound1_16\t/5Phos/AGGCCAGAGCATTCGAAGACGGATTTTTTTTTTTTTTTVN\tAAGACGGA\n",
               " B5\tdt(15)VN\tRound1_17\t/5Phos/AGGCCAGAGCATTCGAAGGTACATTTTTTTTTTTTTTTVN\tAAGGTACA\n",
               " B6\tdt(15)VN\tRound1_18\t/5Phos/AGGCCAGAGCATTCGACACAGAATTTTTTTTTTTTTTTVN\tACACAGAA\n",
               " B7\tdt(15)VN\tRound1_19\t/5Phos/AGGCCAGAGCATTCGACAGCAGATTTTTTTTTTTTTTTVN\tACAGCAGA\n",
               " B8\tdt(15)VN\tRound1_20\t/5Phos/AGGCCAGAGCATTCGACCTCCAATTTTTTTTTTTTTTTVN\tACCTCCAA\n",
               " B9\tdt(15)VN\tRound1_21\t/5Phos/AGGCCAGAGCATTCGACGCTCGATTTTTTTTTTTTTTTVN\tACGCTCGA\n",
               " B10\tdt(15)VN\tRound1_22\t/5Phos/AGGCCAGAGCATTCGACGTATCATTTTTTTTTTTTTTTVN\tACGTATCA\n",
               " B11\tdt(15)VN\tRound1_23\t/5Phos/AGGCCAGAGCATTCGACTATGCATTTTTTTTTTTTTTTVN\tACTATGCA\n",
               " B12\tdt(15)VN\tRound1_24\t/5Phos/AGGCCAGAGCATTCGAGAGTCAATTTTTTTTTTTTTTTVN\tAGAGTCAA\n",
               " C1\tdt(15)VN\tRound1_25\t/5Phos/AGGCCAGAGCATTCGAGATCGCATTTTTTTTTTTTTTTVN\tAGATCGCA\n",
               " C2\tdt(15)VN\tRound1_26\t/5Phos/AGGCCAGAGCATTCGAGCAGGAATTTTTTTTTTTTTTTVN\tAGCAGGAA\n",
               " C3\tdt(15)VN\tRound1_27\t/5Phos/AGGCCAGAGCATTCGAGTCACTATTTTTTTTTTTTTTTVN\tAGTCACTA\n",
               " C4\tdt(15)VN\tRound1_28\t/5Phos/AGGCCAGAGCATTCGATCCTGTATTTTTTTTTTTTTTTVN\tATCCTGTA\n",
               " C5\tdt(15)VN\tRound1_29\t/5Phos/AGGCCAGAGCATTCGATTGAGGATTTTTTTTTTTTTTTVN\tATTGAGGA\n",
               " C6\tdt(15)VN\tRound1_30\t/5Phos/AGGCCAGAGCATTCGCAACCACATTTTTTTTTTTTTTTVN\tCAACCACA\n",
               " C7\tdt(15)VN\tRound1_31\t/5Phos/AGGCCAGAGCATTCGGACTAGTATTTTTTTTTTTTTTTVN\tGACTAGTA\n",
               " C8\tdt(15)VN\tRound1_32\t/5Phos/AGGCCAGAGCATTCGCAATGGAATTTTTTTTTTTTTTTVN\tCAATGGAA\n",
               " C9\tdt(15)VN\tRound1_33\t/5Phos/AGGCCAGAGCATTCGCACTTCGATTTTTTTTTTTTTTTVN\tCACTTCGA\n",
               " C10\tdt(15)VN\tRound1_34\t/5Phos/AGGCCAGAGCATTCGCAGCGTTATTTTTTTTTTTTTTTVN\tCAGCGTTA\n",
               " C11\tdt(15)VN\tRound1_35\t/5Phos/AGGCCAGAGCATTCGCATACCAATTTTTTTTTTTTTTTVN\tCATACCAA\n",
               " C12\tdt(15)VN\tRound1_36\t/5Phos/AGGCCAGAGCATTCGCCAGTTCATTTTTTTTTTTTTTTVN\tCCAGTTCA\n",
               " D1\tdt(15)VN\tRound1_37\t/5Phos/AGGCCAGAGCATTCGCCGAAGTATTTTTTTTTTTTTTTVN\tCCGAAGTA\n",
               " D2\tdt(15)VN\tRound1_38\t/5Phos/AGGCCAGAGCATTCGCCGTGAGATTTTTTTTTTTTTTTVN\tCCGTGAGA\n",
               " D3\tdt(15)VN\tRound1_39\t/5Phos/AGGCCAGAGCATTCGCCTCCTGATTTTTTTTTTTTTTTVN\tCCTCCTGA\n",
               " D4\tdt(15)VN\tRound1_40\t/5Phos/AGGCCAGAGCATTCGCGAACTTATTTTTTTTTTTTTTTVN\tCGAACTTA\n",
               " D5\tdt(15)VN\tRound1_41\t/5Phos/AGGCCAGAGCATTCGCGACTGGATTTTTTTTTTTTTTTVN\tCGACTGGA\n",
               " D6\tdt(15)VN\tRound1_42\t/5Phos/AGGCCAGAGCATTCGCGCATACATTTTTTTTTTTTTTTVN\tCGCATACA\n",
               " D7\tdt(15)VN\tRound1_43\t/5Phos/AGGCCAGAGCATTCGCTCAATGATTTTTTTTTTTTTTTVN\tCTCAATGA\n",
               " D8\tdt(15)VN\tRound1_44\t/5Phos/AGGCCAGAGCATTCGCTGAGCCATTTTTTTTTTTTTTTVN\tCTGAGCCA\n",
               " D9\tdt(15)VN\tRound1_45\t/5Phos/AGGCCAGAGCATTCGCTGGCATATTTTTTTTTTTTTTTVN\tCTGGCATA\n",
               " D10\tdt(15)VN\tRound1_46\t/5Phos/AGGCCAGAGCATTCGGAATCTGATTTTTTTTTTTTTTTVN\tGAATCTGA\n",
               " D11\tdt(15)VN\tRound1_47\t/5Phos/AGGCCAGAGCATTCGCAAGACTATTTTTTTTTTTTTTTVN\tCAAGACTA\n",
               " D12\tdt(15)VN\tRound1_48\t/5Phos/AGGCCAGAGCATTCGGAGCTGAATTTTTTTTTTTTTTTVN\tGAGCTGAA\n",
               " E1\trandom hexamer\tRound1_49\t/5Phos/AGGCCAGAGCATTCGGATAGACANNNNNN\tGATAGACA\n",
               " E2\trandom hexamer\tRound1_50\t/5Phos/AGGCCAGAGCATTCGGCCACATANNNNNN\tGCCACATA\n",
               " E3\trandom hexamer\tRound1_51\t/5Phos/AGGCCAGAGCATTCGGCGAGTAANNNNNN\tGCGAGTAA\n",
               " E4\trandom hexamer\tRound1_52\t/5Phos/AGGCCAGAGCATTCGGCTAACGANNNNNN\tGCTAACGA\n",
               " E5\trandom hexamer\tRound1_53\t/5Phos/AGGCCAGAGCATTCGGCTCGGTANNNNNN\tGCTCGGTA\n",
               " E6\trandom hexamer\tRound1_54\t/5Phos/AGGCCAGAGCATTCGGGAGAACANNNNNN\tGGAGAACA\n",
               " E7\trandom hexamer\tRound1_55\t/5Phos/AGGCCAGAGCATTCGGGTGCGAANNNNNN\tGGTGCGAA\n",
               " E8\trandom hexamer\tRound1_56\t/5Phos/AGGCCAGAGCATTCGGTACGCAANNNNNN\tGTACGCAA\n",
               " E9\trandom hexamer\tRound1_57\t/5Phos/AGGCCAGAGCATTCGGTCGTAGANNNNNN\tGTCGTAGA\n",
               " E10\trandom hexamer\tRound1_58\t/5Phos/AGGCCAGAGCATTCGGTCTGTCANNNNNN\tGTCTGTCA\n",
               " E11\trandom hexamer\tRound1_59\t/5Phos/AGGCCAGAGCATTCGGTGTTCTANNNNNN\tGTGTTCTA\n",
               " E12\trandom hexamer\tRound1_60\t/5Phos/AGGCCAGAGCATTCGTAGGATGANNNNNN\tTAGGATGA\n",
               " F1\trandom hexamer\tRound1_61\t/5Phos/AGGCCAGAGCATTCGTATCAGCANNNNNN\tTATCAGCA\n",
               " F2\trandom hexamer\tRound1_62\t/5Phos/AGGCCAGAGCATTCGTCCGTCTANNNNNN\tTCCGTCTA\n",
               " F3\trandom hexamer\tRound1_63\t/5Phos/AGGCCAGAGCATTCGTCTTCACANNNNNN\tTCTTCACA\n",
               " F4\trandom hexamer\tRound1_64\t/5Phos/AGGCCAGAGCATTCGTGAAGAGANNNNNN\tTGAAGAGA\n",
               " F5\trandom hexamer\tRound1_65\t/5Phos/AGGCCAGAGCATTCGTGGAACAANNNNNN\tTGGAACAA\n",
               " F6\trandom hexamer\tRound1_66\t/5Phos/AGGCCAGAGCATTCGTGGCTTCANNNNNN\tTGGCTTCA\n",
               " F7\trandom hexamer\tRound1_67\t/5Phos/AGGCCAGAGCATTCGTGGTGGTANNNNNN\tTGGTGGTA\n",
               " F8\trandom hexamer\tRound1_68\t/5Phos/AGGCCAGAGCATTCGTTCACGCANNNNNN\tTTCACGCA\n",
               " F9\trandom hexamer\tRound1_69\t/5Phos/AGGCCAGAGCATTCGAACTCACCNNNNNN\tAACTCACC\n",
               " F10\trandom hexamer\tRound1_70\t/5Phos/AGGCCAGAGCATTCGAAGAGATCNNNNNN\tAAGAGATC\n",
               " F11\trandom hexamer\tRound1_71\t/5Phos/AGGCCAGAGCATTCGAAGGACACNNNNNN\tAAGGACAC\n",
               " F12\trandom hexamer\tRound1_72\t/5Phos/AGGCCAGAGCATTCGAATCCGTCNNNNNN\tAATCCGTC\n",
               " G1\trandom hexamer\tRound1_73\t/5Phos/AGGCCAGAGCATTCGAATGTTGCNNNNNN\tAATGTTGC\n",
               " G2\trandom hexamer\tRound1_74\t/5Phos/AGGCCAGAGCATTCGACACGACCNNNNNN\tACACGACC\n",
               " G3\trandom hexamer\tRound1_75\t/5Phos/AGGCCAGAGCATTCGACAGATTCNNNNNN\tACAGATTC\n",
               " G4\trandom hexamer\tRound1_76\t/5Phos/AGGCCAGAGCATTCGAGATGTACNNNNNN\tAGATGTAC\n",
               " G5\trandom hexamer\tRound1_77\t/5Phos/AGGCCAGAGCATTCGAGCACCTCNNNNNN\tAGCACCTC\n",
               " G6\trandom hexamer\tRound1_78\t/5Phos/AGGCCAGAGCATTCGAGCCATGCNNNNNN\tAGCCATGC\n",
               " G7\trandom hexamer\tRound1_79\t/5Phos/AGGCCAGAGCATTCGAGGCTAACNNNNNN\tAGGCTAAC\n",
               " G8\trandom hexamer\tRound1_80\t/5Phos/AGGCCAGAGCATTCGATAGCGACNNNNNN\tATAGCGAC\n",
               " G9\trandom hexamer\tRound1_81\t/5Phos/AGGCCAGAGCATTCGATCATTCCNNNNNN\tATCATTCC\n",
               " G10\trandom hexamer\tRound1_82\t/5Phos/AGGCCAGAGCATTCGATTGGCTCNNNNNN\tATTGGCTC\n",
               " G11\trandom hexamer\tRound1_83\t/5Phos/AGGCCAGAGCATTCGCAAGGAGCNNNNNN\tCAAGGAGC\n",
               " G12\trandom hexamer\tRound1_84\t/5Phos/AGGCCAGAGCATTCGCACCTTACNNNNNN\tCACCTTAC\n",
               " H1\trandom hexamer\tRound1_85\t/5Phos/AGGCCAGAGCATTCGCCATCCTCNNNNNN\tCCATCCTC\n",
               " H2\trandom hexamer\tRound1_86\t/5Phos/AGGCCAGAGCATTCGCCGACAACNNNNNN\tCCGACAAC\n",
               " H3\trandom hexamer\tRound1_87\t/5Phos/AGGCCAGAGCATTCGCCTAATCCNNNNNN\tCCTAATCC\n",
               " H4\trandom hexamer\tRound1_88\t/5Phos/AGGCCAGAGCATTCGCCTCTATCNNNNNN\tCCTCTATC\n",
               " H5\trandom hexamer\tRound1_89\t/5Phos/AGGCCAGAGCATTCGCGACACACNNNNNN\tCGACACAC\n",
               " H6\trandom hexamer\tRound1_90\t/5Phos/AGGCCAGAGCATTCGCGGATTGCNNNNNN\tCGGATTGC\n",
               " H7\trandom hexamer\tRound1_91\t/5Phos/AGGCCAGAGCATTCGCTAAGGTCNNNNNN\tCTAAGGTC\n",
               " H8\trandom hexamer\tRound1_92\t/5Phos/AGGCCAGAGCATTCGGAACAGGCNNNNNN\tGAACAGGC\n",
               " H9\trandom hexamer\tRound1_93\t/5Phos/AGGCCAGAGCATTCGGACAGTGCNNNNNN\tGACAGTGC\n",
               " H10\trandom hexamer\tRound1_94\t/5Phos/AGGCCAGAGCATTCGGAGTTAGCNNNNNN\tGAGTTAGC\n",
               " H11\trandom hexamer\tRound1_95\t/5Phos/AGGCCAGAGCATTCGGATGAATCNNNNNN\tGATGAATC\n",
               " H12\trandom hexamer\tRound1_96\t/5Phos/AGGCCAGAGCATTCGGCCAAGACNNNNNN\tGCCAAGAC\n"]
    for i in range(b1 - 1, b2):
        fo.write(bc_list[i] + bc_list[i + 48])
    fo.close()
