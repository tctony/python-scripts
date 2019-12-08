#!/usr/bin/env python
import sys
import os
import math


def main():
    if len(sys.argv) < 2:
        print("usage: python {0} calorie(KJ)".format(os.path.basename(__file__),))
    else:
        calorie = int(sys.argv[1])
        c = math.ceil(calorie * 0.5 / 4)
        p = math.ceil(calorie * 0.3 / 4)
        f = math.ceil(calorie * 0.2 / 9)
        print("carbonhydrate {0}g\nprotein {1}g\nfat {2}g".format(c, p, f))


if __name__ == "__main__":
    main()
