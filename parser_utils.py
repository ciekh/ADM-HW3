# i clean some field of table
def SplitWord(word):
    for k in range(1,len(word)):
        if word[k].isupper() and word[k-1] != ' ':
            word = word[:k] + ' ' + word[k:]
    return word


