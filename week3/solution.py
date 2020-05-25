from os.path import splitext
import csv


class CarBase:
    valid_list = ['.jpg', '.jpeg', '.png', '.gif']

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        if self.get_photo_file_ext() not in self.valid_list:
            raise ValueError('Фотография должна быть с расширением jpeg,jpg,png или gif!')

    def get_photo_file_ext(self):
        return splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

        try:
            raw_body_whl = body_whl.split('x')
            body_length = float(raw_body_whl[0])
            body_width = float(raw_body_whl[1])
            body_height = float(raw_body_whl[2])

        except ValueError:
            body_length = 0
            body_width = 0
            body_height = 0

        self.body_length = body_length
        self.body_width = body_width
        self.body_height = body_height

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)
