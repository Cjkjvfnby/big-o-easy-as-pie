from enum import Enum
from typing import Callable, NamedTuple

import matplotlib.pyplot as plt
import numpy as np


class Color(Enum):
    CONSTANT = "orange"
    LINEAR = "green"
    QUADRATIC = "dodgerblue"
    DIFF = "tomato"
    DIFF2 = "deeppink"


class Function(NamedTuple):
    function: Callable
    title: str
    color: Color

    def draw(self, x):
        y = self.function(x)
        plt.plot(x, y, self.color.value, label=self.title)


def get_figure(
    title: str, functions: list[Function], size=10, scale="linear", points=100
):
    fig = plt.figure()
    x = np.arange(0, size, 1 / points)
    for f in functions:
        f.draw(x)
    plt.title(title)

    plt.xscale(scale)
    plt.yscale(scale)
    plt.xlim(0, size)
    plt.ylim(0, size)

    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid()
    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")
    plt.legend()
    return fig


constant = Function(lambda x: [1] * len(x), "y = 1", Color.CONSTANT)


linear = Function(lambda x: x, "y = x", Color.LINEAR)

quadratic = Function(lambda x: x * x, "y = x^2", Color.QUADRATIC)

if __name__ == "__main__":
    res = get_figure(
        "title", [quadratic, linear, constant], size=100, scale="log", points=100
    )
    res.show()
