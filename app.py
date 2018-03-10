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
      username = submission.author.name ## TO DO: Collect more data on violating users. Account age, Active communities, etc.
      ## TO DO: create a separate table for the links themselves, store the links with relationships to the users that post them.
      ## TO DO: create a table for violations. Just keep track of any violations, whether that is a comment with a link to a blacklisted item, or a post.
      ## ^^ Relate violation records with users via ID.
      db.execute("""
        INSERT INTO flagged_users (username) VALUES (%s)
        ON CONFLICT (username) DO NOTHING; 
      """, [username]) ## TO DO: When there is a conflicting username, capture the link and keep a count of blacklist violations.
      conn.commit()