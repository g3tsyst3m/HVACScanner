@echo off
type NUL > ips.txt
type NUL > collectedips.txt

echo Do you have a textfile with IPs to scan? Y or N
set /P YorN=:
if "%YorN%"=="Y" goto nmaplist

echo Enter the 1st octet here
set /P octet1=:
echo Enter the 2nd octet here
set /P octet2=:
echo Enter the 3rd octet here
set /P octet3=:
echo Enter the CIDR mask here
set /P cidr=:
echo [Searching for online devices...Please be patient while results are collected]
d:\metasploit\nmap\nmap -PN --open -p 80,443 %octet1%.%octet2%.%octet3%.0/%cidr% | find "%octet1%." >> ips.txt
for /F "tokens=5" %%a in (ips.txt) do echo %%a >> collectedips.txt
echo Done!

goto end

:nmaplist
echo Enter the 1st octet here
set /P octet1=:
echo Enter the FULL path to your list below
set /P listpath=:

echo [Searching for online devices...Please be patient while results are collected]
d:\metasploit\nmap\nmap -PN --open -p 80,443 -iL %listpath% | find "%octet1%." >> ips.txt
for /F "tokens=5" %%a in (ips.txt) do echo %%a >> collectedips.txt
echo Done!
goto end

:end
exit
