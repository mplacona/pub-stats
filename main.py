import webapp2
import urllib2
import json
from google.appengine.api import memcache
import datetime

url = "https://www.kimonolabs.com/api/8mjgyceu?apikey=5YBvcrTB43XXYfhpnXPneBlxTg2lpH4p"
date = datetime.datetime.now()
memcache_key = date.strftime('%Y%m%d')

class MainHandler(webapp2.RequestHandler):
    def get(self):
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
            <!DOCTYPE html>
            <html lang='en-us' itemscope itemtype='http://schema.org/Product'>
                <head>
                    <title>Dart pub stats</title>
                    <meta itemprop='image' content='https://www.dartlang.org/imgs/dart-logo-wordmark-1200w.png'>
                    <meta itemprop='name' content='Dart pub stats'>
                    <meta name='description' content='Statistical information about the Dart&quot;s Pub repositoty'>
                    <meta itemprop='description' content='Statistical information about the Dart&quot;s Pub repositoty'>
                    <script>
                      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                      ga('create', 'UA-53102965-1', 'auto');
                      ga('send', 'pageview');

                    </script>
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

class JsonHandler(webapp2.RequestHandler):
    def get(self):
        try:
            result = memcache.get(memcache_key)
            if result is not None:
                result = result
            else:
                result = urllib2.urlopen(url).read()
                memcache.add(memcache_key, result)

            self.response.headers['Content-Type'] = 'application/json'   
            retdict = json.loads(result)
            self.response.out.write(json.dumps(retdict))
        except urllib2.URLError, e:
            print(e)
        
    
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/json', JsonHandler),
], debug=True)
