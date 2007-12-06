This is how I created the HTML for the API docs. 2 parts.

I found 'dumpObj.py' on Activestate at 
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/137951 
which does a nice job of dumping out object properties to the
console. There's a few bugs in it that I fixed, but mostly I 
made it so that it can dump XML into a file as well. You use
it like this..

0. Place dumpObj.py in your LiveTelnet directory
1. Telnet into LiveTelnet, and in the CLI type 'import dumpObj'
2. Then you can dump an object into XML by typing 'dumpObj.dumpXML(OBJECT, "C:\path\to\save.xml")'

In my case I created a doc=Live.Application.get_application().get_document()
and started out with 'dumpobj.dumpXML(doc, "C:\song.xml")'

After that I post-processed by using 'python_object_xml2html.pl' which is an ugly
as sin perl program that dumps the XML into some human readable HTML. I should
note there are all sorts of nice ID tags so if some person with design skill feels
like throwing together a better live.css I'll name my first child after you
if I ever get around to making one.

-Nathan



