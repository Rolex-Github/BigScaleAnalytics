
import tmdbsimple as tmdb
import time


class TMDB():
    """For retrieving image poster.

    """
    poster_prefix = "https://image.tmdb.org/t/p/w500"
    tmdb_api_key = "577de6ca2c5c1ffa942189ef5843e5f3"

    def __init__(self):
        tmdb.API_KEY = self.tmdb_api_key

    def search(self, search_string):
        search = tmdb.Search()
        response = search.movie(query=search_string)
        return response

    def get_poster_path_by_name(self, search_string):
        """Return just the poster path for the movie"""

        response = self.search(search_string)
        for hit in response["results"]:
            return self.poster_prefix + hit["poster_path"]

    def get_poster_path_by_id(self, tmdb_id):
        movie = tmdb.Movies(tmdb_id)
        response = movie.info()

        return self.poster_prefix + response["poster_path"]
        return self.poster_prefix + response["poster_path"]


if __name__ == '__main__':
    start_time = time.time()

    # check tmdb
    print(TMDB().search("matrix"))
    print(TMDB().get_poster_path_by_name("matrix"))
    print(TMDB().search("matrix"))
    print(TMDB().get_poster_path_by_id("862.0")) # Toy Story

    print("--- %s seconds ---" % (time.time() - start_time))
