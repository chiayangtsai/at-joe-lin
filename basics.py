

def basic_dict():
    # list/array : find : O(N), memory ordered   => pros: random access
    # dict       : find : O(1), memory unordered => cons: space complexity ~O(N)
    #------ init ---
    tab= {"John":90, "Vic":70, "Jason":95, "Mia":60, "Mary":70}

    # ------ insert ----
    #Q: insert "Jens", and his score is 80
    tab["Jens"] = 80

    # ------ find/search key ----
    #Q: access "Apple"
    #tab["Apple"] <=== (X) key does not exist
    key = "John"
    if key in tab: # O(1)
        print("%s, %d" % (key, tab[key]))
    else:
        print("key does not exit")


    print("------ .keys ----")
    # .keys() : return list of keys
    print(list(tab.keys()))

    for key in tab.keys():
        print("%s, %d" % (key, tab[key]))

    print("------ .items ----")
    # .items() : return list of tuples, each tuple (key, value)
    print(list(tab.items()))
    # [('John', 90), ('Vic', 70), ('Jason', 95), ('Mia', 60), ('Mary', 70), ('Jens', 80)]

    for x in tab.items():
        print(x[0], x[1])
    print("==")
    for key,score in tab.items():
        print(key, score)
    
    # ---- erase -----
    # HW0819(VK): start from here




def basic_string():
    # --- ASCII ---
    # how many ASCII codes? 128 <== 7 bits
    # 1 byte = 8 bits
    # ASCII table: https://www.asciitable.com/

    # -- charactor -> ASCII
    # ord(charactor)
    # -- ASCII -> charator
    # chr(ASCII)

    #Q: Given index value of "A" is 0, get the alphabet of index 20.
    # => U
    print(chr(ord('A') + 20))


def leetcode_alphabet_histogram():
    #Q: Given a string s, derive the lower-case alphabet histogram. Print out the results in alphabet order with the following format.
    #NOTE: only print out the appeared alphabets
    #NOTE: can't use "dict" container
    '''
    a 2
    b 2
    d 1
    p 1
    z 1
    '''

    s = "..b* a9bAQ..z(da#p;"

    #time complexity: O(N)
    #space complexity : O(1)
    res = [0] * 26  # key: alphabet order ,  value: show times
    # KES algorithm : using the ASCII characteristics to create a list as a table

    # time complexity : O(N)
    # 1st step : collect statistics
    for c in s:
        #if ord(c) >= ord('a') and ord(c) <= ord('z'):
        if ord('a') <= ord(c) <= ord('z'):
            res[ord(c) - ord('a')] += 1

    # time complexity : O(1)
    # 2nd step : apply analysis
    for i in range(26):
        if res[i] > 0:
            print(chr(i + ord('a')), " ", res[i])


