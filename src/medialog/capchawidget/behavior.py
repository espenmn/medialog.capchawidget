from zope import schema
from zope.interface import Interface
from zope.interface import implements
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from zope.interface import invariant, Invalid
from zope.interface import Invalid
from z3c.form import validator
from z3c.form.validator import SimpleFieldValidator


from medialog.capchawidget.widgets.widget import CapchaFieldWidget

_ = MessageFactory('medialog.capchawidget')

import zope.component


class Over21(SimpleFieldValidator):

    def validate(self, value, force=False):
        import pdb; pdb.set_trace()
        """See interfaces.IValidator"""
        if value is self.field.missing_value:
            pass



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
    
    form.validator (
        capchafield=Over21,
    )
    
    #@invariant
    #def capchafieldInvariant(data):
    #    import pdb; pdb.set_trace()
    #    if data.capchafield == 'abc':
    #        raise Invalid(_(u"Virker som et robot svar!"))
    

        

alsoProvides(ICapchaBehavior, IFormFieldProvider)


