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

def foods():
    for i in range(250):
        kw_list = []
        rand_year = rd.randint(2004, 2021)
        for j in range(4):
            while True:
                rand_foods_index = rd.randint(0, len(gamedata.foods) - 1)
                if len(kw_list) >= 4:
                    break
                elif gamedata.foods[rand_foods_index] not in kw_list:
                    kw_list.append(gamedata.foods[rand_foods_index])
                else:
                    continue
        try:
            pytrends.build_payload(kw_list, timeframe=f'{rand_year}-1-1 {rand_year}-12-30')
            data = pytrends.interest_over_time().to_dict()
        except Exception as e:
            print(e)
        for i in range(len(kw_list)):
            first_key = list(data[kw_list[i]].keys())[0];
            print (first_key)
        question = f'From the year {rand_year}, which of the following was the most popular search worldwide?'

        sleep(5)
# foods()


# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
# pytrends.build_payload(kw_list=['ice cream', 'bagel'])

# # Interest Over Time
# interest_over_time_df = pytrends.interest_over_time()
# print(interest_over_time_df.head())



# top_charts()

