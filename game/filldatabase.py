from pytrends.request import TrendReq
import gamedata
import random as rd
from time import sleep
import sys
sys.path.insert(0, r"C:\Users\micha\OneDrive\Documents\My Code\Flask-Google-Trends-App")
from flask_app.models.question import Question

pytrends = TrendReq(hl='en-US', tz=360)



def format_top_charts(results, question):
    options = results['title']
    history = []
    choices = []
    answer = 100
    min = 100
    while len(choices) <= 3:
        ran_num = rd.randint(0, 9)
        if ran_num not in history:
            history.append(ran_num)
            if ran_num < min:
                min = ran_num
                answer = options[ran_num]
            try:
                choices.append(options[ran_num])
            finally:
                continue
    for i in range(len(choices)):
        if choices[i] == answer:
            choices.pop(i)
            break
    data = {
        "answer" : answer,
        "choice_1" : choices[0],
        "choice_2" : choices[1],
        "choice_3" : choices[2],
        "question" : question,
        "type" : 1
    }
    return data
    

def top_charts():
    for i in range(100):
        rand_year = rd.randint(2004, 2021)
        rand_country_index = rd.randint(0, len(gamedata.trends_countries) - 1)
        try:
            # query = pytrends.top_charts(rand_year, hl='en-US', tz=360, geo=gamedata.trends_countries[rand_country_index][0])
            query = pytrends.top_charts(rand_year, hl='en-US', tz=360, geo="US")
        except Exception as e:
            print(e)
        if query is None:
            continue
        if len(query['title']) < 4:
            print("Too Short")
            continue
        # question = f"In the year {rand_year}, which of the following was {gamedata.trends_countries[rand_country_index][1]}'s more popular search?"
        question = f"In the year {rand_year}, which of the following was United State's more popular search?"
        data = format_top_charts(query, question)
        Question.insert_question_row(data)
        sleep(1)

top_charts()

