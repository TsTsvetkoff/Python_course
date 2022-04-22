"""
5. Define a class named Bulgarian which has a static method called printNationality(e.g.
“Bulgarian”).
"""


class Bulgarian():
    @staticmethod
    def print_nationality():
        print("България над всичко")


new_bulgarian = Bulgarian()
print(new_bulgarian.print_nationality())
#print(Bulgarian.print_nationality())

# Question why "None" is printed - is it due to " Static methods are called static because they always return None."
