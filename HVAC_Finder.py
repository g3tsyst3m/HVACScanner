import urllib2
import requests
import colorama
from colorama import Fore, Back, Style
import os

os.system('cls')
colorama.init()
#run nmap to collect all our web devices that are online and using port 80 or 443
print Fore.YELLOW + "****************************************************************************"
print Fore.YELLOW + "*****************HVAC fingerprint discovery module for python***************"
print Fore.YELLOW + "****************************************************************************"
print Fore.WHITE 

print "Collecting our ips to fingerprint."
os.system("exportips.bat")


with open("collectedips.txt") as f:
    content = f.readlines()
    print "Online machines found: "+Fore.GREEN+str(len(content))+Fore.WHITE
#print content[len(content)-1]
if (len(content)-1)==-1:
    print "no active IPs at this address..."

theresponse=0
machineprefix="http://"
securemachineprefix="https://"

print "Now scanning for HVAC Machines..."

for i in (content):
    try:
        i=i.rstrip() #get rid of the newline
        #print machineprefix+str(i)+"/login/keys.png"
        theresponse = urllib2.urlopen(machineprefix+str(i)+"/login/keys.png",timeout = 1)
        urlbodycontent=theresponse.read()
        #print urlbodycontent
        #print urlbodycontent
        if ("PNG" in urlbodycontent):
            print Fore.GREEN + "*****************************************************************************"
            print "Discovered a valid fingerprint for a ['Tridium Niagara httpd 3.6.47.5'] browser accessible HVAC device panel"
            print "For machine ip: "+machineprefix+str(i)
            os.system( "d:\\metasploit\\nmap\\nmap -v -O --osscan-guess "+str(i))
            print "*****************************************************************************"
            print Fore.WHITE + "" #return to original coloring scheme
            raw_input('Press [enter] to continue with the scan...')
    except:
        print Fore.RED+machineprefix+str(i)+"/login/keys.png"
        print "no Tridium based HVAC machines located at this address..."+Fore.WHITE
    try:
        i=i.rstrip() #get rid of the newline
        theresponse = urllib2.urlopen(machineprefix+str(i)+"/SystemDisplays/Images/HMIWebBrowserHeader.jpg",timeout = 2)
        urlbodycontent=theresponse.read()
        #print urlbodycontent
        if ("JPG" in urlbodycontent) or ("JFIF" in urlbodycontent):
            print Fore.GREEN + "*****************************************************************************"
            print "Discovered a fingerprint for an ['HMIWeb'] browser accessible HVAC device panel"
            print "For machine ip: "+machineprefix+str(i)
            os.system( "d:\\metasploit\\nmap\\nmap -v -O --osscan-guess "+str(i))
            print "*****************************************************************************"
            print Fore.WHITE + ""
            raw_input('Press [enter] to continue with the scan...')
    except:
        print Fore.RED+machineprefix+str(i)+"/SystemDisplays/Images/HMIWebBrowserHeader.jpg"
        print "no Honeywell HMIWeb-based HVAC machines located at this address..."+Fore.WHITE
		
    try:
        i=i.rstrip() #get rid of the newline
        theresponse = urllib2.urlopen(securemachineprefix+str(i)+"/web/", timeout=5)
        urlbodycontent=theresponse.read()
        #print urlbodycontent
        if ("NetAXS" in urlbodycontent):
            print Fore.GREEN + "*****************************************************************************"
            print "Discovered a fingerprint for a ['Honeywell NetAXS'] browser accessible HVAC device panel"
            print "For machine ip: "+securemachineprefix+str(i)
            os.system( "d:\\metasploit\\nmap\\nmap -v -O --osscan-guess "+str(i))
            print "*****************************************************************************"
            print Fore.WHITE + ""
            raw_input('Press [enter] to continue with the scan...')
    except:
        print Fore.RED+securemachineprefix+str(i)+"/web/"
        print "no Honeywell NetAXS-based HVAC machines located at this address..."+Fore.WHITE

    """
	try:
        i=i.rstrip() #get rid of the newline
        theresponse = urllib2.urlopen(machineprefix+str(i)+"/images/enp.gif",timeout = 1)
        urlbodycontent=theresponse.read()
        #print urlbodycontent
        if ("GIF" in urlbodycontent):
            print Fore.GREEN + "*****************************************************************************"
            print "Discovered a fingerprint for an ['Emerson/Liebert Network Power Unit'] browser accessible device panel"
            print "For machine ip: "+machineprefix+str(i)
            print "*****************************************************************************"
            print Fore.WHITE + ""
            raw_input('Press [enter] to continue with the scan...')
    except:
        print machineprefix+str(i)+"/SystemDisplays/Images/HMIWebBrowserHeader.jpg"
        print "no Emerson/Liebert Network Power Unit devices located at this address..."
    """
print ""    
raw_input(Fore.YELLOW + '                 [        Scan Finished!        ]')
print Fore.WHITE
