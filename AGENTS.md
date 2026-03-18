# AGENTS.md

## Eesmärk

See fail kirjeldab juhiseid, mille järgi luua HARNO andmeinseneride täiendkoolituse praktikumi juhendeid selles hoidlas.

Selle repo materjalid võivad olla mõeldud nii baastaseme kui ka edasijõudnute rühmale. Juhendi loomisel lähtu esmalt kontekstist: kasutaja soov, sihtkaust ja olemasolev materjal peavad ütlema, kummale tasemele juhend kuulub.

Kui tase ei ole sõnaselgelt teada ja faili asukoht ka vihjet ei anna, siis eelda vaikimisi baastaset.

## Kursuse kontekst

- Tegemist on Haridus- ja Noorteameti andmeinseneride täiendkoolitusprogrammiga.
- Programm on praktilise suunitlusega, kestab ligikaudu 3 kuud ja lõpeb projektipõhise grupitööga.
- Osalejad õpivad töö kõrvalt ning õpe toimub loengute, praktikumide ja iseseisva töö kombinatsioonina.
- Materjalid peavad sobima kasutamiseks nii kontaktõppes kui ka hiljem Moodle'is iseseisvaks kordamiseks.

## Tase ja sihtrühm

- Selles repos on materjalid tavaliselt jaotatud tasemete kaupa kaustadesse `baastase` ja `edasijoudnud`.
- Kui juhend läheb `.../baastase/` kausta, kirjuta see baastaseme õppijale.
- Kui juhend läheb `.../edasijoudnud/` kausta, kirjuta see edasijõudnud õppijale.
- Kui lood mooduli juurkausta üldise `README.md` faili, kirjuta see tasemeneutraalselt ja seosta see mõlema taseme materjalidega.

### Baastase

- Õppijal ei pruugi olla andmetehnika ega andmeinseneeria tausta.
- Eelda, et õppija võib olla tugev oma erialases töös, kuid talle võivad olla uued andmeinseneeria mõisted, tööriistad, käsurida, pilveteenused, SQL, Python, Docker või versioonihaldus.
- Hoia tempo rahulik ja vii edasi üks oluline uus idee korraga.
- Selgita tausta, töövõtet ja oodatavat tulemust rohkem lahti.

### Edasijõudnud

- Võid eeldada, et õppijal on vähemalt põhiteadmised käsureast, andmebaasidest, SQL-ist, Pythonist, Dockerist ja versioonihaldusest või nendega võrreldav praktiline kogemus.
- Võid liikuda kiiremini ja jätta ära kõige elementaarsemad vahetutvustused.
- Keskendu rohkem valikute põhjendamisele, tehnilistele kompromissidele, veaotsingule ja töövoo tervikpildile.
- Ära muuda juhendit ainult käskude loendiks. Ka edasijõudnud õppija vajab selget eesmärki, oodatavat tulemust ja põhjendust, miks mingi töövõte on kasulik.

### Keeleline põhimõte mõlemal tasemel

- Keeleline kvaliteet, terminikasutus ja selgus peavad olema mõlemal tasemel ühtlaselt head.
- Tasemete erinevus tuleb eelkõige tempos, eelteadmistes, juhendamise detailsuses ja ülesannete keerukuses, mitte keele hoolikuses.

## Põhiprintsiibid

- Kirjuta heas, loomulikus ja korrektses eesti keeles.
- Selgita uusi mõisteid rahulikult, täpselt ja ilma tarbetu žargoonita.
- Eelista selgust täielikkusele: parem üks asi hästi arusaadavaks teha kui viis asja pealiskaudselt.
- Seo iga uus teema praktilise väärtusega: miks seda vaja on, kus seda päriselt kasutatakse ja kuidas see toetab lõppprojekti või igapäevatööd.
- Hoia tempo sihtrühmale sobiv.
- Kui lisad keerukama või kiirematele mõeldud osa, märgi see selgelt valikuliseks lisategevuseks.

## Keele ja stiili juhised

