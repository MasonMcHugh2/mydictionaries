def main():
    movie_ratings = {'Inception': 8, 'Interstellar': 10, 'Memento': 9, 'Alien': 6, 'Dune': 10, 'Avatar': 8, 'Jaws': 6, 'Grease': 5}

    movie_title = input('Please enter a movie title: ')
    print()

    list_movies = list(movie_ratings)   
    
    recommend_movie(movie_ratings, movie_title, list_movies)

def recommend_movie(movie_ratings, movie_title, list_movies):
    good_movies = []
    for movie in movie_ratings:
        if movie_ratings[movie] >= 8:
            good_movies.append(movie)

    if movie_title.title() in list_movies:
        if movie_ratings[movie_title.title()] >= 8:
            print(f"The movie {movie_title.title()} has a rating of {movie_ratings[movie_title.title()]} so we recommend watching!")
        else:
            print(f"The movie {movie_title.title()} has a rating of {movie_ratings[movie_title.title()]} so we do not recommend watching.")
            print()
            print(f'Other movies we recommend are:')
            for movie in good_movies:
                print(movie, end = ' ')
    else:
        print(f'We could not find the movie {movie_title.title()}!')
        print()
        print('Movies we recommend are:')
        for movie in good_movies:
                print(movie, end = ' ')
  
main()
