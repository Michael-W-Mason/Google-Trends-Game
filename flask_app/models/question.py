from flask_app.config.mysqlconnection import connectToMySQL

class Question:
    db = "google_trends_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.question = data['question']
        self.choice_1 = data['choice_1']
        self.choice_2 = data['choice_2']
        self.choice_3 = data['choice_3']
        self.answer = data['answer']

    @classmethod
    def insert_question_row(cls, data):
        query = "INSERT INTO questions (question, answer, choice_1, choice_2, choice_3,type) VALUES (%(question)s, %(answer)s, %(choice_1)s, %(choice_2)s, %(choice_3)s, %(type)s)"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def get_row(cls):
        query = "SELECT * FROM questions ORDER BY RAND() LIMIT 1"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        return cls(results[0])
    
    @classmethod
    def get_answer(cls, data):
        query = "SELECT * FROM questions WHERE id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        result = cls(results[0])
        return result
