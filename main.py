import webapp2
import urllib2
import json
from google.appengine.api import memcache
import datetime

class MainHandler(webapp2.RequestHandler):
    def get(self):
        url = "https://www.kimonolabs.com/api/8mjgyceu?apikey=5YBvcrTB43XXYfhpnXPneBlxTg2lpH4p"
        date = datetime.datetime.now()
        memcache_key = date.strftime('%Y%m%d')
        try:
          result = memcache.get(memcache_key)
          if result is not None:
              result = result
          else:
              result = urllib2.urlopen(url).read()
              memcache.add(memcache_key, result)
          
          retdict = json.loads(result)
          count = retdict['count']
          lastFetch = retdict['lastsuccess']
          template = """
          <html>
                <head>
                    <title>Dart pub stats</title>
                    <meta itemprop='image' content='https://www.dartlang.org/imgs/dart-logo-wordmark-1200w.png'>
                    <meta itemprop='description' content='Statistical information about the Dart's Pub repositoty'>
                </head>
                <body>
                        <h1>Dart pub stats</h1>
                        <h2>There are currently %s packages available</h2>
                        <p>Data last fetched on %s</p>
                </body>
          </html>
          """
          self.response.out.write(template %(count, lastFetch))
        except urllib2.URLError, e:
          print(e)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
