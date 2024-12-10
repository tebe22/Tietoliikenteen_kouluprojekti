# Tietoliikenteen_sovellusprojekti

## Yleiskuvaus

Tässä projektissa **nRF5340 Development Kit** joka kerää kiihtyvyysanturin mittauksia, ja lähettää datan langattomasti **IoT-reitittimelle** (Raspberry Pi). Raspberry Pi välittää tiedon **MySQL-tietokantaan**, joka sijaitseen **Oamkin** palvelimella. Tallennettua dataa käytetään koneoppimismalliin, joka tunnistaa miten päin anturi on.






## Arkkitehtuuri

Projektin keskeiset komponentit ja tiedon kulku:

- **Kehitysalusta (nRF5340):** Lukee kiihtyvyysarvot (X, Y, Z) ADC:llä ja lähettää ne BLE:n yli.  
- **Raspberry Pi:** Vastaanottaa BLE-datan ja toimittaa sen TCP-yhteyden avulla eteenpäin.  
- **Linux-palvelin (MySQL & Apache):** Tallentaa mittausdatan tietokantaan, tarjoaa rajapinnat datan hakemiseen ja pyörittää PHP-skriptejä.  
- **Python-analytiikka:**  
  - Opettaa K-means -keskipisteet datasta.  
  - Muodostaa confusion matriisin tulosten arviointiin.  
- **nRF5340 (C-ohjelma):** Toteuttaa K-means-luokittelun laitteeseen kytketyllä kiihtyvyysanturilla hyödyntäen Pythonilla opetettuja keskipisteitä.



![Arkkitehtuurikaavio](docs/architecture.png)

## Toteutetut Ohjelmat

1. **Arduino/C-ohjelma (nRF5340):**  
   Lukee kiihtyvyysanturin dataa ADC:n kautta ja lähettää mitatun 3D-datan BLE:n yli.

2. **Python TCP/Socket -ohjelma (Raspberry Pi):**  
   Vastaanottaa BLE-datan, muodostaa TCP-yhteyden palvelimelle ja tallentaa saadun datan MySQL-tietokantaan.

3. **Python K-means -opetusohjelma:**  
   Lataa anturidatan tietokannasta, laskee klusterikeskipisteet ja generoi `keskipisteet.h`-tiedoston K-means-luokittelijaa varten.

4. **C-ohjelma (nRF5340, K-means):**  
   Hyödyntää opittuja keskipisteitä luokitellessaan reaaliaikaisesti mitattua kiihtyvyysdataa.

5. **Python Confusion-matriisiohjelma:**  
   Hakee luokittelutulokset tietokannasta, vertaa niitä tunnettuun totuuteen ja tulostaa confusion matriisin.

## K-means Algoritmin Selitys

**K-means** jakaa datan k klusteriin (tässä k=6). Jokainen mittauspiste (X, Y, Z) liitetään lähimpään keskipisteeseen. Klustereita ja niiden keskipisteitä päivitetään iteroiden, kunnes tulos vakiintuu.

3D-visualisaatio 

![image](https://github.com/user-attachments/assets/c25b1892-fdfa-4d92-ad24-f517fac27fda)

## Tulokset: Confusion Matriisi

Confusion matriisi kertoo, miten hyvin laitepohjainen K-means-luokitus vastaa tunnettua "oikeaa" luokittelua. Suuret arvot diagonaalilla tarkoittavat onnistunutta luokitusta.

Matriisi:

![image](https://github.com/user-attachments/assets/542fe772-c58e-421a-b030-c7b987882e7d)

## Sovellusalueet ja Hyödyt

- **Reaaliaikainen Sensoriluokittelu:** Tunnistetaan liiketiloja tai suuntia ilman raskasta pilvianalytiikkaa.  
- **Edistyneet Analytiikkaratkaisut:** Koneoppimismenetelmien siirtäminen reunalaitteisiin (edge computing).  
- **Laajennettavuus:** Järjestelmää voidaan laajentaa erilaisiin antureihin, protokolliin ja analytiikkamenetelmiin.

## Kehitysprosessi ja Työkalut

- **Versiohallinta:** Git & GitHub.  
- **Projektihallinta:** GitHubin Kanban-taulut tehtävien seurantaan.  
- **SDLC-vaiheet:** Vaatimusmäärittely, suunnittelu, toteutus, testaus, käyttöönotto ja ylläpito.  
- **Teknologiat:** C, Python, BLE, TCP/IP, MySQL, Apache, Markdown-dokumentaatio.


*Lisätiedot, koodiesimerkit ja tekniset konfiguraatio-ohjeet löytyvät projektin GitHub-repositorion kansioista.*
