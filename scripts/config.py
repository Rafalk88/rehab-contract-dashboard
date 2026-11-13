"""Assumptions for the synthetic data generator.

Every value marked ASSUMPTION is a guess to be calibrated against the real data
structure (counts and proportions only, never real values).
"""
from datetime import date

# --- Run -------------------------------------------------------------------
SEED = 68
YEAR = 2026
DATE_FROM = date(YEAR, 1, 1)
DATE_TO = date(YEAR, 12, 31)

# --- Calendar --------------------------------------------------------------
# Polish public holidays. Only those on a weekday remove a working day;
# the weekend ones are listed for completeness (they matter in other years).
HOLIDAYS = [
    date(YEAR, 1, 1),    # New Year
    date(YEAR, 1, 6),    # Epiphany
    date(YEAR, 4, 6),    # Easter Monday (Easter Sunday: 5.04)
    date(YEAR, 5, 1),    # Labour Day
    date(YEAR, 5, 3),    # Constitution Day (Sunday in 2026)
    date(YEAR, 6, 4),    # Corpus Christi
    date(YEAR, 8, 15),   # Assumption Day (Saturday in 2026)
    date(YEAR, 11, 1),   # All Saints' Day (Sunday in 2026)
    date(YEAR, 11, 11),  # Independence Day
    date(YEAR, 12, 24),  # Christmas Eve (public holiday since 2025)
    date(YEAR, 12, 25),  # Christmas Day
    date(YEAR, 12, 26),  # Second day of Christmas (Saturday in 2026)
]
# NOTE: Easter Monday and Corpus Christi move every year: update them when YEAR changes.

# --- Units -----------------------------------------------------------------
# type "clinic": doctor visits, low volume. type "rehab_unit": physiotherapy, high volume.
# visits_per_day: average scheduled visits per working day.
# patients: unique patients per year (each gets at least one visit).
# Real reference (13.11): the clinic had 753 unique patients last year.
UNITS = {
    1: dict(name="Poradnia rehabilitacyjna dla dorosłych", type="clinic", age_group="adults",
            visits_per_day=2.5, staff=1, patients=250),                      # ASSUMPTION
    2: dict(name="Poradnia rehabilitacyjna dla dzieci", type="clinic", age_group="children",
            visits_per_day=2.5, staff=1, patients=250),                      # ASSUMPTION
    3: dict(name="Zakład Rehabilitacji Leczniczej dla Dorosłych", type="rehab_unit", age_group="adults",
            visits_per_day=80, staff=8, patients=900),                       # ASSUMPTION
    4: dict(name="Zakład Rehabilitacji Leczniczej dla Dzieci", type="rehab_unit", age_group="children",
            visits_per_day=35, staff=4, patients=400),                       # ASSUMPTION
}
STAFF_ROLE = {"clinic": "doctor", "rehab_unit": "physiotherapist"}

# --- Patients --------------------------------------------------------------
FEMALE_SHARE = 0.65  # ASSUMPTION

# --- Volume over time ------------------------------------------------------
# Multiplier of daily visits by month (summer holidays and December are quieter). ASSUMPTION
SEASONALITY = {1: 1.00, 2: 1.05, 3: 1.05, 4: 1.00, 5: 1.00, 6: 0.95,
               7: 0.75, 8: 0.70, 9: 1.00, 10: 1.05, 11: 1.05, 12: 0.85}
# Extra summer dip for children (camps, holidays). ASSUMPTION
CHILDREN_SUMMER = {7: 0.85, 8: 0.85}
# Multiplier by weekday, Monday = 0. ASSUMPTION
WEEKDAY = {0: 1.10, 1: 1.05, 2: 1.00, 3: 1.00, 4: 0.85}

# --- Visit type and duration -----------------------------------------------
# visit_kind is derived: a patient's earliest visit in a unit is "first", the rest "follow-up".
XRAY_SHARE = {"clinic": 0.35, "rehab_unit": 0.0}  # ASSUMPTION: X-ray only in the clinic
# Scheduled duration in minutes (business question: ~45 with X-ray, ~25 without).
DURATION = {("clinic", True): 45, ("clinic", False): 25, ("rehab_unit", False): 30}
DURATION_NOISE = 5  # +/- minutes, completed visits only

# --- Status and absence reasons --------------------------------------------
STATUS_SHARE = {"completed": 0.83, "no_show": 0.10, "rescheduled": 0.07}  # ASSUMPTION
# Reasons only for visits that did not take place (weights = how often). ASSUMPTION
REASONS = {
    "no_show": {"no specific reason provided": 0.6, "sickness": 0.2, "forgot": 0.2},
    "rescheduled": {"patient request": 0.55, "staff absence": 0.30, "equipment unavailable": 0.15},
}

# --- To decide: not used by the generator yet ------------------------------
# These overlap with UNITS above (which gives 2 doctors, 1800 patients, 36% children).
DOCTOR_NUMBER = 4            # ASSUMPTION: doctors in total
PATIENTS_NUMBER = 3000       # ASSUMPTION: unique patients per year, all units
CHILDREN_SHARE = 0.3         # ASSUMPTION: share of patients who are children