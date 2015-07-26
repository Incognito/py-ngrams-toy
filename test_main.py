import pytest
import textwrap

from main import *

class TestClass:
    def test_example(self):
        inputPhrase = textwrap.dedent("""Hello, I like nuts. Do you like nuts? No? Are you sure?
        Why don't you like nuts? Are you nuts? I like you
        """)
        expectedResult = textwrap.dedent("""Are you: 2
        like nuts: 3
        you like: 3
        I like: 2
        """)
        assert expectedResult == inputPhrase

    def test_split_original_words(self):
        inputPhrase = textwrap.dedent("""Hello, I like nuts. Do you like nuts? No? Are you sure?
        Why don't you like nuts? Are you nuts? I like you
        """)
        assert get_word_list(inputPhrase) == ["hello", "i", "like", "nuts", "do", "you", "like",
            "nuts", "no", "are", "you", "sure", "why", "don't",
            "you", "like", "nuts", "are", "you", "nuts", "i",
            "like", "you"]
