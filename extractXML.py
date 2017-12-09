import xml.etree.ElementTree as ET

def extractXML(path):

    tree = ET.parse(path)
    root = tree.getroot()

    PDF = [[]]
    nr_tabel = 0
    nr_pagina = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    for child in root.iter():
        #if (child.tag == "table"):
            #nr_tabel = child.attrib['id']
        if ( child.tag == "region" ):
            nr_pagina = child.attrib['page']
        if ( child.tag == "bounding-box"):
            x1 = child.attrib['x1']
            y1 = child.attrib['y1']
            x2 = child.attrib['x2']
            y2 = child.attrib['y2']
            boundaries = [int(x1), int(y1), int(x2), int(y2)]

            #print nr_pagina, nr_tabel, x1, y1, x2, y2
            if(len(PDF) == int(nr_pagina)):
                PDF[int(nr_pagina) - 1].append(boundaries)
            else:
                while len(PDF) < int(nr_pagina):
                    PDF.append([])
                PDF[int(nr_pagina) - 1].append(boundaries)

    return PDF
