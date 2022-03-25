from flask import Flask, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def render_home():

    story_list = [story_type for story_type in stories.keys()]


    return render_template("home.html", stories = story_list)


@app.get("/questions")
def get_questions():

    """ Generating form prompts"""

    story_type = request.args.get("story-type")

    prompts = stories[story_type].prompts

    session["story"] = story_type

    return render_template("questions.html", words=prompts)


@app.get("/story")
def get_form_data():

    """ Generate story from form data """

    story_type = session["story"]

    form_data = request.args

    answers  = stories[story_type].generate(form_data)

    return render_template("story.html", answers = answers)
