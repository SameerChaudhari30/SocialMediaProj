import matplotlib.pyplot as plt
from datetime import datetime
import pymongo
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

pd.set_option('mode.chained_assignment', None)

client = pymongo.MongoClient()

db = client['twitterDB']
collec = db['twitterCountData']

db2 = client['redditDB']
collec2 = db2['redditData']

# Twitter
tweetDate = []
tweetCount = []

for tweetData in collec.find():
    tweetCount.append(tweetData['Sports_count'])
    tweetDate.append(tweetData["Time"].split(",")[0][:6])

tweetDate.sort()

# Reddit
data = collec2.find()

finData = pd.DataFrame(data)
for i in range(len(finData)):
    mytime = finData['Comment_Time'][i]
    seconds = int(mytime/1000)
    date_conv = datetime.fromtimestamp(seconds)
    final = date_conv.strftime('%Y-%m-%d')
    finData["Comment_Time"][i] = final

finData['Comment_Time'] = pd.to_datetime(finData['Comment_Time'])

df = finData.groupby([finData['Comment_Time'].dt.date])['Subreddit'].count()
df = df.to_frame().reset_index()[:20]
subList = df.Comment_Time

def combfunc():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=subList, y=tweetCount,
                        mode='lines',
                        name='Twitter'))
    fig.add_trace(go.Scatter(x=subList, y=df.Subreddit,
                        mode='lines+markers',
                        name='Reddit'))
    fig.update_layout(title = 'Twitter vs Reddit Sports Analysis', xaxis_title = 'Date', yaxis_title = 'No. of comments')
    fig.write_html("templates/comb.html")

