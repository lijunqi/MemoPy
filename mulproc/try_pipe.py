import time
from multiprocessing import Process, Pipe

def f(conn):
    print('f: hi')
    conn.send([42, None, 'hello'])
    time.sleep(2)
    conn.send('hello')
    time.sleep(2)
    conn.send('exit')
    print('f: after sending exit')
    time.sleep(2)
    conn.close()
    print('f: after conn close')

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print('start')
    child_conn.close()
    print('parent recv...')
    while True:
        resp = parent_conn.recv()   # prints "[42, None, 'hello']"
        print("[Parent receive]", resp)
        if resp == 'exit':
            break
    p.join()
    print('Done.')