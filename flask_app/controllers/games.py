from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.question import Question
import random as rd
# from flask_app.models.template import User
@app.route("/")
def main():
    if "score" not in session:
        session["score"] = 0
    ran_question = Question.get_row()
    ran_index = rd.randint(0,3)
    choices = [ran_question.choice_1, ran_question.choice_2, ran_question.choice_3]
    choices.insert(ran_index, ran_question.answer)
    return render_template('main.html', question=ran_question, choices=choices, score=session["score"])

@app.route("/check_answer/<int:id>", methods=["POST"])
def check_answer(id):
    data = {
        "id" : id,
        "answer" : request.form["answer"]
    }
    print(Question.check_answer(data))
    if Question.check_answer(data):
        session["score"] += 1
    else:
        session["score"] = 0
    return redirect("/")
