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
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if i == j:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i::]
    if j < len(b):
        c += b[j::]

    print(c)
    return


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
    return


def basic_list_ii():
    a = [5, 4, 1, 3, 2, 9, 8]
    #    0  1  2  3  4  5  6
    d = a[2:6:1]  # => a[2:6]
    print("get the new list from index-2 to index-5: %s" % str(d))

    d = a[3:]
    print("get the new list from index-3 to index-6: %s" % str(d))

    #HW0808(VK) : start from here next time

    return
