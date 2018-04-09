def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print("[CONSUMER] consuming %s " % r)
        r = '200 OK'

def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n+1
        print('[PRODUCER] producing %s ' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
producer(c)