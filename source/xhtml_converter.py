from lxml import etree


def convert(file_name, transform_name):
    dom = etree.parse(file_name)
    xslt = etree.parse(transform_name)
    transform = etree.XSLT(xslt)
    return transform(dom)


def write(file_name, dom):
    dom_str = etree.tounicode(dom, pretty_print=True)
    with open(file_name, 'w') as f:
        f.write(dom_str)
