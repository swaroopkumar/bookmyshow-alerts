#!/usr/bin/python

import re, urllib, smtplib, sys

from email.mime.text import MIMEText

myurl = sys.argv[1]
print "Movie link:" + myurl
mytheatre = sys.argv[2]
print "Theatre name:" + mytheatre

my_regex = r"href=[\"\'].*" + mytheatre + r".*[\"\']"

if re.search(my_regex, urllib.urlopen(myurl).read(), re.I):
	fromaddr = "from@live.com"
	toaddrs = ["to@gmail.com"];
	msg = ("From: %s\r\nTo: %s\r\n" % (fromaddr, ", ".join(toaddrs)))
	msg = msg + "Subject:Tickets available !! for " + mytheatre + "\r\n\r\n"
	msg = msg + "Tickets available.\n"
	server = smtplib.SMTP('smtp.live.com', 587)
	server.ehlo()
	server.starttls()
	server.login("from@live.com", "****")
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
	print "Tickets available !! for " + mytheatre
else:
    print "No Tickets yet :-( for " + mytheatre
