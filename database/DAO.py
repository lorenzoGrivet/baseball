from database.DB_connect import DBConnect
from model.team import Team


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllYears():

        cnx= DBConnect.get_connection()

        cursor= cnx.cursor(dictionary=True)
        risultato=[]

        query="""select distinct (t.`year`)
                from lahmansbaseballdb.teams t 
                where `year` >= 1980
                order by `year` desc """

        cursor.execute(query, ())

        for row in cursor:
            risultato.append(row["year"])

        cursor.close()
        cnx.close()
        return risultato


    @staticmethod
    def getTeamsOfYear(anno):
        cnx = DBConnect.get_connection()

        cursor = cnx.cursor(dictionary=True)
        risultato = []

        query = """select *
            from lahmansbaseballdb.teams t 
            where `year` =%s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            risultato.append(Team(**row))

        cursor.close()
        cnx.close()
        return risultato
