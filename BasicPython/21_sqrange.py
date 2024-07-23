
def sqrange(n):
    for i in range(1,n+1):
        yield i*i

def main():
    for s in sqrange(10):
        print(s)

if __name__ == '__main__':
    main()