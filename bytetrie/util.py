def has_common_prefix(label: ByteString, other_label: ByteString) -> bool:
    """ Whether label and other_label have a prefix in common. """
    assert label and other_label
    return True if label[0] == other_label[0] else False

def common_prefix(label: ByteString, other_label: ByteString) -> ByteString:
    """ Get the common prefix of label and other_label. """
    buffer = bytearray()
    for (a,b) in zip(label, other_label):
        if a == b: buffer.append(a)
        else: break
    return buffer

def is_prefix_of(prefix: ByteString, label: ByteString) -> bool:
    """ Whether label starts with prefix """
    if len(prefix) > len(label):
        return False
    for (a,b) in zip(prefix, label):
        if a != b: return False
    return True

def find_first(predicate, iterable):
    """ Return the first element in iterable that satisfies predicate or None """
    try: return next(filter(predicate, iterable))
    except StopIteration: return None

def cut_off_prefix(prefix: ByteString, label: ByteString) -> ByteString:
    """ Cut prefix from start of label. Return rest of label. """
    assert is_prefix_of(prefix, label)
    return bytes(label[len(prefix):])
