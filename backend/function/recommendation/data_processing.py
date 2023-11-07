from surprise import Dataset
from surprise import Reader
from  sql import get_values

def dataread(path= ""):
    reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
    data = Dataset.load_from_file('./ratings.csv', reader=reader)
    # data = Dataset.load_from_file(path, reader=reader)
    return data 