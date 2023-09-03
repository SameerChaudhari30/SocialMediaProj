## Tech-stack
* 'python' - The project is developed and tested using python v3.9. [Python Website](https://www.python.org/)
* 'pymongo'- This project uses NoSQL database MongoDB to store the collected data
    * [MongoDB Website](https://www.mongodb.com/)
    * [Python MongoDB Adapter - pymongo](https://pymongo.readthedocs.io/en/stable/)

## Python libraries
* 'pandas' - pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language. [pandas Website](https://pandas.pydata.org/)
* 'matplotlib' - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. [matplotlib Website](https://matplotlib.org/)
* 'plotly' - plotly.py is an interactive, open-source, and browser-based graphing library for Python. [plotly Website](https://plotly.com/python/)
* 'flask' - Flask is a popular, extensible web microframework for building web applications with Python. [flask Website](https://flask.palletsprojects.com/)
* 'datetime' - datetime is a python library which can be used for manipulating dates and times. [datetime Website](https://pypi.org/project/DateTime/)
* 'json' - JSON is a syntax for storing and exchanging data. [json Website](https://docs.python.org/3/library/json.html)


## Data Source

* `Twitter`
  * [Sample Stream API](https://api.twitter.com/2/tweets/sample/stream) - API provided by Twitter Inc. to fetch 1% of all tweets that are tweeted in real time

* `Reddit` - We are using 'r/sports', 'r/cricket', etc.
  * [API](https://www.reddit.com/dev/api#GET_comments_{article}) - api for collecting comments from particular subreddit

  * [r/sports](https://reddit.com/r/sports) - sports subreddit will collect information about all sports and sports events happening around the world
  * [r/sports/comments](https://reddit.com/r/sports/comments) - collecting comments from subreddit sports

  * [r/cricket](https://reddit.com/r/cricket) - cricket subreddit will collect information about cricket worldcup, players and matches
  * [r/cricket/comments](https://reddit.com/r/cricket/comments) - collecting comments from subreddit cricket

  * [r/football](https://reddit.com/r/football) - football subreddit will collect information about football tournaments and players
  * [r/football/comments](https://reddit.com/r/football/comments) - collecting comments from subreddit football

  * [r/mlb](https://reddit.com/r/mlb) - mlb subreddit will collect information about all baseball tournaments
  * [r/mlb/comments](https://reddit.com/r/mlb/comments) - collecting comments from subreddit mlb

  * [r/nfl](https://reddit.com/r/nfl) - nfl subreddit will collect information about all football tournaments
  * [r/nfl/comments](https://reddit.com/r/nfl/comments) - collecting comments from subreddit nfl

  * [r/nba](https://reddit.com/r/nba) - nba subreddit will collect information about all basketball tournaments
  * [r/nba/comments](https://reddit.com/r/nba/comments) - collecting comments from subreddit nba

  * [r/tennis](https://reddit.com/r/tennis) - tennis subreddit will collect information about all tennis matches, players and etc
  * [r/tennis/comments](https://reddit.com/r/tennis/comments) - collecting comments from subreddit tennis

* `4chan`
  * [API-Endpoint](https://a.4cdn.org/sp/catalog.json) - Publically available API endpoint to retrieve comments from '/sp/' (Sports) Board
  * [Website-link](https://github.com/4chan/4chan-API) - Data from the 4chan API is exclusively accessible from a.4cdn.org, via either http:// or https:// protocols
  * [Reference code](https://medium.datadriveninvestor.com/how-to-use-the-4chan-json-api-with-python-building-a-dataset-for-machine-learning-part-1-ac36ad4c4be2)


## How to run the project?

Install `Python` and `MongoDB`

```bash
pip install matplotlib, flask, pymongo, pandas, plotly

flask run --host=0.0.0.0

This will run app.py file and all the other python associated files and html files with it
```

## Database schema - NoSQL MongoDB

```bash

twitterDB: twitterCountData
{
  "_id": ...,
  "Time": ...,
  "Tweet_Count": ...,
  "Sports_count": ...
}

redditDB: redditData
{
  "_id": ...,
  "Subreddit": ...,
  "Title": ...,
  "Comment": ...,
  "Comment_Time": ...
}

fourchanDB: fourchanData
{
  "_id": ...,
  "com": ...,
  "comCountry": ...,
  "comTime": ...
}
```
