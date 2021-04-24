# score.py

from typing import Iterator, NoReturn, Tuple


Score = Tuple[str, int]


class ScoreManager:
    """Encapsulate a score manager."""
    file_path = "data/best_scores.txt"

    @classmethod
    def register(cls, name: str, value: int) -> NoReturn:
        """Save a score in a save file."""
        with open(cls.file_path, "a") as f:
            f.write(f"{name}: {value}\n")

    @classmethod
    def load(cls) -> Iterator[Score]:
        """Yield one by one all score parsed already registered."""
        for line in open(cls.file_path):
            line = line.strip()
            if line:
                name, value = line.split(": ")
                yield name, int(value)

    @classmethod
    def get_best(cls, nb: int = 10) -> Tuple[Score]:
        """Return a list of best score. Parameter nb corresponding to
        the number of scores gived at output.
        """
        scores = cls.load()
        sorted_scores = sorted(scores,
                               key=lambda x: x[1],
                               reverse=True)

        return tuple(sorted_scores[:nb])
