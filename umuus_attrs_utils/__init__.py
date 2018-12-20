#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018  Jun Makii <junmakii@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""Utilities, tools, and scripts for Python.

umuus-attrs-utils
=================

Installation
------------

    $ pip install git+https://github.com/junmakii/umuus-attrs-utils.git

Example
-------

    $ umuus_attrs_utils

    >>> import umuus_attrs_utils

    >>> @attr.s()
    ... class A(object):
    ...     s = umuus_attrs_utils.ib(type=str)

    >>> @attr.s()
    ... class B(object):
    ...     a = umuus_attrs_utils.ib(type=A)

    >>> A(s=1)
    A(s='1')

    >>> B(a=dict(s=1))
    B(a=A(s='1'))

----

umuus_attrs_utils.converter
---------------------------

    >>> @attr.s()
    ... class C(object):
    ...     s = attr.ib(converter=umuus_attrs_utils.converter(type=str))

    >>> C(s=1)
    C(s='1')

Authors
-------

- Jun Makii <junmakii@gmail.com>

License
-------

GPLv3 <https://www.gnu.org/licenses/>

"""
import functools
import logging
logger = logging.getLogger(__name__)
import attr
import toolz
__version__ = '0.1'
__url__ = 'https://github.com/junmakii/umuus-attrs-utils'
__author__ = 'Jun Makii'
__author_email__ = 'junmakii@gmail.com'
__author_username__ = 'junmakii'
__keywords__ = []
__license__ = 'GPLv3'
__scripts__ = []
__install_requires__ = [
    'attrs>=18.2.0',
    'toolz>=0.9.0',
]
__dependency_links__ = []
__classifiers__ = []
__entry_points__ = {}
__project_urls__ = {}
__setup_requires__ = []
__test_suite__ = 'umuus_attrs_utils'
__tests_require__ = []
__extras_require__ = {}
__package_data__ = {}
__python_requires__ = ''
__include_package_data__ = True
__zip_safe__ = True
__static_files__ = {}
__extra_options__ = {}
__all__ = []


def ib(default=attr.NOTHING, patterns=[], type=None):
    return attr.ib(
        default=default,
        type=type,
        converter=functools.partial(converter, type=type))


@toolz.curry
def converter(_, type):
    if isinstance(_, type):
        return _
    elif (not issubclass(type, dict) and isinstance(_, dict)):
        return type(**_)
    else:
        return type(_)
