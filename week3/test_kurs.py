import requests
import argparse


class Valut:

    def __init__(self, country):
        self.country = country

    def get(self):
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        data = requests.get(url).json()
        valut_data = data["Valute"][self.country]
        valut = {
            "Country": valut_data['CharCode'],
            "CurrentRate": valut_data['Value'],
            "Name": valut_data['Name']
        }
        list_valut = []
        for val in valut.values():
            list_valut.append(val)
        return valut


def arg_p():
    parser = argparse.ArgumentParser()
    parser.add_argument('Country')
    args = parser.parse_args()
    return args.Country


def main():
    def_country = Valut(arg_p())
    pr_rate = def_country.get()
    # print(' '.join(str(x) for x in pr_rate))
    print(pr_rate)


if __name__ == '__main__':
    main()
