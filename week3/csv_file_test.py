import csv


def get_car_list(csv_filename):

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)


if __name__ == '__main__':
    get_car_list('coursera_week3_cars.csv')
