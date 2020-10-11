import csv
from bytetrie import ByteTrie

def load_geonames():
    t = ByteTrie(multi_value=True)
    with open("cities500.txt", "r") as f:
        reader = csv.reader(f, delimiter='\t')
        for i, row in enumerate(reader):
            try:
                t.insert(row[1].encode("utf-8"), row[17])
            except Exception:
                print(f"Error in row {i}")
                print(f"Label: '{row[1]}'")
                print(f"Type: {type(row[1])}")
                raise
    return t

def insert(trie):
    """ Shall only be used to insert strings """
    t = trie
    def _insert(*vals):
        for val in vals:
            t.insert(val.encode('utf-8'), val)
    return _insert

def load_simple_trie():
    t = ByteTrie()
    ins = insert(t)
    ins("A")
    ins("AA", "AB")
    ins("ABCDE")
    ins("AACDEF", "AACDEGG", "AACDEH")
    return t

# This uses internal representations which are not supposed to
# be used as public API and are subject to change!
from bytetrie.bytetrie import ByteTrie, Node, Root, Child, Terminal
def geonames_to_dot(t: ByteTrie):
    dot_buffer = str()
    dot_buffer += """strict digraph {
    graph [
        bgcolor="transparent"
    ];

    edge [
        arrowhead="none",
        penwidth="0.05",
    ];

    node [
        label="",
        sep="2"
    ];

    root [shape="circle", width="0.4"]
    """

    hue_inc = 1/len(t.root.children)
    hue = 0

    for child in t.root.children:
        dot_buffer += _geonames_node_to_dot(t.root, child, 1, hue)
        hue += hue_inc

    dot_buffer += "}"
    return dot_buffer

def _geonames_node_to_dot(p: Node, n: Child, depth, hue):
    db = f'{p.dot_id()} -> {n.dot_id()} [color="{hue},{depth*0.1},85"]\n'
    db += f'{n.dot_id()} [color="{hue},{depth*0.1},50", shape="circle", width="0.1"]\n'

    for child in n.children:
        db += _geonames_node_to_dot(n, child, depth+1, hue)

    return db


if __name__ == "__main__":
    t = load_geonames()
    s = geonames_to_dot(t)
    with open("geo_dot.dot", "w") as f:
        f.write(s)
