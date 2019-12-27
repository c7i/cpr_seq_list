#!/usr/bin/env python

from sequence_list import SequenceList

six_digits = input(':: Enter first six digits or birth date (format: ddmmyy): ')
gender = input(':: Enter gender as m/f: ')
year = input(':: Enter year: ')
print(':: Printing possibilities...')

seq_list = SequenceList(six_digits, gender, year)
for i in seq_list: print(six_digits + '-' + i)

print('Number of possibilities: ' + str(len(seq_list)))
