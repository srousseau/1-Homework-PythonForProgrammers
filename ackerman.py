'''
Scott Rousseau
Homework 1 part 1
Ackermann 

'''

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif ((n == 0) and (m > 0)):
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

#Result should be 2
print "Test of ackermann funtion with A(1,0)"
result1 = ackermann(1, 0)
print result1

#Result should be 7
print "Test of ackermann function with A(2,2)"
result1 = ackermann(2, 2)
print result1

#Result should be 125
print "Test of ackermann function with A(3,4)"
result1 = ackermann(3, 4)
print result1
