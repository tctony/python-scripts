#!/usr/bin/env python
import sys
import os


def main():
    if len(sys.argv) < 5 or sys.argv[1] not in ["male", "female"]:
        print(
            "usage: python {0} male|female age height(cm) weight(kg)".format(
                os.path.basename(__file__),
            )
        )
    else:
        age = int(sys.argv[2])
        height = int(sys.argv[3])
        weight = int(sys.argv[4])
        if sys.argv[1] == "male":
            fa = -6.8
            fh = 5.0
            fw = 13.7
            extra = 66
        else:
            fa = -4.7
            fh = 1.8
            fw = 9.6
            extra = 655
        print("bmr: {0}".format(fa * age + fh * height + fw * weight + extra))


if __name__ == "__main__":
    main()
