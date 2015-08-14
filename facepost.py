#!/usr/bin/python
# -*- coding: utf-8 -*-

import facebook
import os, sys, argparse

os.system("clear")

# get a token here: https://developers.facebook.com/tools/explorer/
token = ''

graph = facebook.GraphAPI(token)
user = graph.get_object("me")
friends = graph.get_connections(user["id"], "friends")
name = user['name']                                             # get name
gender = user['gender']                                         # get gender
email = user['email']                                           # get email
bday = user['birthday']                                         # get d.o.b
status = user['relationship_status']                            # get relationship status
significant = user['significant_other']                         # get spouse
location = user['location']                                     # get location
fblang = user['locale']                                         # get fb language settings
timezone = user['timezone']                                     # get timezone

print("=") * 60
print("Name: %s" % name)
print("Gender: %s" % gender)
print("Email: %s" % email)
print("Status: %s" % status)
print("Significant Other: %s" % significant)
print("D.O.B: %s" % bday)
print("Location: %s" % location)
print("Language: %s" % fblang)
print("Timezone: %s" % timezone)
print("Friends: %s" % friends)
print("=") * 60

def writePost():
   msgPost = sys.argv[1]
   graph.put_object("me", "feed", message=msgPost)
   print("Just posted the message: %s" % msgPost)

writePost()
