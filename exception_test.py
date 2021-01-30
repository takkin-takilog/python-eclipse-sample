from oandapyV20.exceptions import V20Error
from requests.exceptions import ConnectionError, ReadTimeout


class ExampleErrorException(Exception):

    def __init__(self, errno, msg):
        self.errno = errno
        self.msg = msg
        super().__init__(msg)


def occur_error(no):

    if no == 1:
        raise V20Error(100, "V20Error Occurred")
    elif no == 2:
        raise ConnectionError(200, "ConnectionError Occurred")
    elif no == 3:
        raise ReadTimeout(300, "ReadTimeout Occurred")
    elif no == 4:
        raise Exception(400, "Exception Occurred")


def error_process(no):

    try:
        occur_error(no)
    except V20Error as err:
        raise ExampleErrorException(err.code, err.msg)
    except ConnectionError as err:
        raise ExampleErrorException(err.errno, err.strerror)
    except ReadTimeout as err:
        raise ExampleErrorException(err.errno, err.strerror)
    except Exception as err:
        raise ExampleErrorException(err.args[0], err.args[1])


if __name__ == '__main__':

    for i in range(5):
        try:
            print("----- process no:[{}]".format(i))
            error_process(i)
        except ExampleErrorException as err:
            print("Error Occurred: errno:[{}] errmsg:[{}]".format(err.errno, err.msg))
