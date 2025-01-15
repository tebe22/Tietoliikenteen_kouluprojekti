import numpy as np
from database import hae_data
from kmeans import kmeans
from visuali import visualisoi_data
from tallennus import tallenna_tiedostoon

# Hae data tietokannasta
data = hae_data()
if data is None:
    print("Datan haku epaonnistui.")
    exit(1)

# Arvo keskipisteet ja aja K-means algoritmi
suurin_arvo = np.max(data)
keskipisteet = np.random.rand(6, 3) * suurin_arvo
lopulliset_keskipisteet = kmeans(data, keskipisteet)

# Tallennetaan keskipisteet tiedostoon
with open("keskipisteet.h", "w") as f:
    f.write("int CP[6][3] = {\n")
    for kp in lopulliset_keskipisteet:
        f.write(f"    {{{int(kp[0])}, {int(kp[1])}, {int(kp[2])}}},\n")
    f.write("};\n")

# Visualisointi
visualisoi_data(data, lopulliset_keskipisteet)

tallenna_tiedostoon(lopulliset_keskipisteet)