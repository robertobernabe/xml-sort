import argparse
from lxml import etree
from xml_sort import sort_elements


def main():
    parser = argparse.ArgumentParser(description='Sorting an xml file.')
    parser.add_argument('xmlFilePath', metavar='file', type=str, nargs='+',
                        help='path to xml file')

    args = parser.parse_args()

    for filePath in args.xmlFilePath:

        xmlParser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(filePath, xmlParser)
        root = tree.getroot()
        sort_elements(root)
        tree.write(filePath, pretty_print=True)


main()