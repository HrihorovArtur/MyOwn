from multiprocessing import Process
import os


def run_tests_in_parallel(tag):
    os.system('behave -f allure_behave.formatter:AllureFormatter -o allure-results'.format(tag))


if __name__ == '__main__':
    p1 = Process(target=run_tests_in_parallel, args=('@thread1', ))
    p1.start()
    # p2 = Process(target=run_tests_in_parallel, args=('@thread2', ))
    # p2.start()
    # p3 = Process(target=run_tests_in_parallel, args=('@thread3', ))
    # p3.start()
    # p4 = Process(target=run_tests_in_parallel, args=('@thread4', ))
    # p4.start()
    # p5 = Process(target=run_tests_in_parallel, args=('@thread5', ))
    # p5.start()
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # p5.join()
