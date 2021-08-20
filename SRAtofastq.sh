#step one use SRA tools
prefetch SRR15288538
#download SRA through prefetch
#convert to fastq using SRA tools

#append --outdir, outdir has to be in your home directory, split_spot--seperates reads into left and right reads and combines them into one file, --read-filter pass, filters out reads that
#are N's or useless
fastq-dump --outdir $PWD/ncbi/public/fastq/ --split-spot --readids --read-filter pass --dumpbase --clip SRR15288538

sleep 100
#fastq trim, trimedges of fastq using trimmomatic, minimum(MINLEN) length must be 150 basepairs, LEADING, TRAILING, cut 30 basepairs off of either end of read.
trimmomatic SE -threads 1 $PWD/ncbi/public/fastq/SRR15288538_pass.fastq $PWD/ncbi/public/fastq/SRR15288538_pass_trimmed.fastq MINLEN:150 LEADING:30 TRAILING:30
#Input Reads: 10187 Surviving: 9224 (90.55%) Dropped: 963 (9.45%)

#align to reference,NC-045512.2 and create sam file using minimap2
minimap2 -t 1 -a -x sr $PWD/NC_045512.2.fasta $PWD/ncbi/public/fastq/SRR15288538_pass_trimmed.fastq -o $PWD/ncbi/public/fastq/SRR15288538_pass_trimmed.sam

#count the number of base pairs per position along the genome,python script is written using pysam. Because there are no genomic coordinates, 
#the pileup goes from end to end. 

python3 sort_sam_perform_pileup.py
