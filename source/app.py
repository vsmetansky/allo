import argparse

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


def read_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file-name', dest='file_name',
                        type=str, default='data.xml')
    parser.add_argument('-n', '--item-num', dest='item_num',
                        type=int, default=5)

    return parser.parse_args()


def run():
    args = read_args()
    process = CrawlerProcess(get_project_settings())

    process.crawl('store_item_spider',
                  item_num=args.item_num, file_name=args.file_name)
    process.start()


if __name__ == '__main__':
    run()
