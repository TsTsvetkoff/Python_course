"""
5. Define a class named Bulgarian which has a static method called printNationality(e.g.
“Bulgarian”).
"""


class Bulgarian():
    @staticmethod
    def print_nationality():
        return "България над всичко"


new_bulgarian = Bulgarian()
print(new_bulgarian.print_nationality())
