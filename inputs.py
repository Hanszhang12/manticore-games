# This script takes in four inputs (The accepted tab csv, bitly clicks csv, account verifications csv, monthly responses csv)
# The methods in this script create a dataframe, that can then be manipulated in main.py and the other supporting scripts

import pandas as pd 
import re
import numpy as np 

# Please upload all 4 input files into the folder named "inputs"
# Here you can change the names of the input files if necessary.
# Please name files with underscores instead of spaces.

acceptedTab = "Core_Affiliated_Tabulations_Accepted.csv" 

acceptedTabDf = pd.read_csv("inputs" + acceptedTab)
acceptedTabDf.head()