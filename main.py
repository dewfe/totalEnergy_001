import pandas as pd
import matplotlib.pyplot as plt

fd = pd.read_csv("data\\bristell_001.csv", delimiter=";")
print(fd.head())
print(fd.dtypes)
fd["iasMps"] = fd["ias"] * 1.852 / 3.6
fd["tasMps"] = fd["tas"] * 1.852 / 3.6
fd["gsMps"] = fd["gs"] * 1.852 / 3.6
fd["vvMps"] = fd["vv"] * 0.3048

fd["eIas"] = fd["iasMps"] / -fd["vvMps"]
fd["eTas"] = fd["tasMps"] / -fd["vvMps"]
fd["eGs"] = fd["gsMps"] / -fd["vvMps"]

print(fd.dtypes)
print(fd[["vv", "vvMps"]])

fd[["iasMps", "tasMps", "gsMps"]].plot()
plt.show()

fd[["eIas", "eTas"]].plot()
plt.show()
