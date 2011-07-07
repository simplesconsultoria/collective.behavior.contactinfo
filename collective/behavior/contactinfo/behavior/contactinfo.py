from zope.interface import alsoProvides
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from collective.behavior.contactinfo import MessageFactory as _

class INetContactInfo(form.Schema):
   """
      Marker/Form interface for an Internet set of contact information
   """
   
   email = schema.TextLine(
       title=_(u'E-mail'),
       description=_(u'Please provide an email address'),
       required=False,
       )

   twitter = schema.TextLine(
       title=_(u'Twitter'),
       description=_(u'Please provide your Twitter name, if you have one.'),
       required=False,
       )

   irc_nickname = schema.TextLine(
       title=_(u'IRC Nickname'),
       description=_(u'Please provide your IRC nickname, if you have one.'),
       required=False,
       )

   site = schema.URI(
       title=_(u'Site'),
       description=_(u'Please provide the address of your site, blog or profile'),
       required=False,
       )

alsoProvides(INetContactInfo,IFormFieldProvider)

class IPhoneContactInfo(form.Schema):
   """
      Marker/Form interface for a set of telephone contact information
   """
   
   phone = schema.TextLine(
       title=_(u'Phone'),
       description=_(u'Please provide a telephone number where you can be reached.'),
       required=False,
       )
   
   mobile = schema.TextLine(
       title=_(u'Mobile'),
       description=_(u'Please provide your mobile phone number.'),
       required=False,
       )

alsoProvides(IPhoneContactInfo,IFormFieldProvider)