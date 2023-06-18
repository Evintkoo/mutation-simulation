import random

'''generateDNA: generate a random DNA strain with length "length"'''
# returns DNA strain
def generateDNA(length: int) -> str:
    # the chromosome is either "a", "g", "t", "c"
    choice = "agtc"
    
    # pick random of chromosome and arrange into a dna strain
    s = "".join(random.choice(choice) for x in range(length))
    return s

'''CLASS OF DNA MUTATION: DELETION, DUPLICATION, INVERSION, INSERTION, TRANSLOCATION, POINT MUTATION, AND FRAMESHIFT '''
class mutate:
    
    '''deletion: delete random number of random chromosome in DNA'''
    # mutate.deletion() giving an input of string DNA strain and remove several DNA strain randomly
    # returns deleted DNA strain 
    def deletion(DNAStrain: str) -> str:
        # select a number of deleted genoms
        j = random.randint(0,len(DNAStrain)-1)
        s =  DNAStrain
        
        # deleting random character in DNAStrain with total of j deletion
        for delete in range(0,j):
            # select a random index of string in DNA strain
            i = random.randint(0,len(s)-1)
            
            # delete an character in the index
            s =  s[:i] + s[i+1:]
    
        return s
    
    '''duplication: duplicate 1 random DNA segment'''
    # mutate.duplication() giving an input of string DNA strain and duplicate a segment of the DNA strain with random length and random place
    # return a DNA strain of duplicated DNA segment
    def duplication(DNAStrain: str) -> str:
        # select a random left index of DNA segment
        left = random.randint(0,len(DNAStrain)-1)
        
        # select a random right index of DNA segment
        right = random.randint(left, len(DNAStrain)-1)
        
        # duplicate an character in the index
        s =  DNAStrain[:left] + DNAStrain[left:right] + DNAStrain[left:right] + DNAStrain[right:]
    
        return s
    
    '''inversion: insert a random DNA segment to the strain'''
    # mutate.inversion() giving an input of string DNA strain and duplicate 1 of the DNA strain randomly
    # returns inverted DNA strain
    def inversion(DNAStrain: str) -> str:
        # select a random left index of DNA segment
        left = random.randint(0,len(DNAStrain)-1)
        
        # select a random right index of DNA segment
        right = random.randint(left, len(DNAStrain)-1)
        
        # take a part of strain in DNA and reverse it
        s = DNAStrain[left:right]
        s = s[::-1]
        
        # delete an character in the index
        s =  DNAStrain[:left] + s + DNAStrain[right+1:]
    
        return s
    
    '''insertion: insert a random DNA segment'''
    # mutate.insertion() giving an input of string DNA strain and insert a DNA segment into DNA strain randomly
    # returns inserted DNA strain
    def insertion(DNAStrain: str) -> str:
        # select a random length of string of inserted DNA segment
        length = random.randint(0,len(DNAStrain)-1)
        
        # generate random DNA segment
        s = generateDNA(length)
        
        # select a random index to insert the DNA segment
        i = random.randint(0,len(DNAStrain)-1)
        
        # delete an character in the index
        s =  DNAStrain[:i] + s + DNAStrain[i+1:]
    
        return s
    
    '''translocation: move a random DNA segment'''
    # mutate.inversion() giving an input of string DNA strain and duplicate 1 of the DNA strain randomly
    # returns translocated DNA
    def translocation(DNAStrain: str) -> str:
        # select a random index of string in DNA strain
        i = random.randint(0,len(DNAStrain)-1)
        
        # select a random length of string of inserted DNA segment
        length = random.randint(0,len(DNAStrain)-1)
        
        # generate random DNA segment
        s = generateDNA(length)
        
        # delete an character in the index
        s =  DNAStrain[:i] + s
    
        return s
    
    '''Point mutation: change a single nucleotide in DNA'''
    # mutate.pointMutation giving an input of string of DNA strain and change a char inside it
    # returns modified DNA
    def pointMutation(DNAStrain: str) -> str:
        # select a random index of string in DNA strain
        i = random.randint(0,len(DNAStrain)-1)
        
        # generate a random nucleotide
        s = generateDNA(1)
        
        # delete an character in the index
        s =  DNAStrain[:i] + s + DNAStrain[i+1:]
    
        return s
    
    '''Frameshift mutation: insert a single nucleotide in DNA'''
    # mutate.frameshift giving an input of string of DNA strain and insert a random nucleotide in it
    # return modified DNA strain
    def frameshift(DNAStrain: str) -> str:
        # select a random index of string in DNA strain
        i = random.randint(0,len(DNAStrain)-1)
        
        # generate a random nucleotide
        s = generateDNA(1)
        
        # delete an character in the index
        s =  DNAStrain[:i] + s + DNAStrain[i:]
    
        return s