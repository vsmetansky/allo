"""Provides 'scraper' with class for XML serialization.

Exported classes:
    XmlStoreItemExporter: Used to serialize scraped data into XML.
"""

from scrapy.exporters import XmlItemExporter
from xml.sax.saxutils import XMLGenerator


class XmlStoreItemExporter(XmlItemExporter):
    """Used to serialize scraped data into XML.
    
    Overrides methods of XmlItemExporter for XML serialization
    in specific format.
    """

    def start_exporting(self):
        self.xg.startDocument()
        self.xg._write(
            f'<?xml-stylesheet type="text/xsl" href="transform.xsl"?>')
        self.xg.startElement(self.root_element, {})
        self._beautify_newline(new_item=True)
