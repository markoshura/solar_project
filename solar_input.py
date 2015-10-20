# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                pass  # пустые строки и строки-комментарии пропускаем
            else:
                object_type = line.split()[0].lower()
                if object_type == "Star":
                    star = Star()
                    parse_star_parameters(line, star)
                    objects.append(star)
                elif object_type == "Planet":
                    planet = Planet()
                    parse_planet_parameters(line, planet)
                    objects.append(planet)
                else:
                    print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    a = line.split()
    star.R = float(a[1])
    star.color = a[2]
    star.m = float(a[3])
    star.x = float(a[4])
    star.y = float(a[5])
    star.Vx = float(a[6])
    star.Vy = float(a[7])


def parse_planet_parameters(line, planet):
    a = line.split()
    planet.R = float(a[1])
    planet.color = a[2]
    planet.m = float(a[3])
    planet.x = float(a[4])
    planet.y = float(a[5])
    planet.Vx = float(a[6])
    planet.Vy = float(a[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME: should store real values

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
