SEED = 68

DATE_FROM = "2026-01-01"
DATE_TO = "2026-12-31"

ORGS = ["Zakład Rehabilitacji Leczniczej dla Dorosłych", "Zakład Rehabilitacji Leczniczej dla Dzieci", "Poradnia rehabilitacyjna dla dorosłych", "Poradnia rehabilitacyjna dla dzieci"]
DOCTOR_NUMBER = 4
PATIENTS_NUMBER = 3000 # ZAŁOŻENIE na dany rok - unikalni pacjenci, którzy korzystają z usług jednostek rehabilitacyjnych w danym roku

CHILDREN_PERCENTAGE = 0.3 # ZAŁOŻENIE - procent pacjentów, którzy są dziećmi
RTG_PERCENTAGE = 0.35 # ZAŁOŻENIE - procent pacjentów, którzy korzystają z usług RTG
RTG_MIN_TIME = 45 # ZAŁOŻENIE - minimalny czas trwania badania RTG w minutach
RTG_MIN_WITHOUT_TIME = 25 # ZAŁOŻENIE - minimalny czas trwania wizyty bez badania RTG w minutach

ABSENCE_PERCENTAGE = 0.1 # ZAŁOŻENIE - procent pacjentów, którzy nie przychodzą na wizytę
ABSENCE_REASONS = { # ZAŁOŻENIE (wagi = jak często)
    "sickness": 0.2,
    "forgot": 0.2,
    "no specific reason provided": 0.6
}

SEASONALITY = { # ZAŁOŻENIE (1.0 = normalnie, mniej = słabiej)
    7: 0.7,
    8: 0.7,
    12: 0.6
}