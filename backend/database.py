import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pradeep",
    database="resume_ai"
)

cursor = conn.cursor()

def save_results(results):

    for r in results:

        sql = "INSERT INTO candidates (name,score,skills) VALUES (%s,%s,%s)"

        val = (r["name"], r["score"], ", ".join(r["skills"]))

        cursor.execute(sql,val)

    conn.commit()