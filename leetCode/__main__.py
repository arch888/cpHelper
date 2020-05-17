import sys, requests
from leetCode.help import validHelp, invalidHelp

def main():
	args = sys.argv[1:]
	if len(args):
		pass
	else:
		validHelp()