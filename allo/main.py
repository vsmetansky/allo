"""Main module of the package, runs and setups it."""

import os
import argparse
import pathlib

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from allo.xhtml_converter import convert, write

SETTINGS_PATH = 'allo.scraper.settings'


def setup():
    """Prepares package for running."""
    os.environ['SCRAPY_SETTINGS_MODULE'] = SETTINGS_PATH

def transform_path():
    """Returns path to .xsl transformation."""
    return str(pathlib.Path(__file__).parent.absolute())

def read_args():
    """Reads command line argumens.

    Returns:
        Populated Namespace object.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file-name', dest='file_name',
                        type=str, default='data.xml', help='Name of file for XML serialization.')
    parser.add_argument('-n', '--item-num', dest='item_num',
                        type=int, default=20, help='Number of pages that should be scraped.')

    return parser.parse_args()


def run():
    """Setups and runs 'store_item_spider', converting newly created .xml file to .xhtml."""
    setup()
    args = read_args()

    process = CrawlerProcess(get_project_settings())
    process.crawl('store_item_spider',
                  item_num=args.item_num, file_name=args.file_name)
    process.start()

    name_base = os.path.splitext(args.file_name)[0]
    write(f'{name_base}.xhtml', convert(f'{name_base}.xml', transform_path() + '/transform.xsl'))


if __name__ == '__main__':
    run()
