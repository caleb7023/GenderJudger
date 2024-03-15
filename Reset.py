import numpy as np

# Reset the neuron weights
np.save("Data/NeuronWeights", np.zeros((100, 100, 3)))

# Reset the terms and total fails
with open("Data/Terms"     , "w") as f: f.write("0")
with open("Data/TotalFails", "w") as f: f.write("0")