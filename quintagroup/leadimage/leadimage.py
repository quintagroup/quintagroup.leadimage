from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile

from quintagroup.leadimage import MessageFactory as _


class ILeadImage(form.Schema):
    """ Marker/Form interface for Lead Image"""

    image = namedfile.NamedBlobImage(
        title=_(u"Lead Image"),
        description=u"",
        required=False,
    )

    imageCaption = schema.TextLine(
        title=_(u"Lead Image Caption"),
        description=u"",
        required=False,
    )

alsoProvides(ILeadImage, IFormFieldProvider)


class LeadImage(object):
    """
       Adapter for Lead Image
    """
    implements(ILeadImage)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context
