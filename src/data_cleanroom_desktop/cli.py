import argparse
from data_cleanroom_desktop.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Desktop data cleanup utilities for CSV harmonization and audit notes.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
