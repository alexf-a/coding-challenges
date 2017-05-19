#Sherlock and Anagrams Problem from HackerRank: https://www.hackerrank.com/challenges/sherlock-and-anagrams

import fileinput
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

def l_set(li):
    r = []
    for e in li:
        if not e in r:
            r.append(e)
    return r
        
            

def anagram_pairs(S):
    ''' (str) --> int'''
    S = list(S)
    l = len(S)
    cache = []
    result = 0
    #Append a sorted list of characters for each possible slice.
    #Why sorted? To allow for equality comparisons that ignore order of elements.
    for i in range(l):
        for p in range(i, l):
            s = list(S[i:p+1])
            s.sort()
            cache.append(s)
    #Return the amount of pairs from the quantity of redundant elements.
    cache_set = l_set(cache)
    for e in cache_set:
        c = cache.count(e)
        if cache.count(e) > 1:
            result += int(nCr(c, 2))
    return result

inp = fileinput.input()
i = 0
for line in inp:
    if i == 0:
        T = int(line[0])
    else:
        print(str(anagram_pairs(line)))
    i += 1
    