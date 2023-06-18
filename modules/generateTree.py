import random
from modules.mutation import mutate
from modules.constants import cancerRate, listID, mutationRate
# strainDifference inputing 2 string and count the difference
# return a float [0,1] that represent the similarity between 2 string (1: similar) (0: totally different)
def strainSimilarity (str1: str, str2: str) -> float:
    str1 = str1 + (' ' * (len(str2) - len(str1)))
    str2 = str2 + (' ' * (len(str1) - len(str2)))
    return sum(1 if i == j else 0
               for i, j in zip(str1, str2)) / float(len(str1))


# define if the mutation is a cancer or not based on the difference of the string
# return true if the mutation is a cancer, else return false
def isCancer(strain1: str,strain2: str) -> bool:
    dif = strainSimilarity(strain1,strain2) 
    
    if dif < cancerRate:
        return True
    else :
        return False
    
'''Class of the agent which save the information of its ID: the ID of the agent (int), 
                DNAstrain: unique DNA string of agent (string), and cancerstatus: a boolean that represent the status of agent if it has cancer or not (boolean)'''
# agent is contains:
# ID: unique id of each agent, 
# generationNumber: represents the generation that agent have, 
# DNAstrain: the DNA of agent, 
# status: represent if its a cancer or not
class agent:
    def __init__ (self, id: str, generationNumber: int, DNAstrain: str, status: bool):
        self.id = id
        self.generationNumber= generationNumber
        self.DNAstrain = DNAstrain
        self.status = status
        
'''Class of a tree data structure that contain the agents'''
class TreeNode:
    # for each TreeNode, contains a data of agent, list of children, and the parent
    def __init__(self, data: agent):
        self.data = data
        self.children = []
        self.parent = None
    
    # adding a child on the TreeNode
    def addChild (self, child):
        child.parent = self
        self.children.append(child)
    
    # return the level/generation of the data
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level
    
    # print the tree structure
    def printTree(self):
        print("\t" * self.getLevel(), [self.data.id, self.data.generationNumber, self.data.DNAstrain, self.data.status])
        if self.children:
            for child in self.children:
                child.printTree()
    
    # return list of agent that has cancer
    def cancerNode(self, cancerList: list) -> list:
        if self.data.status == True:
            cancerList.append(self.data)
            # print([self.data.id, self.data.status])
        if self.children:
            for child in self.children:
                child.cancerNode(cancerList)
        return cancerList
    
    # save the tree in a file
    # make a data, save each node as:
    # id, generationNumber, DNAstrain, status, parent.id
    def dataTree(self,data: list) -> list:
        if self.parent: 
            data.append([self.data.id, self.data.generationNumber, self.data.DNAstrain, self.data.status, self.parent.data.id])
        if self.children:
            for childs in self.children:
                childs.dataTree(data)
        return data

'''isMutated() is decide if the mutation will happen or not'''
# return true if it will happen, and return false if not
def isMutated() -> bool:
    x = random.uniform(0,1)
    if x < mutationRate:
        return True
    else :
        return False
    
'''pickMutation is a function that will randomly choose the type of mutation and implement the picked mutation into the DNA strain'''
# return the mutated DNA
def pickMutation(DNAstrain: str) -> str:
    rand = random.choice(range(0,7)) # weighting
    match rand:
        case 0:
            r = mutate.deletion(DNAstrain)
            pass
        case 1:
            r = mutate.duplication(DNAstrain)
            pass
        case 2:
            r = mutate.inversion(DNAstrain)
            pass
        case 3:
            r = mutate.insertion(DNAstrain)
            pass
        case 4:
            r = mutate.translocation(DNAstrain)
            pass
        case 5:
            r = mutate.pointMutation(DNAstrain)
            pass
        case 6:
            r = mutate.frameshift(DNAstrain)
            pass
    return r

'''idMaker is a function that make a unique ID for each agent'''
# returns string of number that represent the unique ID
def idMaker(idList: list) -> str:
    num = "0123456789abcdefghijklmnopqrstuvxyz"
    idLength = 20
    id = "".join(random.choices(num, k=idLength))
    while id in idList:
        id = "".join(random.choices(num, k=idLength))
    listID.append(id)
    # print(id)
    idList = idList.sort()
    return id            
    
'''mutation is a function that generate the mutation of the agent'''
# return agent with new ID, DNAstrain
def mutation(parentAgent: agent, genNumber: int) -> agent:
    if isMutated():
        childDNAMutation = pickMutation(parentAgent.DNAstrain)
        return agent(id= idMaker(listID),
                    generationNumber=genNumber, 
                    DNAstrain=childDNAMutation, 
                    status=isCancer(parentAgent.DNAstrain,childDNAMutation))
    else: 
        return agent(id = idMaker(listID),
                    generationNumber=genNumber, 
                    DNAstrain = parentAgent.DNAstrain, 
                    status = False)
    

'''buildGenerationTree is a function build a tree data structure of the generation'''
# returns tree of genetical mutation
def buildGenerationTree(parentAgent: agent, generation: int, totalAgent: int) -> TreeNode:
    totalAgent = totalAgent+1
    # print([parentAgent.id])
    parrent = TreeNode(parentAgent)
    # print(parentAgent.id)
    
    
    if generation > 0 and parentAgent.status == False:
        # make a mutation of next generation
        for i in range(2):
            child = mutation(parentAgent, totalAgent)

            parrent.addChild(buildGenerationTree(parentAgent=child, 
                            generation= generation-1,
                            totalAgent= totalAgent))
    return parrent

# check the similarity based on its nucleotids
def DNASimilarity (DNAStrain1: str, DNAStrain2: str) -> float:
    ret = 0
    for i in range (min(len(DNAStrain1), len(DNAStrain2))):
        if DNAStrain2[i] == DNAStrain1[i]:
            ret += 1
    return round(ret/min(len(DNAStrain1), len(DNAStrain2))*100,2)