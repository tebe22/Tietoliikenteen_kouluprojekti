def tallenna_tiedostoon(keskipisteet, tiedostonimi="keskipisteet.h"):
    with open(tiedostonimi, 'w') as file:
        file.write("int CP[6][3] = {\n")
        for i, kp in enumerate(keskipisteet):
            file.write(f"    {{{int(kp[0])}, {int(kp[1])}, {int(kp[2])}}}")
            if i < len(keskipisteet) - 1:
                file.write(",\n")
            else:
                file.write("\n")
        file.write("};\n")
