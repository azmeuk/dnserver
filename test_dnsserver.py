import pytest
from dnserver import DNSServer
import dns.resolver


@pytest.fixture
def dnsserver():
    with open("example_zones.txt") as fd:
        zone = fd.read()

    server = DNSServer(5053, zone)
    server.start()
    yield server
    server.stop()


def test_dnsserver(dnsserver):
    answers = dns.resolver.resolve("example.com", "A")
    assert answers[0].address == "93.184.216.34"
