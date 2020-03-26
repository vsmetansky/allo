import argparse
from os.path import splitext

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from xhtml_converter import convert, write


def file_to_xhtml(file_name):
    pass


def read_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file-name', dest='file_name',
                        type=str, default='data.xml')
    parser.add_argument('-n', '--item-num', dest='item_num',
                        type=int, default=20)

    return parser.parse_args()


def run():
    args = read_args()
    process = CrawlerProcess(get_project_settings())

    process.crawl('store_item_spider',
                  item_num=args.item_num, file_name=args.file_name)
    process.start()
    name_base = splitext(args.file_name)[0]
    write(f'{name_base}.xhtml', convert(f'{name_base}.xml', 'transform.xsl'))


if __name__ == '__main__':
    run()
