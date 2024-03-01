::: mermaid
erDiagram
    Users||--|{Accounts : has
    Accounts||--|{Roosters: has
    Roosters||--o|Characters: has
    Roosters}o--||Servers: has
    Characters}o--||Servers: bounded_to
    Characters}o--||Roosters: bounded_to
    Characters}o--||Accounts: bounded_to
    Characters}o--||Users: bounded_to
    Characters}|--o{Tasks: many_to_many
    Roosters}|--o{Tasks: many_to_many

    CharacterTasks||--||Tasks: has
    RoosterTasks||--||Tasks: has

    Tasks}o--o|Content: linked
    Content{
        string code PK "Identifier"

    }

    
:::
