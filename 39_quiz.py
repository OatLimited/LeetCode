from operator import le


class ScoreSheet:
    def __init__(self) -> None:
        self.scores = []

    def add_score(self, input_score: int):
        self.scores.append(input_score)

    def average(self):
        if len(self.scores) > 1:
            self.scores = sorted(self.scores)[1:]
        try:
            self.avg_score = sum(self.scores)/len(self.scores)
        except ZeroDivisionError as e:
            self.avg_score = 0

    def report(self):
        print(f'{'----':20}')
        print(f'{'score':^10}{self.scores}')
        print(f'{'average':^10}{self.avg_score}')

    def __str__(self) -> str:
        return f'{self.avg_score}'


def main():
    active = True
    scoresheet = ScoreSheet()
    user_scores = input("Input list of score: ").split()
    user_scores = [int(i) for i in user_scores]
    for i in user_scores:
        scoresheet.add_score(i)
    scoresheet.average()
    scoresheet.report()
    print(scoresheet)


if __name__ == "__main__":
    main()
