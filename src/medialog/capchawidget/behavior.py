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
import zope.interface



class ICapchaBehavior(form.Schema):
    capchafield = schema.TextLine(
        title = _("capcha", default=u"Capcha"),
        required = False,
        description = _("help_capcha",
                      default="Dont be a robot"),
    )
    form.widget(
            capchafield=CapchaFieldWidget,
    )





@form.validator(field=ICapchaBehavior['capchafield'])
class CapchaValidator(validator.SimpleFieldValidator):
    """ z3c.form validator class for capcha field """

    def validate(self, value):
        """ Validate  on input """
        super(CapchaValidator, self).validate(value)
        
        import pdb; pdb.set_trace()

        if value =='emn':
            return True
        
        # The value is not required
        for c in value:
            if c not in allowed_characters:
                raise zope.interface.Invalid(_(u"Robot"))


# Set conditions for which fields the validator class applies
validator.WidgetValidatorDiscriminators(CapchaValidator, field=ICapchaBehavior['capchafield'])
#
# Register the validator so it will be looked up by z3c.form machinery
zope.component.provideAdapter(CapchaValidator)



alsoProvides(ICapchaBehavior, IFormFieldProvider)


