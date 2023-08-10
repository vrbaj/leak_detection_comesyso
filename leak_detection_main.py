import numpy as np
import matplotlib.pylab as plt
import padasip as pa
import pickle


length = 9

record_numbers = [1, 2, 3, 4, 5]




for record_number in record_numbers:
    # open data
    with open(f"in_sound_data_record_{record_number}.csv", "r", encoding="utf-8") as in_sound_data:
        in_matrix = (np.genfromtxt(in_sound_data, delimiter=",", skip_header=0))

    with open(f"target_sound_data_record_{record_number}.csv", "r", encoding="utf-8") as target_sound_data:
        target_matrix = (np.genfromtxt(target_sound_data, delimiter=",", skip_header=0))
    k = len(target_matrix)
    d = np.reshape(target_matrix, (k,))
    x = np.reshape(in_matrix, (k, length))

    print("midline")

    # detection
    # f = pa.filters.FilterGNGD(n=5, mu=0.50, w="zeros")
    f = pa.filters.FilterAP(n=length, order=3, mu=0.50, ifc=0.005, w="zeros")
    y, e, w = f.run(d, x)


    print("rex")

    # det = pa.detection.learning_entropy(w, m=150, order=2, alpha=[8., 9., 10., 11., 12., 13.])
    det = pa.detection.ELBND(w, e, function="sum")
    # det = pa.detection.ESE(w)

    file = open(f"elbnd_{record_number}.dat", "wb")
    pickle.dump(det, file)
    file.close()
    # ploting
    # fig, axs = plt.subplots(2, 1)
    # axs[0].plot(d)
    # axs[1].plot(det)
    # fig.tight_layout()
    # plt.show()














