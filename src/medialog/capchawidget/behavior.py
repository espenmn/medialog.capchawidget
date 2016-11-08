from zope import schema
from zope.interface import Interface
from zope.interface import implements
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory


from medialog.iconpicker.widgets.widget import CapchaFieldWidget

_ = MessageFactory('medialog.capchawidget')


class ICapchaBehavior(form.Schema):
    """ A field for capcha"""
    
    
    capchafield = schema.TextLine(
        title = _("capcha", default=u"Capcha"),
        required = True,
        description = _("help_capcha",
                      default="Dont be a robot"),
    )

    form.widget(
            capchafield=CapchaFieldWidget,
    )

alsoProvides(ICapchaBehavior, IFormFieldProvider)

