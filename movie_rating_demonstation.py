
import numpy as np

np.set_printoptions(formatter={'float_kind':'{:.3f}'.format})  #Sets the display setting so that all the float values will have 3 values after decimal

#### Task 1: Create a NumPy array of 1000 movie IDs starting from 1301
movie_id = np.arange(1301,2301)
print(movie_id[:10])
movie_id.size

user_id = []
for i in range(20201,20301):
  user_id.append(i)
user_id = np.array(user_id)
user_id.size #checking the number of elements in numpy array
user_id

#### Task 2: Create a matrix movies_matrix, to store users rating such that
    #- There are 100 users
    #- Each user can review as many movies as they want
    #- The review should be in between 0 to 10 (both inclusive)
    #- The movies which are not reviewed by a user should have value -1

import random
movie_matrix = []
for user in range(100):
  movies_rated_by_me = np.full(1000,-1)
  num_movies_rated = random.randint(0,999)
  #random.seed(num_movies_rated)
  movies_that_i_will_rate = random.sample(range(0,1000),num_movies_rated)
  #user rating for movies they chosed to rate
  for index in movies_that_i_will_rate:
    movies_rated_by_me[index] = random.randint(0,10)
  movie_matrix.append(movies_rated_by_me)

type(movie_matrix)

len(movie_matrix)

movie_matrix[:3]

movie_matrix = np.array(movie_matrix)

## Attributes of the numpy ndarray class
print(movie_matrix)
print('Shape of the array',movie_matrix.shape) #100 users(rows) and 1000 movies(columns)
print('Number of elements in the array',movie_matrix.size)
print('Number of dimensions in the array',movie_matrix.ndim)

#### Task 3: Add the reviews of 10 movie experts and 50 more movies

#Expert movie reviews

expert_matrix = []
for user in range(10):
  movies_rated_by_me = np.full(1000,-1)
  num_movies_rated = random.randint(0,999)
  #random.seed(num_movies_rated)
  movies_that_i_will_rate = random.sample(range(0,1000),num_movies_rated)
  #user rating for movies they chosed to rate
  for index in movies_that_i_will_rate:
    movies_rated_by_me[index] = random.randint(0,10)
  expert_matrix.append(movies_rated_by_me)
expert_matrix = np.array(expert_matrix)
print(expert_matrix.shape)
expert_matrix

#adding these expert reviews with original reviews
movie_matrix = np.vstack([movie_matrix,expert_matrix]) # vstack is used to stack arrays vertically
movie_matrix.shape

new_movies_matrix = []
for user in range(110):
  movies_rated_by_me = np.full(50,-1)
  num_movies_rated = random.randint(0,49)
  #random.seed(num_movies_rated)
  movies_that_i_will_rate = random.sample(range(0,50),num_movies_rated)
  #user rating for movies they chosed to rate
  for index in movies_that_i_will_rate:
    movies_rated_by_me[index] = random.randint(0,10)
  new_movies_matrix.append(movies_rated_by_me)
new_movies_matrix = np.array(new_movies_matrix)
print(new_movies_matrix.shape)
new_movies_matrix

new_movies_id = np.append(movie_id,np.arange(2301,2351))
new_movies_id.size

#adding the reviews of new movies with original reviews
movie_matrix = np.hstack([movie_matrix,new_movies_matrix]) # hstack is used to stack arrays horizontally
print(movie_matrix.shape) #100 users + 10 experts(rows) and 1000 + 50 movies(columns

#### Task 4: Create final_movie_rating matrix with four columns i.e.,
#- 'Movie ID'
#- 'Average rating'
#- 'Number of ratings'
#- 'Standard deviation of ratings'

final_movie_rating = []
for i in range(1050):
  #each movie's rating
  m = movie_matrix[:,i] # taking all rows and the ith column
  m = m[m>=0]
  #total_rate = m.sum()
  total_num_rating = m.size
  rating = m.mean()
  standard_deviation = m.std()
  final_movie_rating.append([new_movies_id[i],rating,total_num_rating,standard_deviation])

final_movie_rating = np.array(final_movie_rating)
final_movie_rating

"""#### Task 5: Convert the final movie ratings to have range from 0 to 10, such that the minimum rating converts to 0 and maximum to 10, and the other values in between"""

#Converting the average of movie ratings to have the range 0 to 10
x = final_movie_rating[:,1]
old_range = x.max()-x.min()
new_range = (10 - 0)
final_movie_rating[:,1] = ((x - x.min())*(new_range/old_range) + 0)
final_movie_rating

final_movie_rating.shape

#### Task 6: Display the movies rating-wise, highest to lowest

sorted_films = final_movie_rating[final_movie_rating[:,1].argsort()[::-1]]

print(sorted_films)
