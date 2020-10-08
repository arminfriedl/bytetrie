# Benchmarking
- Gather some general benchmarks and performance behavior
- Compare with other implementations:
    - https://github.com/jfjlaros/dict-trie
    - https://github.com/dcjones/hat-trie
    - https://github.com/fnl/patricia-trie
    - https://github.com/pytries/marisa-trie
    - https://github.com/soumasish/poetries
    - https://github.com/mischif/py-fast-trie

# Profiling
Find optimization possibilites

- Memory usage looks too high. Find if something leaks references and cannot be
  garbage collected.
- Initial creation is expected to take most time. The trie optimizes for
  retrieval. But if there are low hanging fruits left they could be picked up.
- Lookup time is dominated by gathering the terminals especially in nodes high
  up in the trie. To some extend expected and unavoidable, still any possible
  optimizations there are highly desired. Additionally, a limit search could be
  introduced to stop gathering after x terminals.

# Testing and Verification
Tests and correctness verification is currently glaringly lacking. Any
improvements there are highly desired.

# Future Extensions
- A unicode layer on top of bytetrie for simpler handling of string keys
- Key deletion
- Make insertion multi-threaded
