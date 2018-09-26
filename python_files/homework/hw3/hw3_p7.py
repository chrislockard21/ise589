from math import sqrt

def filter_vertex(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        vertex_lines = [
            line.strip(' ').split() for line in lines
            if line.strip(' ').startswith('vertex')
        ]
    return vertex_lines

vertex_lines = filter_vertex('7_Part1.STL')

def tri_info(vertex_lines):
    tri_dict = {}
    tri_list = []
    tri_num = 1
    for line in vertex_lines:
        if len(tri_list) > 2:
            tri_dict['tri' + str(tri_num)] = tri_list
            tri_num += 1
            tri_list = []
        else:
            tri_list.append((line[1], line[2], line[3]))
    return tri_dict

print('Total triangles: ' + str(len(tri_info(vertex_lines))) + '\n')


def area(v_1, v_2, v_3):
    dist_1_2 = sqrt(
            ((float(v_2[0]) - float(v_1[0]))**2) +
            ((float(v_2[1]) - float(v_1[1]))**2) +
            ((float(v_2[2]) - float(v_1[2]))**2)
    )
    dist_2_3 = sqrt(
            ((float(v_3[0]) - float(v_2[0]))**2) +
            ((float(v_3[1]) - float(v_2[1]))**2) +
            ((float(v_3[2]) - float(v_2[2]))**2)
    )
    dist_3_1 = sqrt(
            ((float(v_1[0]) - float(v_3[0]))**2) +
            ((float(v_1[1]) - float(v_3[1]))**2) +
            ((float(v_1[2]) - float(v_3[2]))**2)
    )
    sem_perimeter = (dist_1_2 + dist_2_3 + dist_3_1)/2
    area = sqrt(
        sem_perimeter*
        (sem_perimeter-dist_1_2)*
        (sem_perimeter-dist_2_3)*
        (sem_perimeter-dist_3_1)
    )
    return area

def tri_area(tri_dict):
    for k, v in tri_dict.items():
        v_1 = v[0]
        v_2 = v[1]
        v_3 = v[2]
        print('Triangle id: {}\nArea: {}\n'.format(k, area(v_1, v_2, v_3)))

tri_area(tri_info(vertex_lines))