- Kasuta lühikesi ja selgeid lauseid.
- Väldi liigset bürokraatlikku, akadeemilist või masintõlke moodi sõnastust.
- Väldi põhjendamata ingliskeelset žargooni.
- Kui ingliskeelne termin on valdkonnas vajalik, too esmamainimisel juurde eestikeelne selgitus.
- Kasuta läbivalt samu termineid. Kui valid mõistele eestikeelse vaste, ära vaheta seda hiljem ilma põhjuseta.
- Väldi sõnu ja tooni, mis võivad õppijat pisendada, näiteks "lihtne", "ilmselge" või "nagu kõik teavad".
- Kirjuta toetavalt ja julgustavalt, kuid ära muutu uduseks ega liiga jutustavaks.

## Eesti keele stiili lisajuhised

- Eelista selget ja loomulikku sõnastust kantseliidile.
- Pane lause algusesse see, mis on õppija jaoks kõige olulisem.
- Hoia ühes lauses pigem üks põhiidee.
- Eelista tegusõnu nimisõnalistele konstruktsioonidele.
- Eelista eesti omasõnu võõrapärasele sõnastusele, kui sisu ei lähe kaduma.
- Kui lihtsam tegusõna töötab, eelista seda üldsõnalisemale väljendile nagu "läbi viima".
- Väldi tarbetuid täitesõnu, turunduslikku paisutust ja liigset emotsionaalset rõhutamist.
- Kui mõni keerukas sõna või termin on vältimatu, selgita see kohe lahti.
- Eelista lakoonilist, täpset ja rahulikku tooni. Õppematerjal ei pea olema kuiv, kuid see ei pea olema ka jutukas.

## Kuidas uusi mõisteid selgitada

- Alusta probleemist või vajadusest, mida mõiste lahendab.
- Anna seejärel lühike definitsioon lihtsas keeles.
- Too üks konkreetne näide päriselust või praktikumi kontekstist.
- Alles pärast seda mine tehnilise detaili või tööriista kasutuse juurde.
- Kui mõisteid on mitu, selgita nende omavaheline seos.
- Kui mõni samm eeldab varasemat teadmist, ütle see selgelt välja ja meenuta vajalik taust lühidalt üle.

## Iga praktikumi juhendi soovituslik ülesehitus

Kasuta üldjuhul järgmist struktuuri:

1. Praktikumi eesmärk
2. Õpiväljundid
3. Eeldused
4. Miks see teema on oluline
5. Uued mõisted
6. Samm-sammuline praktikumi käik
7. Kontrollpunktid või oodatavad vahetulemused
8. Levinud vead ja nende lahendused
9. Lühike kokkuvõte
10. Soovi korral lisaharjutus või iseseisev edasiarendus

## Praktikumi sisu loomise reeglid

- Iga juhend peab olema iseseisvalt jälgitav ka siis, kui õppija loengu ajal kõigest kohe aru ei saanud.
- Kirjelda iga sammu juures, mida õppija teeb, miks ta seda teeb ja mis tulemust ta peaks nägema.
- Kui kasutad käske või koodi, seleta enne või kohe pärast plokki, mida see teeb.
- Anna õppijale vihje, milline väljund, fail, tabel või muudatus kinnitab, et samm õnnestus.
- Kui mõni samm on tehniliselt õrn või veale tundlik, lisa kohe juurde lühike veaotsingu osa.
- Väldi suuri hüppeid. Kui samm nõuab mitut tegevust, jaga see väiksemateks osadeks.
- Väldi olukorda, kus õppija peab tegema midagi lihtsalt "usu peale". Selgita, miks just nii tehakse.
- Märgi hinnanguline ajakulu, kui see aitab õppijal oma tööd planeerida.

## Koodi, käskude ja tööriistade kasutamise juhised

