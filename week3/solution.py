from os.path import splitext
import csv


class CarBase:
    valid_list = ['.jpg', '.jpeg', '.png', '.gif']
    csv_car_type = 0
    csv_brand = 1
    csv_passenger_seats_count = 2
    csv_photo_file_name = 3
    csv_body_whl = 4
    csv_carrying = 5
    csv_extra = 6

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        if self.brand == '':
            raise ValueError('Brand пустой')
        if self.get_photo_file_ext() not in self.valid_list:
            raise ValueError('Фотография должна быть с расширением jpeg,jpg,png или gif!')

    def get_photo_file_ext(self):
        return splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    @classmethod
    def from_csv(cls, row):
        return cls(
            row[cls.csv_brand],
            row[cls.csv_photo_file_name],
            row[cls.csv_carrying],
            row[cls.csv_passenger_seats_count],
        )


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

        try:
            raw_body_whl = body_whl.split('x', 2)
            body_length = float(raw_body_whl[0])
            body_width = float(raw_body_whl[1])
            body_height = float(raw_body_whl[2])

        except ValueError:
            body_length = 0
            body_width = 0
            body_height = 0

        self.body_length = float(body_length)
        self.body_width = float(body_width)
        self.body_height = float(body_height)

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length

    @classmethod
    def from_csv(cls, row):
        return cls(
            row[cls.csv_brand],
            row[cls.csv_photo_file_name],
            row[cls.csv_carrying],
            row[cls.csv_body_whl],
        )


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        if self.extra == '':
            raise ValueError('Extra дожна быть не пустой')

    @classmethod
    def from_csv(cls, row):
        return cls(
            row[cls.csv_brand],
            row[cls.csv_photo_file_name],
            row[cls.csv_carrying],
            row[cls.csv_extra],
        )


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)

        dict_creation = {car_class.car_type: car_class for car_class in (Car, Truck, SpecMachine)}

        for row in reader:
            try:
                car_type = row[CarBase.csv_car_type]
                car_class = dict_creation[car_type]
                car_list.append(car_class.from_csv(row))
            except (IndexError, KeyError, ValueError):
                pass
        print(car_list)
        return car_list

if __name__ == '__main__':
    get_car_list('coursera_week3_2_cars.csv')
