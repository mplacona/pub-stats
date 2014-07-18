#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        url = "https://www.kimonolabs.com/api/8mjgyceu?apikey=5YBvcrTB43XXYfhpnXPneBlxTg2lpH4p"
        try:
          result = urllib2.urlopen(url).read()
          retdict = json.loads(result)
          count = retdict['count']
          lastFetch = retdict['lastsuccess']
          self.response.out.write("<html>")
          self.response.out.write("<body>")
          self.response.out.write("<h1>Dart pub stats</h1>")
          self.response.out.write("<h2>There are currently ")
          self.response.out.write(count)
          self.response.out.write(" packages available</h2>")
          self.response.out.write("<p>Data last fetched on ")
          self.response.out.write(lastFetch)
          self.response.out.write("</p>")
          self.response.out.write("</body>")
          self.response.out.write("</html>")
          
        except urllib2.URLError, e:
          print(e)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
