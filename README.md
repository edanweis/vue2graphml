vue2graphml
===========

Converts VUE (Visual Understanding Environment) files into graphml formated files.
--------------------------

Here is some very rough I-just-learned-to-program python code which you can use to convert the kind of XML directed labeled graphs produced in VUEs own XML format. 

People, if you have a better way of parsing VUE's XML into graphml - please fork this repo and show me how it's done!


Features
-------

* Converts all files under a given directory
* Translates node attributes: label, width, height, x position, y position, timestamp, fill and stroke.


Instructions
--------

You must provide the correct path:

```python
for dirname, dirnames, filenames in os.walk('C:\Users\your\path\goes\here'):
```

Note
-------

This script not convert edge labels or links between edges. Also, it is recommended to format the resulting graph in [yED](http://www.yworks.com/en/products_yed_about.html) using the Edit > Properties Mapper. Once opened in yED, map the data attributes to native yED ones.


Python modules dependencies
---------------

* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/#Download)
* [networkx](http://networkx.github.io/)

Todo:
------

- [ ] Add labeled edges to .graphml formats (?)
- [ ] Drag 'n drop ?