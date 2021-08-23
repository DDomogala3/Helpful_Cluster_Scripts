#!/usr/bin/env python3
import os
import mmh3
import screed


sequence_file = "ERR6095742_pass.fastq"                  

    
  

def kmer_count_better(k, sequence):
    '''
#    Return a list of the number of times each possible k-mer appears
#    in seq, including overlapping occurrences.
#    '''

    rv = {}
    for read in screed.open(sequence):
        sequence = read.sequence
        for i in range(0, len(sequence)-k+1):
            subseq = sequence[i:i+k]
            v = rv.get(subseq, 0)
            rv[subseq] = v + 1
           
    return list(rv.items()), len(sequence)

print(kmer_count_better(2, sequence_file))



             
#def hash_construct(kmer):
#    # calculate the reverse complement
#    rc_kmer = screed.rc(kmer)
#    
#    # determine whether original k-mer or reverse complement is lesser
#    if kmer < rc_kmer:
#        canonical_kmer = kmer
#    else:
#        canonical_kmer = rc_kmer
        
#    # calculate murmurhash using a hash seed of 42
#    hash = mmh3.hash64(canonical_kmer, 42)[0]
#    if hash < 0: hash += 2**64
        
#    # done
#    return hash
              
#def hash_kmers(kmers):
#    hashes = []
#    for kmer in kmers:
#        hashes.append(hash_construct(kmer))
#    return hashes   
#hash_kmers()
