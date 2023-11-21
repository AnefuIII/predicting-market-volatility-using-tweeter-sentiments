#!/usr/bin/env python
# coding: utf-8

# #                               Scraping COVID19 Tweets from Twitter using API's
# 
# 
# > 1. Mounting Google Drive
# 
# 
# 

# In The frirst line of code we will mount Google Drive to Google Colab. This is required to access files stored in google drive.

# In[1]:


from google.colab import drive
drive.mount('/content/drive')


# 
# 
# > 2. Creating Properties file to save and access APIKey, SecretAPIkey, Accesstoken and secret access token
# 
# 
# > To connect to twitter
# 
# 
# [twitter]
# accesstoken = xxxxxxxxxxxxxxxxxx
# 
# accesstokensecret = xxxxxxxxxxxxxxxxx
# 
# apikey = xxxxxxxxxxxxxxxxxxxxxx
# 
# apisecretkey = xxxxxxxxxxxxxxxxxxxxx
# 
# > To connect with google maps to get the location of users
# 
# googleapikey = xxxxxxxxxxxxxxxxxxxxx
# 
# 
# 

# In[17]:


get_ipython().system("ls '/content/drive/My Drive/Colab Notebooks/twitter.properties'")


# 3. Installing and Importing Packages
# 
# 
# 
# *   ConfigParser: Used to read the properties file
# 
# 

# In[18]:


get_ipython().system('pip install ConfigParser')


# In[19]:


import configparser
config = configparser.RawConfigParser()
config.read(filenames = '/content/drive/My Drive/Colab Notebooks/twitter.properties')
print(config.sections())


# 
# *   Above we can see [twitter] is the only section in our properties file.
# *   But we can have multiple sections based on our requirements.
# 
# 
# 
# > Install and import Tweepy
# 
# 
# *   Tweepy is a library used to read tweets.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[20]:


get_ipython().system('pip install tweepy')


# In[ ]:


import os
import tweepy as tw


# 
# 
# > 4. Accessing API's
# 
# 

# In[ ]:


accesstoken = config.get('twitter','accesstoken')  #creating 4 varaibles and assigning them basically saying read these 4 keys from file and assign 
accesstokensecret = config.get('twitter','accesstokensecret')
apikey = config.get('twitter','apikey')
apisecretkey = config.get('twitter','apisecretkey')


# In[ ]:


auth = tw.OAuthHandler(apikey,apisecretkey) #calling OAuthHandler required for authantication with Twitter
auth.set_access_token(accesstoken,accesstokensecret)

#calling tw.API func. wait_on_rate_limit is required because twitter has set a limit
api = tw.API(auth,wait_on_rate_limit=True)


# In[ ]:


search_word = '#coronavirus'
date_since = '2020-05-18'


# In[ ]:


#creating a tweepy itemiterator tweets for searching by calling tw.Cursor func, pulling only 1000 records
tweets = tw.Cursor(api.search,q = search_word, lang ='en',since = date_since).items(1000)


# In[13]:


tweets


# # Extracting tweets using Hashtag i.e. search word 

# In[26]:


# get geo = where its tweeted from, location = user location etc.
tweet_details = [[tweet.geo,tweet.text,tweet.user.screen_name,tweet.user.location]for tweet in tweets]
tweet_details


# In[ ]:


import pandas as pd


# In[28]:


tweet_df = pd.DataFrame(data = tweet_details,columns=['geo','text','user','location'])
pd.set_option('max_colwidth',800)
tweet_df.head(20)

