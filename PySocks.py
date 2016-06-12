# Developed by TheBeast808 (BeastsMC) github.com/BeastsMC
# Developed by Goodies hackforums.net/member.php?action=profile&uid=1173142
# Developed by Merkie github.com/Merkie

import requests
import bs4
import os
import os.path
import sys
import socket
import Queue
import threading
import time

url = "https://proxybag.blogspot.com/"
all_proxies = set()

def get_article_urls():
    """A simple generator that will yield each article in the main blog."""
    article_soup = bs4.BeautifulSoup(requests.get(url).content, "html.parser")
    articles = article_soup.find_all("h3", attrs={"class": "post-title entry-title"})
    # print(articles)
    for article in articles:
        soup = bs4.BeautifulSoup(str(article), "html.parser")
        a = soup.find("a")
        yield a["href"] if a else None

def get_textarea(article):
    article_soup = bs4.BeautifulSoup(requests.get(article).content, "html.parser")
    proxies = [proxy for proxy in map(lambda x: x.strip(), article_soup.find("textarea").getText().split())]
    return set(proxies)

#Rscrapes for these websites. Feel free to add your own and see if hey work:

url = "https://proxybag.blogspot.com/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))
    

url = "http://www.vipsocks24.net/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))
    

url = "http://www.live-socks.net/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://www.socks24.org/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socksproxylist24.blogspot.com/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Free%20Socks"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Free%20Socks%205%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Free%20Socks%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Good%20Socks"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Good%20Socks%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Live%20Socks%205"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Live%20Socks%205%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Live%20Socks%205%20US%20Online"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Socks%205%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Socks%205%20US%20Online"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Vip%20Socks"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Vip%20Socks%205"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://msocks5.blogspot.com/search/label/Vip%20Socks%205%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Live%20Socks%205"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Live%20Socks%205%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Socks%205%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Socks%205%20US%20Online"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Vip%20Socks%205"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Vip%20Socks%205%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Vip%20Socks%20Online"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Live%20Socks%205"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Live%20Socks%205%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Socks%205%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Socks%205%20US%20Online"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Vip%20Socks%205"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Vip%20Socks%205%20US"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks5online.blogspot.com/search/label/Vip%20Socks%20Online"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://proxy-hunter.blogspot.com"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://proxy-hunter.blogspot.com/search/label/Anonymous%20Live%20Proxies"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://proxy-hunter.blogspot.com/search/label/Anonymous%20US%20Proxies"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://proxy-hunter.blogspot.com/search/label/Fresh%20Socks%205"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://globalproxies.blogspot.com/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://globalproxies.blogspot.com/search/label/Canada%20Proxies"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://globalproxies.blogspot.com/search/label/France%20Proxies"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://globalproxies.blogspot.com/search/label/UK%20Proxies"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://globalproxies.blogspot.com/search/label/US%20Proxies"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socks-world.blogspot.com/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://globalproxies.blogspot.com/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://socksproxylist24.blogspot.com/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://proxyserverlist-24.blogspot.com/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

url = "http://newfreshproxies24.blogspot.com/"
for article_url in get_article_urls():
	all_proxies = set(filter(None, all_proxies))
	all_proxies.update(get_textarea(article_url))

os.system("clear")

#Proxy readout:

print("\n".join(all_proxies))

#Preparing to check proxies:

if os.path.isfile("output.txt"):
	shouldidelete = raw_input("Found 'output.txt' exiting...")
	if shouldidelete == "no":
		print("")
	else:
		sys.exit()

os.system("touch output.txt")
os.system("touch ignore.txt")

# Writing the proxies to ignore.txt

f = open("ignore.txt","w")
f.write("\n".join(all_proxies))

# Checking proxies

from struct import *
class ThreadChecker(threading.Thread):
	def __init__(self, queue, timeout):
		self.timeout = timeout
		self.q = queue
		threading.Thread.__init__(self)
	def isSocks4(self, host, port, soc):
		ipaddr = socket.inet_aton(host)
		packet4 = "\x04\x01" + pack(">H",port) + ipaddr + "\x00"
		soc.sendall(packet4)
		data = soc.recv(8)
		if(len(data)<2):
			# Null response
			return False
		if data[0] != "\x00":
			# Bad data
			return False
		if data[1] != "\x5A":
			# Server returned an error
			return False
		return True
	def isSocks5(self, host, port, soc):
		soc.sendall("\x05\x01\x00")
		data = soc.recv(2)
		if(len(data)<2):
			# Null response
			return False
		if data[0] != "\x05":
			# Not socks5
			return False
		if data[1] != "\x00":
			# Requires authentication
			return False
		return True
	def getSocksVersion(self, proxy):
		host = proxy.split(":")[0]
		try:
			port = int(proxy.split(":")[1])
			if port < 0 or port > 65536:
				print "Invalid: " + proxy
				return 0
		except:
			print "Invalid: " + proxy
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(self.timeout)
		try:
			s.connect((host, port))
			if(self.isSocks4(host, port, s)):
				s.close()
				return 5
			elif(self.isSocks5(host, port, s)):
				s.close()
				return 4
			else:
				("Not a SOCKS: " + proxy)
				s.close()
				return 0
		except socket.timeout:
			print "Timeout: " + proxy
			s.close()
			return 0
		except socket.error:
			print "Connection refused: " + proxy
			s.close()
			return 0
	def run(self):
		while True:
			proxy = self.q.get()
			version = self.getSocksVersion(proxy)
			if version == 5 or version == 4:
				print "Working: " + proxy
				socksProxies.put(proxy)
			self.q.task_done()
class ThreadWriter(threading.Thread):
	def __init__(self, queue, outputPath):
		self.q = queue
		self.outputPath = outputPath
		threading.Thread.__init__(self)
	def run(self):
		while True:
			toWrite = self.q.qsize()
			outputFile = open(self.outputPath, 'a+')
			for i in xrange(toWrite):
				proxy = self.q.get()
				outputFile.write(proxy + "\n")
				self.q.task_done()
			outputFile.close()
			time.sleep(10)
checkQueue = Queue.Queue()
socksProxies = Queue.Queue()
inputFile = open("ignore.txt")
outputPath = "output.txt"
threads = int(75)
timeout = int(3)
#inputFile = open(raw_input("Proxy list: "), 'r')
#outputPath = raw_input("Output file: ")
#threads = int(raw_input("Number of threads: "))
#timeout = int(raw_input("Timeout(seconds): "))
for line in inputFile.readlines():
	checkQueue.put(line.strip('\n'))
inputFile.close()
for i in xrange(threads):
	t = ThreadChecker(checkQueue, timeout)
	t.setDaemon(True)
	t.start()
	time.sleep(.25)
wT = ThreadWriter(socksProxies, outputPath)
wT.setDaemon(True)
wT.start()
checkQueue.join()
socksProxies.join()

os.system("rm ignore.txt")
sys.exit()


