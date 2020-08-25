
"""
each point in grid represents:

 - 3 triangles; 2 made with perpendicular lines to the x and y axis respecitively,
   and one from a line between the points where the perpendiculars intersect their axis
 - n triangles above and below a line from the origin to the point; formed by taking the 
   perpendicular from the point, and counting integer coordinates it intersects with to get n
"""


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def triangles_from_point(x, y, limit=50):
    m = gcd(x, y)
    x_step = int(y / m)
    y_step = int(x / m)
    points = []
    # above: -x, +y
    points += zip(range(x, -1, -x_step)[1:], range(y, limit + 1, y_step)[1:])
    # below: +x, -y
    points += zip(range(x, limit + 1, x_step)[1:], range(y, -1, -y_step)[1:])

    return len(points) + 3


def answer(limit=50):
    return sum(triangles_from_point(x, y)
               for x in range(1, limit + 1)
               for y in range(1, limit + 1))
