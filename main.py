#Main affiliate tabulation script
import pandas as pd

from inputs import finalDf
import sullygnome_webscraper
import youtube_scraper

def youtube_Tier(views) :
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
# twitchDf = finalDf[finalDf['Team Name'] == 'Team Twitch']
# twitchDf['Average Views'] = sullygnome_webscraper.scrape_list(twitchDf['Stats Link'])

youtubeDf = finalDf[finalDf['Team Name'] == 'Team YouTube']
youtubeDf['Monthly Videos'], youtubeDf['Monthly Views'] = youtube_scraper.youtubeViews(youtubeDf['Links'])
youtubeDf['Tier'], youtubeDf['Cash Reward'] = youtube_Tier(youtubeDf['Monthly Views'])
youtubeDf.rename(columns={"Account Creates":"Referral Signups", "Account Verifies":"Referral Account Creation"}, inplace=True)
youtubeDf = youtubeDf[['Name', 'Core Username',	'Email Address', 'Tier', 'Cash Reward',	'Monthly Videos', 'Monthly Views', 'Stats Link', 'Referral Clicks', 'Referral Signups', 'Referral Account Creation']]
youtubeDf['Total Cash Reward'] = youtubeDf['Cash Reward'] + 2 * youtubeDf['Referral Account Creation']
youtubeDf['Account Creation Percentage'] = youtubeDf['Referral Clicks'] / youtubeDf['Referral Signups']
youtubeDf['Verification Percentage'] = youtubeDf['Referral Signups'] / youtubeDf['Referral Account Creation']
youtubeDf.to_csv("outputs/youtube_affiliate_data.csv")
