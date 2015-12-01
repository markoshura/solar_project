# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from copy import deepcopy as copy

cache=[]

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
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":  # FIXME: do the same for planet
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    raw = line.split()
    if raw[0] != 'Star': raise ValueError('Not a star line!')
    #print('-------------------------------------> ',line)
    star.R = float(raw[1])
    star.color = raw[2]
    star.m = float(raw[3])
    star.x = float(raw[4])
    star.y = float(raw[5])
    star.Vx = float(raw[6])
    star.Vy = float(raw[7])
    star.name = raw[8]

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    
    raw = line.split()
    if raw[0] != 'Planet': raise ValueError('Not a planet line!')
    #print('-------------------------------------> ',line)
    planet.R = float(raw[1])
    planet.color = raw[2]
    planet.m = float(raw[3])
    planet.x = float(raw[4])
    planet.y = float(raw[5])
    planet.Vx = float(raw[6])
    planet.Vy = float(raw[7])
    planet.name = raw[8]


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя выходного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write('{} {} {} {} {} {} {} {}\n'.format(\
                obj.type.capitalize(), obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))
        out_file.close()

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...
def save_to_cache(space_objects):
    cache.append(copy(space_objects))

def dist(a, b):
    return int(((a.x-b.x)**2+(a.y-b.y)**2)**0.5 + 0.5)

def time_format(t):
    y,mon,d,h,min,sec = t//31536000, (t%31536000)//2592000, (t%2592000)//86400, (t%86400)//3600, (t%3600)//60, t%60
    s=''
    for i in [[y, 'year'], [mon, 'month'], [d, 'day'], [h, 'hour'], [min, 'minute'], [sec, 'second']]:
        if i[0]>0: 
            if (i[0]%10!=1)or(i[0]==11): i[1]+='s'
            s+= str(int(i[0]))+' '+i[1]+' '
    return s[:-1]

def dist_format(d):
    if d < 1000: return str(int(d))+' meters'
    if d < 1e6: return str((d//1)/1000) + ' km'
    else: return str((d//1)/1000) + ' km'

def save_stats(fname):
    O=open(fname, 'w')
    O.write(str(len(cache))+'\n')
    for objs in cache:
        O.write(time_format(objs[0].time)+'\n')
        for i in objs:
            if i.attractor.m > i.m: O.write('Distance from {} to {} is {}\n'.format(
                i.name, i.attractor.name, dist_format(dist(i.attractor, i))))
    O.close()
        

if __name__ == "__main__":
    print("This module is not for direct call!")
