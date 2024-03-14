import numpy as np

np.save("Data/NeuronWeights", np.zeros((100, 100, 3)))

with open("Data/Terms"     , "w") as f: f.write("0")
with open("Data/TotalFails", "w") as f: f.write("0")