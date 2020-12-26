import numpy as np

def calculate(list):
  flat_list = np.array(list)
  try:
    #get another list to reshape the list into 3X3 array
    reshaped_list = flat_list.reshape((3, 3))
  except ValueError:
    raise ValueError("List must contain nine numbers.")
  #get the means
  meanCol = np.mean(reshaped_list, axis = 1)
  meanRow = np.mean(reshaped_list, axis = 0)
  meanFlat = np.mean(flat_list)

  #get the variances
  varCol = np.var(reshaped_list, axis = 1)
  varRow = np.var(reshaped_list, axis = 0)
  varFlat = np.var(flat_list)

  #get the standard deviations
  stdCol = np.std(reshaped_list, axis = 1)
  stdRow = np.std(reshaped_list, axis = 0)
  stdFlat = np.std(flat_list)

  #get the max values
  maxCol = np.max(reshaped_list, axis = 1)
  maxRow = np.max(reshaped_list, axis = 0)
  maxFlat = np.max(flat_list)

  #get the min values
  minCol = np.min(reshaped_list, axis = 1)
  minRow = np.min(reshaped_list, axis = 0)
  minFlat = np.min(flat_list)

  #get the sum values
  sumCol = np.sum(reshaped_list, axis = 1)
  sumRow = np.sum(reshaped_list, axis = 0)
  sumFlat = np.sum(flat_list)

  #create a dictionary with the values calculated above
  calculations = {'mean': [meanRow.tolist(), meanCol.tolist(), meanFlat.tolist()],
                  'variance': [varRow.tolist(),varCol.tolist(), varFlat.tolist()],
                  'standard deviation': [stdRow.tolist(),stdCol.tolist(), stdFlat.tolist()],
                  'max': [maxRow.tolist(), maxCol.tolist(), maxFlat.tolist()],
                  'min': [minRow.tolist(), minCol.tolist(), minFlat.tolist()],
                  'sum': [sumRow.tolist(), sumCol.tolist(), sumFlat.tolist()]
  }



  return calculations