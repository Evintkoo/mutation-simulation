from modules import generateTree
from modules.generateTree import idMaker
from modules.generateTree import agent
from modules.constants import listID
parental = agent(id=idMaker(listID),
                            generationNumber=0, 
                            DNAstrain="agct", 
                            status=False)
tree = generateTree.buildGenerationTree(parentAgent=parental,
                                 generation=5,
                                 totalAgent=0)
tree.printTree()