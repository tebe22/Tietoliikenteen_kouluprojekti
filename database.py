import mysql.connector
import numpy as np

def hae_data():
    try:
        # Muodosta yhteys tietokantaan
        yhteys = mysql.connector.connect(
            host="172.20.241.9",  # Tietokantapalvelimen IP-osoite
            user="dbaccess_ro",   # Lukuoikeuksilla varustettu käyttäjänimi
            password="vsdjkvwselkvwe234wv234vsdfas",  # Lukuoikeuksilla varustetun käyttäjän salasana
            database="measurements"  # Tietokannan nimi
        )

        kursori = yhteys.cursor()
        
        # Hae kiihtyvyysanturin data, jossa groupid on 19
        kysely = "SELECT sensorvalue_a, sensorvalue_b, sensorvalue_c FROM rawdata WHERE groupid = 19 ORDER BY timestamp DESC LIMIT 384"
        kursori.execute(kysely)
        
        tulos = kursori.fetchall()

        # Muunna haettu data NumPy-muotoon ja palauta se
        data = np.array(tulos)

        # Sulje tietokantayhteys
        kursori.close()
        yhteys.close()

        return data

    except mysql.connector.Error as err:
        print(f"Tietokantavirhe: {err}")
        return None

# Esimerkki haetun datan tulostamisesta
if __name__ == "__main__":
    data = hae_data()
    if data is not None:
        print("Haettu data:")
        print(data)
    else:
        print("Datan haku epäonnistui.")