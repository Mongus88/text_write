Feladat

Írj egy olyan programot ami mátrixként jeleníti meg a betűket egymás mellet úgy , hogy minden betű a saját betűjéből legyen kiírva.

Megoldás

update 1.1
2026_02_26
Az előző program nem a saját betújével írta a betűket, ez javítva.
Átláthatóság érdekében bekerült a zip funkció.
A mátrixok nem változokból hanem jelölőkből épülnek fel.

Végig megyek egy ciklussal a beírt szó minden betűjén és a megfelelő abc mátrixot beleteszem a matrixok változóba. A zip segítségével veszem minden betű mátris első sorát majd 2. 3. ... 8. sorát. A második for ciklusba létrehzok egy listát ahol az elemeknek két értéke van a betű és mátrix sora. A harmadik ciklusban végig megyek karakterlistán és megnézem, hogy az a pixel háttér vagy betu és eldöntöm milegyen a sorsa.

*Ahhoz, hogy a betűk egymás mellet legyenek tisztáznunk kell, hogy a gép soronként tudja kiírni az a karaktereket a képernyőre.
Tehet az 1. sorba minden betű mátrix első sorát kell kiírni. Ezért is fontos, hogy egy magasak legyenek a mátrixok.
A szélesség mindegy.
A külső ciklus felel a sorokért.
A középső cilus keresi meg a betűhöz tartozó mátrixot.
A belső ciklus az oszlop számát adja meg.*

*Az első print végi end=" " azért felel, hogy szellősebb legyen a karakter
A második print azért szükséges, hogy a betűk ne folyannak össze.
A harmadik print a sortörést csinálja.*
