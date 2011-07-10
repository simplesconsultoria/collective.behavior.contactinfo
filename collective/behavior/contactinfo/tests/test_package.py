# -*- coding:utf-8 -*-
import unittest
import transaction
from Testing.ZopeTestCase import app, close, installProduct, installPackage
from zope.interface import implements, Interface
from zope.component import getUtility, getMultiAdapter
from Products.CMFCore.utils import getToolByName
from plone.app.dexterity.tests.base import DexterityFunctionalTestCase

from Products.PloneTestCase.setup import default_user
from Products.PloneTestCase.layer import PloneSite
from zope.app.component.hooks import setSite, setHooks
from DateTime import DateTime

import collective.behavior.contactinfo

# BBB Zope 2.12
try:
    from Zope2.App import zcml
    from OFS import metaconfigure
    zcml # pyflakes
    metaconfigure
except ImportError:
    from Products.Five import zcml
    from Products.Five import fiveconfigure as metaconfigure

class TestCase(DexterityFunctionalTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            metaconfigure.debug_mode = True
            import plone.app.dexterity
            zcml.load_config('meta.zcml', plone.app.dexterity)
            zcml.load_config('configure.zcml', plone.app.dexterity)
            zcml.load_config('configure.zcml', collective.behavior.contactinfo)
            metaconfigure.debug_mode = False

            # import the default profile
            root = app()
            portal = root.plone
            setHooks()
            setSite(portal)
            tool = getToolByName(portal, 'portal_setup')
            profile = 'profile-plone.app.dexterity:default'
            tool.runAllImportStepsFromProfile(profile, purge_old=False)
            setSite(None)
            # and commit the changes
            transaction.commit()
            close(root)

        @classmethod
        def tearDown(cls):
            pass

def test_suite():
    from unittest import TestSuite, makeSuite
    from Testing import ZopeTestCase as ztc
    suite = unittest.TestSuite([ztc.FunctionalDocFileSuite(
                'netcontactinfo.txt', package='collective.behavior.contactinfo.docs',
                test_class=TestCase),
            ztc.FunctionalDocFileSuite(
                'phonecontactinfo.txt', package='collective.behavior.contactinfo.docs',
                test_class=TestCase),
            ztc.FunctionalDocFileSuite(
                'address.txt', package='collective.behavior.contactinfo.docs',
                test_class=TestCase),])

    return suite
