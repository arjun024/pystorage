#!/usr/bin/env python
# Copyright (c) 2014 Arjun Sreedharan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__author__ = "Arjun Sreedharan (arjun024@gmail.com)"


import wsgiref.handlers
from google.appengine.api import urlfetch
import webapp2

urlfetch.set_default_fetch_deadline(60)


########## CHANGE THESE TO REFLECT YOUR PERSONAL SETTINGS ##############
# Your Dropbox user-id  and folder-name. 
# Your public folder have the will have the following syntax: 
# dl.dropboxusercontent.com/u/<USERID>/<YOURFOLDER>/examplefile
# If you want to use the entire "Public" folder, set DROPBOX_FOLDER = ""
DROPBOX_USERID = "<USERID>"
DROPBOX_FOLDER = "<YOURFOLDER>"
########################################################################


class DboxHandler(webapp2.RequestHandler):
  def get(self, url_path):
    slash_position = self.request.url.find("/", len(self.request.scheme + "://"))
    if slash_position == -1:
      dropbox_url = "http://"
    else:
      dropbox_path = "" if DROPBOX_FOLDER == "" else "/" + DROPBOX_FOLDER
      dropbox_url = "http://dl.dropbox.com/u/" + DROPBOX_USERID + dropbox_path + self.request.url[slash_position:]

    fetched = urlfetch.fetch(dropbox_url)

    if fetched.status_code == 200:
      for key, value in fetched.headers.iteritems():
        self.response.headers[key] = value
      self.response.out.write(fetched.content)

    else:
      self.response.status = fetched.status_code
      self.response.out.write("Error: status code:" + str(fetched.status_code))


app = webapp2.WSGIApplication([
  (r"/(.*)", DboxHandler)
], debug=False)