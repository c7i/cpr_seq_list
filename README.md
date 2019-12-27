# cpr_seq_list
Find all possible Danish Personal Identification (CPR) numbers using a date of birth and optionally gender. 

This script generates a list of all possible sequence numbers, which are the last 4 unknown digits in a CPR number.

A date of birth before October 2007 and a specified gender will give about 272 possibilities, making a brute force more feasible.

### example usage
```
$ ./print_possibilities.py
```

### note
* Omitting gender is possible, but will double amount of possibilities
* Year of birth not necessary to specify unless person is > 100 years old
