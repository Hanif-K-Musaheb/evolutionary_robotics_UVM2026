import solution
import constants as c
import copy
import os
import csv

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

        self.fitness_data=[]


    def Evolve(self):
        self.Evaluate(self.parents)
        
        for currentGeneration in range(c.numberOfGenerations):
            isLastGen= True if currentGeneration==0 else False
            self.Evolve_For_One_Generation(isLastGen)
    
    
    def Evolve_For_One_Generation(self,isFirstGen):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.fittest_of_gen(self.children)
        self.Print()
        self.Select()

       

    def fittest_of_gen(self,solutions):
        generation_fitness=[]
        for solution in solutions:
            generation_fitness.append(solutions[solution].Get_Fitness())

        self.fitness_data.append(max(generation_fitness))
        
        

        

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
            #print(f"{self.children[key].fitness}    {self.parents[key].fitness}    {self.children[key].fitness > self.parents[key].fitness}")
            if self.children[key].fitness > self.parents[key].fitness:
                self.parents[key] = self.children[key]
       
    
    def Print(self):#explore if other
        for key in self.parents:
            print(f"fitness:\nparent: {self.parents[key].fitness}\nchild: {self.children[key].fitness}\n")

    
    def Show_Best(self):
        best = max(self.parents, key= lambda x: self.parents[x].fitness)
        self.parents[best].Start_Simulation("GUI") 
        print(f"best fitness: {self.parents[best].fitness}")

    def log_fitness_data(self):
        with open('brainiac_brain_generation_fitness20.csv', 'a', newline='') as file:#'peak_brainacs_fitness_data.csv'
            writer = csv.writer(file)
            writer.writerow(self.fitness_data)#labelled_data)




        
