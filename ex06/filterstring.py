import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        string = sys.argv[1]
        number = int(sys.argv[2])

        result = ft_filter(lambda word: len(word) > number, string.split())

        print(result)

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()