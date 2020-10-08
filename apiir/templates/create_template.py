from shutil import copyfile
import xml.etree.ElementTree as ET
from xml.dom import minidom

def NewFile(filePath, fileNames='None', rootTemplate="/home/marcus/Code/APIIR/apiir/templates/analysis_dirElement.xml"):
    # copyfile("/home/marcus/Code/APIIR/apiir/templates/analysis_dirElement.xml", filePath)
    
    # parsing the template xml file as an Elementree, and acessing the root element:
    tree = ET.parse(rootTemplate)
    root = tree.getroot()

    # naming the dir:
    root.attrib['dirName'] = 'testing'

    # parsing and acessing the moviElement
    if isinstance(fileNames, list):
        for (i, name) in enumerate(fileNames):
            print(name)
            movieElement = ET.parse('/home/marcus/Code/APIIR/apiir/templates/analysis_movieElement.xml').getroot()
            # set analysis name
            movieElement.attrib['fileName'] = name

            # insert movieElement into parsed root
            root.insert(i, movieElement)

    # writing the tree to file:

    # tree.write(filePath) # writes the same format as template

    with open(filePath, mode='w') as f: # prettyprintes, takes alot of space
        f.write(prettify(root))

def prettify(elem): 
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='\t', newl='\n')


    



NewFile('/home/marcus/Code/APIIR/apiir/templates/test.xml', fileNames=['test1', 'test2', 'test3'])

