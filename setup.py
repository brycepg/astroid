#!/usr/bin/env python
# pylint: disable=W0404,W0622,W0704,W0613
# copyright 2003-2013 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of astroid.
#
# astroid is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option) any
# later version.
#
# astroid is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with astroid.  If not, see <http://www.gnu.org/licenses/>.
"""Setup script for astroid."""
from setuptools import setup, find_packages

pkginfo = 'astroid/__pkginfo__.py'

with open(pkginfo, 'rb') as fobj:
    exec(compile(fobj.read(), pkginfo, 'exec'), locals())

with open('README') as fobj:
    long_description = fobj.read()


def install():
    return setup(name = distname,
                 version = version,
                 license = license,
                 description = description,
                 long_description = long_description,
                 classifiers = classifiers,
                 author = author,
                 author_email = author_email,
                 url = web,
                 include_package_data = True,
                 install_requires = install_requires,
                 packages = ['astroid', 'astroid.tests'],
                 )


if __name__ == '__main__' :
    install()
