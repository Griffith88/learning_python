from os.path import splitext
import csv

class CarBase:
    valid_list = ['.jpg', '.jpeg', '.png']

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        if self.get_photo_file_ext() not in self.valid_list:
            raise ValueError('blalalal')

    def get_photo_file_ext(self):
        file_ext = splitext(self.photo_file_name)[1]
        return file_ext


class Car(CarBase):

    car_type = 'Car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        pass


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
    car_type = 'SpecMachine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        pass


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)

