from database.DB_connect import DBConnect
from model.player import Player


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def get_players(anno, salario):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select p.* , sum(s.salary) tot_salary
        from salaries s , people p 
        where s.`year` = %s and s.salary > %s  and p.playerID = s.playerID 
        group by s.playerID """
        cursor.execute(query, (anno, salario))
        result = []
        for row in cursor:
            result.append(Player(**row))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_appearances(anno, salario):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinctrow a.playerID , a.teamID 
        from appearances a , salaries s 
        where a.`year` = %s and s.salary > %s
        and a.playerID = s.playerID """
        cursor.execute(query, (anno, salario))
        result = {}
        for row in cursor:
            try:
                result[row['playerID']].append(row['teamID'])
            except KeyError:
                result[row['playerID']] = [row['teamID']]
        cursor.close()
        cnx.close()
        return result
