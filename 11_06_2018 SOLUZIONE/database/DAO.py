from database.DB_connect import DBConnect


class DAO():
        @staticmethod
        def getAllYears():
            conn = DBConnect.get_connection()

            result = []

            cursor = conn.cursor(dictionary=True)
            query = """select DISTINCT YEAR(s.`datetime`) as anno, count(*) as num
            FROM sighting s 
            GROUP by YEAR(s.`datetime`)
            ORDER BY YEAR(s.`datetime`)"""

            cursor.execute(query)

            for row in cursor:
                result.append((row["anno"], row["num"]))

            cursor.close()
            conn.close()
            return result

        @staticmethod
        def getNodes(anno):
            conn = DBConnect.get_connection()

            result = []

            cursor = conn.cursor(dictionary=True)
            query = """SELECT distinct s.state 
            from sighting s 
            where YEAR(s.`datetime`)=%s"""

            cursor.execute(query, (anno,))

            for row in cursor:
                result.append(row["state"])

            cursor.close()
            conn.close()
            return result

        @staticmethod
        def getEdges(anno):
            conn = DBConnect.get_connection()

            result = []

            cursor = conn.cursor(dictionary=True)
            query = """select s1.state as stato1, s2.state as stato2
            from sighting s1, sighting s2
            where  YEAR(s1.`datetime`)=YEAR(s2.`datetime`) and YEAR(s1.`datetime`)=%s
            and s1.`datetime`<s2.`datetime` 
            group by s1.state, s2.state """

            cursor.execute(query, (anno,))

            for row in cursor:
                result.append((row["stato1"], row["stato2"]))

            cursor.close()
            conn.close()
            return result

