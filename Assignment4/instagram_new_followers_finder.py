import instaloader
import getpass

f=open("folowers.txt","r")
old_followers=[]
for line in f :
    old_followers.append(line)
f.close()    

l=instaloader.Instaloader()

username=input("enter your user name :  ")
password=getpass.getpass("enter your password : ")

l.login(username,password)
print("hooraaa")

profile=instaloader.Profile.from_username(l.context,"mahdis._khb")

new_followers=[]
for follower in profile.get_followers():
    new_followers.append(follower)


for old_follower in   old_followers:
    if old_follower not in old_followers:
        print (old_follower)


f=open("followers.txt","w")
for follower in new_followers:
    f.write(follower+"\n")
f.close()