# This script takes in four inputs (The accepted tab csv, bitly clicks csv, account verifications csv, monthly responses csv)
# The methods in this script create a dataframe, that can then be manipulated in main.py and the other supporting scripts
#%%
import pandas as pd 
import re
import numpy as np 

# Please upload all 4 input files into the folder named "inputs"
# Here you can change the names of the input files if necessary.
# Please name files with underscores instead of spaces.
# Please remove any commas from numbers (1,823 -> 1823)

acceptedTab = "Core_Affiliate_Tabulation_Accepted.csv" 
bitlyClicks = "Core_Bitly.csv"
monthlyResponses = "Core_Affiliate_February.csv"
account_Verifications = "Account_Verifies.csv"


## Beginning of dataframe creation

#Reading CSV
acceptedTabDf = pd.read_csv("inputs/"  + acceptedTab)
bitlyClicksDf = pd.read_csv("inputs/" + bitlyClicks)
monthlyResponsesDf = pd.read_csv("inputs/" + monthlyResponses)
account_VerificationsDf = pd.read_csv("inputs/" + account_Verifications)


# %%
# Extracts required columns from acceptedTab
finalDf = acceptedTabDf[['Name', 'Core Username', 'Email Address', 'Team Name', 'Stats Link']]

# %%
# Extracts Referral Clicks
finalDf = finalDf.merge(bitlyClicksDf, how = "inner", left_on = "Core Username", right_on = 'Core Username')


# %%
# Cleans up Accounts Verified and adds it to the data frame

usernames = account_VerificationsDf['UTM Campaign'].str.split('_', expand = True)[1]
account_VerificationsDf['UTM Campaign'] = usernames
account_VerificationsDf = account_VerificationsDf.groupby('UTM Campaign').agg(sum)
account_VerificationsDf = account_VerificationsDf[['Account Creates', 'Account Verifies', 'Session Starts First', 'Game Plays First', 'Game Creates First']]
finalDf = finalDf.merge(account_VerificationsDf, how = 'inner', left_on = 'Core Username', right_on = 'UTM Campaign')
# %%
finalDf.head()
# %%
