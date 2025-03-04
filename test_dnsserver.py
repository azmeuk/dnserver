import pytest
from dnserver import DNSServer
import dns.resolver


@pytest.fixture
<<<<<<< HEAD
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
=======
def dnsresolver():
    port = 5053
    with open("example_zones.txt") as fd:
        zone = fd.read()

    server = DNSServer(port, zone)
    server.start()

    resolver = dns.resolver.Resolver()
    resolver.nameservers = ["127.0.0.1"]
    resolver.port = port
    yield resolver

    server.stop()


def test_dnsserver(dnsresolver):
    answers = dnsresolver.resolve("example.com", "A")
    assert answers[0].address == "1.2.3.4"
>>>>>>> refactor
