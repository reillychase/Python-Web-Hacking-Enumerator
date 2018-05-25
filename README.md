# Python-Web-Hacking-Enumerator
This script takes in a list of hosts (from a Sublist3r.py scan for example), performs a port scan on each from port 0-800, and then groups them by IP address.

This is how I kick off web application pen tests, it helps sort domains to see which ones are on the same server. 

## Why use it?
For example, you find out there is a subdomain named "test" that is on the same server as \<insert-high-value-target-here\>, then you can figure out where to spend your time faster.

## How to use it
1. Collect a list of hostnames for which you want to find out which ones have the same IP address (I recommend using Sublist3r.py)
2. Put the hostnames int hosts.txt
3. Run main.py and the result will be output to result_domain.txt

## Sample output:
+------------------+----------------+----------------+---------+
| REVERSE DNS      | IP ADDRESS     | OPEN PORTS     | DOMAINS |
|------------------+----------------+----------------+---------+
|
+------------------+----------------+----------------+---------+
