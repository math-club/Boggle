
from typing import Iterable, Sequence, TypeVar


T = TypeVar("T")


def chunked(seq: Sequence[T],
            n: int) -> Iterable[T]:
    """Returns an iterable that contains given iterable separated into n
    bundles.
    """
    return (seq[chunk:chunk + n]
            for chunk in range(0, len(seq), n))
