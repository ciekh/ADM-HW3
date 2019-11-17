#calculating the length of the maximum palindrome
#is how to calculate the length of the maximum 
#sub-sequence between the input string and its inverse
def Palindroma(X): 
    # calculation Y as the inverse of X
    Y = X[::-1]
    # calculate the length of the string X to then create a matrix where to save the values
    n = len(X) 
    L = [[None]*(n + 1) for i in range(n + 1)] 
  
    #Following steps build L[m + 1][n + 1] in bottom up fashion 
    #L[i][j] contains length of palindroma of X[0..i-1] and Y[0..j-1]
    for i in range(n + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # L[n][n] contains the length of Palindroma of X[0..n-1] & Y[0..n-1] 
    return L[n][n] 
Palindroma('DATAMININGSAPIENZA')