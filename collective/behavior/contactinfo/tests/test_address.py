# -*- coding:utf-8 -*-
import unittest


class TestBehaviorFactory(unittest.TestCase):
    #
    def _makeOne(self):
        #
        class Dummy(object):
            pass
        dummy = Dummy()
        from collective.behavior.contactinfo.behavior.address import Address
        return Address(dummy)
    #
    def test_address_setter(self):
        b = self._makeOne()
        b.address = u'R. dos Pinheiros 836 cj.6'
        self.assertEqual(u'R. dos Pinheiros 836 cj.6', b.context.address)
    #
    def test_city_setter(self):
        b = self._makeOne()
        b.city = u'São Paulo'
        self.assertEqual(u'São Paulo', b.context.city)
    #
    def test_state_setter(self):
        b = self._makeOne()
        b.state = u'São Paulo'
        self.assertEqual(u'São Paulo', b.context.state)
    #
    def test_country_setter(self):
        b = self._makeOne()
        b.country = u'br'
        self.assertEqual(u'br', b.context.country)
    #
    def test_postcode_setter(self):
        b = self._makeOne()
        b.postcode = u'05422-001'
        self.assertEqual(u'05422-001', b.context.postcode)
    #
    def test_latitude_setter(self):
        b = self._makeOne()
        b.latitude = -23.56645
        self.assertEqual(-23.56645, b.context.latitude)
    #
    def test_longitude_setter(self):
        b = self._makeOne()
        b.longitude = -46.68612
        self.assertEqual(-46.68612, b.context.longitude)
    #
    def test_latlong(self):
        b = self._makeOne()
        b.latitude = -23.56645
        b.longitude = -46.68612
        self.assertEqual((-23.56645,-46.68612), b.latlong)
