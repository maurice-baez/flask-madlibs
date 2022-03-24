from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/questions")
def get_questions():
    question = silly_story.prompts
#all logic to generate the form questions goes here
    return render_template("questions.html", words=question)


@app.post("/questions")
def get_form_data():
    silly_story.generate(answers)
    return render_template("story.html")
# all logic to get form data goes here
#return render template story.html






#loop through the form array and generate the html input for each