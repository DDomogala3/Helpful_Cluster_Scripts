
#!/usr/bin/env python3
import os
import mmh3
import screed
import itertools
import argparse
import statistics

parser = argparse.ArgumentParser()
parser.add_argument("input",help = "the input fastq file")
#args = parser.parse_args()
parser.add_argument("k",help = "the kmer input size",type=int)
args = parser.parse_args()
sequence_file = args.input
k = args.k

#sequence_file = "ERR6095742_pass.fastq"

def kmer_count_better(k, sequence):
    '''
#    Return a list of the number of times each possible k-mer appears
#    in seq, including overlapping occurrences.
#    '''

    rv = {}
    for read in screed.open(sequence):
        sequence = read.sequence
    for i in range(0, len(sequence)-k+1):
        read_subseq = sequence[i:1+k]
        v = rv.get(read_subseq, 0)
        for i in range(0, len(sequence)-k+1):
              subseq = sequence[i:i+k]
              v = rv.get(subseq, 0)
              rv[subseq] = v + 1
              while v > 0:
                  rv[read_subseq] = v + 1
                  rv_len = len(rv)
#                 print(rv)
                  sumrv = sum(rv.values())
                  sumrv_list = list(rv.values())
                  print(statistics.median(sumrv_list))
