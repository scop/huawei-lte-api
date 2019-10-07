import enum


@enum.unique
class PasswordTypeEnum(enum.IntEnum):
    BASE_64 = 0
    SHA256 = 4


# not @enum.unique as long as the deprecated ORERRUN spelling is there
class LoginErrorEnum(enum.IntEnum):
    USERNAME_WRONG = 108001
    PASSWORD_WRONG = 108002
    ALREADY_LOGIN = 108003
    USERNAME_PWD_WRONG = 108006
    USERNAME_PWD_OVERRUN = 108007
    """Deprecated misspelling, use USERNAME_PWD_OVERRUN instead."""
    USERNAME_PWD_ORERRUN = USERNAME_PWD_OVERRUN
    USERNAME_PWD_MODIFY = 115002


@enum.unique
class LoginStateEnum(enum.IntEnum):
    LOGGED_IN = 0
    LOGGED_OUT = -1
    REPEAT = -2


@enum.unique
class SessionErrorEnum(enum.IntEnum):
    VOICE_BUSY = 120001
    WRONG_TOKEN = 125001
    WRONG_SESSION = 125002
    WRONG_SESSION_TOKEN = 125003
