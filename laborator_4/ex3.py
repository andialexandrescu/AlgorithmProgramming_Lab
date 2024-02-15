with open("test.in", "r") as f:
    l = []
    nota = 1
    for line in f:
        aux, res = line.split("=")
        x, y = aux.split("*")
        if int(res) == int(x) * int(y):
            nota += 1
            l.append(f"{line.strip()} Corect")
        else:
            l.append(f"{line.strip()} Gresit {int(x)*int(y)}")
    l.append(f"Nota {nota}")
with open("test.out", "w") as g:# write va scrie un singur parametru de tip str
    g.write("\n".join(l))
