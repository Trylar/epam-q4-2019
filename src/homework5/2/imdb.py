from collections import Counter
import os


def count_and_write_to_file(filename, column):
    data = Counter([movie[column] for movie in movies_top250])
    min_data_num = min(data.values())
    max_data_num = max(data.values())
    max_len = len(str(max_data_num))
    max_len_value = max(len(str(key)) for key in data)
    data_order = sorted(data)
    with open(os.path.join("homework5", "2", "data", filename),
              "w") as data_file:
        for data_val in range(max_data_num, min_data_num - 1, -1):
            data_file.write(str(data_val).zfill(max_len))
            [data_file.write(max_len_value * " " + "#" if data[key] >= data_val
                             else (max_len_value + 1) * " ")
             for key in data_order]
            data_file.write("\n")
        data_file.write((max_len + 1) * " ")
        [data_file.write(" " + str(key)) for key in data_order]


movies_top250 = []
try:
    with open(os.path.join("homework5", "2", "data",
                           "ratings.list")) as rating_file:
        for i, line in enumerate(rating_file):
            if i == 27:  # read keys
                keys = line.split()
                keys.append("Year")
            elif 27 < i <= 277:  # read movies
                movie = [""] + line.strip().split(None, 3)
                movie = movie[:-1] + movie[-1].rsplit(" ", 1)  # separate year
                movie[-1] = movie[-1][1:5]  # delete braces
                movies_top250.append(dict(zip(keys, movie)))
            elif i > 277:  # 27+250
                break

        with open(os.path.join("homework5", "2", "data", "top250_movies.txt"),
                  "w") as titles_file:
            [titles_file.write(movie["Title"] + "\n") for movie in
             movies_top250]

        count_and_write_to_file("ratings.txt", "Rank")

        count_and_write_to_file("years.txt", "Year")
except Exception:
    print("File does not exist")