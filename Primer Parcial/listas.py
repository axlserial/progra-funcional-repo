# List comprehentions
from math import sqrt


def func():
    # numbers = [i for i in range(1, 100000) if i % 3 == 0 and i % 6 == 0 and i % 9 == 0]
    # print(len(numbers))
    
	students = (
        ("Carlos", [7.7, 6.6, 8.9], 19, "H"),
        ("Anabel", [8.1, 8.8, 7.9], 18, "M"),
        ("Octavio", [7.9, 8.9, 6.9], 17, "H"),
		("Angel", [7.9, 8.9, 6.9], 16, "H"),
		("Denisse", [7.9, 8.9, 6.9], 21, "M")
    )

	studentsFilter = [s for s in students if sum(s[1]) / len(s[1]) >= 8.0]
	print(studentsFilter)

def listComp():
	num = [1, 2, 3]
	alfa = ['a', 'b', 'c']
	
	l = [(x, y) for x in num for y in alfa]
	print(l)

def dictComp():
	my_dict = {i : i**3 for i in range(1, 101) if i % 3 != 0}
	print(my_dict)


if __name__ == "__main__":
    # func()
	# listComp()
	dictComp()
