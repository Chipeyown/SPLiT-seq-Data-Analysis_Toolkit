SPLiT-seq Data Analysis Toolkit (SDAT)

SDAT is designed for analysing SPLiT-seq data


# News

You can use "pip install sdat" to install SDAT.


# Requirement:
# featureCounts samtools tophat bowtie2

# Unix & Python2 & python3

# Installation:

pip install sdat  or

python setup.py install

# Usage:

sdat filters |  [options]  | barcode_folder | output_path | -R1 read1 | -R2 read2



sdat align |   [options]  | index_path | genome_annotation(.gtf) | filtered_fastq | output_path 



sdat cell  |  [options]  |  aligned_reads(.bam) |  output_path 



sdat counts  |  [options]  |  cell_folder  |  genome_annotation(.gtf)  |  output_path 





# Attention:  

a. the input data for "sdat filters" need to be clean data

b. Before using "sdat cell", BAM file should be sorted by  postion. 
