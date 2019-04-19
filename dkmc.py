import os
from core.ui import UI
from core.menu import MenuUI
from module.gen import GenModule
from module.web import WebModule
from module.ps import PsModule
from module.shellcode import ShellcodeModule
from module.rawhex import RawhexModule
from module.winrawhex import WinRawhexModule

if __name__ == "__main__":

    if not os.path.exists("output/"):
	os.makedirs("output/")

    options = []
    options.append(("gen", "Generate a malicious BMP (Bitmap) image"))
    options.append(("web", "Start a web server and deliver malicious image"))
    options.append(("ps", "Generate Powershell payload"))
    options.append(("sc", "Generate shellcode from raw file"))
    options.append(("rawhex", "Generate Metasploit Payload + install metasploit"))
    options.append(("winrawhex", "Generate Metasploit Payload + install metasploit (WINDOWS MODULE)"))
    options.append(("exit", "Fucking Quit the application"))
    
    exit_loop = False
    error = ""
    ui = UI()
    menu = MenuUI()
    
    while not exit_loop:
	try:
	        ui.banner()
        	choice = ui.show_menu(options, error)
	        error = ""
        	if menu.is_an_option(choice):
	            mod = None
        	    if choice == "exit":
                	os.system("clear")
                        print"\033[91m   ____                 _ ____     "
                        print"  / ___| ___   ___   __| | __ ) _   _  ___ "
                        print" | |  _ / _ \ / _ \ / _` |  _ \| | | |/ _ \ "
                        print" | |_| | (_) | (_) | (_| | |_) | |_| |  __/ "
                        print"  \____|\___/ \___/ \__,_|____/ \__, |\___| "
                        print"                                |___/   "
                        print"[------------------------------------------]"
                        print"[--] If there is a problem or bug....feel free to report on https://github.com/GetRektBoy724/DKMCPRO/issues [--]\033[91m"
                        exit(0)
	            if choice == "gen":
        	        mod = GenModule(ui)
	            if choice == "web":
        	        mod = WebModule(ui)
	            if choice == "ps":
        	        mod = PsModule(ui)
	            if choice == "sc":
        	        mod = ShellcodeModule(ui)
                    if choice == "rawhex":
                        mod = RawhexModule(ui)
                    if choice == "winrawhex":
                        mod = WinRawhexModule(ui)
                    mod.show_menu()
                else:
            		error = "%s is not a valid option,sorry" % choice
	except KeyboardInterrupt:
		print ""
		ui = UI()
		menu = MenuUI()
