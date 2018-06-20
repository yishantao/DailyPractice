import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsecond):
    print('start loop', nloop, ctime())
    sleep(nsecond)
    print('end loop', nloop, ctime())


def main():
    print('start at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all Done at', ctime())


if __name__ == '__main__':
    main()
