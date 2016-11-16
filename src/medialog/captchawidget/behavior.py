from zope import schema
from zope.interface import Interface
from zope.interface import implements
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from zope.interface import Invalid
from z3c.form import validator
from z3c.form.validator import SimpleFieldValidator


from medialog.captchawidget.widgets.widget import CaptchaFieldWidget

_ = MessageFactory('medialog.captchawidget')

import zope.component
import zope.interface



class ICaptchaBehavior(form.Schema):
    captchafield = schema.TextLine(
        title = _("captcha", default=u"Captcha"),
        required = False,
        description = _("help_captcha",
                      default="Dont be a robot"),
    )
    form.widget(
            captchafield=CaptchaFieldWidget,
    )





@form.validator(field=ICaptchaBehavior['captchafield'])
class CaptchaValidator(validator.SimpleFieldValidator):
    """ z3c.form validator class for captcha field """

    def validate(self, value):
        """ Validate  on input """
        super(CaptchaValidator, self).validate(value)
        
        context = self.context
        value = context.restrictedTraverse('@@captcha').verify()

        if value ==True:
            return True
        
        # Robot answer
        raise zope.interface.Invalid(_(u"Robot"))


# Set conditions for which fields the validator class applies
validator.WidgetValidatorDiscriminators(CaptchaValidator, field=ICaptchaBehavior['captchafield'])
#
# Register the validator so it will be looked up by z3c.form machinery
zope.component.provideAdapter(CaptchaValidator)



alsoProvides(ICaptchaBehavior, IFormFieldProvider)


