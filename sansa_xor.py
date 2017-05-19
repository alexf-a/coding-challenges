#Sansa XOR problem from Hacker Rank: https://www.hackerrank.com/challenges/sansa-and-xor
import fileinput

def xor(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l
    result = l[0]^l[1]
    for i in range(2, len(l)):
        result = result^l[i]
    return result

counter = 0
for line in fileinput.input():
    if counter > 1 and counter%2 == 0:
        tests = line.split(' ')
        tests = [int(str(test)) for test in tests]
        for i in range(len(tests)):
            count = (i + 1)*(len(tests) - i)
            if count%2 == 0:
                tests[i] = 0
        print(xor(tests))
    counter = counter + 1