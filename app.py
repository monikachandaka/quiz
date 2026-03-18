from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
{
"question":"What is the capital of India?",
"options":["Delhi","Mumbai","Chennai","Kolkata"],
"answer":"Delhi"
},
{
"question":"Which language is used for web development?",
"options":["HTML","Python","JavaScript","All"],
"answer":"All"
},
{
"question":"Who created Python?",
"options":["Guido van Rossum","Bill Gates","Elon Musk","Mark Zuckerberg"],
"answer":"Guido van Rossum"
},
{
"question":"Which is a database?",
"options":["MySQL","HTML","CSS","Python"],
"answer":"MySQL"
}
]

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html",questions=questions)

@app.route("/result",methods=["POST"])
def result():

    score=0

    for i,q in enumerate(questions):
        ans=request.form.get(f"q{i}")
        if ans==q["answer"]:
            score+=1

    return render_template("result.html",score=score,total=len(questions))

if __name__=="__main__":
    app.run(debug=True)