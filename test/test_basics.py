from csirtg_re import get


INDICATORS = {
    '1.1.1.1': 'ipv4',
    'example.com': 'fqdn',
    '0000:0000::': 'ipv6',
    'a95c530a7af5f492a74499e70578d150': 'md5',
    "http://example.com": "url",
    "https://example.com": "url",
    "1.1.1.0/8": "ipv4",
}


def test_re():
    for i in INDICATORS:
        assert get(i) == INDICATORS[i]
