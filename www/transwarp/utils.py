#!/usr/bin/env python
# coding:utf-8
import urllib


def to_str(s):
    if isinstance(s, str):
        return s
    if isinstance(s, unicode):
        return s.encode('utf-8')
    return str(s)


def to_unicode(s, encoding='utf-8'):
    return s.decode('utf-8')


def quote(s, encoding='utf-8'):
    '''
    Url quote as str.
    >>> quote('http://example/test?a=1+')
    'http%3A//example/test%3Fa%3D1%2B'
    >>> quote(u'hello world!')
    'hello%20world%21'
    '''
    if isinstance(s, unicode):
        s = s.encode(encoding)
    return urllib.quote(s)


def unquote(s, encoding='utf-8'):
    '''
    Url unquote as unicode.
    >>> unquote('http%3A//example/test%3Fa%3D1+')
    u'http://example/test?a=1+'
    '''
    return urllib.unquote(s).decode(encoding)


def _unquote_plus(s, encoding='utf-8'):
    '''
    Url unquote_plus as unicode.
    >>> _unquote_plus('http%3A//example/test%3Fa%3D1+')
    u'http://example/test?a=1 '
    '''
    return urllib.unquote_plus(s).decode(encoding)