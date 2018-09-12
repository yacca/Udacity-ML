import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Initialize the Movie instance

        Args:
            movie_title: Title of the movie
            movie_storyline: Storyline of the movie
            poster_image: URL string of the poster image
            trailer_youtube: URL string of the trailer on Youtube
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showTrailer(self):
        """Open the trailer"""
        webbrowser.open(self.trailer_youtube_url)