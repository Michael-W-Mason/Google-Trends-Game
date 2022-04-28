from flask_app import app
from flask import render_template, redirect, request, session, jsonify
from flask_app.models.question import Question
from flask_app.models.leaderboard import Leaderboard
import random as rd

@app.route("/")
def main():
    if "score" not in session:
        session["score"] = 0
    return render_template('main.html')

@app.route("/get_answer/<int:id>")
def get_answer(id):
    data = {
        "id" : id
    }
    question = Question.get_answer(data)
    answer = question.answer
    return jsonify(answer=answer)

@app.route("/get_question")
def get_question():
    ran_question = Question.get_row()
    ran_index = rd.randint(0,3)
    choices = [ran_question.choice_1, ran_question.choice_2, ran_question.choice_3]
    choices.insert(ran_index, ran_question.answer)
    return jsonify(question = ran_question.question, question_choices = choices, id=ran_question.id)

@app.route("/get_leaderboard")
def get_leaderboard():
    leaderboard = Leaderboard.get_rows()
    return jsonify(leaderboard=leaderboard)

@app.route("/submit_leaderboard", methods=["POST"])
def submit_leaderboard():
    print(request.form)
    data = {
        'name' : request.form['name'],
        'score' : request.form['score']
    }
    add_to_leaderboard = Leaderboard.insert_row(data)
    return jsonify(message="Success")
