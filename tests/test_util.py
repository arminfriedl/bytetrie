import pytest

from bytetrie import util

class TestHasCommonPrefix:
    @pytest.mark.parametrize(
        ("label", "other_label"),
        ((b"", b"val"),
         ("val", b""),
         (None, b"val"),
         (b"val", None)))
    def test_falsy_argument_false(self, label, other_label):
        assert not util.has_common_prefix(label, other_label)

    def test_first_char_differs_false(self):
        assert not util.has_common_prefix(b"ab", b"bb")

    def test_first_char_equal_true(self):
        assert util.has_common_prefix(b"ab", b"aa")

    def test_handles_different_byte_types(self):
        assert util.has_common_prefix(b"a", bytes([97]))
        assert util.has_common_prefix(bytes("a", 'utf-8'), bytes([0x61]))
        assert util.has_common_prefix(bytearray("a", 'utf-8'), bytes([0x61]))
        assert util.has_common_prefix(b"a", memoryview(bytes("a", 'utf-8')))

class TestCommonPrefix:
    @pytest.mark.parametrize(
        ("label", "other_label"),
        ((b"", b"val"),
         ("val", b""),
         (None, b"val"),
         (b"val", None)))
    def test_falsy_argument_empty(self, label, other_label):
        assert util.common_prefix(label, other_label) == bytes()

    def test_first_char_differs_empty(self):
        assert util.common_prefix(b"ab", b"bb") == bytes()

    def test_has_common_prefix_prefix(self):
        assert util.common_prefix(b"abd", b"abc") == b"ab"

    def test_handles_different_lengths(self):
        assert util.common_prefix(b"abde", b"abc") == b"ab"
        assert util.common_prefix(b"ab", b"ab") == b"ab"
        assert util.common_prefix(b"ab", b"abc") == b"ab"
        assert util.common_prefix(b"abde", b"abcde") == b"ab"

    def test_other_label_is_prefix(self):
        assert util.common_prefix(b"abc", b"ab") == b"ab"

class TestIsPrefixOf:
    @pytest.mark.parametrize(
        ("label", "other_label"),
        ((b"", b"val"),
         ("val", b""),
         (None, b"val"),
         (b"val", None)))
    def test_falsy_argument_false(self, label, other_label):
        assert not util.is_prefix_of(label, other_label)

    def test_prefix_too_long_false(self):
        assert not util.is_prefix_of(b"ab", b"a")

    def test_no_prefix_false(self):
        assert not util.is_prefix_of(b"b", b"ab")
        assert not util.is_prefix_of(b"ab", b"ac")

    def test_prefix_true(self):
        assert util.is_prefix_of(b"ab", b"abc")

class TestCutOffPrefix:
    def test_no_prefix_error(self):
        with pytest.raises(AssertionError):
            util.cut_off_prefix(b"ab", "bb")

    def test_prefix_cut_off(self):
        assert util.cut_off_prefix(b"ab", b"abc") == b"c"

    def test_equals_empyt(self):
        assert util.cut_off_prefix(b"ab", b"ab") == b""

    @pytest.mark.parametrize(
        ("prefix", "label"),
        ((b"", b"val"),
         ("val", b""),
         (None, b"val"),
         (b"val", None)))
    def test_falsy_error(self, prefix, label):
        with pytest.raises(AssertionError):
            util.cut_off_prefix(prefix, label)

    def test_does_not_modify(self):
        p = b"ab"
        l = b"abc"

        assert util.cut_off_prefix(p, l) == b"c"
        assert l == b"abc"
        assert p == b"ab"

