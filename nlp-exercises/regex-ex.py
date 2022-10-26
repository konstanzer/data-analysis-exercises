import re
import pandas as pd


def is_vowel(s):
    """Is it a vowel?
    Args:
        s: any string
    Out:
        True if s is a vowel (bool)
    """
    return bool(re.search(r'^[aeiou]$', s.lower()))


def is_valid_user(s):
    """Is string a good username?
    Args:
        s: any string
    Out:
        True if s is lowercase letters, numbers, and _
        and < 32 chars (bool)
    """
    return bool(re.search('^[a-z][a-z0-9_]{,31}$', s))

    
def capture_numbers(lst):
    """Capture phone numbers
    Args:
        list o strimgs
    Out:
        list of phone numbers
    """
    phone_regex = re.compile('''^
    (?P<country_code>\+\d+)?
    \D*?
    (?P<area_code>\d{3})?
    \D*?
    (?P<exchange_code>\d{3})
    \D*?
    (?P<line_number>\d{4})
    \D*
    $''', re.VERBOSE)
    lst.str.extract(phone_regex)
    
    return re.search(r'', lst).groups()
    
phone = ['(210) 867 5309','+1 210.867.5309','867-5309','210-867-5309']
print(is_valid_user(phone))


def change_dates(lst):
    """Standardize dates phone numbers
    Args:
        list of dates
    Out:
        list of Y-M-D dates 
    """
    r = r'(\d+)/(\d+)/(\d+)'
    return [re.sub(r, r'20\3-\1-\2',date) for date in lst]
    
dates = ['02/04/19','02/05/19','02/06/19','02/07/19']
print(change_dates(dates))


def parse_logs(logs):
    """Extract parts of logfiles.
    Args:
        list of logfiles
    Out:
        list of lists
    """
    r = r'''^
    (?P<method>GET|POST)
    \s
    (?P<path>/[/\w\-\?=]+)
    \s
    \[(?P<timestamp>.+)\]
    \s
    (?P<http_version>HTTP/\d+\.\d+)
    \s
    \{(?P<status_code>\d+)\}
    \s
    (?P<bytes>\d+)
    \s
    "(?P<user_agent>.+)"
    \s
    (?P<ip>\d+\.\d+\.\d+\.\d+)
    $'''
    return [re.search(r, l, re.VERBOSE).groupdict() for l in logs.strip().split('\n')]

logs = ['GET /api/v1/sales?page=86 [16/Apr/2019:193452+0000] HTTP/1.1 {200} 510348 "python-requests/2.21.0" 97.105.19.58',
        'POST /users_accounts/file-upload [16/Apr/2019:193452+0000] HTTP/1.1 {201} 42 "User-Agent: Mozilla/5.0 (X11; Fedora; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" 97.105.19.58',
        'GET /api/v1/items?page=3 [16/Apr/2019:193453+0000] HTTP/1.1 {429} 3561 "python-requests/2.21.0" 97.105.19.58']
print(parse_logs(logs))