#!/usr/bin/env python
from sys import stdin

sum = 0
for line in stdin:
    line = line.strip()
    numbers = []

    first_number = ''
    first_index = 1000000
    last_index = -1
    last_number = ''
    for thing, number in [
        ('0' ,'0' ),
        ('1' ,'1' ),
        ('2' ,'2'),
        ('3' ,'3' ),
        ('4' ,'4' ),
        ('5' ,'5' ),
        ('6' ,'6' ),
        ('7' ,'7' ),
        ('8' ,'8' ),
        ('9' ,'9'  ),
        ('0' ,'zero'),
        ('1' ,'one'),
        ('2' ,'two'),
        ('3' ,'three'),
        ('4' ,'four'),
        ('5' ,'five'),
        ('6' ,'six'),
        ('7' ,'seven'),
        ('8' ,'eight'),
        ('9' ,'nine'),
        ]:
        if number in line:
            fi = line.index(number)
            li = line.rindex(number)
            if fi < first_index:
                first_index = fi
                first_number = thing

            if li > last_index:
                last_index = li
                last_number = thing

    sum += int(first_number + last_number)

    # for char in line:
    #     if char in "1234567890":
    #         numbers.append(char)
    #     else:
            
    # sum += int(numbers[0] + numbers[-1])
print(sum)

