import time
from multiprocessing import Process, Pipe

def f(conn):
    print('hihi')
    conn.send([42, None, 'hello'])
    time.sleep(2)
    conn.send('hello')
    time.sleep(2)
    conn.send('exit')
    print('close')
    time.sleep(2)
    conn.close()
    print('close done')

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print('start')
    child_conn.close()
    while True:
        resp = parent_conn.recv()   # prints "[42, None, 'hello']"
        print(resp)
        if resp == 'exit':
            break
    p.join()
    print('Done.')