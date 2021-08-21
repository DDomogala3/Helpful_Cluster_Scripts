pysam.sort("-o", "ncbi/public/fastq/SRR15288538_pass_trimmed_sort.sam", "ncbi/public/fastq/SRR15288538_pass_trimmed.sam")
samfile = pysam.AlignmentFile("ncbi/public/fastq/SRR15288538_pass_trimmed_sort.sam","rb")


#for read in samfile.fetch(until_eof=True):
#    print(read)
#samfile.close()
#c = Counter({'C':0,'A':0,'G':0,'T':0,'N':0})
for pileup in samfile.pileup(until_eof=True):
    c = Counter({'C':0,'A':0,'G':0,'T':0,'N':0})
    print ("\ncoverage at base %s = %s" %
    (pileup.pos, pileup.n))
    for pileupread in pileup.pileups:
       if not pileupread.is_del and not pileupread.is_refskip:
           c[pileupread.alignment.query_sequence[pileupread.query_position].upper()]+=1
           print('\tbase =%s' % (pileupread.alignment.query_sequence[pileupread.query_position]))
           #c[pileupread.alignment.query_sequence[pileupread.query_position].upper()]
           print(c)
           #break
        
           

samfile.close()
