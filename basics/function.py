# Code for methods, loops and arrays

students = []
count = int(input("Enter no of students"))
i = 0


def add_stud():
	students.append(input("Enter Name: "))


def print_stud():
	print("You have entered all {0} users. Please find the users array below".format(i))
	print(students)


while i < count:
	add_stud()
	# print(i, count)
	i += 1


print_stud()
