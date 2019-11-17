#calculating the length of the maximum palindrome
#is how to calculate the length of the maximum 
#sub-sequence between the input string and its inverse
def Palindroma(X): 
    # calculation Y as the inverse of X
    Y = X[::-1]
    # calculate the length of the string X to then create a matrix where to save the values
    n = len(X) 
    Matrix = [[None]*(n + 1) for i in range(n + 1)]

    for i in range(n + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                Matrix[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                Matrix[i][j] = Matrix[i-1][j-1]+1
            else: 
                Matrix[i][j] = max(Matrix[i-1][j], Matrix[i][j-1])
  
    # Matrix[n][n] contains the length of Palindroma of X[0..n-1] & Y[0..n-1]
    return Matrix[n][n]
Palindroma('DATAMININGSAPIENZA')