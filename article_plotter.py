from pathlib import Path
import matplotlib.pyplot as plt
import pickle


path_to_results = Path(".")
nd_methods = ["ese"]
experiments = [2, 3, 5]
threshold = 60
method = "ese"
for experiment in experiments:
    for idx, item in enumerate(path_to_results.glob(f"ese_{experiment}.dat")):
        print(item)
        with open(item, "rb") as data_file:
            ese_data = pickle.load(data_file)
        ese_data[ese_data< 60] = 0
        plt.figure()
        plt.plot(ese_data)
        plt.xlabel("$k$ [-]")
        plt.ylabel(f"${method.upper()}$ [-]")
        plt.margins(x=0)
        #plt.title(f"{method.upper()} experiment {idx + 1}")
        plt.tight_layout()
        plt.savefig(f"ese_{experiment}.png", format="png", dpi=300)
plt.show()