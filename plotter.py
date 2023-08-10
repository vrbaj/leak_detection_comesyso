from pathlib import Path
import matplotlib.pyplot as plt
import pickle


path_to_results = Path(".")
nd_methods = ["elbnd", "ese"]
for method in nd_methods:
    for idx, item in enumerate(path_to_results.glob(f"{method}_*.dat")):
        print(item)
        with open(item, "rb") as data_file:
            ese_data = pickle.load(data_file)
        plt.figure()
        plt.plot(ese_data)
        plt.xlabel("$k$ [-]")
        plt.ylabel(f"${method.upper()}$ [-]")
        plt.title(f"Experiment {idx + 1}")
plt.show()