# -*- coding: utf-8 -*-
from five import grok
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from plone.i18n.locales.countries import _countrylist


class CountriesVocabulary(object):
    """Vocabulary factory for a list of countries
    """
    grok.implements(IVocabularyFactory)
    
    def __call__(self, context):
        countries = [(v['name'],k) for k, v in _countrylist.items()]
        countries.sort()
        items = [SimpleTerm(k,k,v) for v,k in countries]
        return SimpleVocabulary(items)

grok.global_utility(CountriesVocabulary, name=u"contact.countries")