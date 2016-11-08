import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text

from plone import api
from medialog.capchawidget.interfaces import ICapchaSettings



class ICapchaWidget(interfaces.IWidget):
    """Iconpicker widget."""
 

class CapchaWidget(text.TextWidget):
    """Capcha Widget"""

    zope.interface.implementsOnly(ICapchaWidget)
    
    pass

        
def CapchaFieldWidget(field, request):
    """IFieldWidget factory for CapchaWidget."""
    return widget.FieldWidget(field, CapchaWidget(request))
    
