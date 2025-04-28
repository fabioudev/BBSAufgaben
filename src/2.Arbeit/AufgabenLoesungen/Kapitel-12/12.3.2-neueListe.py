L = ['Meier', 'Bauer', 'Moser', 'Molitor', 'Martin']
def filter_namen_m(List):
    M_namen = []
    for name in List:
        if name[0] == 'M':
            M_namen.append(name)
    return M_namen

print(filter_namen_m(L))