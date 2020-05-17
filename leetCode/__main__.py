import sys, requests
from leetCode.help import validHelp, invalidHelp

# Web Scraping 
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import urllib.request
import time


def main():
	args = sys.argv[1:]
	
	# Set of commands for package
	commands = {
		"set": setupProblem, 
		"check": checkProblem, 
		"visualize": visualize,
	    "customVisualize": customVisualize
	}

	# Condition to check if the commands
	# are good enough to go with
	if len(args):
		if args[0] in commands:
			commands[args[0]](args[1:])
		else:
			invalidHelp()
	else:
		validHelp()


def setupProblem(args):
	link = args[0]
	if link.startswith("https://leetcode.com/problems/"):
		try:
			response = requests.get(link)
			pageHTML = response.content
			page_soup = soup(pageHTML, "html.parser")
			page_soup.prettify()
			# containers=page_soup.findAll("pre")
			print(page_soup)
		except:
			print("Invalid LeetCode Problem")
	else:
		print("Invalid LeetCode Problem") 

def checkProblem(args):
	print("Under Maintainance")



def visualize(args):
	print("Under Maintainance")


def customVisualize(args):
	print("Under Maintainance")