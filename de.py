import json
import xml.etree.ElementTree as ET

with open('countryCodes.json', 'r') as json_file:
    json_data = json.load(json_file)

# Convert JSON to XML
def json_to_xml(json_data, parent=None):
    if isinstance(json_data, dict):
        if parent is None:
            parent = ET.Element('root')
        for key, value in json_data.items():
            element = ET.SubElement(parent, key)
            json_to_xml(value, element)
        return parent
    elif isinstance(json_data, list):
        for item in json_data:
            json_to_xml(item, parent)
    else:
        parent.text = str(json_data)
        return parent

xml_root = json_to_xml(json_data)

# Create an ElementTree object and write to XML file
xml_tree = ET.ElementTree(xml_root)
xml_tree.write('countryCodes.xml', encoding='utf-8', xml_declaration=True)