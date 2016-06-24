"""
movie media main page


"""
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", "https://youtu.be/KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", "https://youtu.be/d1_JBMrrYw8")
avengers = media.Movie("Avengers", "American superhero film based on Marvel Comics", "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Avengers_Age_of_Ultron.jpg/220px-Avengers_Age_of_Ultron.jpg", "https://youtu.be/tmeOjFno6Do")
school_of_rock = media.Movie("Schoo of rock", "crazy dude made his band", "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg", "https://youtu.be/XCwy6lW5Ixc")
johnny_english = media.Movie("Johnny English", "Mr.Bean acts", "https://upload.wikimedia.org/wikipedia/en/thumb/9/92/Johnny_English_movie.jpg/220px-Johnny_English_movie.jpg", "https://youtu.be/74qGvVoyN1Q")
ratatouille = media.Movie("Ratatouille", "mouse cook the food", "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg", "https://youtu.be/niD-jahFURU")


#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
#print(avengers.title +": "+avengers.storyline)
#avengers.show_trailer()


movies = [toy_story, avatar, avengers, school_of_rock, johnny_english, ratatouille] #list of the movies
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.valid_ratings)
print(media.Movie.__name__)
print(media.Movie.__module__)
print(media.Movie.__doc__)
