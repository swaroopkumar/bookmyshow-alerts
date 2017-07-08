#!/usr/bin/python

import re, urllib, smtplib, sys

from email.mime.text import MIMEText

if len(sys.argv) < 3:
    print "Movie link and at least one theater name is required!"
    sys.exit()

myurl = sys.argv[1]
print "Movie link:" + myurl

mytheatres = []
length = len(sys.argv)
if length >= 3:
    mytheatres.append(sys.argv[2])
if length >= 4:
    mytheatres.append(sys.argv[3])
if length >= 5:
    mytheatres.append(sys.argv[4])

print "Theatre names:" + ", ".join(mytheatres)

for mytheatre in mytheatres:

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
