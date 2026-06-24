import os


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_len = 65

    for i, item in enumerate(lst, 1):
        percent = i / total
        filled = int(bar_len * percent)

        bar = "=" * filled
        if filled < bar_len:
            bar += ">"
            bar += " " * (bar_len - filled - 1)

        print(f"\r{percent:3.0%}|[{bar}]| {i}/{total}",end="",flush=True)

        yield item

    print()