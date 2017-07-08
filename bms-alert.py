#!/usr/bin/python

import re, urllib, smtplib, sys

from email.mime.text import MIMEText

if len(sys.argv) < 4:
    print "Email, Movie link and at least one theater name is required!"
    sys.exit()

email_ids = sys.argv[1]
email_ids = email_ids.split(",")

movie_url = sys.argv[2]
print "Movie link:" + movie_url

mytheatres = []
length = len(sys.argv)
if length >= 4:
    mytheatres.append(sys.argv[3])
if length >= 5:
    mytheatres.append(sys.argv[4])
if length >= 6:
    mytheatres.append(sys.argv[5])

print "Theatre names:" + ", ".join(mytheatres)

def send_email(email_ids, myurl, mytheatre):
    fromaddr = "from@live.com"
    toaddrs = email_ids
    msg = ("From: %s\r\nTo: %s\r\n" % (fromaddr, ", ".join(toaddrs)))
    movie_name = re.search(".*buytickets\/([a-z0-9\-]+)\/", myurl, re.I)
    if movie_name:
        movie_name = movie_name.group(1)
    msg = msg + "Subject:Tickets available !! for " + movie_name + " at " + mytheatre + "\r\n\r\n"
    msg = msg + "Tickets available.\n"
    server = smtplib.SMTP('smtp.live.com', 587)
    server.ehlo()
    server.starttls()
    server.login("from@live.com", "*****")
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return

html_text = urllib.urlopen(movie_url).read()

for mytheatre in mytheatres:
    my_regex = r"href=[\"\'].*" + mytheatre + r".*[\"\']"
    if re.search(my_regex, html_text, re.I):
        send_email(email_ids, movie_url, mytheatre)
        print "Tickets available !! for " + mytheatre
    else:
        print "No Tickets yet :-( for " + mytheatre
