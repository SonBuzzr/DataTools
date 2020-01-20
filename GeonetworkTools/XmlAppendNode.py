# Read and Edit xml file with namespaces using minidom
# Update user limitation
# Search for user limitation, remove empty node, append new node

import xml.dom.minidom
from xml.dom import minidom

legalNode = "gmd:MD_LegalConstraints"
ulNode = "gmd:useLimitation"
charNode = "gco:CharacterString"


# function to add/append node to xml
def append_node(main_xml):
    # print("Appending node...")
    # print(citation)
    node_string = """<?xml version="1.0" encoding="UTF-8"?> <gmd:MD_Metadata 
    xmlns:gmd="http://www.isotc211.org/2005/gmd" xmlns:gco="http://www.isotc211.org/2005/gco" 
    xmlns:gts="http://www.isotc211.org/2005/gts" xmlns:gml="http://www.opengis.net/gml" 
    xmlns:geonet="http://www.fao.org/geonetwork" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:schemaLocation="http://www.isotc211.org/2005/gmd http://www.isotc211.org/2005/gmd/gmd.xsd 
    http://www.isotc211.org/2005/srv http://schemas.opengis.net/iso/19139/20060504/srv/srv.xsd"> <gmd:useLimitation> 
    <gco:CharacterString>Free to use with attribution to the source. Suggested citation:</gco:CharacterString> 
    </gmd:useLimitation> </gmd:MD_Metadata> """
    # print(node_string)
    add_xml = xml.dom.minidom.parseString(node_string)
    intNode = main_xml.getElementsByTagName(legalNode)[0]
    update_node = add_xml.getElementsByTagName(ulNode)[0]

    intNode.insertBefore(update_node, intNode.firstChild)
    # intNode.firstChild(update_node)
    # intNode.appendChild(update_node)
    print(main_xml.toxml())
    return main_xml


def main():
    xmlFile = 'xmlfile.xml'
    i = 0

    # Parsing xml file
    metaXml = xml.dom.minidom.parse(xmlFile)
    # print(metaXml.toxml())

    topNode = metaXml.getElementsByTagName(legalNode)

    # Loop through each and every child node
    for firstChild in topNode:
        fChild = firstChild.getElementsByTagName(ulNode)

        # Check if node has child or not
        if not fChild.length:
            print("No child node adding New Node ...")
            addUL = append_node(metaXml)

        #  List all the child node value
        else:
            for i, child in enumerate(fChild):
                print("index {}, value {}".format(i, child))
                lastChild = child.getElementsByTagName(charNode)[0]

                # check for blank user limitation
                # Remove child of the node with empty field
                # Create updated user limitation node
                if not lastChild.childNodes.length:
                    print("Removing empty node with index {} and appending value ...".format(i))
                    fChild[0].parentNode.removeChild(fChild[i])
                    appendUL = append_node(metaXml)
                else:
                    print("Node values: {} with index {}".format(lastChild.childNodes[0].nodeValue, i))

    return metaXml


if __name__ == "__main__":
    main()
