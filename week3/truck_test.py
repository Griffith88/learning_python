class Truck:

    def __init__(self, brand, photo_file_name, carrying, body_whl):

        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
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
