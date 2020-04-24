# Instructions:
# Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. 
# You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. 
# If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

# Tip: Remember that break works in both for and while loops. Use whichever loop seems most appropriate. 

# My solution
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break
    elif len(news_ticker) == 140:
        continue
    else:
        news_ticker = ' '.join(headlines)
print(news_ticker)