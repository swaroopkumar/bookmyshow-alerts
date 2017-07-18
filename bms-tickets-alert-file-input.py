#!/usr/bin/python

import re, urllib, smtplib, sys

from datetime import datetime
from email.mime.text import MIMEText

def send_email(email_ids, myurl, mytheatre):
    fromaddr = "from@live.com"
    toaddrs = email_ids
    msg = ("From: %s\r\nTo: %s\r\n" % (fromaddr, ", ".join(toaddrs)))
    movie_name = re.search(".*buytickets\/([a-z0-9\-]+)\/", myurl, re.I)
    if movie_name:
        movie_name = movie_name.group(1)
    msg = msg + "Subject:Tickets available !! for " + movie_name + " at " + mytheatre + "\r\n\r\n"
    msg = msg + "Book here " + myurl
    server = smtplib.SMTP('smtp.live.com', 587)
    server.ehlo()
    server.starttls()
    server.login("from@live.com", "******")
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return

print "start:" + str(datetime.now())

if len(sys.argv) < 3:
    print "File path, email is required!"
    print "end:" + str(datetime.now())
    sys.exit()

print "File path:" + sys.argv[1]
print "emails:" + sys.argv[2]
movie_inputs = []
email_ids = sys.argv[2].split(",")

with open(sys.argv[1]) as f:
    movie_inputs = f.readlines()

for input in movie_inputs:
    movie_args = input.strip().split(" ")

    if len(movie_args) < 2:
        print "Movie link and at least one theater name is required!" + input
        continue

    movie_url = movie_args[0]
    print "Movie link:" + movie_url

    mytheatres = []
    length = len(movie_args)
    if length >= 2:
        mytheatres.append(movie_args[1])
    if length >= 3:
        mytheatres.append(movie_args[2])
    if length >= 4:
        mytheatres.append(movie_args[3])

    print "Theatre names:" + ", ".join(mytheatres)

    html_text = urllib.urlopen(movie_url).read()

    for mytheatre in mytheatres:
        my_regex = r"href=[\"\'].*" + mytheatre + r".*[\"\']"
        if re.search(my_regex, html_text, re.I):
            send_email(email_ids, movie_url, mytheatre)
            print "Tickets available !! for " + mytheatre
        else:
            print "No Tickets yet :-( for " + mytheatre

print "end:" + str(datetime.now())
