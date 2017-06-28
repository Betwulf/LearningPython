import pickle

data = [[0, 1], [1, 0]]
tempfile = "C:\Temp\Test_pickle.pkl"
with open(tempfile, 'wb') as f:
    pickle.dump(data, f, -1)

print("File written...")
loaded_data = []
with open(tempfile, 'rb') as f:
    loaded_data = pickle.load(f)

print("Loaded Data:")
print(loaded_data)
