import os.path
import tempfile

class File:

    def __init__(self, file_path, value=None):
        self.file_path = file_path
        self.value = value or ''
        with open(self.file_path, 'w') as f:
            f.write(self.value)

    def __add__(self, other):
        new_obj = File(str.join(tempfile.gettempdir(), 'new_file'), self.value + other.value)
        print(new_obj)
        return new_obj

    def __str__(self):
        return self.file_path

    def read(self):
        with open(self.file_path, 'r') as f:
            self.value = f.read()
            return self.value

    def write(self, data):
        with open(self.file_path, 'w') as f:
            f.write(data)
            print(len(data))
            return f.write(data)

path_to_file = 'some_filename'
file_obj = File(path_to_file)
os.path.exists(path_to_file)
file_obj.read()
file_obj.write('some text')
file_obj.read()
file_obj.write('other text')
file_obj.read()
file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('line 1\n')
file_obj_2.write('line 2\n')
new_file_obj = file_obj_1 + file_obj_2


