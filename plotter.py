from pathlib import Path
import matplotlib.pyplot as plt
import pickle


path_to_results = Path(".")

for idx, item in enumerate(path_to_results.glob("ese_*.dat")):
    print(item)
    with open(item, "rb") as data_file:
        ese_data = pickle.load(data_file)
    plt.figure()
    plt.plot(ese_data)
    plt.xlabel("$k$ [-]")
    plt.ylabel("$ESE$ [-]")
    plt.title(f"Experiment {idx + 1}")
plt.show()