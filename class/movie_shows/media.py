"""
Movie program

title
storyline
poster image
youtube trailer


"""

import webbrowser


class Video():
	"""
	1.title
	2.duration
	"""

	def __init__(self, )




class Movie(Video):
	"""This class provides a way to store movie related information"""
	valid_ratings = ["G", "PG", "PG-13", "R"]
	
	"""docstring for Movie"""
	#__init__ gets called : self = toy_story, avartar ...(instance), 
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

		#if i delete (self.) it can not be used outside of class.
		#these are Thing to remeber! ->instance variables
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	#Things to do! -> instance methods! 
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


class TvShow():
	"""
	1.title
	2.season
	3.episode
	4.tv_station
	def get_local_listing()
	"""

	def __init__(self)