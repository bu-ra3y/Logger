#!/usr/bin/python3
#
# logreader module
#  
#
from collections import defaultdict
import matplotlib.pyplot as plt



# This is our data store.
# It is a defaultdict(list) which is a dict with one exception:
#   Whenever a key doesn't exist, it is automatically 
#   initialized with list() (empty list)
# The data lives here as named lists
#       keyA -> (val1, val2, val3, ...)
# e.g.  angle -> (20.1, 19.8, 16.4, 15.2)
#
data = defaultdict(list)

# Mainly a debugging function
def printData():
  for key in data.keys():
    print("%s: %s" % (key, data[key]))
    print("")


# Read in the lines froma file and store them
def readInput(inputFile):
  with open(inputFile) as _inputFile:
    for line in _inputFile:
      # First split the line into key-value pairs
      # The line looks like:
      #   x 1, y 2, z 3.00, r 25.1
      keyValues = line.split(",")
      for key_value in keyValues:
        # split the key and value on whitespace
        key, value = key_value.split()
        # insert the value into the list for the key
        data[key].append(float(value))

# Return all of the data
def getData():
  return data

# Chart the data using MatPlotLib
def plotData(config):
  # config contains 1 item for each intended subplot.
  #  thus, the length of config should tell us how many subplots we want
  num_subplots = len(config)
  
  # Create a figure with several subplots
  #  number of subplots according to the config
  #  all subplots share the temporal axis (x)
  figure, axes_array = plt.subplots(num_subplots, sharex=True)
  
  for key in data.keys():
    # grab the data values for this series
    y = data[key]
  
    # we have no x-axis reference, so 
    #  we will simply plot each value incrementally
    #  along the x-axis, starting at 0, going up
    #  to len(y)
    x = range(len(y))
  
    # Now we need to use the config to plot
    #  this data on the correct subplot/axes
    # go through each item/plot in the config list
    for i in range(len(config)):
      if key in config[i]:
        # if this series belongs in this plot
        #  then plot it on the right axes
        axes_array[i].plot(x, y, label=key)
  
  # Activate each legend
  for axes in axes_array:
    axes.legend()  

  # Display
  plt.show()
