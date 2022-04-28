from flask_app.config.mysqlconnection import connectToMySQL

class Leaderboard:
    db = "google_trends_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data['name']

    @classmethod
    def insert_row(cls, data):
        query = "INSERT INTO leaderboard (name, score) VALUES (%(name)s, %(score)s)"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def get_rows(cls):
        query = "SELECT * FROM leaderboard ORDER BY score DESC LIMIT 10"
        results = connectToMySQL(cls.db).query_db(query)
        leaderboard = []
        for result in results:
            leaderboard.append(result)
        return leaderboard
