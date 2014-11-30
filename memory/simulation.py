from memory.memory import (
    FirstInFirstOutAlgorithm,
    TheOptimalAlgorithm,
    LastRecentlyUsedAlgorithm,
    ApproximalLastRecentlyUsedAlgorithm
)

PAGE_SIZE = 100
FRAMES = 10

NUM_REQUESTS = 500


def test():
    algorithms = [
        FirstInFirstOutAlgorithm(),
        TheOptimalAlgorithm(),
        LastRecentlyUsedAlgorithm(),
        ApproximalLastRecentlyUsedAlgorithm()
    ]


if __name__ == "__main__":
    test()

# spr czy jest w ramkach