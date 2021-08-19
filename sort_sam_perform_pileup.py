#!/usr/bin/env python3
import pysam
from pysam.libcalignmentfile import IteratorColumnRegion

pysam.sort("-o", "ncbi/public/fastq/SRR15288538_pass_trimmed_sort.sam", "ncbi/public/fastq/SRR15288538_pass_trimmed.sam")
samfile = pysam.AlignmentFile("ncbi/public/fastq/SRR15288538_pass_trimmed_sort.sam","rb")
#for read in samfile.fetch(until_eof=True):
#    print(read)
#samfile.close()
for pileup in samfile.pileup(until_eof=True):
    print ("\ncoverage at base %s = %s" %
    (pileup.pos, pileup.n))
    for pileupread in pileup.pileups:
       if not pileupread.is_del and not pileupread.is_refskip:
           print('\tbase =%s' % (pileupread.alignment.query_sequence[pileupread.query_position]))

samfile.close()
