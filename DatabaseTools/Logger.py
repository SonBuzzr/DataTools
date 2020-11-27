# Module for generating a log file

import logging


class SMLogger:

    def __init__(self, source, log_name, file_name):
        self.source = source

        logger = logging.getLogger(source)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')

        # file_handler.setLevel(logging.ERROR)  # only log record for error e.g logger.error('Tried to divide by zero')
        file_handler = logging.FileHandler(log_name)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    def handle_request(file_name):
        logger.info('Processing file: {} '.format(file_name))
        logger.warning('Hello')


# names = ['Ram', 'Sita', 'Gita']
#
# for name in names:
#     print(name)
#     SMLogger(name, 'myteslogo.log', 'hello.csv')


SMLogger('DataConnect', 'FreshError.log', 'file2.csv')
n = SMLogger("Logger Test", 'FError.log', 'file999.csv')
n.info("NEW test")

# new1 = SMLogger('DataConnect', 'Error.log', 'file2.csv')
# ne1w = SMLogger('DataConnect', 'Error.log', 'file2.csv')

class Test:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def show(self):
        print("hello ", self.name)


class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee {}".format(self.Employee.empCount))

    def displayEmployee(self):
        print("Name : {}, Salary : {}".format(self.name, self.salary))


# emp1 = Employee('Ram', 5000)
# emp2 = Employee('Hari', 6000)
# emp3 = Employee('Sita', 10000)
#
# emp2.displayEmployee()

class MyLogger:
    def __init__(self, source, log_name):
        self.source = source
        self.log_name = log_name

        logger = logging.getLogger(self.source)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
