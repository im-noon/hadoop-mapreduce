#!/usr/bin/python


def reducer():
    import sys

    num_movies = {}
    oldGenre = None
    oldMovie = None
    Movies = 0

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue

        genre, movieID = data
        if oldGenre and oldGenre != genre:
            num_movies[oldGenre] = Movies
            Movies = 0

        Movies += 1
        oldGenre = genre

    for key in sorted(num_movies, key=num_movies.get, reverse=True):
        print("{}\t{}".format(key, num_movies[key]))


if __name__ == "__main__":
    reducer()
