def basic_bubble_sort():
    #Q: use bubble sort to complete ascending sort results
    a = [3, 5, 1, 4, 2]
    #time complexity : O(N^2)
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    print(a)


def basic_time_complexity():
    # execution time response vs input data size (N)
    #  Big-O function : O(N)
    #                   O(N^2) : 2nd order
    #                   O(1) : data size irrelevant
    return


def basic_list_i():

    #-- memory ---
    a = [3, 5, 1, 4, 2]  #<== vector/array
    #    0  1  2  3  4
    # a represent the "memory address" of the elements in the list

    # -- indexing
    #Q: print out the index-2 element => 1
    print(a[2])

    # -- last index
    #Q: print out the last index element => 2
    print(a[-1])
    print(a[len(a) - 1])

    # --- + : connect /cascade
    a = [3, 1, 2]
    b = [1, 2]
    #Q: append b to a
    a = a + b

    #Q: append a new element -1 to a => [3, 1, 2, -1]
    a = [3, 1, 2]
    a = a + [-1]  #拆掉重蓋

    a = [3, 1, 2]
    a += [-1]  #加蓋

    a = [3, 1, 2]
    a.append(-1)  #加蓋


def leetcode_shuffle_two_lists():
    a = [3, 5, 1, 4, 2]
    b = [0, 7, 6]
    c = []
    #Q: shuffle a and b to a new list c following index order
    # c=> [3, 0, 5, 7, 1, 6, 4, 2]
    #HW0808 : O(N)
    #
    print("-------- v0------")
    #time complexity : O(N) 
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if i == j:
            c.append(a[i])  #O(1) 
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i::]
    if j < len(b):
        c += b[j::]

    print(c)
    print("-------- v1------")
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if i < len(a):
            c.append(a[i])
            i += 1
        if j < len(b):
            c.append(b[j])
            j += 1

    print("------ v2--------")
    a = [3, 5, 1, 4, 2]
    b = [0, 7, 6]
    c = []
    #time complexity : O(N^2)
    while len(a) > 0 or len(b) > 0: #N
        if len(a) > 0:
            c.append(a.pop(0)) #N
        if len(b) > 0:
            c.append(b.pop(0))
    print(c)


    print("------ v2.1--------")
    a = [3, 5, 1, 4, 2]
    b = [0, 7, 6]
    c = []

    a= a[::-1]  #N
    b= b[::-1]  #N

    while len(a) > 0 or len(b) > 0: #N
        if len(a) > 0:
            c.append(a.pop())
        if len(b) > 0:
            c.append(b.pop())
    print(c)

    print("------ v2.1--------")
    a = [3, 5, 1, 4, 2]
    b = [0, 7, 6]
    c = []
    
    a= a[::-1]  #N
    b= b[::-1]  #N
    
    while a or b: #N
        if a:
            c.append(a.pop())
        if b:
            c.append(b.pop())
    print(c)
    
                


