# Primjer 2.3: analiza slučajnih promjenljivih u Python okruženju (knjiga, sekcija 2.6, str. 46)

Za slučajnu promjenljivu iz zadane raspodjele analiziraju se: realizacije slučajne promjenljive, očekivana vrijednost,
srednjekvadratna vrijednost, varijansa, medijana, te funkcija raspodjele i funkcija gustine vjerovatnoće
(numerički i analitički, uz biblioteku `ssp` iz ovog repozitorija).

Rayleigheva raspodjela je urađena u knjizi i u `Primjeri/Kodovi_2.1-2.15.ipynb` / `Kodovi_2.16-2.37.ipynb`
(programski kodovi 2.8–2.15 i 2.23–2.29). Kodovi su preuzeti odatle, a ostale tri raspodjele su urađene istim postupkom.

| Raspodjela | Parametri (programski kod 2.11) | Colab |
|---|---|---|
| Uniformna | $a=0$, $b=10$ | [otvori](https://colab.research.google.com/github/ierovic1ba/ssp/blob/main/SIS2_Raspodjele/Z1_Uniformna_raspodjela.ipynb) |
| Normalna (Gaussova) | $a=3$, $\sigma=0.1$ | [otvori](https://colab.research.google.com/github/ierovic1ba/ssp/blob/main/SIS2_Raspodjele/Z2_Normalna_raspodjela.ipynb) |
| Rayleigheva | $\eta=5$ | [otvori](https://colab.research.google.com/github/ierovic1ba/ssp/blob/main/SIS2_Raspodjele/Z3_Rayleigheva_raspodjela.ipynb) |
| Eksponencijalna | $a=0.25$ (`np.random.exponential(4, N)`) | [otvori](https://colab.research.google.com/github/ierovic1ba/ssp/blob/main/SIS2_Raspodjele/Z4_Eksponencijalna_raspodjela.ipynb) |

U Colabu: `Runtime → Run all`. Prva ćelija sama klonira repozitorij i učita biblioteku `ssp`.
