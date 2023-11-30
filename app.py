from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.debug = True
debug = DebugToolbarExtension(app)

@app.get("/questions")
def index():
    """Show question prompts with customized input fields for the story"""

    return render_template(
        "questions.html",
        prompts=silly_story.prompts
    )

@app.get("/results")
def show_story():
    """Displays story on /results page with user inputs from /questions page"""

    print(request.args)

    print(f"This is the template: {silly_story.template}")

    return render_template(
        "results.html",
        story=silly_story.get_result_text(request.args)
        # call this outside, we're missing the chance to name the story
    )