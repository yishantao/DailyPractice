import threading
import requests
import time
import queue as Queue

start = time.time()

link_list = ['https://www.baidu.com/', 'http://fanyi.youdao.com/', 'http://study.163.com/', 'https://www.imooc.com/',
             'http://www.abchina.com/cn/', 'https://www.baidu.com/', 'https://www.baidu.com/',
             'https://www.chunyuyisheng.com/']


class myThread(threading.Thread):
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q

    def run(self):
        while True:
            try:
                crawler(self.name, self.q)
            except:
                break


def crawler(threadName, q):
    url = q.get(timeout=2)
    try:
        r = requests.get(url, timeout=20)
        print(q.qsize(), threadName, r.status_code, url)
    except Exception as e:
        print(q.qsize(), threadName, url, 'Error', e)


thread_list = ['Thread-1', 'Thread-2', 'Thread-3', 'Thread-4', 'Thread-5']
work_queue = Queue.Queue(1000)
threads = []

# 创建新线程
for tName in thread_list:
    thread = myThread(tName, work_queue)
    thread.start()
    threads.append(thread)

# 填充队列
for url in link_list:
    work_queue.put(url)

# 等待所有线程完成
for t in threads:
    t.join()

end = time.time()
print('Queue多线程爬虫的总时间为：', end - start)

