from main import main

class TestClass:
    def test_example(self):
        inputPhrase = """Hello, I like nuts. Do you like nuts? No? Are you sure?
        Why don't you like nuts? Are you nuts? I like you
        """
        expectedResult = """like you: 3
like nuts: 3
are you: 2
like i: 2"""

        #This fails because the object order is not assured
        assert expectedResult == main(inputPhrase)
