# Title: Juniper Network Connect for GNU/Linux
<!-- Position: 1 -->
<!-- Description: JNC Client for GNU/Linux -->
<!-- Tags: Networking, Juniper -->
<!-- Date: 2016-03-10 18:20:00 -->
---
I made a little script to connect to the Juniper VPN, this script used the Java client (32bits) from Juniper Network Connect.

## Notes
- If you are running a 64bits plataform you need to install 32bits runtime libraries.
- This script works with password and RSA passcode.

## Download
Github proyect: https://github.com/dignajar/dvpn

<!-- pagebreak -->

## Installation on Ubuntu
```
$ sudo apt-get install -y wget unzip lib32z1 lib32ncurses5 lib32bz2-1.0
$ cd /tmp/
$ wget https://raw.githubusercontent.com/dignajar/dvpn/master/install_dvpn.sh
$ chmod 755 install_dvpn.sh
$ ./install_dvpn.sh {url} {realm}
```

Replace *{url}* for the URL of your Juniper web portal and the *{realm}* for the user group associated.

## Usage
- Connect to the VPN
```$ dvpn```
- Disconnect
```$ dvpn --disconnect```
- Regenerate certificate
```$ dvpn --certificate```

## Links
This script is based on the next links:

- http://www.scc.kit.edu/scc/net/juniper-vpn/linux/
- http://mad-scientist.us/juniper.html