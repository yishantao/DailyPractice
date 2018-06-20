import _thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsecond, lock):
    print('start loop', nloop, ctime())
    sleep(nsecond)
    print('end loop', nloop, ctime())
    """每个线程将被分配到一个已获得的锁，当sleep时间到了，释放对应的锁，向主线程表明该线程已经完成"""
    lock.release()


def main():
    print('start at:', ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        # 得到锁对象
        lock = _thread.allocate_lock()
        # 取得每个锁，效果相当于“把锁锁上”
        lock.acquire()
        # 一旦锁被锁上，就可以把它添加到所列表locks中
        locks.append(lock)

    for i in nloops:
        # 派生线程
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print('all Done at', ctime())


if __name__ == '__main__':
    main()
