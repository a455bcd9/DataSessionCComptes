import xml.etree.ElementTree as ET
from lxml import etree

# tree = ET.parse('fulltext.html')
# html = etree.HTML('/fulltext.html')
parser = etree.HTMLParser()
tree = etree.parse("fulltext.html", parser)
# tree = etree.fromstring(tree)
result = etree.tostring(tree, pretty_print=True, method="html")
print(result)
# root = tree.getroot()