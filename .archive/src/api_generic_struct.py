"""src/utils/api_generic_struct.py - API Generic Struct"""

api_generic_struct = {
    "users": {
        "name": "users",
        "api": {
            "prefix": "/users",  # If empty, name.
            "tags": ["Users"],  # If empty, name capitalized.
            "actions": ["post", "get_all", "get_by_pk"],
        },
        "table_name": "users",
        "pk": "code",
        "unique_fields": ["username"],
        "fields": {
            "username": (str, ...),
            "display_name": (str, None),
        },
    },
    "contents": {
        "name": "contents",
        "api": {
            "prefix": "/contents",  # If empty, name.
            "tags": ["Contents"],  # If empty, name capitalized.
            "actions": ["post", "get_all", "get_by_pk"],
        },
        "table_name": "contents",
        "pk": "code",
        "unique_fields": ["name"],
        "fields": {
            "name": (str, ...),
            "scope": (str, ...),  # Character, Rooster
            "repetitions": (
                str,
                ...,
            ),  # If Daily, times per day, if Weekly, times per week and So on.
            "frequency": (str, ...),  # Daily, Weekly, Bi-Weekly, Specific Days, One Time
            "rests": (bool, ...),  # Yes (Has Rests) o No.
            "min_ilvl": (int, ...),
            "max_ilvl": (int, ...),
            "modes": (str, ...),  # Only for Abyssal Dungeons and Legion Raids
        },
    },
    "characters": {
        "name": "characters",
        "api": {
            "prefix": "/characters",  # If empty, name.
            "tags": ["Characters"],  # If empty, name capitalized.
            "actions": ["post", "get_all", "get_by_pk"],
        },
        "table_name": "characters",
        "pk": "code",
        "unique_fields": ["name", "account", "rooster", "user"],
        "combo_key": True,
        "fields": {
            "name": (str, ...),
            "account": (str, ...),
            "rooster": (str, ...),
            "class": (str, ...),
            "item_level": (int, ...),
            "main": (bool, ...),
            "weekly_gold": (bool, ...),
            "lazy": (bool, ...),
            "user": (str, ...),
        },
    },
}
