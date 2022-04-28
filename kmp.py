def KmpPatternSearch(pat, txt):
    m = len(pat)
    n = len(txt)

    lps = [0]*m
    length = 0 
    i = 1
    while i<m:
        if pat[i]==pat[length]:
            length+=1
            lps[i] = length
            i+=1
        else:
            if length!=0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i+=1
    
    j = 0 # index for pat[]
    i = 0 # index for txt[]

    while i<n:
        if pat[j]==txt[i]:
            i+=1
            j+=1
        if j==m:
            return i-j
            j = lps[j-1]
        elif i<n and pat[j]!=txt[i]:
            if j!=0:
                j = lps[j-1]
            else:
                i+=1