import os.path
import tempfile


class File:

    def __init__(self, file_path, value=None):
        self.file_path = file_path
        self.value = value or ''
        if os.path.exists(self.file_path):
            open(self.file_path).close()
        else:
            with open(self.file_path, 'w') as f:
                f.write(self.value)

    def __add__(self, other):
        file_dir = tempfile.NamedTemporaryFile(delete=False).name
        #fd, file_dir = tempfile.mkstemp()
        print(f'Впишем эти значения {self.read()} и {other.read()}')
        new_obj = File(file_dir)
        with open(file_dir, 'w') as f:
            f.write(self.read() + other.read())
        return new_obj

    def __str__(self):
        return self.file_path

    def __iter__(self):
        with open(self.file_path, 'r') as f:
            self.line_list = f.readlines()
        self.start_line = 0
        return self

    def __next__(self):

        if self.start_line == len(self.line_list):
            raise StopIteration
        line_c = self.line_list[self.start_line]
        self.start_line += 1
        return line_c

    def read(self):
        with open(self.file_path, 'r') as f:
            self.value = f.read()
            print(self.value)
            return self.value

    def write(self, data):
        with open(self.file_path, 'w') as f:
            f.write(data)
            print(len(data))

# path_to_file = 'some_filename'
# file_obj = File(path_to_file)
# os.path.exists(path_to_file)
# file_obj.read()
# file_obj.write('some text')
# file_obj.read()
# file_obj.write('other text')
# file_obj.read()
# file_obj_1 = File(path_to_file + '_1')
# file_obj_2 = File(path_to_file + '_2')
# file_obj_1.write('line 1\n')
# file_obj_2.write('line 2\n')
# new_file_obj = file_obj_1 + file_obj_2
# print(new_file_obj)
# print(isinstance(new_file_obj, File))
# for line in new_file_obj:
#     print(ascii(line))
