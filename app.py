from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.debug = True
debug = DebugToolbarExtension(app)


# silly_story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time, in a long-ago {place}, there lived an exceptionally
#        {adjective} {noun}. It loved to {verb} with {plural_noun}."""
# )

@app.get("/")
def index(silly_story):
    """Show homepage with customized input fields for the story"""
    silly_story.prompts
    silly_story.template
    prompts, template = silly_story.items()
    print(f"prompts: {prompts}, template: {template}")

    # loop over the prompts list in the silly_story
    # for prompt in prompts:
        # make an label/input field for each prompt
        # label text should be the current prompt
        # form input name is the current prompt
    # return a template html questions.html, with the custom field inputs