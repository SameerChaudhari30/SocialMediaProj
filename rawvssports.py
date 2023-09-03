import pymongo
from plotly.subplots import make_subplots
import plotly.graph_objects as go

client = pymongo.MongoClient()

db = client['twitterDB']
collec = db['twitterCountData']

tweetDate = []
tweetCount = []
sportsCount = []

for tweetData in collec.find():
    tweetCount.append(tweetData['Tweet_Count'])
    tweetDate.append(tweetData["Time"].split(",")[0][:6])
    sportsCount.append(tweetData['Sports_count'])

tweetDate.sort()

def dailysports():
    fig = make_subplots(rows=2,cols=1)
    fig.append_trace(go.Scatter(
        x=tweetDate,
        y=tweetCount,
        name="Twitter Raw"
        ),
        row=1,col=1)

    fig.append_trace(go.Scatter(
        x=tweetDate,
        y=sportsCount,
        name="Twitter Sports"
        ),
        row=2,col=1)

    fig.update_layout(title_text="Twitter Daily Raw vs Daily Sports Count", xaxis_title = 'Date', yaxis_title = 'Count')
    fig.update_layout(xaxis2_title = 'Date', yaxis2_title = 'Count')
    fig.write_html("templates/dailysports.html")