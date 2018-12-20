
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

Table of Contents
-----------------
.. toctree::
   :maxdepth: 2
   :glob:

   *

