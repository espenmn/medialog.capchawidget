import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text

#from plone import api
#from medialog.captchawidget.interfaces import IRecaptchaSettings



class ICaptchaWidget(interfaces.IWidget):
    """Captchar widget."""
 

class CaptchaWidget(text.TextWidget):
    """Captcha Widget"""
    zope.interface.implementsOnly(ICaptchaWidget)
    

        
def CaptchaFieldWidget(field, request):
    """IFieldWidget factory for CaptchaWidget."""
    return widget.FieldWidget(field, CaptchaWidget(request))