#!/usr/bin/python

# movieId,title,genres


import sys


def mapper():

    rowid = 0
    for line in sys.stdin:
        # skipped header in
        if rowid > 0:
            data = line.strip().split(",")
            if len(data) == 3:
                movieID, title, genre = data
                data2 = genre.split("|")
                for item in data2:
                    print("{}\t{}".format(item, movieID))
        rowid += 1


if __name__ == "__main__":
    mapper()
