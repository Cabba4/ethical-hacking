## Basíc Information (Google)

1) An exploit kit is a utility program which is used by attackers to launch exlpoits against vulnerable programs. It can have multiple exploits for different versions of the same target and can be used by users with lesser techincal knowledge as well.
2) Exploit kits are packaged with exploits that can target commonly installed software such as Adobe Flash, Java, Microsoft Silverlight and other popularly available softwares because exploit kits are not designed to work on specific systems but try to cover most of them.
3) Magnitude EK(2019) one of the longest-standing exploit kits. Delivers malware to users from Asia-Pacifi(APAC) countries. https://securelist.com/magnitude-exploit-kit-evolution/97436/
Neutrino - Threat actors can have zero coding experience and still use it.
List for others - https://www.trendmicro.com/vinfo/us/security/definition/exploit-kit
4) Tool for threat actors with very little information to brute force targets and hope that something sticks.

## Scenario

1) Should be worried
2) The attack started at 21:45:25 after the user clicked on some link on the affected website, and it lasted till 22:58:02 which is where the wireshark capture ends. So around 1hour and 13minutes.
3) Sharik/Smoke
4) Exploit Kit working

	a) Target - 10.1.4.102
	b) User browser - 88.208.7.193
	c) Ad delivery system - 185.56.233.186
	d) Landing page - 185.178.47.70
	e) Malware page - letitbit.su 185.68.93.102


	User - 10.1.4.102 -> 88.208.7.193 (http://datitngforllives.info/)

	datitingforllives has some javascript code in it coming from -> www.freebitc.pro/unlimited/howareyou which is being run on window.setTimeout('visits()', 99)
	so 99miliseconds after page is viewed.

	Then host asks gateway 10.4.1.1 whois freebitc.pro 

	freebit.pro -> 185.56.233.186 (most probably an advertisement server?)

	Then user click on the link in the html page which goes to fdating.com/?u=<payload here>

	This server is 185.178.47.70 

	Frame 161 - sends shockwave-flash media type from http (malware comes from here)

	Frame 509 - sends application/x-msdownload 

	Frame 531 - sends application/x-www-form-urlencoded obfuscated code

5) Legal - Netherlands, Illegal - Russia
6) Command and control attack
7) Data from target to advertisement website is encrypted with SSL
8) There are 5 devices associated with this attack, target-user browser-Ad delivery page-Landing page and Malware page
9) News article on the website, user clicked on it which led to connection with hacked server.
10) Browser had javascript enabled which led to windows.setTimeout code execution.
11) Malware downloaded is Rig-EK-flash-exploit which uses CVE-2018-4878 to exploit a vulnerabilty in Adobe Flash player before 28.0.0.161. A successful attack can lead to arbitary code execution.

12) F-secure recognizes the malware.
13) CVE-2018-4878
14) A user viewed a website called datitngforllives.info which had some advertisements being loaded from some other server. Upon clicking a link on the website the user is connected to the malware server which starts scanning the user for potential vulnerabilities. The users device had outdated flash player and the malware server is able to identify this, then it sends the malware which is executed in the background.
15) Better user awareness is definitely required, the attack started from the users carelessness of visting such a website and then clicking on articles on it.
Antivirus will also help as it can detect any malware that is downloaded on the device and prevent it from running.
Up-to-date updates will help by removing older flash player versions and potential exploit points.
Firewall can help if device is managed by someone else and regularly adds such sites to be auto blocked so that user doesnt view them even by mistake(phishing).