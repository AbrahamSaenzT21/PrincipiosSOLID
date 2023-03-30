from movie_data import MovieData
from csv_write import CsvWriter


def main():
    movie_data = MovieData()
    movie_list = movie_data.movie_data()

    csv_writer = CsvWriter(movie_list)
    csv_writer.csv_write()


if __name__ == '__main__':
    main()
