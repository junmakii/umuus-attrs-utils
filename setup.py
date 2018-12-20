
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def run_tests(self):
        import sys
        import shlex
        import pytest
        errno = pytest.main(['--doctest-modules'])
        if errno != 0:
            raise Exception('An error occured during installution.')
        install.run(self)


setup(
    packages=setuptools.find_packages('.'),
    version='0.1',
    url='https://github.com/junmakii/umuus-attrs-utils',
    author='Jun Makii',
    author_email='junmakii@gmail.com',
    keywords=[],
    license='GPLv3',
    scripts=[],
    install_requires=['attrs>=18.2.0', 'toolz>=0.9.0'],
    dependency_links=[],
    classifiers=[],
    entry_points={},
    project_urls={},
    setup_requires=[],
    test_suite='umuus_attrs_utils',
    tests_require=[],
    extras_require={},
    package_data={},
    python_requires='',
    include_package_data=True,
    zip_safe=True,
    name='umuus-attrs-utils',
    description='Utilities, tools, and scripts for Python.',
    long_description=('Utilities, tools, and scripts for Python.\n'
 '\n'
 'umuus-attrs-utils\n'
 '=================\n'
 '\n'
 'Installation\n'
 '------------\n'
 '\n'
 '    $ pip install git+https://github.com/junmakii/umuus-attrs-utils.git\n'
 '\n'
 'Example\n'
 '-------\n'
 '\n'
 '    $ umuus_attrs_utils\n'
 '\n'
 '    >>> import umuus_attrs_utils\n'
 '\n'
 '    >>> @attr.s()\n'
 '    ... class A(object):\n'
 '    ...     s = umuus_attrs_utils.ib(type=str)\n'
 '\n'
 '    >>> @attr.s()\n'
 '    ... class B(object):\n'
 '    ...     a = umuus_attrs_utils.ib(type=A)\n'
 '\n'
 '    >>> A(s=1)\n'
 "    A(s='1')\n"
 '\n'
 '    >>> B(a=dict(s=1))\n'
 "    B(a=A(s='1'))\n"
 '\n'
 '----\n'
 '\n'
 'umuus_attrs_utils.converter\n'
 '---------------------------\n'
 '\n'
 '    >>> @attr.s()\n'
 '    ... class C(object):\n'
 '    ...     s = attr.ib(converter=umuus_attrs_utils.converter(type=str))\n'
 '\n'
 '    >>> C(s=1)\n'
 "    C(s='1')\n"
 '\n'
 'Authors\n'
 '-------\n'
 '\n'
 '- Jun Makii <junmakii@gmail.com>\n'
 '\n'
 'License\n'
 '-------\n'
 '\n'
 'GPLv3 <https://www.gnu.org/licenses/>'),
    cmdclass={"pytest": PyTest},
)
