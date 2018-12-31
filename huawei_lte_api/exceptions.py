class ResponseErrorException(Exception):
    def __init__(self, message, code):
        super(ResponseErrorException, self).__init__(message)
        self.code = code


class ResponseErrorNotSupportedException(ResponseErrorException):
    pass


class ResponseErrorLoginRequiredException(ResponseErrorException):
    pass


class ResponseErrorSystemBusyException(ResponseErrorException):
    pass


class ResponseErrorLoginCsrfException(ResponseErrorException):
    pass


# Deprecated misspelling
ResponseErrorLoginCsfrException = ResponseErrorLoginCsrfException


class LoginErrorUsernameWrongException(ResponseErrorException):
    pass


class LoginErrorPasswordWrongException(ResponseErrorException):
    pass


class LoginErrorAlreadyLoginException(ResponseErrorException):
    pass


class LoginErrorUsernamePasswordWrongException(ResponseErrorException):
    pass


class LoginErrorUsernamePasswordOverrunException(ResponseErrorException):
    pass


class LoginErrorUsernamePasswordModifyException(ResponseErrorException):
    pass
