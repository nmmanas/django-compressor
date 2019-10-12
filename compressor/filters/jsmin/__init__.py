from __future__ import absolute_import
from compressor.filters import CallbackOutputFilter


class rJSMinFilter(CallbackOutputFilter):
    callback = "rjsmin.jsmin"
    dependencies = ["rjsmin"]
    kwargs = {
        "keep_bang_comments": True
    }


# This is for backwards compatibility
JSMinFilter = rJSMinFilter


class SlimItFilter(CallbackOutputFilter):
    dependencies = ["slimit"]
    callback = "slimit.minify"
    kwargs = {
        "mangle": True,
    }


class CalmjsFilter(CallbackOutputFilter):
    dependencies = ["calmjs.parse"]
    callback = "calmjs.parse.unparsers.es5.minify_print"
    kwargs = {
        "obfuscate": True,
    }
