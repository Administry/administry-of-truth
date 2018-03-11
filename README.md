# (AD[MIN)ISTRY] OF TRUTH

### ADMIN
> An individual who is entrusted to act in the best interest of an online community and uphold it's standards. A servant of the community. 

### THE MINISTRY OF TRUTH
> The infamous government bureaucracy responsible for the spead of propaganda and misinformation in George Orwell's dystopian masterpiece, 1984.

---------------------------------

Bots, Trolls (russian or otherwise), Astro-turfing, Shills, Propaganda, and "fake news" are all different heads of the same beast: Weponized Misinformation. It is not an overstatement to say that we are living in a new age of psychological warfare, epitomized by misinformation campaigns via channels we have learned to trust.

The goal of this project begins small: to build a bot that will monitor and record the activity of those who spread misinformation, propaganda, and lies on reddit. This information could be absolutely vital to understanding not only how these agents currently behave, but how they evolve. Patterns will emerge in the data which will help us find ways of combatting this misinformation problem head-on.

The larger goal of the project is to develop a system that is capable of holding individuals, organizations, and media outlets accountible for their words and actions on the inernet. A system that can be trusted because the code is open for all to view, and the methodogies employed rely solely on verifiable facts as the source of truth.

Although there will still be discussions and disagreements about political, social, and economic issues - as there always should be - it is vital that these discussions are built upon reality, and made in good faith. We must reclaim our right to information, and reclaim the internet for its role in the next evolution of humanity: The power of knowledge must be shared among us all.

-------------------------------------------------------------------------------------------------------------------------

Prerequisites
-------------
- Python 3 & Pip
- Postgres database with URI / URL

Getting started
-----------------
If you're interested in contributing, please reach out: stoptherussianredditbots@gmail.com

To run the project locally, do the following:
```
# clone the repository. From the terminal:
git clone https://github.com/Administry/administry-of-truth.git

# move into the parent directory and install required packages. From the terminal:
cd administry-of-truth && pip install -r requirements.txt

# create your .env file inside the parent directory. From the terminal:
touch .env

# populate your .env file with the required environment variables. Descriptions provided below. In a text editor:
export CLIENT_ID=''   ## provided by reddit
export CLIENT_SECRET=''  ## provided by reddit
export USERNAME=''   ## reddit username
export PASSWORD=''  ## reddit password
export DATABASE_URL=''  ## url to a postgres database

# run the project. From the terminal:
python3 app.py
```

Useful links
-----------------
Contributing Guide (COMING SOON)
If you're interested in contributing, please reach out: stoptherussianredditbots@gmail.com