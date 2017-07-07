import re, urllib, smtplib

from email.mime.text import MIMEText

print "Enter the bookmyshow movie url (with double quotes).."
myurl = "https://in.bookmyshow.com/buytickets/ninnu-kori-hyderabad/movie-hyd-ET00053894-MT/20170707"
print "Enter the bookmyshow theatre name (with double quotes).."
mytheatre = "svc-cinemas-eeshwar-attapur"
my_regex = r"href=[\"\'].*" + mytheatre + r".*[\"\']"

if re.search(my_regex, urllib.urlopen(myurl).read(), re.I):
	fromaddr = "from@live.com"
	toaddrs = ["to@email.com"];
	msg = ("From: %s\r\nTo: %s\r\n" % (fromaddr, ", ".join(toaddrs)))
	msg = msg + "Subject:Tickets available !! for " + mytheatre + "\r\n\r\n"
	msg = msg + "Tickets available.\n"
	server = smtplib.SMTP('smtp.live.com', 587)
	server.ehlo()
	server.starttls()
	server.login("from@live.com", "******")
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
	print "Tickets available !! for " + mytheatre
else:
    print "No Tickets yet :-( for " + mytheatre
