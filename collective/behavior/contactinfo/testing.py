# -*- coding: utf-8 -*-

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.behavior.contactinfo
        self.loadZCML(package=collective.behavior.contactinfo)
    
    def setUpPloneSite(self, portal):
        # Setup Plone Site -- install dexterity
        self.applyProfile(portal, 'plone.app.dexterity:default')

FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='collective.behavior.contactinfo:Integration',
    )
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='collective.behavior.contactinfo:Functional',
    )
