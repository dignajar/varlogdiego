# Title: GNU/Linux Bind as a slave DNS
<!-- Position: 2 -->
<!-- Tags: Linux, Bind, DNS -->
---
Bind as slave DNS server.

- DNS Master: 10.1.1.1
- DNS GNU/Linux Bind: 10.1.1.2
- Domain: mydomain.com

## Config file

File configuration `/etc/named.conf`

```
options {
	listen-on port 53 { any; };
	directory 	"/var/named";
	dump-file 	"/var/named/data/cache_dump.db";
	statistics-file "/var/named/data/named_stats.txt";
	memstatistics-file "/var/named/data/named_mem_stats.txt";

	// Allow internal network only
	allow-query     { any; };

	forwarders {
		8.8.8.8;
		8.8.4.4;
	};

	recursion yes;

	dnssec-enable yes;
	dnssec-validation yes;
	dnssec-lookaside auto;

	/* Path to ISC DLV key */
	bindkeys-file "/etc/named.iscdlv.key";

	managed-keys-directory "/var/named/dynamic";

	pid-file "/run/named/named.pid";
	session-keyfile "/run/named/session.key";

	version none;
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};

zone "." IN {
	type hint;
	file "named.ca";
};

zone "mydomain.com" IN {
	type slave;
	file "slaves/mydomain.com";
	masters { 10.1.1.1; };
};

zone "1.10.in-addr.arpa" IN {
	type slave;
	file "slaves/reverse.mydomain.com";
	masters { 10.1.1.1; };
};

include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";
```
