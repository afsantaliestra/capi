"""DB"""
# APP ITEMS
servers = [
    {"name": "Thirain"},
    {"name": "Kayangel"},
    {"name": "Ealyn"},
]

contents = [
    {
        "title": "Valtan",
        "modes": [
            {
                "mode": "normal",
                "min_ilvl": 1415,
                "max_ilvl": None,
                "gates": 2,
            },
            {
                "mode": "hard",
                "min_ilvl": 1445,
                "max_ilvl": None,
                "gates": 2,
            },
            {
                "mode": "inferno",
                "min_ilvl": 1445,
                "max_ilvl": None,
                "gates": 2,
            },
            {
                "mode": "extreme",
                "min_ilvl": 1415,
                "max_ilvl": None,
                "gates": 2,
            },
        ],
    },
    {
        "title": "Brel",
        "modes": [
            {
                "mode": "rehershal",
                "min_ilvl": 1460,  # TODO: Review
                "max_ilvl": None,
                "gates": 3,
            },
            {
                "mode": "normal",
                "gates": [
                    {
                        "gate": 1,
                        "min_ilvl": 1490,
                        "max_ilvl": None,
                    },
                    {
                        "gate": 2,
                        "min_ilvl": 1490,
                        "max_ilvl": None,
                    },
                    {
                        "gate": 3,
                        "min_ilvl": 1500,
                        "max_ilvl": None,
                    },
                    {
                        "gate": 4,
                        "min_ilvl": 1520,
                        "max_ilvl": None,
                    },
                ],
            },
            {
                "mode": "hard",
                "gates": [
                    {
                        "gate": 1,
                        "min_ilvl": 1540,
                        "max_ilvl": None,
                    },
                    {
                        "gate": 2,
                        "min_ilvl": 1540,
                        "max_ilvl": None,
                    },
                    {
                        "gate": 3,
                        "min_ilvl": 1550,
                        "max_ilvl": None,
                    },
                    {
                        "gate": 4,
                        "min_ilvl": 1560,
                        "max_ilvl": None,
                    },
                ],
            },
            {
                "mode": "inferno",
                "gates": [
                    {
                        "gate": 1,
                        "min_ilvl": 1490,  # TODO: Review
                        "max_ilvl": None,
                    },
                    {
                        "gate": 2,
                        "min_ilvl": 1490,  # TODO: Review
                        "max_ilvl": None,
                    },
                ],
            },
        ],
    },
]

# USER ITEMS
users = [{"username": "Necros"}]

accounts = [
    {"name": "Main", "user": users[0]},
    {"name": "Alt", "user": users[0]},
]

roosters = [
    {"server": servers[0], "account": accounts[0]},
    {"server": servers[1], "account": accounts[0]},
    {"server": servers[2], "account": accounts[0]},
    {"server": servers[0], "account": accounts[1]},
    {"server": servers[1], "account": accounts[1]},
]

characters = [
    {
        # Data
        "name": "Kayleenaiah",
        # Links
        "user": users[0],
        "account": accounts[0],
        "rooster": roosters[0],
    },
]

tasks = [
    {
        "title": "Get Prime Gaming Capsule",
        "scope": "account",  # TODO: Podría ser de usuario, ya que no es normal tener 2 cuentas de Prime.
        "frequency": "monthly",  # Cada cuanto se tiene que hacer.
        "repetitions": {
            "max": 1,  # Cuantas veces se tiene que hacer por cada frecuencia.
            "actual": 0,  # Cuantas se ha hecho
        },
    },
    {
        "title": "Login",
        "scope": "rooster",
        "frequency": "daily",
        "repetitions": {
            "max": 1,  # Cuantas veces se tiene que hacer por cada frecuencia.
            "actual": 0,  # Cuantas se ha hecho
        },
    },
    {
        "title": "Chaos Dungeon",
        "scope": "character",
        "frequency": "daily",
        "repetitions": {
            "max": 2,  # Cuantas veces se tiene que hacer por cada frecuencia.
            "actual": 0,  # Cuantas se ha hecho
        },
    },
    {  # TODO: Esto no sirve para raids.
        "title": "Brel",
        "scope": "character",
        "frequency": "weekly",
        "repetitions": {
            "max": 1,  # Cuantas veces se tiene que hacer por cada frecuencia.
            "actual": 0,  # Cuantas se ha hecho
        },
    },
]
