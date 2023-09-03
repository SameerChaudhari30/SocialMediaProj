import matplotlib.pyplot as plt
from datetime import datetime
import pymongo
import pandas as pd
import plotly.express as px

client = pymongo.MongoClient()

db = client['redditDB']
collec = db['redditData']

data = collec.find()

finData = pd.DataFrame(data)

subCount = list(finData['Subreddit'].value_counts())
subList = finData['Subreddit'].value_counts().index.tolist()

def reddit():
    fig = px.bar(x = subList, y = subCount, labels = { 'x': 'Subreddit', 'y': 'No. of comments'})
    fig.write_html("templates/subred.html")