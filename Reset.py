import numpy as np

# Reset the neuron weights
np.save("TrainData/NeuronWeights", np.zeros((100, 100, 3)))
np.save("TrainData/FailList"     , np.array([])           )

# Reset the terms and total fails
with open("TrainData/Terms"     , "w") as f: f.write("0")
with open("TrainData/TotalFails", "w") as f: f.write("0")
