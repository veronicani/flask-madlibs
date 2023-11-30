"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, ...):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.get_result_text(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text #"Here is ____ I am ____"

    def get_result_text(self, answers):
        """Return result text from dictionary of {prompt: answer, ...}."""

        text = self.template # text = "Here is __place__ I am __adj__" {place: Dubai, adj: hairy}

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val) # text = "Here is Dubai. I am hairy"

        return text


# Here's a story to get you started

silly_story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, in a long-ago {place}, there lived an exceptionally
       {adjective} {noun}. It loved to {verb} with {plural_noun}."""
)
# {"place" : "Dubai", "noun" : "rice" , "verb": "eat", "adjective":"hairy", "plural_noun":"ricii"}

# Here's another --- you should be able to swap in app.py to use this story,
# and everything should still work

excited_story = Story(
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)
