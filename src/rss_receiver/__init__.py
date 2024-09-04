"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "rss_receiver"

_ = MessageFactory("rss_receiver")

logger = logging.getLogger("rss_receiver")
