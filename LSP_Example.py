from Rectangle import Rectangle
from Square import Square


def main():
    rectangle = Rectangle()
    rectangle.set_width(10)
    rectangle.set_height(20)
    print("Rectangle area:", rectangle.get_area())

    rectangle = Square()
    rectangle.set_width(10)
    rectangle.set_height(20)
    print("Square stored as Rectangle area:", rectangle.get_area())
    # Expected from the Rectangle contract: 10 * 20 = 200.
    # Actual result is 20 * 20 = 400 because Square changes width when height changes.


if __name__ == "__main__":
    main()
