# -*- coding:utf-8 -*-
import unittest

from collective.behavior.contactinfo.behavior import contactinfo


class TestBehaviorFactory(unittest.TestCase):
    #
    def _makeOne(self):
        #
        class Dummy(object):
            pass
        dummy = Dummy()
        return contactinfo.PhoneContactInfo(dummy)
    #
    def test_phone_setter(self):
        b = self._makeOne()
        b.phone = u'551138982121'
        self.assertEqual(u'551138982121', b.context.phone)
    #
    def test_mobile_setter(self):
        b = self._makeOne()
        b.mobile = u'551138982121'
        self.assertEqual(u'551138982121', b.context.mobile)
