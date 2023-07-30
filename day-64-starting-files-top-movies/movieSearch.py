import requests
class Search_movie():

    def __init__(self):
        #https://api.themoviedb.org/3/movie/550?api_key=76132e2f954546547e034fcbcc07cd3a
        self.movie_api_key = '76132e2f954546547e034fcbcc07cd3a'
        self.reading_key = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NjEzMmUyZjk1NDU0NjU0N2UwMzRmY2JjYzA3Y2QzYSIsInN1YiI6IjY0YzY3MWJmY2FkYjZ' \
                               'iMDBhYzY2MjI3ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.M3DHepkPxGvjKFOSgrAzfhqtP4IjQM74Ht0krum7e3g'
        self.url = "https://api.themoviedb.org/3/search/movie"
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.reading_key}"
        }

    def search_movie(self,title):
        query = self.url + f"?query={title}"
        request = requests.get(url=query, headers=self.headers)
        print(request.json())
        return request.json()




