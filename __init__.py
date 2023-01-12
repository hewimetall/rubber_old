try:
    from django.conf import settings
except:
    class _settings:
        RUBBER_ELASTICSEARCH_URL = None
        RUBBER_DISABLE_AUTO_INDEX = False
        RUBBER_MOCK_HTTP_RESPONSE = None

    settings = _settings()

from old_req.rubber.resource import Resource
from old_req.rubber.client import ElasticSearch
