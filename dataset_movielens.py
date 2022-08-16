from keras.utils import Sequence
from tensorflow_datasets.core.features import FeaturesDict, ClassLabel
import os
import pprint
import tempfile

from typing import Dict, Text

import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_recommenders as tfrs

dataset_name = "movielens/latest-small-movies"

ratings = tfds.load(dataset_name, split="train")
# Features of all the available movies.
movies = tfds.load(dataset_name, split="train")

# Ratings data.
ratings = tfds.load(dataset_name, split="train")
# Features of all the available movies.
movies = tfds.load(dataset_name, split="train")

for x in ratings.take(1).as_numpy_iterator():
    pprint.pprint(x)

for x in ratings.take(1).as_numpy_iterator():
    pprint.pprint(x)

ratings = tfds.load(dataset_name, split="train")

ratings = ratings.map(lambda x: {
    "movie_title": x["movie_title"],
    "user_id": x["user_id"],
    "user_rating": x["user_rating"]
})

tf.random.set_seed(42)
shuffled = ratings.shuffle(100_000, seed=42, reshuffle_each_iteration=False)

train = shuffled.take(80_000)
test = shuffled.skip(80_000).take(20_000)

movie_titles = ratings.batch(1_000_000).map(lambda x: x["movie_title"])
user_ids = ratings.batch(1_000_000).map(lambda x: x["user_id"])

unique_movie_titles = np.unique(np.concatenate(list(movie_titles)))
unique_user_ids = np.unique(np.concatenate(list(user_ids)))

FeaturesDict({
    'movie_genres': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=21)),
    'movie_id': tf.string,
    'movie_title': tf.string,
})


class RankingModel(tf.keras.Model):

    def __init__(self):
        super().__init__()
        embedding_dimension = 32

        # Compute embeddings for users.
        self.user_embeddings = tf.keras.Sequential([
            tf.keras.layers.StringLookup(
                vocabulary=unique_user_ids, mask_token=None),
            tf.keras.layers.Embedding(len(unique_user_ids) + 1, embedding_dimension)
        ])

        # Compute embeddings for movies.
        self.movie_embeddings = tf.keras.Sequential([
            tf.keras.layers.StringLookup(
                vocabulary=unique_movie_titles, mask_token=None),
            tf.keras.layers.Embedding(len(unique_movie_titles) + 1, embedding_dimension)
        ])

        # Compute predictions.
        self.ratings = tf.keras.Sequential([
            # Learn multiple dense layers.
            tf.keras.layers.Dense(256, activation="relu"),
            tf.keras.layers.Dense(64, activation="relu"),
            # Make rating predictions in the final layer.
            tf.keras.layers.Dense(1)
        ])

    def call(self, inputs):
        user_id, movie_title = inputs

        user_embedding = self.user_embeddings(user_id)
        movie_embedding = self.movie_embeddings(movie_title)

        return self.ratings(tf.concat([user_embedding, movie_embedding], axis=1))


RankingModel()((["42"], ["One Flew Over the Cuckoo's Nest (1975)"]))
