from xml.etree.ElementInclude import LimitedRecursiveIncludeError
import praw
import time

rt = open("replied_to.txt", "a+")
rrt = open("replied_to.txt", "r")

reddit = praw.Reddit(
    client_id="_Ebr_4fwWFfGklwsEqbkOg",
    client_secret="pHfoKRKsPOZ4Bim6NuQReDJD3ZJfOw",
    user_agent="<console:BREAD:1.0>",
    username="garlic-bread-bot",
    password="2m0e0r8t"
)


subr = reddit.subreddit("garlictest2")

lines = rrt.read()
replied_to = lines.split()



for submmision in subr.hot(limit=1000):
    #print("****************")
    #print(submmision.title)

    for comment in submmision.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " bread " or "bread " or "bread" in comment_lower and comment.id not in replied_to:    
                print("\n bread")
                comment.reply(body="Bread 👍")
                rt.write(comment.id + "\n")
                time.sleep(660)
            elif comment.id in replied_to:
                pass

rt.close()
rrt.close()