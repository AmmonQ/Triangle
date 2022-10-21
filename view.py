# This is a sample Python script.
import sys

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


def check_valid_triangle(side_a, side_b, side_c):
    a_b_sum = side_a + side_b
    b_c_sum = side_b + side_c
    a_c_sum = side_a + side_c

    if a_b_sum < side_c:
        return False
    if b_c_sum < side_a:
        return False
    if a_c_sum < side_b:
        return False
    return True


def type_of_triangle(a, b, c):
    triangle_type = None
    angle = None

    if a == b == c:
        triangle_type = 'equilateral'
    elif (a == c and b != c and a != b) or (a == b and a != c and c != b) or (a != c or b != c and c == b):
        triangle_type = 'isosceles'
    elif a != b and a != c and b != c:
        triangle_type = 'scalene'

    # if square of two shorter sides are smaller than the square of the longest side, triangle is obtuse
    # if square of two shorter sides is greater than the square of the longest side, triangle is acute
    # if square of two shorter sides is equal to the square of the longest side, triangle is right
    sides = [a, b, c]
    longest_side = max(sides)
    sides.remove(longest_side)

    square_of_longest_side = longest_side ** 2
    square_of_shorter_sides = sides[0] ** 2 + sides[1] ** 2

    if square_of_shorter_sides < square_of_longest_side:
        angle = "obtuse"
    elif square_of_shorter_sides > square_of_longest_side:
        angle = "acute"
    else:
        angle = "right"

    return f"These sides lengths produce a valid {angle} {triangle_type} triangle"


def analyze():
    side_a_input = side_a_length.text()
    side_b_input = side_b_length.text()
    side_c_input = side_c_length.text()

    if side_a_input and side_b_input and side_c_input:
        if side_a_input.lstrip('-').isdigit() and side_b_input.lstrip('-').isdigit() and side_c_input.lstrip(
                '-').isdigit():
            side_a_input = float(side_a_input)
            side_b_input = float(side_b_input)
            side_c_input = float(side_c_input)

            if side_a_input > 0 and side_b_input > 0 and side_c_input > 0:
                # check that given values produce a valid triangle
                # no two sides added up can be less than the other side
                if check_valid_triangle(side_a_input, side_b_input, side_c_input):
                    output_label.setText(type_of_triangle(side_a_input, side_b_input, side_c_input))
                    output_label.setStyleSheet('color: black')
                else:
                    output_label.setText('The lengths do not make a valid triangle')
                    output_label.setStyleSheet('color: red')
            else:
                output_label.setText('Lengths must be greater than 0')
                output_label.setStyleSheet('color: red')
        else:
            output_label.setText('Lengths must be numbers (decimals allowed)')
            output_label.setStyleSheet('color: red')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(600, 600)
    w.setWindowTitle("Triangle")

    label_a = QLabel(w)
    label_a.setText("Side a length: ")
    label_a.move(100, 130)
    label_a.show()

    side_a_length = QLineEdit(w)
    side_a_length.move(200, 130)
    side_a_length.textChanged.connect(analyze)
    side_a_length.show()

    label_b = QLabel(w)
    label_b.setText("Side b length: ")
    label_b.move(100, 180)
    label_b.show()

    side_b_length = QLineEdit(w)
    side_b_length.move(200, 180)
    side_b_length.textChanged.connect(analyze)
    side_b_length.show()

    label_c = QLabel(w)
    label_c.setText("Side c length: ")
    label_c.move(100, 230)
    label_c.show()

    side_c_length = QLineEdit(w)
    side_c_length.move(200, 230)
    side_c_length.textChanged.connect(analyze)
    side_c_length.show()

    output_label = QLabel(w)
    output_label.setText("Output")
    output_label.move(100, 400)
    output_label.show()
    output_label.resize(450, 15)

    w.show()

    sys.exit(app.exec_())
