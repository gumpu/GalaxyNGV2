#Possible technologies

##Languages

On the client side only javascript seems to be an option.

##Graphics

We need to draw a map of the galaxy and show graphs.
Two possible canvases to do this on are:

1. HTML5 Canvas
2. SVG - Better but not widely supported.

##Toolkits

1. YUI
2. MooTools
3. KineticJS
4. jQuery  - seems to be the standard.
5. jQueryGui
6. Node.js
7. jCanvas -- jQuery like API on top of HTML5 Canvas.
   <http://calebevans.me/projects/jcanvas/>

##Data exchange 

Server and client need to exchange reports, orders, and forecasts.
Possible dataformats for these:

1. XML - Yuck.
2. JSON - Easy to process in Javascript.

##Development

1. Firebug
2. jslint
3. nodejs  - javascript on the command line!

##Pipeline

[webserver python] -> [report in json] -> [client javascript]

##Webserver

1. CherryPie - Maybe, but is an extra dependency.
2. Django - over kill
3. SimpleHTTPServer - Works out of the box.

#Development

To test run

    python -m SimpleHTTPServer

Then browse to <http://0.0.0.0:8000/gng.html>.


#Resources

1. <http://www.json.org/js.html>
2. <http://jqfundamentals.com/>
3. <https://developer.mozilla.org/en-US/docs/HTML/Canvas/Tutorial>
4. <http://www.ibm.com/developerworks/web/library/wa-games/>
5. <https://developer.mozilla.org/en-US/docs/JavaScript/A_re-introduction_to_JavaScript>
6. <https://github.com/rwldrn/idiomatic.js>
7. <http://www.masswerk.at/JavaPac/JS-PacMan2.html>
8. <http://javascript.crockford.com/code.html>  Coding standard



vi: spell spl=en ft=markdown
