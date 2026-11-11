# NEXT: rehab-contract-dashboard

> Jedna rzecz naraz. Na górze zawsze to, co robię w najbliższej sesji.
> Ostatnia aktualizacja: 2026-11-09
> Plik planistyczny, poza repo (repo jest po angielsku). Ogólny plan toru Power BI: `powerbi/NEXT.md`.

## Teraz (wtorek 10.11, blok 2 h)

**Zadanie:** generator danych syntetycznych, wersja 0 (pozycja 3 z kolejki w `powerbi/NEXT.md`)
**Zrobione, gdy:** `python scripts/generate.py` jednym poleceniem zapisuje 7 plików CSV do `data/` (tabele z modelu gwiazdy w README, bez kalendarza), dwa uruchomienia dają identyczne pliki (stały seed), wydruk kontrolny pokazuje sensowne liczby, a całość jest na GitHubie.

Dlaczego teraz, choć struktura z pracy jest dopiero do 20.11: wszystkie założenia (liczby jednostek, proporcje, powody nieobecności) siedzą w jednym pliku `scripts/config.py` z dopiskiem „ZAŁOŻENIE”. Po spisaniu struktury w pracy zmieniam tylko ten plik, a kod zostaje.

- [x] (0–15 min) Start
  - `git pull`, środowisko: `python -m venv .venv`, `requirements.txt` (tylko `numpy` i `pandas`), `.venv/` do `.gitignore`
  - `scripts/config.py`: seed, okres (1.01–31.12.2026), jednostki, liczba lekarzy i pacjentów, proporcje dzieci / dorośli, z RTG / bez (45 / 25 min), % nieobecności i powody z wagami, sezonowość (lato, grudzień słabiej). Każda wartość z komentarzem `# ZAŁOŻENIE, sprawdzić 20.11`
- [x] (15–40 min) Wymiary
  - `units.csv`: 4 jednostki (poradnia / zakład × dzieci / dorośli)
  - `doctors.csv`: rola (lekarz / fizjoterapeuta), jednostka
  - `procedures.csv`: ok. 15 procedur, kod, nazwa, punkty (wartości umowne, w kolumnie lub README dopisek, że punkty NFZ są do podmiany na publiczny katalog)
  - `patients.csv`: ok. 2000 pacjentów, grupa wiekowa zgodna z jednostką, płeć
  - `calendar.csv`: na razie pomijam, `dim_date` powstanie w SQL (`generate_series`)
- [ ] (40–85 min) Fakty
  - `visits.csv`: dni robocze 2026, liczba wizyt dziennie wg jednostki × sezonowość, typ wizyty (pierwsza / kontrolna, z RTG / bez), status (zrealizowana / nieobecność / przesunięta), powód tylko przy nieodbytych, czas trwania
  - `visit_procedures.csv`: tylko dla wizyt zrealizowanych, 1–3 procedury, ilość
  - `contract_plan.csv`: jednostka × miesiąc, plan punktów i cena punktu. Plan liczony tak, żeby wykonanie wyszło ok. 90–105% (różnie w jednostkach, żeby raport miał co pokazać)
- [ ] (85–100 min) Kontrola na wydruku (koniec skryptu)
  - liczba wierszy w każdym pliku, % nieobecności ogółem, top 3 powody, wykonanie kontraktu % wg jednostki, brak osieroconych kluczy (id w faktach istnieją w wymiarach)
  - Drugie uruchomienie + `git diff --stat data/`: zero zmian
- [ ] (100–120 min) Zamknięcie
  - README: sekcja „How to generate the data” (2 polecenia), w strukturze dopisać `scripts/generate.py`, `scripts/config.py`
  - Commit `feat: synthetic data generator v0` + push
  - Wpis w trackerze, odhaczyć pozycję 3 w `powerbi/NEXT.md` jako „v0” (kalibracja po 20.11), tu wpisać następny blok

**Jeśli zabraknie czasu:** tnę od końca faktów. Minimum na koniec bloku to wymiary + `visits.csv` + kontrola + push. `visit_procedures` i `contract_plan` przechodzą na następny blok.

**Poza zakresem:** Faker, prawdziwe nazwy procedur NFZ, kolejka pacjentów (raport 2), Docker i SQL.

## Kolejka (po kolei, nie skacz)

1. [ ] Kalibracja generatora po spisaniu struktury w pracy (po 20.11, ok. 30 min, zmiany tylko w `config.py`)
2. [ ] Hurtownia SQL minimum: PostgreSQL w Dockerze, schematy `staging` i `dw`, `dim_date` z `generate_series` (pierwszy blok), termin 10.12
3. [ ] Raport 1 w PBIP na widokach z `dw`, termin 21.12

## Zrobione

| Data       | Co                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------- |
| 2026-11-09 | Repo na GitHubie, szkielet folderów, README (architektura, źródła danych, pytania, model gwiazdy) |
