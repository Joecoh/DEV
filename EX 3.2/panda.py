import pandas as pd

data = pd.DataFrame({"x1": ["y", "x", "y", "x", "x", "y"],
                     "x2": range(16, 22),
                     "x3": range(1, 7),
                     "x4": ["a", "b", "c", "d", "e", "f"],
                     "x5": range(30, 24, -1)})

print(data)

data_row = data[data.x2 < 20]
print(data_row)

data_col = data.drop("x1", axis=1)
print(data_col)

data_med = data["x5"].median()
print(data_med)
