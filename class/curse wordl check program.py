"""
curse wordl check program
1. Read text from document.
2. Check text for curse words.

"""

import urllib

#1. read text
def read_text():
	quotes = open("C:\movie_quotes.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

#2. check text
def check_profanity(text_to_check):
	# this url recognize curse word. if curse is there, return true.
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) 
	output = connection.read()
	#print(output)
	connection.close()
	

	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Could not scan the document properly")


read_text()






