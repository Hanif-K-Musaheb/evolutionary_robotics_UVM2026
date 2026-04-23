from pyrosim.neuron  import NEURON

from pyrosim.synapse import SYNAPSE

import csv

class NEURAL_NETWORK: 

    def __init__(self,nndfFileName):

        self.neurons = {}

        self.synapses = {}

        f = open(nndfFileName,"r")

        for line in f.readlines():

            self.Digest(line)

        f.close()

    def Print(self):

        self.Print_Sensor_Neuron_Values()

        self.Print_Hidden_Neuron_Values()

        self.Print_Motor_Neuron_Values()

        self.Print_Recursive_Neuron_Values()

        

        print("")

    def save_hidden_neuron_data(self,it):
        hidden_neuron_vals= [it] + self.Hidden_Neuron_Values2list()
        with open('hidden_neuron_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(hidden_neuron_vals)
    
    def save_recurrent_neuron_data(self,it):
        recurrent_neuron_vals= [it] + self.Recurrent_Neuron_Values2list()
        with open('recurrent_neuron_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(recurrent_neuron_vals)

    
    def Update(self):
        for neuronName in self.neurons.keys():
            if self.neurons[neuronName].Is_Sensor_Neuron():
                self.neurons[neuronName].Update_Sensor_Neuron()
            else:
                self.neurons[neuronName].Update_Hidden_Or_Motor_Neuron()

        for (sourceNeuronName, targetNeuronName) in self.synapses.keys():
            weight = self.synapses[sourceNeuronName, targetNeuronName].Get_Weight()
            self.neurons[targetNeuronName].Add_To_Value(self.neurons[sourceNeuronName].Get_Value() * weight)
            
        for neuronName in self.neurons.keys():
            if not self.neurons[neuronName].Is_Sensor_Neuron():
                self.neurons[neuronName].Threshold()
    
    def Get_Neuron_Names(self):
        return self.neurons.keys()
    
    def Is_Motor_Neuron(self,neuronName):
        return self.neurons[neuronName].Is_Motor_Neuron()
    
    def Get_Motor_Neurons_Joint(self,neuronName):
        return self.neurons[neuronName].Get_Joint_Name()
    
    def Get_Value_Of(self,neuronName):
        return self.neurons[neuronName].Get_Value()


# ---------------- Private methods --------------------------------------

    def Add_Neuron_According_To(self,line):

        neuron = NEURON(line)

        self.neurons[ neuron.Get_Name() ] = neuron

    def Add_Synapse_According_To(self,line):

        synapse = SYNAPSE(line)

        sourceNeuronName = synapse.Get_Source_Neuron_Name()

        targetNeuronName = synapse.Get_Target_Neuron_Name()

        self.synapses[sourceNeuronName , targetNeuronName] = synapse

    def Digest(self,line):

        if self.Line_Contains_Neuron_Definition(line):

            self.Add_Neuron_According_To(line)

        if self.Line_Contains_Synapse_Definition(line):

            self.Add_Synapse_According_To(line)

    def Line_Contains_Neuron_Definition(self,line):

        return "neuron" in line

    def Line_Contains_Synapse_Definition(self,line):

        return "synapse" in line

    def Print_Sensor_Neuron_Values(self):

        print("sensor neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Sensor_Neuron():

                self.neurons[neuronName].Print()

        print("")


    def Print_Hidden_Neuron_Values(self):

        print("hidden neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Hidden_Neuron():

                self.neurons[neuronName].Print()

        print("")

    def Print_Recursive_Neuron_Values(self):

        print("recurrent neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Recurrent_Neuron():

                self.neurons[neuronName].Print()

        print("")


    def Print_Motor_Neuron_Values(self):

        print("motor neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Motor_Neuron():

                self.neurons[neuronName].Print()

        print("")


    def Hidden_Neuron_Values2list(self):
        hidden_neuron_vals=[]
        for neuronName in sorted(self.neurons):
            if self.neurons[neuronName].Is_Hidden_Neuron():
                hidden_neuron_vals.append(self.neurons[neuronName].Get_Value())
        return hidden_neuron_vals

    def Recurrent_Neuron_Values2list(self):
        recurrent_neuron_vals=[]
        for neuronName in sorted(self.neurons):
            if self.neurons[neuronName].Is_Recurrent_Neuron():
                recurrent_neuron_vals.append(self.neurons[neuronName].Get_Value())
        return recurrent_neuron_vals


