from bs4 import BeautifulSoup
import re
import networkx as nx
import os

for dirname, dirnames, filenames in os.walk('C:\Users\edanw_000\Documents\PhD\cognitive mapping\VUE\Year 4'):
    # print path to all filenames.
    for filename in filenames:
        # print os.path.join(dirname, filename)
        with open(os.path.join(dirname, filename)) as file:
            xml = file.read()
        xml = re.sub("<child ID", "<child identity", xml, 0, re.I | re.M | re.DOTALL)
        soup = BeautifulSoup(xml)
        G = nx.Graph()
        out = os.path.join(dirname, filename)[:-4] + ".graphml"
        ids = soup.findAll("child")

        for item in ids:
            if item['xsi:type'] == "node":
                try:
                    label = item['label']
                    label = re.sub("\n", " ", label, 0, re.I | re.M | re.DOTALL)
                    label = re.sub("\ \ ", " ", label, 0, re.I | re.M | re.DOTALL)
                    G.add_node(item['identity'], created=item['created'], x=item['x'], y=item['y'], width=item['width'], height=item['height'], fillColor=item.fillcolor.get_text(), strokeColor=item.strokecolor.get_text(), label=label)
                except:
                    G.add_node(item['identity'], created=item['created'], x=item['x'], y=item['y'], width=item['width'], height=item['height'], fillColor=item.fillcolor.get_text(), strokeColor=item.strokecolor.get_text())
        
            try:
                G.add_edge(item.id1.string, item.id2.string)
            except:
                continue
            
        nx.write_graphml(G, out)
        print("saved " + out)