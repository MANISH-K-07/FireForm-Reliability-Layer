import random
random.seed(42)

incident_types = [
    "fire", "explosion", "gas leak", "chemical spill", "smoke"
]

severity_phrases = [
    "massive", "minor", "severe", "small", "dangerous",
    "catastrophic", "low impact", "critical", "manageable"
]

locations = [
    "warehouse", "residential complex", "factory unit",
    "industrial area", "shopping mall", "office building",
    "apartment block", "construction site", "parking lot"
]

time_phrases = [
    "yesterday evening",
    "last night",
    "this morning",
    "today",
    "a few hours ago",
    "earlier today"
]

outcomes = [
    "with casualties",
    "with no injuries",
    "but no visible damage",
    "causing panic",
    "with multiple reports",
    "with minor impact"
]


def generate_incident():

    s = random.choice(severity_phrases)
    i = random.choice(incident_types)
    l = random.choice(locations)
    t = random.choice(time_phrases)
    o = random.choice(outcomes)

    templates = [
        f"{s} {i} reported at {l} {t} {o}",
        f"There was a {s} {i} in the {l} {t}",
        f"{i.capitalize()} occurred at the {l} {t} {o}",
        f"Emergency due to {s} {i} near {l} {t}",
        f"{s.capitalize()} incident involving {i} at {l} {t}"
    ]

    return random.choice(templates)


def generate_dataset(n=150):
    return [generate_incident() for _ in range(n)]
