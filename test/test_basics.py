from csirtg_re import get
from faker import Faker

fake = Faker()


INDICATORS = {
    '1.1.1.1': 'ipv4',
    'example.com': 'fqdn',
    '0000:0000::': 'ipv6',
    'a95c530a7af5f492a74499e70578d150': 'md5',
    "http://example.com": "url",
    "https://example.com": "url",
    "1.1.1.0/8": "ipv4",
    "bc1qjm4zu6rcg7a00ws26qr6u08dq35r3sj70yrj2e": "btc",
    "bc1qjm4zu6rcg7a00ws26qr6u08dq35r": "btc",
    "cve-2021-27104": "cve",
    "WES@barely3am.com": "email",
    "1b2a30776df64fbd7299bd588e21573891dcecbe": "sha1",
    "https://www.church.com/terms.htm": "url"
}


def test_re():
    for i in INDICATORS:
        assert get(i) == INDICATORS[i]

    for d in range(0, 100):
        assert get(fake.email()) == 'email'

    for d in range(0, 100):
        assert get(fake.ipv4()) == 'ipv4'

    for d in range(0, 100):
        assert get(fake.ipv6()) == 'ipv6'

    for d in range(0, 100):
        assert get(fake.url()) == 'url'

    for d in range(0, 100):
        assert get(fake.md5()) == 'md5'

    for d in range(0, 100):
        assert get(fake.sha256()) == 'sha256'

    for d in range(0, 100):
        assert get(fake.sha1()) == 'sha1'

    for d in range(0, 100):
        assert get(fake.domain_name()) == 'fqdn'
