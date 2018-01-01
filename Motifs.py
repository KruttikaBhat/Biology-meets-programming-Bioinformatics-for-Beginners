def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    k=len(Motifs[0])
    r=len(Motifs)
    for symbol in 'ACGT':
        count[symbol]=[]
        for i in range(k):
            count[symbol].append(0)
    for i in range(r):
        for j in range(k):
            symbol=Motifs[i][j]
            count[symbol][j]+=1
            
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile=Count(Motifs)
    for symbol in 'ACGT':
        for j in range(k):            
            profile[symbol][j]/=t
    # insert your code here
    return profile

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol     
     
    return consensus   


def Score(Motifs):
    consensus=Consensus(Motifs)
    count=0
    r=len(Motifs)
    c=len(Motifs[0])
    for j in range(c):
        for i in range(r):
            symbol=Motifs[i][j]
            if symbol==consensus[j]:
                pass
            else:
                count+=1
    return count        

    
# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    prod=1
    for i in range(len(Text)):
        prod*=Profile[Text[i]][i]
    return prod      

# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
    maxprob=0
    maxpos=0
    for i in range(len(Text)-k+1):
        subText=Text[i:i+k]
        prob=Pr(subText,Profile)
        if prob>maxprob:
            maxprob=prob
            maxpos=i
    return Text[maxpos:maxpos+k]        


def GreedyMotifSearch(Dna, k, t):
    # type your GreedyMotifSearch code here.
    BestMotifs=[]
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])
    n=len(Dna[0])
    
    for i in range(n-k+1):
        Motifs=[]
        Motifs.append(Dna[0][i:i+k])
        
        for j in range(1,t):
            P=Profile(Motifs)
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
            
        if Score(Motifs)<Score(BestMotifs):
            BestMotifs=Motifs
        
    return BestMotifs        

            
# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {} # initializing the count dictionary
    for symbol in 'ACGT':
        count[symbol]=[]
        for i in range(k):
            count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol=Motifs[i][j]
            count[symbol][j]+=1
            
    return count
    # insert your code here                    

# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {} # output variable
    # your code here
    profile=CountWithPseudocounts(Motifs)
    for symbol in 'ACGT':
        for j in range(k):
            profile[symbol][j]/=t+4
    return profile    


def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = [] # output variable
    # your code here
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])
    n=len(Dna[0])
    
    for i in range(n-k+1):
        Motifs=[]
        Motifs.append(Dna[0][i:i+k])
        
        for j in range(1,t):
            P=ProfileWithPseudocounts(Motifs)
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
            
        if Score(Motifs)<Score(BestMotifs):
            BestMotifs=Motifs
    return BestMotifs    

# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    # insert your code here
    motifs=[]
    n=len(Dna[0])
    k=len(Profile)
    t=len(Dna)
    for i in range(t):
        motifs.append(ProfileMostProbablePattern(Dna[i],k,Profile))
    return motifs    

def RandomMotifs(Dna, k, t):
    # place your code here.
    Motifs=[]
    n=len(Dna[0])
    for i in range(t):
        index=random.randint(0,n-k)
        Motifs.append(Dna[i][index:index+k])
    return Motifs    

def RandomizedMotifSearch(Dna, k, t):
    # insert your code here
    M=RandomMotifs(Dna,k,t)
    BestMotif=M
    while True:
        Profile=ProfileWithPseudocounts(M)
        M=Motifs(Profile,Dna)
        if Score(M)<Score(BestMotif):
            BestMotif=M
        else:
            return BestMotif   

def Normalize(Probabilities):
    # your code here
    sum=0
    for i in Probabilities:
        sum=sum+Probabilities[i]
        
    for j in Probabilities:
        Probabilities[j]=(float)(Probabilities[j])/sum
    return Probabilities    
 
 def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    index=random.uniform(0,1)
    sum=0
    for i in Probabilities:
        newSum=sum+Probabilities[i]
        if (sum<index) and (index<newSum):
            kmer=i
            break
        else:
            sum=newSum
    return kmer            
# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    n=len(Text)
    probabilities={}
    for i in range(n-k+1):
        probabilities[Text[i:i+k]]=Pr(Text[i:i+k],profile)
    probabilities=Normalize(probabilities)
    return WeightedDie(probabilities)


# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] # output variable
    # your code here
    Motifs=[]
    n=len(Dna[0])
    for i in range(t):
        index=random.randint(0,n-k)
        Motifs.append(Dna[i][index:index+k])
    BestMotifs=Motifs
    for j in range(N):
        i=random.randint(0,t-1)
        modMotifs=Motifs[0:i]+Motifs[i+1:t]
        Profile=ProfileWithPseudocounts(modMotifs)
        Motifs[i]=ProfileGeneratedString(Dna[i],Profile,k)
        
        if Score(Motifs)<Score(BestMotifs):
            BestMotifs=Motifs
        
    return BestMotifs
    