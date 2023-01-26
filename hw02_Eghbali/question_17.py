danger_symbols = input().upper()
n = 5

if len(danger_symbols) != n:
    pass
else:
    r_count, y_count, g_count = danger_symbols.count(
        "R"), danger_symbols.count("Y"), danger_symbols.count("G")

    if (r_count >= 3) or (r_count >= 2 and y_count >= 2) or (g_count == 0):
        print("nakhor lite")
    else:
        print("rahat baash")
