import json
import argparse
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()


def put_data_in_file(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))



def get_data():
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            read_data = f.read()
            if read_data:
                js_data = json.loads(read_data)
                return js_data
            else:
                return {}
    else:
        return {}


if args.key and args.val:
    put_data_in_file(args.key, args.val)
elif args.key:
    js_data = get_data()
    if args.key in js_data:
        print(str.join(', ', js_data[args.key]))
    else:
        print(None)

