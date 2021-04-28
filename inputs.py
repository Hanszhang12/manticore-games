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
youtubeLinks = "Youtube_Links.csv"


## Beginning of dataframe creation

#Reading CSV
acceptedTabDf = pd.read_csv("inputs/"  + acceptedTab)
bitlyClicksDf = pd.read_csv("inputs/" + bitlyClicks)
monthlyResponsesDf = pd.read_csv("inputs/" + monthlyResponses)
account_VerificationsDf = pd.read_csv("inputs/" + account_Verifications)
youtubeDf = pd.read_csv("inputs/" + youtubeLinks)

# %%
# Extracts required columns from acceptedTab
finalDf = acceptedTabDf[['Name', 'Core Username', 'Looker ID', 'Email Address', 'Team Name', 'Stats Link']]

# %%
# Extracts Referral Clicks
finalDf = finalDf.merge(bitlyClicksDf, how = "inner", left_on = "Core Username", right_on = 'Core Username')


# %%
# Cleans up Accounts Verified and adds it to the data frame
account_VerificationsDf = account_VerificationsDf.groupby('UTM Campaign').agg(sum)
account_VerificationsDf = account_VerificationsDf[['Account Creates', 'Account Verifies', 'Session Starts First', 'Game Plays First', 'Game Creates First']]
finalDf = finalDf.merge(account_VerificationsDf, how = 'left', left_on = 'Looker ID', right_on = 'UTM Campaign')


# Clean Youtube Links and add to data frame
youtubeDf.rename(columns={'If your primary platform is YouTube, please link all new Core videos for the month of February below. ': 'Links'}, inplace=True)
youtubeDf = youtubeDf[['Core Usernames', 'Links']]
finalDf = finalDf.merge(youtubeDf, how = 'left', left_on = 'Core Username', right_on = 'Core Usernames')

# %%
# %%
