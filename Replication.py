def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 


def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if (Count[i] == m and not(Text[i:i+k] in FrequentPatterns)):
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns

def ReverseComplement(Pattern):
    revComp = ''# output variable
    temp=[]
    # your code here
    for i in range(len(Pattern)-1,0,-1):
        temp.append(complement(Pattern[i])) 
    temp.append(complement(Pattern[0]))    
    revComp="".join(temp)    
    return revComp


# Copy your reverse function from the previous step here.


# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    if Nucleotide=='A':
        comp='T'
    elif Nucleotide=='T':
        comp='A'
    elif Nucleotide=='G':
        comp='C'
    elif Nucleotide=='C':
        comp='G'    
    return comp

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    k=len(Pattern)
    for i in range(len(Genome)-k+1):
        if Genome[i:i+k]==Pattern:
            positions.append(i)
    return positions

def SymbolArray(Genome, symbol):
    array = {}
    # type your code here
    n=len(Genome)
    Egenome=Genome+Genome[0:n//2]
    for i in range(n):
        array[i]=PatternCount(symbol,Egenome[i:i+(n//2)])
        
    return array    

def FasterSymbolArray(Genome, symbol):
    array = {}
    # your code here
    n=len(Genome)
    Egenome=Genome+Genome[0:n//2]
    array[0]=PatternCount(symbol,Genome[0:n//2])
    for i in range(1,n):
        array[i]=array[i-1]
        if Egenome[i-1]==symbol:
            array[i]-=1
        if Egenome[i+n//2-1]==symbol:
            array[i]+=1
    return array

def Skew(Genome):
    skew = {} #initializing the dictionary
    # your code here
    skew[0]=0
    for i in range(0,len(Genome)):
        skew[i+1]=skew[i]
        if Genome[i]=='G':
            skew[i+1]+=1
        if Genome[i]=='C':
            skew[i+1]-=1
    return skew

def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    skew=Skew(Genome)
    mini=min(skew.values())
    for i in range(0,len(skew)):
        if skew[i]==mini:
            positions.append(i)
    return positions

def HammingDistance(p, q):
    # your code here
    HD=0
    n=len(p)
    for i in range(n):
        if p[i]==q[i]:
            pass
        else:
            HD+=1
    
    return HD        

def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    # your code here
    for i in range(len(Text)-len(Pattern)+1):
        slice=Text[i:i+len(Pattern)]
        HammingD=HammingDistance(Pattern,slice)
        if HammingD<=d and d!=0:
            positions.append(i)
    else:
        if len(positions)==0:
            positions.append(0)
    return positions
    
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    # your code here
    for i in range(len(Text)-len(Pattern)+1):
        slice=Text[i:i+len(Pattern)]
        HammingD=HammingDistance(Pattern,slice)
        if HammingD<=d:
            count+=1
    
    return count    
