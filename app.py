import praw
import os
import psycopg2
import urllib.parse as urlparse

from blacklist import link_blacklist

ENV_CLIENT_ID = os.environ.get('CLIENT_ID')
ENV_CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
ENV_USERNAME = os.environ.get('USERNAME')
ENV_PASSWORD = os.environ.get('PASSWORD')
ENV_DATABASE_URL = os.environ.get('DATABASE_URL')

url = urlparse.urlparse(ENV_DATABASE_URL)
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

conn = psycopg2.connect(ENV_DATABASE_URL, sslmode='require')

db = conn.cursor()

db.execute("INSERT INTO flagged_users (username) VALUES ('test')")

db.execute("SELECT * FROM flagged_users")
table = db.fetchall()

print(table)

conn.commit()

def makebot ():
  return praw.Reddit(
  user_agent = 'SysAdministry Of Truth v0.1',
  client_id = ENV_CLIENT_ID,
  client_secret = ENV_CLIENT_SECRET,
  username = ENV_USERNAME,
  password = ENV_PASSWORD
)

##### Link watcher #####
## flags any submissions to reddit that come from a blacklisted source ##
link_watcher = makebot().subreddit('all').stream.submissions()

for submission in link_watcher:
  for source in link_blacklist:
    if source in submission.url.lower():
      print(submission.author)