- Kõik käsud ja koodinäited peavad olema kopeeritavad ning võimalikult vähese varjatud eeldusega.
- Kasuta näidetes võimalikult selgeid failinimesid, tabelinimesid ja muutujanimesid.
- Ära eelda, et õppija tunneb käsurea põhikäske. Kui need on vajalikud, selgita neid lühidalt vähemalt baastaseme materjalides.
- Kui kasutad keskkonnaspetsiifilisi samme, ütle välja, millises keskkonnas neid tehakse.
- Kui samm võib sõltuda varasemast seadistusest, nimeta see eraldi peatükis "Eeldused" või "Enne alustamist".
- Kui väljund võib versiooniti erineda, kirjelda olulist osa, mida õppija peab märkama, mitte ära kopeeri pikka toorväljundit.
- Kui viitad repo failidele, kontrolli, et relatiivsed teed vastaksid päriselt selle hoidla struktuurile.

## Didaktilised rõhuasetused

### Baastase

- Lähtu sellest, et õppija vajab lisaks juhistele ka mõttemudelit.
- Selgita mitte ainult "kuidas", vaid ka "miks".
- Seo tehniline tegevus arusaadava tööprotsessi või ärilise olukorraga.
- Kasuta vajadusel väikseid vahekokkuvõtteid, et õppija ei kaotaks järge.
- Eelista vähem, aga paremini läbimõeldud samme suurele mahule.
- Kui võimalik, too paralleele tuttavate olukordadega, näiteks Exceli, tabelite, failide või tavapäraste tööprotsessidega.

### Edasijõudnud

- Lähtu sellest, et õppija vajab vähem sissejuhatust, kuid endiselt selget töövoogu.
- Selgita, miks üks lähenemine on teisest parem just selles olukorras.
- Too sisse arhitektuurilised valikud, tehnilised piirangud ja levinud kompromissid.
- Kasuta praktilisi ülesandeid, kus õppija peab midagi ise otsustama, kohandama või parandama.
- Jäta ruumi iseseisvaks mõtlemiseks, kuid ära jäta olulisi eeldusi või kontrollpunkte sõnastamata.

## Mida vältida

- Ära kirjuta juhendeid nii, nagu need oleksid mõeldud ainult tehnilise taustaga osalejale, kui materjal ei ole selgelt edasijõudnutele.
- Ära kuhja ühte juhendisse liiga palju uusi mõisteid.
- Ära jäta olulisi eeldusi nimetamata.
- Ära kasuta seletamata lühendeid.
- Ära anna ainult käskude loendit ilma selgituse ja oodatava tulemuseta.
- Ära kopeeri dokumentatsiooni stiili üks ühele; õppejuhend peab olema õpetav, mitte ainult kirjeldav.
- Ära eelda, et õppija oskab veateadet iseseisvalt tõlgendada.

## Kvaliteedikontroll enne juhendi üleandmist

Enne juhendi esitamist kontrolli alati järgmist:

- Kas juhend on kirjutatud loomulikus ja korrektses eesti keeles?
- Kas valitud tasemele vastav õppija saab aru, mida ta igas sammus teeb ja miks?
- Kas kõik uued mõisted on lahti seletatud või vähemalt tasemele sobivalt raamitud?
- Kas juhendit saab kasutada ka ilma juhendaja suulise lisaselgituseta?
- Kas iga olulisema sammu juures on arusaadav oodatav tulemus?
- Kas võimalikud komistuskohad on ennetatud või lahti kirjutatud?
- Kas juhendi maht ja tempo on valitud tasemele realistlik?
- Kas juhend toetab praktilist õppimist ja seostub andmeinseneeria tegelike töövõtetega?
- Kas faili- ja kaustaviited vastavad selle repo tegelikule struktuurile?

## Vaikimisi tööreegel tulevaste sessioonide jaoks

Kui kasutaja palub luua uue praktikumi juhendi, siis:

1. määra kõigepealt juhendi tase kasutaja soovi, sihtkausta või olemasoleva materjali põhjal;
2. kui tase ei selgu, eelda baastaset;
3. kirjuta juhend heas eesti keeles;
4. selgita uued mõisted valitud tasemele sobiva põhjalikkusega lahti;
5. loo juhend samm-sammulise praktikumi vormis;
6. lisa kontrollpunktid, oodatavad tulemused ja levinumad vead;
7. hoia toon toetav, selge ja professionaalne.
