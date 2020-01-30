import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s:\n%(message)s')

file_handler = logging.FileHandler('employee.log')
# file_handler.setLevel(logging.ERROR)  # only log record for error e.g logger.error('Tried to divide by zero')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('rt', 'Smith')
emp_2 = Employee('Oorey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')


class SMLogger:

    def __init__(self, source, log_name):
        self.source = source
        logger = logging.getLogger(source)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
        file_handler = logging.FileHandler(log_name)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

class NewLogger:

    def __init__(self, source, log_name):
        self.source = source
        logger = logging.getLogger(source)
        logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', filename=log_name,
                            filemode='w', level=logging.DEBUG)
        logger.info(' : Starting new task: ')


test1 = NewLogger('Hello', 'test.log')
