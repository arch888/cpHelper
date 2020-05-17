def validHelp():
	helpStr = """This app generally contains three packages which can be used individually -

	leet - A package for setting up the problems workspace for LeetCode problems.

	chef - A package for setting up the problems workspace for CodeChef Challenges / Problems.

	forces - A package for setting up the problems workspace for Codeforces Challenges / Problems.
	"""

	print(helpStr)


def invalidHelp():
	print("Sorry Invalid command !\n\n")

	validHelp()