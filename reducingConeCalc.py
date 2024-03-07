import math

def get_small_dia():
    print("Small Diameter: ", end="")
    dia = int(input())
    return dia

def get_large_dia():
    print("Large Diameter: ", end="")
    dia = int(input())
    return dia

def get_height():
    print("Height (Nearest Inch): ", end="")
    h = int(input())
    return h

def get_thick():
    print("Material Thickness: ", end="")
    h = float(input())
    return h

def get_r(x, y, z):
    r = math.sqrt((0.5 * x - 0.5 * y) ** 2 + z ** 2)
    return r

def get_p(x, y, z):
    p = x * (math.sqrt((0.5 * x - 0.5 * y) ** 2 + z ** 2)) / (y - z)
    return p

def get_length(x, y, z):
    d = (2 * x) * math.sin(y / (2 * x)) + z * 2
    return d

def get_arc(x, y, z):
    d = (2 * x) * math.sin(y / (2 * x)) + z * 2
    return d

def get_sagitta(x, y):
    s = x - (math.sqrt(x ** 2 - (y / 2) ** 2))
    return s

def print_vector(input):
    for i in input:
        print(i, end=' ')
    print()

def print_string_vector(input):
    for i in input:
        print(i, end=' ')
    print()

def print_matrix(input):
    with open("ducts.csv", "w") as my_file:
        for row in input:
            my_file.write(",".join(map(str, row)) + "\n")
            print()

def main():
    names = ['Name']
    small_d = ['Small Diameter']
    large_d = ['Large Diameter']
    height_v = ['Height']
    thickness_v = ['Thickness']
    slant_h = ['Slant Height']
    flat_ir = ['Flat Inside Radius']
    width = ['Flat Width']
    length = ['Flat Legnth']
    weight = ['Bounding Box Weight']
    flat_angle = ['Flat Pattern Angle']
    flat_or = ['Flat Outside Radius']

    while True:
        name_in = input("Enter Duct Name (0 to stop): ")
        if name_in == "0":
            break

        steel_weight = 0.2833
        s_dia = get_small_dia()  # User input
        l_dia = get_large_dia()  # User input
        height = get_height()  # User input
        thickness = get_thick()  # User input
        r = get_r(l_dia, s_dia, height)  # Slant height
        p = get_p(height, l_dia, s_dia)  # Flat pattern inside radius
        q = r + p  # Flat pattern outside radius (large diameter)
        l_inner_arc = 3.14 * s_dia  # Length of inner arc along perimeter
        l_outer_arc = 3.14 * l_dia  # Length of outer arc along perimeter
        a = l_inner_arc / p  # Angle in radians
        d = (a * 180) / 3.14  # Angle in degrees
        b_length = get_length(q, l_outer_arc, thickness)  # Bounding box length
        b_arc = get_arc(p, l_inner_arc, thickness)  # Bounding box arc
        sagitta = get_sagitta(p, b_arc)
        b_width = sagitta + r
        b_sqft = b_width * b_length
        b_volume = b_width * b_length * thickness
        b_weight = b_volume * steel_weight

        names.append(name_in)
        small_d.append(s_dia)
        large_d.append(l_dia)
        height_v.append(height)
        thickness_v.append(thickness)
        width.append(b_width)
        length.append(b_length)
        weight.append(b_weight)
        slant_h.append(r)
        flat_ir.append(p)
        flat_angle.append(d)
        flat_or.append(q)


    all_nums = [small_d, large_d, height_v, slant_h, flat_ir, flat_or, flat_angle]

    print(all_nums)
    print_matrix(all_nums)

if __name__ == "__main__":
    main()
