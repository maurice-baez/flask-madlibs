from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/questions")
def get_questions():

    """ Generating form prompts"""

    prompts = silly_story.prompts

    return render_template("questions.html", words=prompts)


@app.get("/story")
def get_form_data():

    """ Generate story from form data """

    form_data = request.args

    answers  = silly_story.generate(form_data)

    return render_template("story.html", answers = answers)
# all logic to get form data goes here
#return render template story.html






#loop through the form array and generate the html input for each