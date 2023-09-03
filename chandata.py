import pandas as pd
import plotly.graph_objs as go
import pymongo
  
client = pymongo.MongoClient()
db = client['fourchanDB']
collection = db['fourchanData']

data = collection.find()
df = pd.DataFrame(data)

df2=df.drop(df.columns[1], axis=1)

df2["comTime"] = df2["comTime"].dt.strftime('%y-%m-%d')


data_1=df2.groupby(['comTime',"comCountry"]).count()
data_1=data_1.reset_index() 


def chancountry(country):
    plots_new = data_1[data_1["comCountry"] == country]
    fig = go.Figure(data=go.Scatter(x=plots_new['comTime'].astype(dtype=str), y=plots_new['_id'], marker_color='indianred', text="counts"))
    fig.update_layout({"title": 'Comments from '+country+' from Nov 5 to Nov 28',
                    "xaxis": {"title":"Date"},
                    "yaxis": {"title":"No. of comments"},
                    "showlegend": False})
    fig.write_html("templates/"+country+".html")
    return country