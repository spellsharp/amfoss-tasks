import os
import telebot
import requests
import json
import csv


# TODO: 1.1 Get your environment variables 
yourkey = 'e2700b5c'
bot_id = '5682923095:AAGanEjptVwQAJukSM2X4Br_Yf2WgWIA5PM'

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hey there mothaf*ker, whatcha want?!.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Adios, BITCH!!\n\n')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    res = requests.get('https://www.omdbapi.com/')
    # TODO: 1.2 Get movie information from the API
    movie_info = message.text
    movie_name = movie_info.replace('/movie ','')
    print ("reached here")
    global movie 
    movie = []
    movie_req = requests.get(f"https://www.omdbapi.com/?apikey=e2700b5c&t={movie_name}")
    repsponse = movie_req.status_code
    print (repsponse)
    print ("reached part 2")
    # TODO: 1.3 Show the movie information in the chat window
    movie_data = json.loads(movie_req.text)
    print (movie_data)
    movie.append(movie_data['Title'])
    movie.append(movie_data['Year'])
    movie.append(movie_data['imdbRating'])
    movie_output = "Title: "+movie[0]+"\n"+"Year Of Release: "+movie[1]+"\n"+"IMDB Rating: "+movie[2]
    print ("reached part 3")

    poster = movie_data["Poster"]
    # movie_poster_request = requests.get(poster)

    bot.send_photo(message.chat.id, poster, movie_output)
    
    # TODO: 2.1 Create a CSV file and dump the movie information in it
    csv_file_headings = ["Title","Year","imdbRating"]
    with open('omdbbot.csv','w', encoding = 'UTF8', newline='') as newcsv:
        writer = csv.writer(newcsv)
        writer.writerow(csv_file_headings)
        writer.writerow(movie)
  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    chatcsv = open('omdbbot.csv','rb')
    bot.send_document(message.chat.id, chatcsv)

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()