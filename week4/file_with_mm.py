import os.path
from tempfile import gettempdir
class File:

    def __init(self, file_path):
        self.file_path = file_path
        self.file_path = str.join(gettempdir(), self.file_path)
        with open(self.file_path, 'w') as f:
            f.write('')

    def read(self):
        pass

    def write(self):
        pass

if __name__ = '__main__':
    main()