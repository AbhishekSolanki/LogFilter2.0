# Starts CGI Http Server and MongoDB Server
import os
import time
import threading

def cgiServer():
    print "Starting CGI Server"
    os.system("python -m CGIHTTPServer")

def mongoServer():
    print "Starting MongoDB Server"
    os.chdir("MongoDB 2.6 Standard/bin")
    os.system("mongod -dbpath=data")
    
def main():
    cgi_Server=threading.Thread(target=cgiServer)
    mongo_Server=threading.Thread(target=mongoServer)
    cgi_Server.start()
    mongo_Server.start()
    
main()
