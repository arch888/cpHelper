

def validHelp():
	helpStr = """Hey There, Here are some list of commands for LeetCode

	set [link] - For Setting up the workspace for the leet code question
	    [link] - This denotes a valid link of the leetCode Problem. 
	             Square Brackets are not neccesary.

	check [file] - This command is used for checking the input and output for the 
	               sample inputs provided by the LeetCode.

	visualize [Input Number] - This command is used to visualize any LeetCode Input test.
							   (Under Process)

	customVisualize [link] [file] - This command is used to visualize any Custom Input for 
	                                the LeetCode question. (Under Process)
	"""

	print(helpStr)


def invalidHelp():
	print("Sorry Invalid command !\n\n")

	validHelp()