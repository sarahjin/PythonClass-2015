#Register an app: https://dev.twitter.com/

#pip install tweepy
import tweepy
import time

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/
#check the documentation for new methods

#Get access to API
#get authorization
#never share the consumer key, secret, access token, secret

auth = tweepy.OAuthHandler('0rXZcgKAgKt28JPIgtBJdH05s', '48CneSOyP7CNkgVVetezu6y7bxa9fSG1gKL5BRl3oaTCDhFYqn')
auth.set_access_token('3413855949-v20n4ugjLqT6hlGpkowYfg6VRJZB7bxZPyFU5mr', 'gUT1qy5t9g15mKz3FFtKe4G3skREYT8fH59YPpizVJ7rY')    
api = tweepy.API(auth)

#See rate limit
api.rate_limit_status()

#Create user objects, put the user's screen name, or id: all work
betuld = api.get_user('BetulD_')
krugman = api.get_user('NYTimeskrugman')

#What can I do using this object?
#get the methods we can use with this object
dir(betuld)

#Get some of her information
betuld.id
betuld.name
betuld.screen_name
betuld.location

#Check her tweets
betuld.status
betuld.status.text
betuld.statuses_count
betuld.status.lang 

#Check her followers
betuld.followers_count
betuld.followers() #creates a list of user objects - only the first 20!
api.followers(betuld.id,count=200) #creates a list of id or screen_name objects - can get up to 200
api.followers('BetulD_')  #creates a list of the followers - also only the first 20!

#can get the list of the followers, and their information
betuld.followers()[0].screen_name

betuld.followers_ids() #creates a list of user ids - up to 5000
api.followers_ids(betuld)
api.followers_ids('BetulD_')

for follower_id in betuld.followers_ids():
	user = api.get_user(follower_id)
	print user.screen_name

#How to deal with limits

#Get the first 2 "pages" of follower ids
krugmans_followers=[]
for page in tweepy.Cursor(api.followers_ids, 'NYTimeskrugman').pages(2):
    krugmans_followers.extend(page)
    time.sleep(60) #wait 60secs to go to the next iteration
#Cursor object go through all the pages, give it the method, and the argument in the method
#extend the list of the followers 
#if leave pages(), then go through all the pages
#time.sleep is when the program reaches the tweeiter limit
    
#Get the ids of 6000 followers
krugmans_followers=[]

for item in tweepy.Cursor(api.followers_ids, 'NYTimeskrugman').items(6000):
	krugmans_followers.append(item)
	time.sleep(1)

#get the people the user follows
api.friends_ids('BetulD_')


