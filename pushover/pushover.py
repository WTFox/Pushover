#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)
try:
    #python 2
    from urllib2 import urlopen
    from urlparse import urljoin
    from urllib import urlencode
except ImportError:
    #python 3
    from urllib.request import urlopen
    from urllib.parse import urljoin, urlencode
import json
import os


PUSHOVER_API = "https://api.pushover.net/1/"


class PushoverError(Exception): pass


def pushover(**kwargs):
    assert 'message' in kwargs

    if not 'token' in kwargs:
        kwargs['token'] = os.environ['PUSHOVER_TOKEN']
    if not 'user' in kwargs:
        kwargs['user'] = os.environ['PUSHOVER_USER']

    url = urljoin(PUSHOVER_API, "messages.json")
    data = urlencode(kwargs)
    binary_data = data.encode('ascii')
    req = urlopen(url, binary_data)
    data = json.loads(req.read().decode('utf-8'))
    if data['status'] != 1:
        raise PushoverError(output)


if __name__ == "__main__":
    pass
