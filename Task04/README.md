Telegram bot was a bit confusing since I was focused on resolving my ENV_VARs. But I found out that I could just directly add my botToken and omdbAPI to the code. I figured that the ENV_VAR thing was for the safety of my code since anybody who gets access to my code now also has access to my API token and bot token. But since I couldn't proceed at all when I was trying the dotenv method, I just skipped that part. I'll learn how to set my ENV_VAR in linux soon. I googled a lot. A lot. 
Then I used the request-get method to fetch my data, and I converted it from json to text format.
Then I appended the data to a list I created. And then I used the keys from the dictionary in the json file to access whatever data I wanted. 
Now using the bot.send_photo etc was all easy, but I had to google to find how to put my data into a csv file. I had some experience in it since I did the Rust task before.  
Oh yeah, there were a few things I added for debugging to make sure my code even reached a certain stage; I haven't removed them. 
Personal Experience: Like I previously mentioned I was struggling with the dotenv etc so I had initially given up on the task. Then after a week I met a friend  who claimed he had the same issue and that he didn't need to use dotenv. And that got me googling. 


https://user-images.githubusercontent.com/115102691/207613634-14170b10-7856-45f2-a89b-d5693a868008.mp4

