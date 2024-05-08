""" 
Engeto Online Python Akademie: Projekt3 - Elections Scraper 
author: Andrea Kvapilová 
email: a.ndrea@centrum.cz 
discord: andreakvapilova 
"""

# Elections Scraper - English
Hello! Welcome to elections scraper held on 2017.
Enter two arguments when the first is the territorial unit and the second
is the name of the file to which the results will be saved.
The link to the territorial unit can be obtained from this website [election 2017](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=EN).
The output contains information about the municipality code and its name, registered voters, issued envelopes, valid votes and valid votes for each party.

## Instaling libraries
The libraries needed to run this script are stored in the "requierements.txt" file.
To install, it is recommended to create a new virtual environment and use pip (package installer) to run the following commands:
<pre>
pip --version
pip install -r requirements.txt
</pre>

## Running programm
The script is executed using the command line. Two arguments are required. The first argument is url address of the requested subdivision and the second argument is the name of the csv file where the results are exported. 
<pre>
python elections_scraper.py "territorial unit url" "file name with result"
</pre>  
If the link and file name are correct, a message that the file has been downloaded will be displayed.


## Example of the project
1. selection on this website of the territorial unit and clicking on the link Choise of a municipality - Prostějov "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
2. select the file name to save - prostejov.csv
3. running in terminal
<pre>
python elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "prostejov.csv"
</pre>
4. download progress: Preparing beautiful soup, please wait. File prostejov.csv was successfully created.
5. a preview of the output: modified data splitting into columns using separator in Excel [odkaz na csv soubor](/prostejov.csv)

### Sample output:
code,location,registred voters,issued envelopes,valid votes,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů,-
589292,Bohuslavice,376,236,236,20,0,0,23,0,3,22,3,4,6,0,1,17,0,4,53,1,1,39,0,0,3,0,36,0,-
589357,Buková,264,170,169,16,0,0,19,0,3,33,2,0,3,0,0,14,0,2,35,1,0,25,0,1,0,0,15,0,-
589322,Brodek u Prostějova,1 224,656,655,54,0,0,42,0,21,61,5,4,11,1,2,57,0,22,202,0,1,53,2,1,3,4,107,2,-

# Volební scraper - Čestina
Dobrý den, vítejte v programu na scrapování volebních výsledků z roku 2017. 
Pro úspěšné spustění programu zadejte dva argumenty prvnéí je odkaz na územní celek a druhý název souboru, kde se mají výsledky uložit.
Odkaz na územní celek získáte z této webové stránky [volby 2017](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).
Výstup obsahuje informaci o kódu obce, jejím názvu, registrovaných voličích, vydaných obálek, počet platných hlasů, počet hlasů pro jednotlivé kandidující strany. 

## Instalace knihoven
Knihovny potřebné pro spuštění tohoto skriptu jsou uloženy v souboru "requirements.txt".
Pro instalaci je vhodné vytvořit nové virtuální prostředí a pomocí pip spustit instalaci těmito příkazy:
<pre>
pip --version
pip install -r requirements.txt
</pre>

## Spuštění projektu
Spuštění skriptu se provádí pomocí příkazového řádku. Povinné jsou dva argumenty, první je url adresa požadovaného územního celku a druhý argument název souboru s příponou csv, kam se mají stažené výsledky exportovat.
<pre>
python nazev_souboru "url odkaz uzemniho celku" "nazev_souboru_s_vysledky"
</pre>
Pokud bude odkaz a název souboru v pořádku. Proběhne hláška, že soubor s názvem byl stažený.

## Ukázka projektu
1. výběr na těchto stránkách územního celku a rozkliknutí odkazu Výběr obce - Prostějov "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" 
2. zvolení názvu souboru na uložení - prostejov.csv
3. spuštění v terminálu 
<pre>
python elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "prostejov.csv"
</pre>
4. průběh stahování: Preparing beautiful soup, please wait. File prostejov.csv was successfully created.
5. ukázka výstupu: provedena úprava rozdělení dat do sloupců pomocí oddělovače v excelu [odkaz na csv soubor](/prostejov.csv)

### částečný výstup:
code,location,registred voters,issued envelopes,valid votes,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů,-
589292,Bohuslavice,376,236,236,20,0,0,23,0,3,22,3,4,6,0,1,17,0,4,53,1,1,39,0,0,3,0,36,0,-
589357,Buková,264,170,169,16,0,0,19,0,3,33,2,0,3,0,0,14,0,2,35,1,0,25,0,1,0,0,15,0,-
589322,Brodek u Prostějova,1 224,656,655,54,0,0,42,0,21,61,5,4,11,1,2,57,0,22,202,0,1,53,2,1,3,4,107,2,-
