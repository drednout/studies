"""This module parses the contents of the file '/etc/passwd' and
returns a list whose elements are dictionaries with keys.

Examples:
    import passwd_parser

    res = passwd_parser.read_passwd(file_path)

"""

FILE_NAME = '/etc/passwd'
LIST_KEYS = [
    'login',
    'passwd',
    'user_id',
    'group_id',
    'comment',
    'home',
    'interpreter'
]

LEN_LINE = 7


class BaseModuleException(Exception):
    """This base class for all exceptions in this module
    """
    pass


class ParserException(BaseModuleException):
    """Exceptions generated by the transmission of incorrect data
    """
    pass


def _parser_passwd(passwd_line):
    """This function parses the contents of strings based on a
    delimiter ':' and returns a dictionaries with keys:
        login, passwd, user_id, group_id, comment, home, interpreter

    >>> res = _parser_passwd('root:x:0:0:root:/root:/bin/bash')
    >>> res['comment'] == 'root', res['home'] == '/root'
    (True, True)
    >>> res['group_id'] ==  '0', res['user_id'] == '0'
    (True, True)
    >>> res['interpreter'] == '/bin/bash', res['login'] == 'root'
    (True, True)
    >>> res['passwd'] == 'x'
    True
    >>> res = _parser_passwd(u'root:x:0:0:root:/root:/bin/bash')
    >>> res['comment'] == 'root', res['home'] == '/root'
    (True, True)
    >>> res['group_id'] ==  '0', res['user_id'] == '0'
    (True, True)
    >>> res['interpreter'] == '/bin/bash', res['login'] == 'root'
    (True, True)
    >>> res['passwd'] == 'x'
    True
    >>> _parser_passwd(-1)
    Traceback (most recent call last):
        ...
    ParserException: passwd_line must be str
    >>> _parser_passwd({})
    Traceback (most recent call last):
        ...
    ParserException: passwd_line must be str
    """
    if isinstance(passwd_line, unicode):
        passwd_line = passwd_line.encode()

    if not isinstance(passwd_line, str):
        raise ParserException('passwd_line must be str')

    line = passwd_line.split(':')
    if len(line) != LEN_LINE:
        raise ParserException('invalid format string')

    return dict(zip(LIST_KEYS, line))


def _str_to_int(number):
    """This function converts the number represented as a string in int.
    If this is not possible, the value doesn't change.

    >>> _str_to_int('0')
    0
    >>> _str_to_int('str')
    'str'
    >>> _str_to_int([])
    []
    """
    res = number
    try:
        res = int(number)
    except (ValueError, TypeError):
        pass
    return res


def read_passwd(file_path=FILE_NAME):
    """ This function reads the contents of file '/etc/passwd' and
    returns a list whose elements are dictionaries.

    >>> res = read_passwd('tests/passwd')
    >>> isinstance(res, list)
    True
    >>> res[0]['login'] == 'root'
    True
    >>> read_passwd('file')
    Traceback (most recent call last):
        ...
    IOError: [Errno 2] No such file or directory: 'file'
    >>> read_passwd('tests/passwderror')
    Traceback (most recent call last):
        ...
    ParserException: id conversion from str to int: fail
    """
    res = []
    with open(file_path, 'r') as file_:
        for line in file_:
            dict_ = _parser_passwd(line.strip())
            dict_['user_id'] = _str_to_int(dict_['user_id'])
            dict_['group_id'] = _str_to_int(dict_['group_id'])
            if isinstance(dict_['user_id'], str) or \
                    isinstance(dict_['group_id'], str):
                raise ParserException('id conversion from str to int: fail')
            res.append(dict_)

    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
