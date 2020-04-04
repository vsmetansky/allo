"""Module to convert XML using XSL transformation.

Exported functions:
    convert: Constructs ElementTree using XSL transformation.
    write: Writes ElementTree string to file.
"""

from lxml import etree


def convert(file_name, transform_name):
    """Constructs ElementTree using XSL transformation.

    Returns:
        Result of lxml XSL transformation.
    """

    dom = etree.parse(file_name)
    xslt = etree.parse(transform_name)
    transform = etree.XSLT(xslt)
    return transform(dom)


def write(file_name, dom):
    """Writes ElementTree string to file."""
    dom_str = etree.tounicode(dom, pretty_print=True)
    with open(file_name, 'w') as f:
        f.write(dom_str)
