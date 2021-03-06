"""
A degenerated ByteTrie fixture. ByteTrie resolves to a doubly-linked list. The
worst case scenario.

See degenerated_trie.png
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
def degenerated_trie():
    t = ByteTrie()
    ins = insert(t)
    ins("A")
    ins("AB")
    ins("ABC")
    ins("ABCD")
    ins("ABCDE")
    ins("ABCDEF")
    ins("ABCDEFG")
    ins("ABCDEFGH")
    ins("ABCDEFGHI")
    ins("ABCDEFGHIJ")
    ins("ABCDEFGHIJK")
    ins("ABCDEFGHIJKL")
    ins("ABCDEFGHIJKLM")
    ins("ABCDEFGHIJKLMN")
    ins("ABCDEFGHIJKLMNO")
    ins("ABCDEFGHIJKLMNOP")
    ins("ABCDEFGHIJKLMNOPQ")
    ins("ABCDEFGHIJKLMNOPQR")
    ins("ABCDEFGHIJKLMNOPQRS")
    ins("ABCDEFGHIJKLMNOPQRST")
    ins("ABCDEFGHIJKLMNOPQRSTU")
    ins("ABCDEFGHIJKLMNOPQRSTUV")
    ins("ABCDEFGHIJKLMNOPQRSTUVW")
    ins("ABCDEFGHIJKLMNOPQRSTUVWX")
    ins("ABCDEFGHIJKLMNOPQRSTUVWXY")
    ins("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    return t
