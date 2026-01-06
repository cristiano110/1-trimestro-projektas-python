# Sandėlio inventoriaus sistema

Sveiki! Tai yra mano I trimestro Python AI grupės projektas "Sandėlio inventoriaus sistema".
Tai yra paprasta sandėlyje esančių prekių valdymo sistema, kuriai panaudojau Python duomenų apdorojimo funkcijas ir prieš tai dar nebandytą PDF failo generavimą su 'reportlab'.

PRIEŠ NAUDOJANT:
Dėl PDF funkcionalumo, šiai programai veikti būtinas 'reportlab' library. Jei sistemoje dar neįrašyta, į Python terminalą reikia įrašyti 'pip install reportlab' prieš paleidžiant kodą.

**

Šis kodas turi 8 funkcijas, štai trumpi aprašymai, ką kiekviena iš jų atlieka.

0. išeiti - Ši funkcija tinkamai uždaro programą ir sustabdo veikimą.

1. Pridėti prekę - Ši funkcija leidžia vartotojui pridėti dictionary elementą - prekę.

2. Pakeisti kiekį - Ši funkcija gali pakeisti jau pridėtos prekės kiekio reikšmę.

3. Rodyti inventorių - Ši funkcija rodo dabar pridėtus inventoriaus elementus.

4. Saugoti į failą - Ši funkcija išsaugo dabartinį inventorių į JSON failą Python failo buvimo direkcijoje.

5. Užkrauti iš failo - Ši funkcija užkrauna inventoriaus reikšmę iš jau išsaugoto JSON failo Python failo buvimo direkcijoje.

6. Rodyti visą vertės sumą - Ši funkcija apskaičiuoja sandėlyje esančių prekių sumą padauginant prekės kainą iš jos kiekio.

7. Eksportuoti duomenis į PDF - Ši funkcija formatuoja duomenis į paprastą PDF, naudojant pasirinktinį šriftą dėl lietuviškų raidžių ypatumų palaikymo. 

**

Tikiuosi, jums patiko mano projektas!
Gero išbandymo 😁
