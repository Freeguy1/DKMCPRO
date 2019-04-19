import os

class UI:
    version = "1.0"
    
    def __init__(self):
        pass

    def clearscreen(self):
        os.system("clear")
        
    def banner(self):
        self.clearscreen()
        print "\n\n\033[91m  DKMCPRO - Don't kill my cat PRO"
        print "         Evasion tool - GetRektBoy724"
        print "          ____  _  ____  __  ____ ____  ____   ___        "
        print "         |  _ \| |/ /  \/  |/ ___|  _ \|  _ \ / _ \       "
        print "         | | | | ' /| |\/| | |   | |_) | |_) | | | |      "
        print "    _ _ _| |_| | . \| |  | | |___|  __/|  _ <| |_| | _ _  "
        print "   (_|_|_)____/|_|\_\_|  |_|\____|_|   |_| \_\\___(_|_|_) "
        print ""
        print " [---] Created By: Muhammad Syihan Zhafiri (GetRektBoy724) [---]"
        print " [---]    Follow Me At https://github.com/GetRektBoy724    [---]"
        print " [---]                Codename: 'Mati Lampu'               [---]"
        print " [---]                   Version: v4.3                     [---]"
        print " [---]-----------------------------------------------------[---]"
        print " [---]        !!!PLEASE RUN THIS TOOL AS ROOT!!!           [---]\033[91m"

    def show_menu(self, options, error = ""):
        print "Select an option:\n"
        for option in options:
            print "\t[*] (%s)\t%s" % (option)
        if not error == "":
            print "\n\033[91m[-] >>> %s\033[00m" % error
        return self.capture_input()  
      
    def capture_input(self, mod = ""):
        if not mod == "":
            mod = "(%s)" % mod
        return raw_input("\n%s>>> " % mod).strip()
    
    def print_msg(self, msg):
        print "\t\033[32m[+] %s\033[00m" % msg
        
    def print_error(self, error):
        print "\033[91m[-] >>> %s\033[00m" % error
        
    def print_debug(self, msg):
        print "\033[36m[DEBUG] >>> %s\033[00m" % msg
