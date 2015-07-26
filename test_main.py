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
        assert expectedResult == main(inputPhrase)

