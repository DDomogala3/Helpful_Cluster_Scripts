#step one use SRA tools
prefetch SRR15288538
#download SRA through prefetch
#convert to fastq using SRA tools


fastq-dump --outdir $PWD/ncbi/public/fastq/ --skip-technical --readids --read-filter pass --dumpbase --clip SRR15288538

sleep 100
#fastq trim, trimedges of fastq using trimmomatic
trimmomatic SE -threads 1 $PWD/ncbi/public/fastq/SRR15288538_pass.fastq $PWD/ncbi/public/fastq/SRR15288538_pass_trimmed.fastq MINLEN:300 LEADING:30 TRAILING:30
#Input Reads: 10187 Surviving: 9224 (90.55%) Dropped: 963 (9.45%)

#align to reference,NC-045512.2 and create sam file using minimap2
minimap2 -t 1 -a -x sr $PWD/NC_045512.2.fasta $PWD/ncbi/public/fastq/SRR15288538_pass_trimmed.fastq -o $PWD/ncbi/public/fastq/SRR15288538_pass_trimmed.sam

#count(ACTGS per position), start of python sript using pysam

python3 sort_sam_perform_pileup.py
