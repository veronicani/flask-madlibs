from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import story, excited_story

STORIES = {"silly_story": story, "excited_story": excited_story}

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.debug = True
debug = DebugToolbarExtension(app)


@app.get("/")
def index():
    """Show a drop down menu of story templates"""

    return render_template("index.html")


@app.get("/questions/<story_url>")
def show_questions(story_url):
    """Show question prompts with customized input fields for the story"""

    story = STORIES[story_url]

    return render_template(
        "questions.html",
        story_url=story_url,
        prompts=story.prompts
    )


@app.get("/results/<story_url>/")
def show_story(story_url):
    """Displays story on /results page with user inputs from /questions page"""
    story = STORIES[story_url]

    print(f"request args: {request.args}")

    print(f"This is the template: {story.template}")

    story_result = story.get_result_text(request.args)

    return render_template(
        "results.html",
        story=story_result
    )
