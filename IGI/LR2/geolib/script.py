import os
import circle
import square

size = float(os.environ.get("SIZE"))
shape = os.environ.get("SHAPE")
func = os.environ.get("FUNCTION")

functions = {
    ("circle", "area"): circle.area,
    ("circle", "perimeter"): circle.perimeter,
    ("square", "area"): square.area,
    ("square", "perimeter"): square.perimeter
}

function = functions.get((shape, func))

print(function(size))