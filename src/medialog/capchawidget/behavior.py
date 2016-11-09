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
    
    form.validator (
        capchafield=CapchaValidator,
    )

alsoProvides(ICapchaBehavior, IFormFieldProvider)


@form.validator.validator(field=ICapchaBehavior['capchafield'])
class CapchaValidator(validator.SimpleFieldValidator):
    """ z3c.form validator class for international phone numbers """

    import pdb;pdb.set_trace()
            
    def validate(self, value):
        #info = IRecaptchaInfo(self.request)
        #if info.verified:
        #    return True

        #if not self.settings.private_key:
        #    raise ValueError(
        #        'No recaptcha private key configured. '
        #        'Go to /@@recaptcha-settings to configure.'
        #    )
        import pdb;pdb.set_trace()
        response_field = self.context.request.get('g-recaptcha-response')
        remote_addr = 'https://www.google.com/recaptcha/api/siteverify'
        key = self.portal_registry['medialog.capchawidget.interfaces.ICapchaSettings.key']
        res = submit(response_field, self.settings.private_key, remote_addr)
        if res.error_code:
            info.error = res.error_code

        info.verified = res.is_valid
        return res.is_valid


