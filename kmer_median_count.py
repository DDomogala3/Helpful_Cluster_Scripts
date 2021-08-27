#!/usr/bin/env python3
import os
import screed
import itertools
import argparse
import statistics
from collections import Counter
import csv

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


first_read_kmer = kmer_count_better(seq, k)
trimer = Counter(first_read_kmer)
#print(trimer)




def build_kmers(seq, ksize):
    kmers = []
    db = screed.read_fastq_sequences(input)
    for name in db:
        full_seq = db[name].sequence
        n_kmers = len(full_seq) - ksize + 1
        for i in range(n_kmers):
            kmer = full_seq[i:i + ksize]
            kmers.append(kmer)

    return kmers

km3 = build_kmers(seq, k)
kmer_seq = Counter(km3)
#print(trimer)
#print(trimer)
total = sum(kmer_seq.values(),1)
median = statistics.median(kmer_seq.values())
quantiles = statistics.quantiles(kmer_seq.values())
#print(median)
for key in kmer_seq:
    normal_result = []
    kmer_seq[key] /= median
    normal_result.append(kmer_seq)
    print(normal_result)
