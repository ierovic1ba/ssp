# 📘 Slučajni signali i procesi – Primjeri i SSP biblioteka

Ovaj repozitorij sadrži **programske kodove** i **SSP biblioteku** koji prate knjigu  
**_Slučajni signali i procesi_**  
autora **Emir Sokić** i **Almir Salihbegović**  
📖 Izdavač: [Univerzitet u Sarajevu](https://ebooks.unsa.ba/index.php/ebooks/catalog/book/81)  
🆔 ISBN-13: 978-9926-575-03-8 (2025)

---

## 📂 Struktura repozitorija

```
├── Primjeri/          # Svi primjeri iz knjige
├── ssp/               # SSP biblioteka (namjenski razvijena za knjigu)
│   ├── __init__.py
│   ├── slproc.py
│   ├── slprom1D.py
│   ├── slprom2D.py
└── Pomoc/ (planirano) # Dokumentacija i dodatna objašnjenja (TODO)
```

---

## 🧩 SSP biblioteka

`ssp` (Slučajni Signali i Procesi) je Python biblioteka razvijena kao podrška za izvođenje i vizuelizaciju svih primjera i eksperimenata u knjizi.  
Biblioteka je optimizovana za rad u **Jupyter Notebook** i **Google Colab** okruženjima.

---

## 🚀 Brzi početak

### 1️⃣ Klonirajte repozitorij

U terminalu pokrenite:

```bash
git clone https://github.com/esokic/ssp.git
```

Zatim pređite u direktorij projekta:

```bash
cd ssp
```

---

### 2️⃣ Podesite putanju do `ssp` biblioteke

U svakom primjeru na početku koda se ručno dodaje putanja ka `ssp` direktoriju:

```python
import sys
sys.path.insert(0, '/putanja/do/lokalnog/foldera/ssp')
import ssp
```

🔹 Primjer:  
Ako ste repozitorij preuzeli u `C:\Knjiga_SSP`, putanja bi mogla biti:

```python
sys.path.insert(0, 'C:/Knjiga_SSP/ssp')
```

ili na Linux/Mac:

```python
sys.path.insert(0, '/home/korisnik/Knjiga_SSP/ssp')
```

---

### 3️⃣ Uvoz biblioteka i format prikaza

Kodovi iz knjige koriste sledeću strukturu:

```python
# Uvoz SSP modula
import sys
sys.path.insert(0, '/putanja/do/ssp')
import ssp

# Uvoz dodatnih biblioteka
import numpy as np

# Podesavanje prikaza za knjigu:
ssp.FORMATIRANJE_PRIKAZA = "BOOK"
ssp.REZOLUCIJA = "LOW"

# Podesavanje prikaza za rad studenata:
# ssp.FORMATIRANJE_PRIKAZA = "JUPYTER"
# ssp.REZOLUCIJA = "LOW"
```

📘 **Napomena:**  
- `"BOOK"` format koristi se za generisanje slika i grafikona identičnih onima u knjizi.  
- `"JUPYTER"` format koristi se za interaktivni rad u Colab/Jupyter okruženju. Preporučuje se korištenje ovog formata.
- `"LOW"`/`"HIGH"` se odnosi na izbor rezolucije generiranih grafikona.
---

 
## ☁️ Primjer upotrebe u Google Colab / Jupyter Notebook

1. U Colab-u otvorite novi notebook.  
2. Pokrenite primjere iz foldera **Primjeri**.

---

## 📘 Planirani dodatni sadržaji

📁 `Pomoc/` direktorij (u pripremi) će sadržavati:
- kratke opise i primjere upotrebe svake funkcije unutar SSP librarija  
- tehničku dokumentaciju biblioteke  
- uputstva za proširenje biblioteke

---

## 🧭 TODO

- [ ] Dodati dokumentaciju za SSP funkcije   
- [ ] Uključiti automatske Colab linkove   

---

## 🛠️ Tehnologije

- Python 3.9+  
- NumPy, Matplotlib  
- Jupyter Notebook / Google Colab

---

## 📚 Reference

> Emir Sokić, Almir Salihbegović  
> **Slučajni signali i procesi**,  
> Univerzitet u Sarajevu, 2025.  
> ISBN-13: 978-9926-575-03-8  
> [Link na knjigu](https://ebooks.unsa.ba/index.php/ebooks/catalog/book/81)

---

## © Autorska prava

Sav sadržaj u ovom repozitoriju je namijenjen **obrazovnoj i istraživačkoj upotrebi**.  
Autorska prava pripadaju autorima knjige i Univerzitetu u Sarajevu.
