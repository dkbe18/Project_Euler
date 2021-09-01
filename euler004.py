#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrom(n):
    n=str(n)
    if n[0]==n[-1]:
        if n[1]==n[-2]:
            if n[2]==n[-3]:
                return True
    else:
        return False
    
result=0
for m in range (100,1000):
    for n in range(100,1000):
        mul=m*n
        if isPalindrom(mul):
            if mul>result:
                result=mul
        

print(result)
    
