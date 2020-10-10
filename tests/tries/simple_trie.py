"""
Create a simple ByteTrie fixture for testing basic functionality. Without edge
cases. Single-valued.

See simple_trie.png
"""

import pytest

from bytetrie import ByteTrie

def insert(trie):
    """ Shall only be used to insert strings """
    t = trie
    def _insert(*vals):
        for val in vals:
            t.insert(val.encode('utf-8'), val)
    return _insert

@pytest.fixture
def simple_trie():
    t = ByteTrie()
    ins = insert(t)
    ins("A")
    ins("AA", "AB")
    ins("ABCDE")
    ins("AACDEF", "AACDEGG", "AACDEH")
    return t
