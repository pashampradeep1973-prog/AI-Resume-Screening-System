from flask import Flask,request,jsonify
from flask_cors import CORS
from resume_ai import analyze_resumes
from database import save_results,cursor

app=Flask(__name__)
CORS(app)

@app.route("/screen",methods=["POST"])

def screen():

    job=request.form.get("job")

    files=request.files.getlist("resumes")

    results=analyze_resumes(files,job)

    save_results(results)

    return jsonify(results)


@app.route("/candidates")

def candidates():

    cursor.execute("SELECT name,score,skills FROM candidates")

    rows=cursor.fetchall()

    data=[]

    for r in rows:

        data.append({
        "name":r[0],
        "score":r[1],
        "skills":r[2]
        })

    return jsonify(data)


if __name__=="__main__":

    app.run(debug=True)