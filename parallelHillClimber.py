import solution
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # try:
        #     os.system("rm brain*.nndf")
        #     os.system("rm fitness*.txt")
        # except FileNotFoundError as e:
        #     print(e)

        self.nextAvailableID = 0
        self.parents = {}

        for i in range(c.populationSize):
            self.parents[i] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1


    def Evolve(self):
        self.Evaluate(self.parents)
        
        for currentGeneration in range(c.numberOfGenerations):
            isLastGen= True if currentGeneration==0 else False
            self.Evolve_For_One_Generation(isLastGen)
    
    
    def Evolve_For_One_Generation(self,isFirstGen):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        

    def Spawn(self):
        self.children={}
        for key in self.parents:
            self.children[key]=copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
       

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Evaluate(self,solutions):
        for solution in solutions:
            solutions[solution].Start_Simulation("DIRECT")#GUI


        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness > self.parents[key].fitness:
                self.parents[key] = self.children[key]
       
    
    def Print(self):
        for key in self.parents:
            print(f"fitness:\nparent: {self.parents[key].fitness}\nchild: {self.children[key].fitness}\n")

    
    def Show_Best(self):
        best = max(self.parents, key= lambda x: self.parents[x].fitness)
        self.parents[best].Start_Simulation("GUI") 
        print(f"best fitness: {self.parents[best].fitness}")



        
