pub-stats
=========

Stats about Dart Pub Packages
------------

I wanted to know how many packages we currently had on [Pub Package Manager - Dart](https://pub.dartlang.org/). Because of the way it's been built, there didn't seem to be a way to get this information, so I wrote a little scrapper that would navigate through all the pages, and get information about the packages as well as quantities.

I programmed it in such way that it will only scrape the website once a day, as to not overload the servers.

I have also created an app-engine application that displays this information in a nice(ish) format. It also gives you acces to the JSON file I'm creating, which is also cached as to not overload my app-engine account :-)

Live example can be seen on [http://pub-stats.appspot.com/](http://pub-stats.appspot.com/)

If you want to use the JSON, you can pick it up on [http://pub-stats.appspot.com/json](http://pub-stats.appspot.com/json). 

**Disclaimer 1: Feel free to use any information from here, but do not rely too much on it. As I previously mentioned, I'm scraping a website to get this information, and the process is likely to break if the markup were to change.**

**Disclaimer 2: i;m in no way associated with either Google or Dart, and this little application is in no way endorsed by either of them**
