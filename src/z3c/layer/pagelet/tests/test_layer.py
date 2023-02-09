##############################################################################
#
# Copyright (c) 2007-2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Test Pagelet Layer
"""
import doctest
import unittest

import z3c.layer.pagelet.testing


def create_suite(*args, **kw):
    kw['optionflags'] = (
        doctest.NORMALIZE_WHITESPACE
        | doctest.ELLIPSIS
    )
    kw['globs'] = dict(
        getRootFolder=z3c.layer.pagelet.testing.TestLayer.getRootFolder,
        make_wsgi_app=z3c.layer.pagelet.testing.TestLayer.make_wsgi_app)
    suite = doctest.DocFileSuite(*args, **kw)
    suite.layer = z3c.layer.pagelet.testing.TestLayer
    return suite


def test_suite():
    suite = unittest.TestSuite((
        create_suite('../README.rst'),
        create_suite('bugfixes.rst'),
    ))
    return suite
