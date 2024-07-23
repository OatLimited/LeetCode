class Wage:
    def __init__(self, hours=0.0, rate=0.0) -> None:
        self.hours = float(hours)
        self.rate = float(rate)

    def payment(self):
        if self.hours > 40:
            return ((40 * self.rate)+((self.hours - 40) * self.rate * 1.5))
        return (self.hours * self.rate)


class Worker:
    def __init__(self, name, rate) -> None:
        self.name = name
        self.rate = rate
        self.total_hours = 0

    def work(self, hours):
        self.total_hours += hours

    def total_working_hours(self):
        return self.total_hours

    def payment(self):
        wage = Wage(self.total_hours, self.rate)
        return wage.payment()


def main():
    name = input("Name : ")
    rate = input('Rate : ')
    worker = Worker(name, rate)
    for i in range(4):
        working = int(input(f"Week {i} > Work hours : "))
        worker.work(working)
    print(worker.payment())


if __name__ == "__main__":
    main()
