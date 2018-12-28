
from framework import *
from output import *


def main():
    m = menuet.Menuet(transkey=-1)
    m.generate()

    c = convert_to_score.Converter(m)
    score = c.convert_menuet()

    # print(score)

    g = ly_generator.Generator()
    g.create("score.ly")
    g.add(score)
    g.write_and_close()
    g.build()


if __name__ == '__main__':
    main()
