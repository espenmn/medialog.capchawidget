from zope import schema
from zope.interface import Interface
from zope.interface import implements
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from zope.interface import invariant, Invalid

from medialog.capchawidget.widgets.widget import CapchaFieldWidget

_ = MessageFactory('medialog.capchawidget')

    
def checkForMagic(value):
       return 'magic' in value

class ICapchaBehavior(form.Schema):
    """ A field for capcha"""
    
    
    capchafield = schema.TextLine(
        title = _("capcha", default=u"Capcha"),
        constraint=checkForMagic,
        required = True,
        description = _("help_capcha",
                      default="Dont be a robot"),
    )

    form.widget(
            capchafield=CapchaFieldWidget,
    )
    
    
    def checkForMagic(value):
       return 'magic' in value
       
       
    def verify(self, input=None):
        info = IRecaptchaInfo(self.request)
        if info.verified:
            return True

        if not self.settings.private_key:
            raise ValueError(
                'No recaptcha private key configured. '
                'Go to /@@recaptcha-settings to configure.'
            )
        response_field = self.request.get('g-recaptcha-response')
        remote_addr = self.request.get('HTTP_X_FORWARDED_FOR', '').split(',')[0]
        if not remote_addr:
            remote_addr = self.request.get('REMOTE_ADDR')
        res = submit(response_field, self.settings.private_key, remote_addr)
        if res.error_code:
            info.error = res.error_code

        info.verified = res.is_valid
        return res.is_valid

alsoProvides(ICapchaBehavior, IFormFieldProvider)



