#Main affiliate tabulation script
import pandas as pd

from inputs import finalDf
import sullygnome_webscraper
import youtube_scraper

# Put the usernames of people who you would like to ignore in this list
IGNORE = ['Morticai']

# Determines the tier of a youtuber based on their views
def youtube_Tier(views):
    tiers = []
    cash = []
    for v in views:
        if (int(v) > 50000):
            tiers.append("Platinum")
            cash.append(500)
        elif (int(v) > 15000):
            tiers.append("Gold")
            cash.append(300)
        elif (int(v) > 7500):
            tiers.append("Silver")
            cash.append(150)
        elif (int(v) > 3000):
            tiers.append("Bronze")
            cash.append(100)
        else:
            tiers.append("--")
            cash.append(0)
    return tiers, cash

# Determines the tier of a twitch streamer based on their views
def twitch_tier(views):
    tiers = []
    cash = []
    for v in views:
        v = v.split(' ')[0]
        if (float(v) > 350):
            tiers.append("Platinum")
            cash.append(500)
        elif (float(v) > 120):
            tiers.append("Gold")
            cash.append(300)
        elif (float(v) > 60):
            tiers.append("Silver")
            cash.append(150)
        elif (float(v) > 25):
            tiers.append("Bronze")
            cash.append(100)
        else:
            tiers.append("--")
            cash.append(0)
    return tiers, cash


twitchDf = finalDf[finalDf['Team Name'] == 'Team Twitch']
twitchDf['Monthly Hours'], twitchDf['Monthly Average Viewers'] = sullygnome_webscraper.scrape_list(twitchDf['Stats Link'])
twitchDf['Tier'], twitchDf['Cash Reward'] = twitch_tier(twitchDf['Monthly Hours'])
twitchDf.rename(columns={"Account Creates":"Referral Signups", "Account Verifies":"Referral Account Creation"}, inplace=True)
twitchDf = twitchDf[['Name', 'Core Username',	'Email Address', 'Tier', 'Cash Reward',	'Monthly Hours', 'Monthly Average Viewers', 'Stats Link', 'Referral Clicks', 'Referral Signups', 'Referral Account Creation']]
twitchDf['Total Cash Reward'] = twitchDf['Cash Reward'] + 2 * twitchDf['Referral Account Creation']
twitchDf['Account Creation Percentage'] = twitchDf['Referral Clicks'] / twitchDf['Referral Signups']
twitchDf['Verification Percentage'] = twitchDf['Referral Signups'] / twitchDf['Referral Account Creation']

youtubeDf = finalDf[finalDf['Team Name'] == 'Team YouTube']
youtubeDf['Monthly Videos'], youtubeDf['Monthly Views'] = youtube_scraper.youtubeViews(youtubeDf['Links'])
youtubeDf['Tier'], youtubeDf['Cash Reward'] = youtube_Tier(youtubeDf['Monthly Views'])
youtubeDf.rename(columns={"Account Creates":"Referral Signups", "Account Verifies":"Referral Account Creation"}, inplace=True)
youtubeDf = youtubeDf[['Name', 'Core Username',	'Email Address', 'Tier', 'Cash Reward',	'Monthly Videos', 'Monthly Views', 'Stats Link', 'Referral Clicks', 'Referral Signups', 'Referral Account Creation']]
youtubeDf['Total Cash Reward'] = youtubeDf['Cash Reward'] + 2 * youtubeDf['Referral Account Creation']
youtubeDf['Account Creation Percentage'] = youtubeDf['Referral Clicks'] / youtubeDf['Referral Signups']
youtubeDf['Verification Percentage'] = youtubeDf['Referral Signups'] / youtubeDf['Referral Account Creation']

# for user in IGNORE:
#     twitchUser = twitchDf[twitchDf['Core Username'] == user]
#     if twitchUser.size > 0:
#         twitchUser['Tier', 'Cash Reward', 'Monthly Videos', 'Monthly Views', 'Referral Clicks', 'Referral Signups', 'Referral Account Creation'] = [['?']] * 7
#     ytUser = youtubeDf[youtubeDf['Core Username'] == user]
#     if ytUser.size > 0:
#         ytUser[3] = '?'
twitchDf.loc[twitchDf['Core Username'].isin(IGNORE), 'Tier'] = '?'
twitchDf.loc[twitchDf['Core Username'].isin(IGNORE), 'Cash Reward'] = '?'
twitchDf.loc[twitchDf['Core Username'].isin(IGNORE), 'Monthly Hours'] = '?'
twitchDf.loc[twitchDf['Core Username'].isin(IGNORE), 'Monthly Average Viewers'] = '?'
twitchDf.loc[twitchDf['Core Username'].isin(IGNORE), 'Stats Link'] = '?'
twitchDf.loc[twitchDf['Core Username'].isin(IGNORE), 'Referral Clicks'] = '?'
twitchDf.loc[twitchDf['Core Username'].isin(IGNORE), 'Referral Signups'] = '?'
twitchDf.loc[twitchDf['Core Username'].isin(IGNORE), 'Referral Account Creation'] = '?'

youtubeDf.loc[youtubeDf['Core Username'].isin(IGNORE), 'Tier'] = '?'
youtubeDf.loc[youtubeDf['Core Username'].isin(IGNORE), 'Cash Reward'] = '?'
youtubeDf.loc[youtubeDf['Core Username'].isin(IGNORE), 'Monthly Videos'] = '?'
youtubeDf.loc[youtubeDf['Core Username'].isin(IGNORE), 'Monthly Views'] = '?'
youtubeDf.loc[youtubeDf['Core Username'].isin(IGNORE), 'Stats Link'] = '?'
youtubeDf.loc[youtubeDf['Core Username'].isin(IGNORE), 'Referral Clicks'] = '?'
youtubeDf.loc[youtubeDf['Core Username'].isin(IGNORE), 'Referral Signups'] = '?'
youtubeDf.loc[youtubeDf['Core Username'].isin(IGNORE), 'Referral Account Creation'] = '?'

twitchDf.to_csv("outputs/twitch_affiliate_data.csv")
youtubeDf.to_csv("outputs/youtube_affiliate_data.csv")
