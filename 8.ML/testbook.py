import pandas as pd
from IPython.display import display
data = {
    'Name' : ["John", "Anna", "Peter", "Linda"],
    'Location' : ["New York", "Paris", "Berlin", "London"],
    'Age' : [24, 13, 32, 33]
}

data_pandas = pd.DataFrame(data)
display(data_pandas)