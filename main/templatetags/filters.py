from django.core.serializers import serialize
from django.db.models.query import QuerySet, ValuesListIterable
from django.utils.safestring import mark_safe
from django.template import Library

import json

register = Library()

def jsonify(object):

    if isinstance(object, ValuesListIterable):
        return mark_safe(json.dumps(list(object)))
    if isinstance(object, QuerySet):
        return mark_safe(serialize('json', object))
    return mark_safe(json.dumps(object))

register.filter('jsonify', jsonify)
jsonify.is_safe = True