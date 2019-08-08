from lxml.etree import Element


def sort_elements(root: Element):
    print(root.tag)
    root[:] = sorted(root, key=lambda child: (child.tag, child.get('name')))
    children = list(root)
    for c in children:
        sort_elements(c)
        sort_attributes(c)


def sort_attributes(root):
    for el in root.iter():
        attrib = el.attrib
        if len(attrib) > 1:
            attributes = sorted(attrib.items())
            attrib.clear()
            attrib.update(attributes)