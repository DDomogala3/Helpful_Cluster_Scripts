#!/usr/bin/env python3
import os
import screed
import itertools
import argparse
import statistics

parser = argparse.ArgumentParser()
parser.add_argument("input",help = "the input fastq file")
#args = parser.parse_args()
parser.add_argument("k",help = "the kmer input size",type=int)
#parser.add_argument("sn", help = "the number of sequences in the file", type = int)
args = parser.parse_args()
sequence_file = args.input
k = args.k
#sn = args.sn
#sequence_file = "ERR6095742_pass.fastq"
import sys
import time
#this is just a function I stole off of stackoverflow to produce a spinning cursor :)

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for _ in range(50):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

def kmer_count_better(k, sequence):
    '''
#    Return a list of the number of times each possible k-mer appears
#    in seq, including overlapping occurrences.
#    '''

    rv = {}
    for record in screed.open(sequence):
        sequence = record.sequence
        for i in range(0, len(sequence)-k+1):
               read_subseq = sequence[i:1+k]
               v = rv.get(read_subseq, 0)
               rv[read_subseq] = v + 1
#              print(rv)
#              print(sequence)
               read_rvlist = list(rv.values())
               statistics.median(read_rvlist)
               break

    return statistics.median(read_rvlist)
print(kmer_count_better(k, sequence_file))
