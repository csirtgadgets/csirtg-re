import re

from ._version import get_versions
VERSION = get_versions()['version']
del get_versions

RE_IPV4 = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(\d{1,3})$')
RE_IPV4_CIDR = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\/\d{1,2})$')

# http://stackoverflow.com/a/17871737
RE_IPV6 = re.compile(r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))')

# http://goo.gl/Cztyn2 -- probably needs more work
# http://stackoverflow.com/a/26987741/7205341
# ^((xn--)?(--)?[a-zA-Z0-9-_@]+(-[a-zA-Z0-9]+)*\.)+[a-zA-Z]{2,}(--p1ai)?$
#RE_FQDN = re.compile('^((?!-))(xn--)?[a-z0-9][a-z0-9-_\.]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$')
# http://stackoverflow.com/questions/14402407/maximum-length-of-a-domain-name-without-the-http-www-com-parts
RE_FQDN = re.compile(r'^((?!-))(xn--)?[a-z0-9][a-z0-9-_\.]{0,245}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$')
RE_URI_SCHEMES = re.compile(r'^(https?|ftp)://')
RE_EMAIL = re.compile(r'^[_a-z0-9-\!\#\$\%\&\'\*\+\-\/\=\?\^\_\`\{\|\}\~]+(\.[_a-z0-9-\!\#\$\%\&\'\*\+\-\/\=\?\^\_\`\{\|\}\~]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,8})$')
RE_ASN = re.compile(r'^(AS|as)[0-9]{1,6}$')

RE_HASH = {
    'uuid': re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'),
    'md5': re.compile(r'^[a-fA-F0-9]{32}$'),
    'sha1': re.compile(r'^[a-fA-F0-9]{40}$'),
    'sha256': re.compile(r'^[a-fA-F0-9]{64}$'),
    'sha512': re.compile(r'^[a-fA-F0-9]{128}$'),
}

RE_IPV4_PADDING = re.compile(r"(^|\.)0+([^/.])")


MAP = {
    RE_IPV4: 'ipv4',
    RE_IPV6: 'ipv6',
    RE_FQDN: 'fqdn',
    RE_ASN: 'asn',
    RE_URI_SCHEMES: 'url',
    RE_EMAIL: 'email',
    RE_IPV4_CIDR: 'ipv4',
}


def get(i):
    """Regex Indicators Fast

Example:
    from csirtg_re import get
    itype = get('1.1.1.1')

    :param i: indicator string
    :return: indicator type string
    """

    for k, v in MAP.items():
        if k.match(i):
            return v

    for k, v in RE_HASH.items():
        if v.match(i):
            return k


def main():
    import sys
    i = sys.argv[1]

    print(get(i))


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
