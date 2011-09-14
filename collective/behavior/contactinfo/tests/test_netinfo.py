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
        return contactinfo.NetContactInfo(dummy)
    #
    def test_email_setter(self):
        b = self._makeOne()
        b.email = u'info@email.org'
        self.assertEqual(u'info@email.org', b.context.email)
    #
    def test_twitter_setter(self):
        b = self._makeOne()
        b.twitter = u'foo'
        self.assertEqual(u'foo', b.context.twitter)
    #
    def test_irc_nickname_setter(self):
        b = self._makeOne()
        b.irc_nickname = u'foobar'
        self.assertEqual(u'foobar', b.context.irc_nickname)
    #
    def test_site_setter(self):
        b = self._makeOne()
        b.site = u'http://www.plone.org'
        self.assertEqual(u'http://www.plone.org', b.context.site)
