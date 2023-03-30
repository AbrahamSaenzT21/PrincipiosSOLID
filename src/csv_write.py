import csv


class CsvWriter:
    def __init__(self, movie_list):
        self.movie_list = movie_list

    def csv_write(self):
        fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
        with open("movie_results.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for movie in self.movie_list:
                writer.writerow({**movie})

