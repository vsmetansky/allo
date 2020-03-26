from scrapy.exporters import XmlItemExporter
from xml.sax.saxutils import XMLGenerator


class XmlStoreItemExporter(XmlItemExporter):
    def start_exporting(self):
        self.xg.startDocument()
        self.xg._write(
            f'<?xml-stylesheet type="text/xsl" href="transform.xsl"?>')
        self.xg.startElement(self.root_element, {})
        self._beautify_newline(new_item=True)