def leetcode_merge_two_lists():
    a = [1, 2, 5, 6, 8]
    b = [0, 3, 4, 7, 10, 11]
    c = []
    #Q: Given two sorted lists a and b, merge these two lists to c and c is also sorted
    # c=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
    #HW0808 : O(N)
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    if i < len(a):
        c += a[i::]
    if j < len(b):
        c += b[j::]

    print(c)

    print("----- v1--------")
    a = [1, 2, 5, 6, 8]
    b = [0, 3, 4, 7, 10, 11]
    c = []
    i, j = 0, 0

    while i < len(a) or j < len(b):
        # if a and b exist
        #  compare a and b
        # else b not exist => take a
        # else take b
        
        if i < len(a) and j < len(b):
            if a[i] > b[j]:
                c.append(b[j])
                j += 1
            else:
                c.append(a[i])
                i += 1
        elif j >= len(b):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    print(c)
    print("----- v1.1--------")
    a = [1, 2, 5, 6, 8]
    b = [0, 3, 4, 7, 10, 11]
    c = []
    i, j = 0, 0
    
    while i < len(a) or j < len(b):
        if j >= len(b) or (i< len(a) and j< len(b) and a[i] < b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    print(c)
    
    print("--------- v2--------")
    a = [1, 2, 5, 6, 8]
    b = [0, 3, 4, 7, 10, 11]
    c = []
    #---
    a = a[::-1]
    b = b[::-1]
    while a or b:
        if a and b:            
            if a[-1] > b[-1]:
                c.append(b.pop())
            else:
                c.append(a.pop())
        elif not b: #explit
            c.append(a.pop())
        else:
            c.append(b.pop())
    print(c)

    print("--------- v2.1--------")
    a = [1, 2, 5, 6, 8]
    b = [0, 3, 4, 7, 10, 11]
    c = []
    #---
    a = a[::-1]
    b = b[::-1]
    while a or b:
        if (a and b and a[-1] > b[-1]) or not a:            
            c.append(b.pop())
        else:
            c.append(a.pop())
    print(c)

    print("--------- v3--------")
    #TBV
    

def basic_list_ii():
    a = [5, 4, 1, 3, 2, 9, 8]
    #    0  1  2  3  4  5  6
    d = a[2:6:1]  # => a[2:6]
    print("get the new list from index-2 to index-5: %s" % str(d))

    d = a[3:]
    print("get the new list from index-3 to index-6: %s" % str(d))

    d= a[::-1]
    print("get the new list with reversed order : %d" % str(d))

    return


def basic_list_iii():
    a= [3, 1, 5]

    #----- append ---- time complexity O(1) (most likely)
    #SKIP

    #----- pop(index) ----return the "popped-out" value
    #Q: pop out the first element in a
    a.pop(0)
    #Q: pop out the last element in a
    a.pop() #without index as input => default is the last index
    '''
    time complexity : 
     - last index : pop()- O(1)
     - Otherwise : O(N)

    '''
    #----- remove(element) ----
    # O(N)
    a= [100, 200, 300]
    #Q: remove the element with 200 value
    a.remove(200)


    # ---- del a[index] - LEGACY from C++
    # the same as .pop
    a= [3, 1, 5]
    #Q: pop out the first element in a
    del a[0]

    #----- insert(pos, element)
    #Q: O(N)
    a= [3, 1, 5]
    #Q: insert -1 to the position index-2
    a.insert(2, -1)


def leetcode_stock_trade_i():
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description
    
    
    # You are given an array prices where prices[i] is the price of a given stock on
    # the ith day.
    
    # You want to maximize your profit by choosing a single day to buy one stock and
    # choosing a different day in the future to sell that stock.
    
    # Return the maximum profit you can achieve from this transaction. If you cannot
    # achieve any profit, return 0.
    
    
    
    # Example 1:
    
    # Input: prices = [7,1,5,3,6,4]
    # Output: 5
    # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
    # 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because
    # you must buy before you sell. 
    
    #Example 2:
    # Input: prices = [7,6,4,3,1]
    # Output: 0
    # Explanation: In this case, no transactions are done and the max profit = 0.
    
    
    # Constraints:
    
    # 1 <= prices.length <= 10^5
    # 0 <= prices[i] <= 10^4

    '''
    7 1 5 3 6 4
              s
      b
    0   4 2 5 3 <== 5
    '''
    
    
    def maxProfitLR(prices):
        #HW0812
        return -1 #TBD
    
    prices = [7, 1, 5, 3, 6, 4]
    print("max profit : %d (ans 5)\n" % maxProfitLR(prices))
    
    prices = [7, 6, 4, 3, 0]
    print("max profit : %d (ans 0)\n" % maxProfitLR(prices))


    def maxProfitRL(prices):
        #HW0812
        return -1 #TBD
    
    prices = [7, 1, 5, 3, 6, 4]
    print("max profit : %d (ans 5)\n" % maxProfitRL(prices))
    
    prices = [7, 6, 4, 3, 0]
    print("max profit : %d (ans 0)\n" % maxProfitRL(prices))
    
    

    