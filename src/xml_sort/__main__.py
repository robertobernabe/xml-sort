from lxml import etree
from . import sort_elements


def main():
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse("", parser)
    root = tree.getroot()
    sort_elements(root)
    tree.write("", pretty_print=True)


main()