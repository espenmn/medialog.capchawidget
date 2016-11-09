from zope import schema
from zope.interface import Interface
from zope.interface import implements
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

#from zope.interface import invariant, Invalid
from zope.interface import Invalid
from z3c.form import validator

from medialog.capchawidget.widgets.widget import CapchaFieldWidget

_ = MessageFactory('medialog.capchawidget')


class ICapchaBehavior(form.Schema):
    """ A field for capcha"""
    
    
    capchafield = schema.TextLine(
        title = _("capcha", default=u"Capcha"),
        required = False,
        description = _("help_capcha",
                      default="Dont be a robot"),
    )

    form.widget(
            capchafield=CapchaFieldWidget,
    )
    
        
alsoProvides(ICapchaBehavior, IFormFieldProvider)



