#!/usr/bin/env python3

from country_levels_lib.wam.wam_collect import collect_iso, save_population


def main():
    collect_iso()
    save_population()


if __name__ == "__main__":
    main()
