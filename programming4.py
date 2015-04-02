"""
  Comp 221 F14 
  Programming Assignment #4 
  Marcio Porto
"""

import random
import timeit
import time

def heapBottomUp(array):
    """ Takes in an array and construct a max-heap using bottom-up heap building algorithm """
    l = len(array)
    for i in range(int(l/2), 0, -1):
        k = i
        v = array[k-1]
        heap = False
        while (not heap) and (2*k <= l):
            j = 2*k
            if (j < l):
                if (array[j-1] < array[j]):
                    j += 1
            if (v >= array[j-1]):
                heap = True
            else:
                array[k-1] = array[j-1]
                k = j
        array[k-1] = v
    return array

array = random.sample(xrange(1, 100001), 100000)

start = time.time()
heapBottomUp(array)
end = time.time()
print end-start

array1 = [25, 2, 56, 1, 18, 23, 47, 71, 29, 8]
print(heapBottomUp(array1))
array2 = [81, 37, 42, 97, 73, 45, 47, 32, 33, 34, 27, 48, 96, 61, 38]
print(heapBottomUp(array2))
array3 = [74, 3, 28, 45, 40, 78, 20, 86, 19, 52, 39, 27, 11, 77, 64, 56, 80, 57, 24, 15]
print(heapBottomUp(array3))


def shiftTable(P, charList):
    """ Takes in a string P and a list of all its possible characters charList, 
    then creates a shift table for P """
    Table = {}
    m = len(P)
    for c in charList:
        Table[c] = m
    for j in range(0, m-1):
        nextChar = P[j]
        print nextChar
        Table[nextChar] = m-1-j
    return Table


def horspool(P, T):
    """ Takes in two strings P and T, and search for P in T """
    Table = shiftTable(P, charList)
    print Table
    m = len(P)
    n = len(T)
    i = m-1
    blank = ""
    count = 0    
    while i <= n-1:
        print("current position: ", i)
        print(T)
        print((i-m+1)*" "  + P)        
        blk = "" 
        k=0
        while k <= m-1 and P[m-1-k] == T[i-k]:
            count += 1
            k += 1
            print((i-len(blk))*" "+ "^   Match!!!!")
            blk += " " 
        if k == m:
            print("Pattern found at position: ", i-m+1)
            print("total comparisions: ", count)             
            return i-m+1
        else:
            print((i-len(blk))*" "+ "^   No Match!!!")  
            rightChar = T[i]
            if rightChar in Table.keys():
                i += Table[rightChar]
            else:
                i = i + len(P)   
    return -1

charList = ['C', 'A', 'N', 'D', 'L', 'E']
print(horspool('CANDLE' ,  "A MAN, A PLAN, A CANAL: PANAMA!"))
print(horspool('CANAL',  "A MAN, A PLAN, A CANAL: PANAMA!"))
print(horspool('BANANA', "MY NANA LOVES BANANAS"))


def stringMatching(text, string):
    """ Same idea as horspool function above.
    Takes in two strings text and string, and search for text in string """
    n = len(text)
    m = len(string)
    blank = ""
    count = 0
    for i in range(0, n-m):
        print("current position: ", i)
        print(text)
        print(blank + string)
        blk = ""
        j = 0 
           
        while (j < m) and (string[j].lower()==text[i+j].lower()):
            count += 1
            j+=1
            print(blank+blk+"^   Match!!!!")
            blk += " "                
        if (j == m):
            print("Pattern found at position: ", i)
            print("total comparisions: ", count)                            
            return i
        if (string[j].lower()!=text[i+j].lower()):
            print(blank+blk+ "^   No Match!!!")         
        blank = blank + " "
        count += 1        
    return -1


print(stringMatching("MY NANA LOVES BANANAS", "BANANA"))
print(stringMatching("A MAN, A PLAN, A CANAL: PANAMA!", "CANAL"))