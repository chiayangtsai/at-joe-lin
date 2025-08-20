#windows platform

import sys
from basics import *

if __name__ == '__main__':
    testID = 20

    if len(sys.argv) != 2:
        print("default: %d" % testID)
    else:
        testID = int(sys.argv[1])

    if testID == 0:
        print("Hello world")
    elif testID == 1:
        basic_bubble_sort()  #bubble sort
    elif testID == 2:
        basic_time_complexity()  #time complexity
    elif testID == 3:
        basic_list_i()  # list i
    elif testID == 5:
        leetcode_shuffle_two_lists()
    elif testID == 6:
        leetcode_merge_two_lists()
    elif testID == 7:
        basic_list_ii()  # list ii
    elif testID == 8:
        basic_list_iii()  # built-in methods
    elif testID == 9:
        leetcode_stock_trade_i()  #sliding window
    elif testID == 10:
        leetcode_stock_trade_iii() #<=== HW0816(VK): start from here
    elif testID == 11: 
        basic_copy() #shallow copy, deep copy, immutable/mutable
    elif testID == 12:
        basic_string() # ASCII, KES algorithm
    elif testID == 14:
        leetcode_alphabet_histogram()
    elif testID == 15:
        leetcode_lonest_substring_without_repeating() # sliding, LUT (KES), LUT(dict)
    elif testID == 16:
        leetcode_alternating_strings() #sliding window
    elif testID == 20:
        basic_dict()
        

'''
上

中
- dict : LUT
- search : single element, series of numbers
- leetcode : two sum 
- sliding window + LUT (Look-up Table, Hash table)
- string <-> list
- decimal, binary representation
- .sort()

下
- recursive programming | DP principles
- 2D problems - coordinators conversion - raster-scan, zig-scan order

- leetcode 150 : "easy", "medium", before "stack"

- binary tree concept
- binary tree - breadth-first (BF) creation

---- ADVANCED LEVEL ---
- binary tree..
......

'''
