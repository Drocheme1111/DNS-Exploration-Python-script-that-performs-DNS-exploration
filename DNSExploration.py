#!/usr/bin/python3

import dns.resolver
import socket

def reverse_dns(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]] + result[1]
    except socket.herror:
        return None

def dns_request(domain):
    ips = []
    try:
        result = dns.resolver.resolve(domain)
        if result:
            print("Domain: %s" % domain)
            for answer in result:
                print(answer)
                print("Reverse DNS: %s" % reverse_dns(answer.to_text()))
                ips.append(answer.to_text())
    except dns.resolver.NoAnswer:
        print("No answer found for domain: %s" % domain)
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        pass
    return ips

def subdomain_search(domain, dictionary, nums):
    successes = []
    for word in dictionary:
        subdomain = word + "." + domain
        successes.extend(dns_request(subdomain))
        if nums:
            for i in range(10):
                s = word + str(i) + "." + domain
                successes.extend(dns_request(s))
    return successes

if __name__ == "__main__":
    domain = input("Enter your domain name\n")
    dictionary_file = "subdomains.txt"
    dictionary = []
    with open(dictionary_file, "r") as f:
        dictionary = f.read().splitlines()
    results = subdomain_search(domain, dictionary, True)
    print("Successful DNS Resolutions:")
    for result in results:
        print(result)
