import pytest

import sys
import os

from bytetrie import ByteTrie

sys.path.append("tests/tries/")
import simple_trie
import degenerated_trie

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

def test_degenerated_find_first_finds_all(degenerated_trie):
    r = degenerated_trie.find(b"A")
    assert len(r) == 26
    assert r[0].key() == b"A"
    assert r[0].value() == "A"

    assert r[25].key() == b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert r[25].value() == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def test_degenerated_find_last_finds_one(degenerated_trie):
    r = degenerated_trie.find(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert len(r) == 1
    assert r[0].key() == b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert r[0].value() == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
