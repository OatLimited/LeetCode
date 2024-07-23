import pickle
from numpy import place, record


class Place:
    def __init__(self) -> None:
        self.passport = {}

    def record(self, name, latitude, longtitude, visited_date):
        self.passport['name'] = name
        self.passport['latitude'] = latitude
        self.passport['longtitude'] = longtitude
        self.passport['date'] = visited_date

    def get_record(self):
        return self.passport


class TravelBook:
    def __init__(self) -> None:
        self.book = []

    def add_book(self, data):
        self.book.append(data)

    def save_book(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.travel = pickle.load(f)
            self.travel.extend(self.book)
            with open(filename, 'wb') as f:
                pickle.dump(self.travel, f)
        except:
            with open(filename, 'wb') as f:
                pickle.dump(self.book, f)
            self.travel = self.book

    def get_record(self):
        return self.travel


def main():
    place = Place()
    travelbook = TravelBook()
    print(f'{'----'*20}')
    print(f'{"Welcome to Travel book recorder":^80}')
    print(f'{'----'*20}')
    print(f'Press q to exit')
    while True:
        print(f'{'----'*20}')
        name = input('Enter name (Press q to exit): ')
        if name == 'q':
            break
        try:
            latlong = input("Enter lat, long : ").split()
            latitude, longtitude = latlong
        except:
            print("Please input latitude and longtitude with spec")
            continue
        date = input("Enter date : ")
        place.record(name, latitude, longtitude, date)
        data = place.get_record()
        travelbook.add_book(data)
        travelbook.save_book('travelbook.dat')
        for i in travelbook.get_record():
            for k, y in i.items():
                print(f'{k} : {y}')


if __name__ == "__main__":
    main()
