from module import ModuleObject
import os
import re

class ShellcodeModule(ModuleObject):
    
    def __init__(self, ui):
        ModuleObject.__init__(self)
        self.ui = ui
        self.vars = {}
        self.vars["source"] = ["", "Path to the raw shellcode file"]
        self.description = "Module to generate shellcode out of raw metasploit shellcode file ."
        self.module_name = "root@dkmcpro:~/sc#"
    
    def run_action(self):
        if os.path.exists(self.vars["source"][0]):
            self.ui.print_msg("Shellcode:")
            print "\\x" + "\\x".join(re.findall("..", open(self.vars["source"][0], "rb").read().encode("hex")))
            print "You Can Copy This Shellcode To Your Text Editor!!"
        else:
            self.ui.print_error("%s not found,please check your input!" %self.vars["source"][0])

    def help_me(self):
       print ""
       print "[-------------------------------------------------------]"
       print "[---]         Example To Use This Module Is:        [---]"
       print "[---] 1. set source <metasploitrawpayloadpath>      [---]"
       print "[---] 2. exploit                                    [---]"
       print "[-------------------------------------------------------]"
