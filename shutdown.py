import socket
pc = socket.gethostname()
if pc == "":
    print("error try on difrint pc")
    quit
else:
    os.system("shutdown /s /t 1")
