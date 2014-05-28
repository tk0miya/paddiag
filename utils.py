# -*- coding: utf-8 -*-
import re
import zlib
import base64


# for supporting base64.js
def base64_decode(string):
    string = re.sub('-', '+', string)
    string = re.sub('_', '/', string)

    padding = len(string) % 4
    if padding > 0:
        string += "=" * (4 - padding)

    return base64.b64decode(string)


def decode_source(source, encoding, compression):
    if encoding == 'base64':
        source = base64_decode(source)

    if compression == 'deflate':
        source = zlib.decompress(source)

    if isinstance(source, str):
        source = unicode(source, 'UTF-8')

    return source
