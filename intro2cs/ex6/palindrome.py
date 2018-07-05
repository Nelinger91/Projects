def is_palindrome_1(s):
    n=len(s)-1
    if n==0:
        return True
    elif s[0]==s[n]:
        s=s[1:n]
        return is_plaindrome_1(s)
    else:
        return False

def is_palindrome_2(s,i,j):
    if i==j:
        return True
    if i>j
        return True
#for cases where the amount of chars is
##even number and j will pass i if there is a palindrome
##between i and j in strin.g s
    elif s[i]==s[j]:
        return is_palindrome_2(s,i+1,j-1)
    else:
        return False



