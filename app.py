import praw
import os

ENV_CLIENT_ID = os.environ.get('CLIENT_ID')
ENV_CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
ENV_USERNAME = os.environ.get('USERNAME')
ENV_PASSWORD = os.environ.get('PASSWORD')

bot = praw.Reddit(
  user_agent = 'SysAdministry Of Truth v0.1',
  client_id = ENV_CLIENT_ID,
  client_secret = ENV_CLIENT_SECRET,
  username = ENV_USERNAME,
  password = ENV_PASSWORD
)

comments = bot.subreddit('all').stream.comments()

for comment in comments:
  print(comment.author)

