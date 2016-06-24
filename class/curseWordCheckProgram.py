"""
curse wordl check program
1. Read text from document.
2. Check text for curse words.

"""


def read_text():
	quotes = open("C:\movie_quotes.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()


read_text()
