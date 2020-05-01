#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapping and Filtering

Map: just an accumulation pattern which contains every item of a list or
every *transformed* item of a list (for instance, each_item *2) . But all of them.
Filtering: similarly to mapping, it cointains items from a list. There item are
in their original state or transformed. But not every item (in its original state or transformed)
is acucumulated
"""

numbers=[1,2,3,4,5,6,7]

numbers_multiplied = []
#Ex1. map; every item is accumulated -transformed (*2) in this case, it doesn't matter
for number in numbers:
    numbers_multiplied.append(number * 2)
print(numbers_multiplied)
    
odd_numbers = []
# filter, not every item (transformed or in its original form) appears in the list
for number in numbers:
    if not number %2==0:
        odd_numbers.append(number)
print(odd_numbers)

#using the map function.
#Parameters: a function that will be apllied to every item of the list, and a list
#itdoes the same that Ex 1..
print("MAP FUNCTION")

multiplied = map(lambda x: x*2, numbers)
print(multiplied)
# ..or it doesn't. map returns an iterable (map class) object, not the expected list. We need to cast it
print(type(multiplied))
multiplied=list(multiplied)
print("Now it works! ")

print(multiplied)

#Filter function works similarly. With one difference:
#int the map function , each item is transformed according to the function we are usging as an argument
#and stored in is trasnformed form
#IN filtering, the function returns a boolean, and its value is not stored, but used
#to decide a given element of the list must be stored (the function return True for that element)
# or not (the function returns False)
#As with map, we have to transform it as well from "filter" (iterable) to list format.
print("FILTER FUNCTION")

odd_numbers=filter(lambda x: not x%2==0, numbers)
print(type(odd_numbers))
odd_numbers=list(odd_numbers)
print("Now it works! ")

print(odd_numbers)





