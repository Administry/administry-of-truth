import praw
import os
from blacklist import link_blacklist

ENV_CLIENT_ID = os.environ.get('CLIENT_ID')
ENV_CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
ENV_USERNAME = os.environ.get('USERNAME')
ENV_PASSWORD = os.environ.get('PASSWORD')

link_watcher = praw.Reddit(
  user_agent = 'SysAdministry Of Truth v0.1',
  client_id = ENV_CLIENT_ID,
  client_secret = ENV_CLIENT_SECRET,
  username = ENV_USERNAME,
  password = ENV_PASSWORD
)

submissions = link_watcher.subreddit('all').stream.submissions()


for submission in submissions:
  for link in link_blacklist:
    if link in submission.url.lower():
      print(submission.url.lower())