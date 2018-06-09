from multiprocessing import Process, Queue
import time
import requests

link_list = ['https://www.baidu.com/', 'http://fanyi.youdao.com/', 'http://study.163.com/', 'https://www.imooc.com/',
             'http://www.abchina.com/cn/', 'https://www.baidu.com/', 'https://www.baidu.com/',
             'https://www.chunyuyisheng.com/']
start = time.time()


class MyProcess(Process):
    def __init__(self, q):
        Process.__init__(self)
        self.q = q

    def run(self):
        print('starting ', self.pid)
        while not self.q.empty():
            crawler(self.q)
        print('Exiting', self.pid)


def crawler(q):
    url = q.get(timeout=2)
    try:
        r = requests.get(url, timeout=20)
        print(q.qsize(), r.status_code, url)
    except Exception as e:
        print(q.qsize(), url, 'Error', e)


if __name__ == '__main__':
    ProcessName = ['Process-1', 'Process-2', 'Process-3']
    work_queue = Queue(1000)
    # 填充队列
    for url in link_list:
        work_queue.put(url)
    for i in range(0, 3):
        p = MyProcess(work_queue)
        p.daemon = True
        p.start()
        p.join()
    end = time.time()
    print('Process+Queue多进程爬虫的总时间为：', end - start)
    print('Main process Ended!')
