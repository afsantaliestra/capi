db = {  # TODO: Implement a real DB.
    "users": {
        1: {"code": 1, "username": "necros", "display_name": "Necros"},
        2: {"code": 2, "username": "sorcen", "display_name": "Sorcen"},
    },
    "accounts": {
        1: {"code": 1, "alias": "Primary"},
        2: {"code": 2, "alias": "Secondary"},
    },
    "user_accounts": {
        1: {"user": 1, "account": 1},
        2: {"user": 1, "account": 2},
    },
    "servers": {
        1: {"code": 1, "name": "Thirain"},
        2: {"code": 2, "name": "Kayangel"},
    },
    "account_servers": {
        1: {"account": 1, "server": 1},
        2: {"account": 1, "server": 2},
    },
    "characters": {
        1: {
            "code": 1,
            "name": "Kay",
            "user_code": 1,
            "account_code": 1,
            "server_code": 1,
        },
        2: {
            "code": 2,
            "name": "Nec",
            "user_code": 1,
            "account_code": 1,
            "server_code": 2,
        },
        3: {
            "code": 3,
            "name": "Bärd",
            "user_code": 1,
            "account_code": 2,
            "server_code": 1,
        },
    },
    "tasks": {
        1: {"code": 1, "name": "Daily Login", "predefined": True},
        2: {"code": 2, "name": "Daily Playtime", "predefined": True},
    },
    "character_tasks": {
        1: {
            "code": 1,
            "character_code": 1,
            "task_code": 1,
            "complete": False,
        }
    },
}
