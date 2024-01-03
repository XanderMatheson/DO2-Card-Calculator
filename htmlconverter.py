def main():
    html_file = open("table.txt")
    lines = []
    for i in range(27):
        lines.append([])
    all_lines = html_file.readlines()
    part = 0
    offset = 0
    i = 0
    while i < len(all_lines):
        line = all_lines[i]
        if "<tr>" in line:
            i += 1
            continue
        if "</tr>" in line:
            i += 1
            offset += 3
            continue
        section = all_lines[i:i+5]
        lines[part + offset].append(section)
        part += 1
        part %= 3
        i += 5
    for i in range(len(lines)):
        print("<tr>")
        for j in range(len(lines[i])):
            for k in range(len(lines[i][j])):
                print(lines[i][j][k], end="")
        print("</tr>")



main()
