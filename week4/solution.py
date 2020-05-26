from tempfile import gettempdir


class File:

    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'w') as f:
            f.write('')

    def __add__(self, other):
        new_obj = File(self.read() + other.read())
        return new_obj

    def read(self):
        with open(self.file_path, 'r') as f:
            print(f.read())
        return f.read()

    def write(self, data):
        with open(self.file_path, 'w') as f:
            f.write(data)
            print(len(data))

def main():
    pass


if __name__ == '__main__':
    main()
