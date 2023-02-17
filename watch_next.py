# This program will tell you what to watch next based on the word vector similarity of the description of movies.

import spacy # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use.

# define the function watch_next
# The function takes in the description as a parameter and returns the title of the most similar movie.
def watch_next(description):
   # open the text file with all the movies we will be comparing
   with open("movies.txt", "r") as f:
      # read each text line and turn it into a list
      # each line will represent one element aka one movie
      movies_list = f.read().splitlines()
      # define the variables movie_rec and high_similarity
      movie_rec = ""
      high_similarity = 0
      # for each movie in the movies_list
      for movie in movies_list:
          # activate the similarity function
          similarity = nlp(movie).similarity(description)
          # if the similarity found is higher than the current value
          # then high_similarity takes that value
          # and recommends that movie
          if similarity > high_similarity:
             high_similarity = similarity
             # only return the title of the movie without the description
             movie_rec = movie[:7]
      return(movie_rec)

# Below is our movie description we will test the recommendation similarity against
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
description = nlp(description)

print(f"Your next movie recommendation is: {watch_next(description)}.")