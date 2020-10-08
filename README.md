# Bytetrie
A fast, dependency-free, self-compressing trie with radix 256 in pure python.

Bytetrie allows fast prefix search in a large corpus of keys. Each key can be
associated with arbitrary data. It features fast lookup times at the cost of
expensive insertion. A Bytetrie is best used if it can be pre-filled with data.
However, due to its in-band compression it can be also used for on-the-fly
updates.

## Keys
Keys are byte strings. Therefore, each node in the trie can have up to 256
children (the radix). Keys do work well with utf-8 and other encodings as long
as the encoding is consistent and deterministic. That is, a grapheme clusters
are always encoded to the same byte sequence. Even if the standard allows for
ambiguity. Usually that's a non-issue as long as the same encoder is used for
insertion and lookup.

Since prefix search in unicode strings is one of the most common use-cases of
bytetrie, a unicode layer on top of bytetrie is [planned](TODO.md).

## Data
Bytetrie can associate arbitrary data (python objects) with keys. Data (or
rather a reference thereof) is kept in-tree. No further processing is done.

In addition bytrie allows multi-valued tries. Every key is then associated with
a sequence of arbitrary objects.

## Performance
Despite being in pure python bytetrie is _fast_. Sifting through the full
[geonames](http://download.geonames.org/export/dump/) "allCountries" dataset for
places starting with `Vienna` takes a mere 512µs. That's not even one
millisecond for searching through 12,041,359 places. For comparison a warmed-up
ripgrep search through the same dataset takes three orders of magnitude (400ms)
longer on the same machine.

On the downside building the trie takes about 20 minutes and considerable
memory. Also the performance is mostly trumped by the time it takes to collect
terminal nodes. That is, the higher up the trie the search ends (and hence the
more results the prefix search yields) the longer it takes. There are several
low-hanging fruits left and further performance improvements are in the
[pipeline](TODO.md).

## Dependencies
None. That's the point.

# Getting started
TODO

# Github Users
If you are visiting this repository on GitHub, you are on a mirror of
https://git.friedl.net/incubator/bytetrie. This mirror is regularily updated
with my other GitHub mirrors.

Like with my other incubator projects, once I consider `bytetrie` reasonable
stable the main tree will move to GitHub.

If you want to contribute to `bytetrie` feel free to send patches to
dev[at]friedl[dot]net. Alternatviely, you can issue a pull request on GitHub
which will be cherry picked into my tree. If you plan significant long-term
contributions drop me a mail for access to the incubator repository.
