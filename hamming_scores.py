import itertools
from itertools import izip, imap
import operator
str1 = raw_input(" ")
str2 = raw_input(" ")
def hamming2(str1, str2):
	assert len(str1) == len(str2)
	ne = operator.ne
	return sum(imap(ne, str1, str2))
print "Your hamming score for your forward primer pair is %d" % hamming2(str1,str2
)

str3 = raw_input(" ")
str4 = raw_input(" ")
def hamming2(str3, str4):
	assert len(str3) == len(str4)
	ne = operator.ne
	return sum(imap(ne, str3, str4))
print "Your hamming score for your reverse primer pair is %d" % hamming2(str3,str4)

