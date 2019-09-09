SPLiT-seq Data Analysis Toolkit (SDAT)

SDAT is designed for analysing SPLiT-seq data


# News

You can use "pip install sdat" to install SDAT.


# Requirement:
# featureCounts samtools STAR

# Python2 & python3

# Installation:

pip install sdat  or

python setup.py install

# Usage:

sdat filter -b1 1-8  -b2 1-96  -b3 1-96  -e 1 -R1 xxxx_R1.fq(.gz)  -R2 xxxx_R2.fq(.gz)



sdat align -g -m 5000 -o output_dir/prefix  -gtf gtf_file  -G index   -fq xxxx_filtered.fq



sdat cell  -b xxxx.bam    or    sdat cell  -s xxxx.sam



sdat count -d 200 -p 10 -gtf  gtf_file  -g Reads_number_per_cell.log  -in cell_folder





# Attention:  

a. the input data for "sdat filters" need to be clean data

b. Before using "sdat cell", BAM file should be sorted by  postion. 
