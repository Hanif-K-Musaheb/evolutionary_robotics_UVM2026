import solution
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = solution.SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            isLastGen= True if currentGeneration==0 else False
            self.Evolve_For_One_Generation(isLastGen)
    
    
    def Evolve_For_One_Generation(self,isFirstGen):
        self.Spawn()
        self.Mutate()
        if isFirstGen: self.child.Evaluate("GUI")
        else: self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
    


    def Select(self):
        if self.child.fitness<self.parent.fitness:
            self.parent=self.child
       
    
    def Print(self):
        print(f"{'='*20}\n{self.parent.fitness} : {self.child.fitness}\n{'='*20}")

    
    def Show_Best(self):
        self.parent.Evaluate("GUI")


        



