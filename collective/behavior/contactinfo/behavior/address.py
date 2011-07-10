from zope.interface import alsoProvides
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from collective.behavior.contactinfo import MessageFactory as _

class IAddress(form.Schema):
   """Marker/Form interface for Address behavior
   """
   address = schema.TextLine(
       title=_(u'Address'),
       required=False,
       )
   
   city = schema.TextLine(
       title=_(u'City'),
       required=True,
       )
   
   state = schema.TextLine(
       title=_(u'State'),
       required=False,
       )
   
   postcode = schema.TextLine(
       title=_(u'Post Code / Zip Code'),
       required=False,
       )
   
   country = schema.Choice(
       title=_(u'Country'),
       required=True,
       vocabulary='contact.countries',
       )

alsoProvides(IAddress,IFormFieldProvider)