def basic_copy():
    #--- deep copy ---
    a = 5
    b = a  #deep copy
    print("a= %d, b= %d" % (a, b))
    b = -1
    print("a= %d, b= %d" % (a, b))

    #--- shallow copy ---
    a = [3, 1, 2]  # a is memory address, a[0], a[1], a[2]
    b = a  # <== shallow copy ( pointer copy in C/C++)
    print("a= %s, b= %s" % (str(a), str(b)))
    b[0] = -1
    print("a= %s, b= %s" % (str(a), str(b)))

    #--- mutable / immutable -----
    '''
    mutable : list, dict (TBV)
     - copy operation : shallow copy (address copy)
     - deep copy? YES

    immutable : integer, float, string (TBV), tuple(TBV)
     - copy operation : deep copy (memory copy)
     - shallow copy? NO
    '''
    #--- deep copy for mutable variable ---
    a = [3, 1, 2, 0]
    #-- method 0 ---
    b = []
    for x in a:
        b.append(x)
    #-- method 0.1 ---
    b = [x for x in a]
    # === OVA ==
    #Q: get all element greater than 1 in a to b
    b = [x for x in a if x > 1]
    # ==========

    #-- method 1 ---
    b = list(a)

    #-- method 2----
    b = a[:]

    print("a= %s, b= %s" % (str(a), str(b)))
    b[0] = -1
    print("a= %s, b= %s" % (str(a), str(b)))

    #---- immutable ----- readable but not writable
    name = "John"
    #name[0] = "L" # => "Lohn" <== (X) string is immutable
    for x in name:
        print("... %s" % x)


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
    while len(a) > 0 or len(b) > 0:  #N
        if len(a) > 0:
            c.append(a.pop(0))  #N
        if len(b) > 0:
            c.append(b.pop(0))
    print(c)

    print("------ v2.1--------")
    a = [3, 5, 1, 4, 2]
    b = [0, 7, 6]
    c = []

    a = a[::-1]  #N
    b = b[::-1]  #N

    while len(a) > 0 or len(b) > 0:  #N
        if len(a) > 0:
            c.append(a.pop())
        if len(b) > 0:
            c.append(b.pop())
    print(c)

    print("------ v2.1--------")
    a = [3, 5, 1, 4, 2]
    b = [0, 7, 6]
    c = []

    a = a[::-1]  #N
    b = b[::-1]  #N

    while a or b:  #N
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
        if j >= len(b) or (i < len(a) and j < len(b) and a[i] < b[j]):
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
        elif not b:  #explit
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

    d = a[::-1]
    print("get the new list with reversed order : %d" % str(d))

    return


def basic_list_iii():
    a = [3, 1, 5]

    #----- append ---- time complexity O(1) (most likely)
    #SKIP

    #----- pop(index) ----return the "popped-out" value
    #Q: pop out the first element in a
    a.pop(0)
    #Q: pop out the last element in a
    a.pop()  #without index as input => default is the last index
    '''
    time complexity : 
     - last index : pop()- O(1)
     - Otherwise : O(N)

    '''
    #----- remove(element) ----
    # O(N)
    a = [100, 200, 300]
    #Q: remove the element with 200 value
    a.remove(200)

    # ---- del a[index] - LEGACY from C++
    # the same as .pop
    a = [3, 1, 5]
    #Q: pop out the first element in a
    del a[0]

    #----- insert(pos, element)
    #Q: O(N)
    a = [3, 1, 5]
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
        #return -1 #TBD

        # prices = [7, 1, 5, 3, 6, 4]
        # print("max profit : %d (ans 5)\n" % maxProfitLR(prices))

        # prices = [7, 6, 4, 3, 0]
        # print("max profit : %d (ans 0)\n" % maxProfitLR(prices))
        min_price = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            if p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit

    prices = [7, 1, 5, 3, 6, 4]
    print("max profit : %d (ans 5)\n" % maxProfitLR(prices))

    prices = [7, 6, 4, 3, 0]
    print("max profit : %d (ans 0)\n" % maxProfitLR(prices))

    def maxProfitRL(prices):
        #HW0812
        sell_price = float('-inf')
        max_profit = 0
        for b in prices[::-1]:
            if b > sell_price:
                sell_price = b
            if sell_price - b > max_profit:
                max_profit = sell_price - b
            print(sell_price, b)

        return max_profit  #TBD
        #        5  1     3
        #     b
        #                 s

    prices = [7, 1, 5, 3, 6, 4]
    print("max profit : %d (ans 5)\n" % maxProfitRL(prices))

    prices = [7, 6, 4, 3, 0]
    print("max profit : %d (ans 0)\n" % maxProfitRL(prices))


