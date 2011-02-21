#-*- coding:utf-8 -*-
"""
$Id$
"""
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import render_to_string


def render_to(template):
    """ /from snippet/
    Decorator for Django views that sends returned dict to render_to_response function
    with given template and RequestContext as context instance.

    If view doesn't return dict then decorator simply returns output.
    Additionally view can return two-tuple, which must contain dict as first
    element and string with template name as second. This string will
    override template name, given as parameter

    Parameters:

     - template: template name to use
    """
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return render_to_response(output[1], output[0], RequestContext(request))
            elif isinstance(output, dict):
                return render_to_response(template, output, RequestContext(request))
            return output
        return wrapper
    return renderer


def render_to_str(template):
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return render_to_string(output[1], output[0], RequestContext(request))
            elif isinstance(output, dict):
                return render_to_string(template, output, RequestContext(request))
            return output
        return wrapper
    return renderer
