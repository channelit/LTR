import requests as req
import tensorflow as tf
import tensorflow_datasets as tfds


def config_solr():
    req_obj = {
        "add-requesthandler": {
            "name": "/mypath",
            "class": "solr.DumpRequestHandler",
            "defaults": {"x": "y", "a": "b", "rows": 10},
            "useParams": "x"
        }
    }
    pass


class Solr:
    def __int__(self, solr_url):
        self.solr_url = solr_url

    def index(self):
        movies = tfds.load("movielens/latest-small-movies", shuffle_files=False, batch_size=-1)
        ds_numpy = tfds.as_numpy(movies)
        for item in ds_numpy:
            # movie_genres, movie_id, movie_title = item['movie_genres'], item['movie_id'], item['movie_title']
            movie_genres, movie_id, movie_title = item[0], item[1], item[2]
            print(movie_genres)

    def add_user_rating(self, user, rating):
        pass

    def add_user(self, user):
        pass

    def add_movie(self):
        pass

    def send_req(self, req_obj):
        result = req.post(self.solr_url)
        print("The response is:", result)

solr = Solr()
Solr.index(solr)
