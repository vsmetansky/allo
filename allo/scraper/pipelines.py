from allo.scraper.exporters import XmlStoreItemExporter


class XmlExportPipeline(object):
    """Exports items to XML in specific format."""

    def open_spider(self, spider):
        self.file = open(spider.file_name, 'w')
        self.exporter = XmlStoreItemExporter(
            self.file, item_element='product', root_element='data')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
