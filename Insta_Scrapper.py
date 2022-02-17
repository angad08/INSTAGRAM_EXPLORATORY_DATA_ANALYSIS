import instaloader
import pandas as pd
import numpy
bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, 'akn_268_996')
posts = profile.get_posts()
bot.login(user="USERNAME",passwd="PASSWORD")
#Code For Getting usernmaes,Likes and Posts
insta_1=[]
insta_2=[]
insta_3=[]
likes=[]
posttype=[]
for index, post in enumerate(posts):
    Post="Post "+str(index+1)
    for j in post.get_likes():
        insta_1.append(Post)
        insta_2.append(j.username)
        insta_3.append(post.typename)
    likes.append(post.likes)
    posttype.append(post.typename)

#getting Folloowers and Followees
youFollow=[str(i).split()[1] for i in list(profile.get_followees())]
followers=[str(i).split()[1] for i in list(profile.get_followers())]


#Storing all in csv files
pd.DataFrame({"POST_NO":insta_1,"USERS":insta_2,"POST_TYPE":insta_3}).to_csv("C:\\Users\\Angat\\Downloads\\Instagram.csv",index=False)
pd.DataFrame({"Likes":likes,"Post":posttype}).to_csv("C:\\Users\\Angat\\Downloads\\Instagram_Likes.csv",index=False)
pd.DataFrame({"Followers":followers}).to_csv("C:\\Users\\Angat\\Downloads\\Instagram_Followers_Followers.csv",index=False)
pd.DataFrame({"Followees":youFollow}).to_csv("C:\\Users\\Angat\\Downloads\\Instagram_Followers_Followees.csv",index=False)
