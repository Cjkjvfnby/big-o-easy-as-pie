from pathlib import Path

from draw_graphs.functions import (
    Color,
    Function,
    constant,
    get_figure,
    linear,
    quadratic,
)

linear_plus = Function(lambda x: x + 1, "y = x + 1", Color.DIFF)

quadratic_plus = Function(lambda x: x * x + x, "y = x^2 + x", Color.DIFF)


linear_mul = Function(lambda x: x * 2, "y = 2x", Color.DIFF)

quadratic_mul = Function(lambda x: (x * x) / 2, "y = x^2 / 2", Color.DIFF2)


def main():
    base = Path(__file__).parent.parent / "_static" / "images"

    images = [
        ("Constant", "constant.png", [constant], {}),
        ("Linear", "linear.png", [linear], {}),
        ("Quadratic", "quadratic.png", [quadratic], {}),
        ("All together", "all.png", [constant, linear, quadratic], {}),
        ("Intersection", "close_scale.png", [linear, quadratic], {"size": 2}),
        ("O(n)", "linear_plus.png", [linear, linear_plus], {}),
        ("O(n^2)", "quadratic_plus.png", [quadratic, quadratic_plus], {}),
        (
            "Coefficients compare",
            "coefficients_compare.png",
            [linear, linear_mul, quadratic, quadratic_mul],
            {},
        ),
    ]

    for title, file_name, functions, kwargs in images:
        path = base / file_name

        fig = get_figure(title, functions, **kwargs)
        print(f"Saving file to {path}")
        fig.savefig(path)


if __name__ == "__main__":
    main()
