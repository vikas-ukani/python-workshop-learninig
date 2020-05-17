import multiprocessing
import queue

in_queue = queue.Queue()
out_queue = queue.Queue()


def square_mp(in_queue, out_queue):
    while True:
        n = in_queue.get()
        if n == 'STOP':
            return

        n_squared = n**2
        out_queue.put(n_squared)


if __name__ == '__main__':
    process = multiprocessing.Process(
        target=square_mp,
        args=(in_queue, out_queue))
    process.start()

    for i in range(10):
        in_queue.put(i)
        i_squared = out_queue.get()
        print(i, " square is  ", i_squared)
    process.terminate()
