import xml.etree.ElementTree as tree_element

data = '''<person>
    <name>Chuck</name>
    <email hide="yes" />
</person>'''

tree = tree_element.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
