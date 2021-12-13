import numpy as np

def calculate(list):

    if len(list)!= 9:
        raise ValueError("List must contain nine numbers.")

    ls = np.array(list)
    matrix = ls.reshape((3,3))
    print(matrix)
    calculations = {}
    calculations['mean'] = [np.mean(matrix,axis=0).tolist(),np.mean(matrix,axis=1).tolist(),np.mean(ls)]
    calculations['variance'] = [np.var(matrix,axis=0).tolist(),np.var(matrix,axis=1).tolist(),np.var(ls)]
    calculations['standard deviation'] = [np.std(matrix,axis=0).tolist(),np.std(matrix,axis=1).tolist(),np.std(ls)]
    calculations['max'] = [np.nanmax(matrix,axis=0).tolist(),np.nanmax(matrix,axis=1).tolist(),np.nanmax(ls)]
    calculations['min'] = [np.nanmin(matrix,axis=0).tolist(),np.nanmin(matrix,axis=1).tolist(),np.nanmin(ls)]
    calculations['sum'] = [np.sum(matrix,axis=0).tolist(),np.sum(matrix,axis=1).tolist(),np.sum(ls)]
    print(calculations)

    return calculations