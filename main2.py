import xml.etree.ElementTree as ET


def square(x, y, n):
    res = 0
    for i in range(0, n - 1):
        res += x[i] * y[i+1]
    res += x[n-1] * y[0]
    for i in range(0, n - 1):
        res -= x[i+1] * y[i]
    res -= x[0] * y[n-1]
    return 0.5*res


tree = ET.parse("21.osm")
root = tree.getroot()
max_Square = 0
id_max = 0
nodes = dict()


for child in root:
    if child.tag == "node":
        nodes[child.get("id")] = (child.get("lat"), child.get("lon"))
    if child.tag == "way":
        nds = child.findall('nd')
        if nds[0].get("ref") == nds[-1].get("ref"):
            for tag in child.findall('tag'):
                if tag.get("k") == 'building':
                    x = []
                    y = []
                    for nd in nds:
                        node = nodes[nd.get("ref")]
                        x.append(float(node[0]))
                        y.append(float(node[1]))
                    s = square(x, y, len(nds))
                    if s > max_Square:
                        max_Square = s
                        id_max = child.get("id")
print(id_max)
