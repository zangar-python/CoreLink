import numpy as np

def numpy_classis_analitics(list):
    arr = np.array(list)
    
    return {
        "max":float(arr.max()),
        "min":float(arr.min()),
        "mean":float(arr.mean()),
        "count":arr.size,
        "sum":float(arr.sum())
    }