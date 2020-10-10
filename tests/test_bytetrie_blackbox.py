import pytest

import sys
import os
sys.path.append("tests/tries/")

from bytetrie import ByteTrie

import simple_trie

def test_find_all(simple_trie):
    r = simple_trie.find(b"A")
    ls = [n.value() for n in r]
    expected = ["A", "AA", "AACDEGG", "AACDEF", "AACDEH", "AB", "ABCDE"]
    not_expected = ["AACDE"]

    for e in expected:
        assert e in ls
    for ne in not_expected:
        assert not ne in ls

def test_find_single_terminal(simple_trie):
    r = simple_trie.find(b"AACDEH")
    assert len(r) == 1
    assert r[0].value() == "AACDEH"
    assert r[0].key() == b"AACDEH"

def test_unknown_prefix_empty(simple_trie):
    r = simple_trie.find(b"AAD")
    assert len(r) == 0

def test_partial_prefix_find_subnodes(simple_trie):
    r = simple_trie.find(b"AACD")
    ls = [n.value() for n in r]

    expected = ["AACDEGG", "AACDEF", "AACDEH"]
    not_expected = ["A", "AA", "AB", "ABCDE", "AACDE"]

    assert len(r) == 3
    for e in expected:
        assert e in ls
    for ne in not_expected:
        assert not ne in ls

def test_partial_prefix_find_terminal(simple_trie):
    r = simple_trie.find(b"ABC")
    assert len(r) == 1
    assert r[0].key() == b"ABCDE"
    assert r[0].value() == "ABCDE"
