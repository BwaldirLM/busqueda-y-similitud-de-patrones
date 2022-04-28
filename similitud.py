def Hamming(seq1, seq2):
    dif =abs(len(seq1)-len(seq2))
    if len(seq1)<len(seq2):seq1+="-"*dif
    elif len(seq2)<len(seq1):seq2+="-"*dif
    cnt=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:cnt+=1
    return (len(seq1)-cnt)/len(seq1)*100

def Levenshtein(seq1,seq2):
    M=[[0]*(len(seq1)+1) for i in range(len(seq2)+1)]
    for i in range(len(seq2)+1):M[i][0]=i
    for j in range(len(seq1)+1):M[0][j]=j
    for i in range(len(seq2)):
        for j in range(len(seq1)):
            if seq1[j]!=seq2[i]:M[i+1][j+1]+=1
            M[i+1][j+1]=min(M[i+1][j]+1,M[i][j+1]+1,M[i+1][j+1]+M[i][j])
    return (max(len(seq1),len(seq2))-M[len(seq2)][len(seq1)])/max(len(seq1),len(seq2))*100
def N_Gramas(s,t,n):
  t1,t2=set(),set()
  for i in range(len(s)-(n-1)):t1.add(s[i:i+n])
  for i in range(len(t)-(n-1)):t2.add(t[i:i+n])
  t3=t1.intersection(t2)
  return str(len(t3)*n/(len(t1)+len(t2))*100)
def Jaro(seq1,seq2):
    dis=max(len(seq1),len(seq2))//2-1
    m1,m2=[0]*len(seq1),[0]*len(seq2)
    transp,mat=0,0
    for i in range(len(seq1)):
        l=max(0,i-dis)
        r=min(i+dis+1,len(seq2))
        for j in range(l,r):
            if m2[j]==1 or seq1[i]!=seq2[j]:continue
            m1[i],m2[j]=1,1
            mat+=1
            break
    j=0
    for i in range(len(seq1)) :
        if m1[i]==0:continue
        while j<len(seq2) and m2[j]==0:j+=1
        if j>=len(seq2):break
        if seq1[i]!=seq2[j]:transp+=1
        j+=1
        if j>=len(seq2):break
    transp/=2
    if mat==0:return 0
    return 100*(mat/len(seq1)+mat/len(seq2)+(mat-transp)/mat)/3.0
def ventana_deslizante(seq1,seq2,w,d):
    t1,t2=set(),set()
    for i in range(0,len(seq1)-(w-1),d): t1.add(seq1[i:i+w])
    for i in range(0,len(seq2)-(w-1),d): t2.add(seq2[i:i+w])
    l1,l2=list(t1),list(t2)
    tot=0
    for i in range(min(len(l1),len(l2))):
        tot+=Hamming(l1[i],l2[i])
    return tot/min(len(l1),len(l2))