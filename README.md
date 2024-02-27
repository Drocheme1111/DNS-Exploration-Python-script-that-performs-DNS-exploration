# DNS-Exploration-Python-script-that-performs-DNS-exploration
Python script that performs DNS exploration. The script allows you to search for subdomains of a given domain and retrieve their corresponding IP addresses and reverse DNS information.

    The script starts by importing the necessary modules: dns.resolver for DNS resolution and socket for reverse DNS lookup.

    The reverse_dns function takes an IP address as input and uses the socket.gethostbyaddr method to perform a reverse DNS lookup. It returns the hostname and additional information if successful, or None if an error occurs.

    The dns_request function takes a domain name as input and uses the dns.resolver.resolve method to perform a DNS resolution. It retrieves the IP addresses associated with the domain and prints them along with their reverse DNS information using the reverse_dns function. It also stores the IP addresses in a list and returns it.

    The subdomain_search function takes a domain name, a dictionary of subdomains, and a boolean flag indicating whether to include numbers in the subdomains. It iterates over each subdomain in the dictionary and appends the results of the dns_request function to a list of successes. If the nums flag is True, it also appends the results of subdomains with numbers appended to them.

    In the main block, the script prompts the user to enter a domain name. It then reads a file named "subdomains.txt" which contains a list of subdomains to search for. The file is read line by line and stored in the dictionary list.

    The subdomain_search function is called with the domain name, dictionary, and True for the nums flag. The results are stored in the results list.

    Finally, the script prints the successful DNS resolutions by iterating over the results list.

    That's it! You can now use this script to explore DNS information for a given domain and its subdomains.

    Remember to have a file named "subdomains.txt" in the same directory as the script, containing the list of subdomains you want to search for.
