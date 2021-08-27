#!/usr/bin/env python3
import os
import screed
import itertools
import argparse
import statistics
from collections import Counter
parser = argparse.ArgumentParser()
parser.add_argument("input",help = "the input fastq file")
#args = parser.parse_args()
parser.add_argument("k",help = "the kmer input size",type=int)
#parser.add_argument("sn", help = "the number of sequences in the file", type = int)
args = parser.parse_args()
input = args.input
k = args.k
#sn = args.sn
#sequence_file = "ERR6095742_pass.fastq"
import sys
import time
#this is just a function I stole off of stackoverflow to produce a spinner
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

def readFastqFile(input):
    """
    Reads and returns file as FASTA format with special characters removed.
    """
    with screed.open(input) as seqfile:
        for read in seqfile:
            seq = read.sequence
            for record in seqfile:
                record = record.sequence
    return seq
seq = readFastqFile(input)
record = readFastqFile(input)


def kmer_count_better(sequence,ksize):
    kmers = []
    n_kmers = len(sequence) - ksize + 1
    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)
    return kmers
    print(kmers)


km3 = kmer_count_better(seq, k)
trimer = Counter(km3)




def build_kmers(seq, ksize):
    kmers = []
    n_kmers = len(seq) - ksize + 1
    db = screed.read_fastq_sequences(input)
    for name in db:
        full_seq = db[name].sequence
        for i in range(n_kmers):
            kmer = seq[i:i + ksize]
            kmers.append(kmer)

    return kmers

km3 = build_kmers(seq, k)
trimer = Counter(km3)
total = statistics.median(trimer.values())
print(total)
for key in trimer:
    trimer[key] /= total
    print(trimer)
