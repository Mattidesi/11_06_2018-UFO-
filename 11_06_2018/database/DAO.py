from database.DB_connect import DBConnect
from model.edges import Edge
from model.states import State


class DAO():
    pass

    @staticmethod
    def getYears():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct year(`datetime`) as anno,count(*) as nAvvistamenti
                        from sighting s
                        group by year(`datetime`)"""
            cursor.execute(query)

            for row in cursor:
                result.append((row["anno"],row["nAvvistamenti"]))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getAllNodes(year):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct s2.* 
                        from sighting s,state s2 
                        where s.state = s2.id 
                        and year(s.`datetime`) = %s """
            cursor.execute(query,(year,))

            for row in cursor:
                result.append(State(**row))

            cursor.close()
            cnx.close()
        return result


    @staticmethod
    def getAllEdges(year,idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select t1.id as id1,t2.id as id2
                        from 
                        (select distinct s2.id ,s.datetime
                        from sighting s,state s2 
                        where s.state = s2.id 
                        and year(s.`datetime`) = %s) as t1,
                        (select distinct s2.id ,s.datetime
                        from sighting s,state s2 
                        where s.state = s2.id 
                        and year(s.`datetime`) = %s) as t2
                        where t1.datetime < t2.datetime
                        group by t1.id,t2.id

"""
            cursor.execute(query,(year,year))

            for row in cursor:
                result.append(Edge(idMap[row["id1"]],idMap[row["id2"]]))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getStates(year):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct s2.* 
                        from sighting s,state s2 
                        where s.state = s2.id 
                        and year(s.`datetime`) = %s """
            cursor.execute(query,(year,))

            for row in cursor:
                result.append(State(**row))

            cursor.close()
            cnx.close()
        return result
