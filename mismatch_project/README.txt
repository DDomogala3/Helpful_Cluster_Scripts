The input to this script is a combination of 8 bp Illumina primers that are unique to a sample on a sequencing plate. 
The output of this script will be a pair of 8 bp Illumina primers that are unique but as distinct as possible from 
barcodes that were used with samples from the previous run. 

This script will grab input reads, slice out the 8 bp combination for a particular sample, then 
assign a new pair of primers that have the farthest hamming distance possible from the previous primer set. 

The Hamming Distance for the mismatch between primer sets should be a score of 3 or higher(Bystrykh, 2012). 




