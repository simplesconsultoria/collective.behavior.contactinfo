# -*- coding:utf-8 -*-

import unittest2 as unittest
import doctest

from plone.testing import layered

from collective.behavior.contactinfo.testing import FUNCTIONAL_TESTING

optionflags = doctest.REPORT_ONLY_FIRST_FAILURE


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('docs/address.txt',
                                     package='collective.behavior.contactinfo',
                                     optionflags=optionflags),
                layer=FUNCTIONAL_TESTING),
        layered(doctest.DocFileSuite('docs/netcontactinfo.txt',
                                     package='collective.behavior.contactinfo',
                                     optionflags=optionflags),
                layer=FUNCTIONAL_TESTING),
        layered(doctest.DocFileSuite('docs/phonecontactinfo.txt',
                                     package='collective.behavior.contactinfo',
                                     optionflags=optionflags),
                layer=FUNCTIONAL_TESTING),
        ])
    return suite