def leetcode_stock_trade_iii():
    '''
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
    
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    
    Find the maximum profit you can achieve. You may complete at most two transactions.
    
    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    
    Example 1:
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
    
    Example 2:
    
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
    Example 3:
    
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
    
    Constraints:
    
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^5
    '''

    def maxProfit(prices):
        #HW0816
        # straight-forward : O(N^2)
        # best : O(N)
        #
        n = len(prices)
        if n == 0:
            return 0
        left = [0] * n
        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left[i] = max(left[i - 1], prices[i] - min_price)

        right = [0] * n
        max_price = prices[-1]

        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right[i] = max(right[i + 1], max_price - prices[i])

        res = 0
        for i in range(n):
            res = max(res, left[i] + right[i])
        return res

    prices = [1, 3, 5, 4, 3, 7, 6, 9, 2, 4]
    print("max profit : %d (ans 10)\n\n" % maxProfit(prices))

    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print("max profit : %d (ans 13)\n\n" % maxProfit(prices))

    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print("max profit : %d (ans 6)\n\n" % maxProfit(prices))

    prices = [1, 2, 3, 4, 5]
    print("max profit : %d (ans 4)\n\n" % maxProfit(prices))

    prices = [7, 6, 4, 3, 1]
    print("max profit : %d (ans 0)\n\n" % maxProfit(prices))


def leetcode_lonest_substring_without_repeating():
    #https://leetcode.com/problems/longest-substring-without-repeating-characters/

    # Given a string s, find the length of the longest
    # substring
    #  without repeating characters.

    # Example 1:

    # Input: s = "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.

    # Example 2:
    # Input: s = "bbbbb"
    # Output: 1
    # Explanation: The answer is "b", with the length of 1.

    # Example 3:
    # Input: s = "pwwkew"
    # Output: 3
    # Explanation: The answer is "wke", with the length of 3.
    # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    # Constraints:

    # 0 <= s.length <= 5 * 10^4
    # s consists of English letters, digits, symbols and spaces

    '''
    time complexity : O(N)
    NOTE : "dict" is not allowed

        0 1 2 3 4 5 6 7 8 9
        a b c a b c b b a c
        r
        l
        1 2 3        
    '''
    #time complexity: O(N)
    #space complexity: O(1) 
    def lengthOfLongestSubstring(s):

        left = 0
        arr = [-1] * 128 # key: ord()    value: index
        max_length = 0
        for right in range(len(s)): # right = 0
            if arr[ord(s[right])] >= left: #    -1 >= 0
                left = arr[ord(s[right])] + 1 # left = 1
            else:
                max_length = max(max_length, right - left + 1) # max=1
            arr[ord(s[right])] = right # ord(a):0
                
        return max_length #TBD

    print("%s : %d (ans 3)" %
          ("abcabcbbac", lengthOfLongestSubstring("abcabcbbac")))
    print("%s : %d (ans 1)" % ("bbbbb", lengthOfLongestSubstring("bbbbb")))
    print("%s : %d (ans 3)" % ("pwwkew", lengthOfLongestSubstring("pwwkew")))

    #-----


def leetcode_alternating_strings():
    # -- APCS ---
    
    # k-alternating string:
    #          StRiNg => 1-alternating string
    #          heLLow => 2-alternating string
    #          aBBaaa => NOT alternating string
    #          aaaAAbbCCCC => NOT alternating string

    # Q: Given k and a string, find the maximum sub-string length which matches k-alternating string condition.
    # Example:
    #       Given k = 2, string = "aBBaaa" => the maximum k-alternating string is BBaa, Answer:  4
    #       Given k= 1, string = "BaBaBB" => the maximum k-alternating string is BaBaB, Anser : 5
    #
    def getMaxAlternatingStringLength(k, s):
        #HW0819 : sliding window, Finite-State Machine(FSM) (optional)
        return -1 #TBD


    k = 1
    s = "aBBdaaa"
    maxLen = getMaxAlternatingStringLength(k, s)
    print("k=%d, string is %s => max len = %d (ans: 2)" % (k, s, maxLen))

    k = 3
    s = "DDaasAAbbCC"
    maxLen = getMaxAlternatingStringLength(k, s)
    print("k=%d, string is %s => max len = %d (ans: 3)" % (k, s, maxLen))

    k = 2
    s = "aafAXbbCDCCC"
    maxLen = getMaxAlternatingStringLength(k, s)
    print("k=%d, string is %s => max len = %d (ans: 8)" % (k, s, maxLen))

    k = 3
    s = "DDaaAAbbCC"
    maxLen = getMaxAlternatingStringLength(k, s)
    print("k=%d, string is %s => max len = %d (ans: 0)" % (k, s, maxLen))
