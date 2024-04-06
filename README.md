# Warhammer 40,000 Kill Team Data Framework [2021 Edition]

    - Data framework for use with a Warhammer Kill Team application.
    - Designed for use with team building and general searches for information.

## Design, Requirements, and Known Issues

Required Code Elements

    - The Combi ability provides a Boltgun for every operative carrying a weapon with the "Combi" special rule. There needs to be a boolean to provide the operative with a Boltgun if true.

Required UI Elements

    - Some weapons have options for how to fire them. To make it user friendly, a tab style of swapping between choices would be simple and quick. No dropdown menus. Only seamless transitions.

    - A plus sign (+) is required to the right of these integers:
        - Save
        - Ballistic Skill
        - Weapon Skill
    
    - A quotation mark (") is required to the right of this integer:
        - Movement
    
    - A forward slash (/) is required between the two (2) integers:
        - Damage
    
    - The following factions, using the "house" variable, require the following name to the left of the string:
        - Space Marine "Chapter"
        - Grey Knight "Brotherhood"
        - Imperial Guard "Regiment"
        - Forge World "Forge World"
        - Ecclesiarchy "Order"
        - Talons of the Emperor "Shield Host"
        - Traitor Space Marine "Legion"
        - Death Guard "Plague Company"
        - Thousand Sons "Great Cult"
        - Chaos Daemon "Chaos God"
        - Craftworld "Craftworld"
        - Commorrite "Kabal"
        - Troupe "Masque"
        - Greenskin "Clan"
        - Tomb World "Dynasty"
        - Hunter Cadre "Sept"
        - Cadre Mercenary "Sept"
        - Hive Fleet "Hive Fleet"
        - Brood Coven "Cult"

Outdated Frameworks

    - Brood Coven
    - Chaos Daemon
    - Commorrite
    - Craftworld
    - Death Guard
    - Imperial Guard
    - Space Marine
    - Thousand Sons
    - Tomb World
    - Traitor Space Marine

TO-DO

    - Review and potentially update all Global frameworks

### Change Log

v0.06.04.24

    - Operatives
        - Migration work is proceeding quickly with half the faction data already consolidated.

    - Global Data
        - All files located in this folder have been moved to the main location and the folder removed.

v0.04.04.24

    - Framework
        - Design has been updated. All stats are now integers instead of strings. This will require certain UI design elements to display information properly. Damage was split into two integers for ease of use.
        - A redesign for abilities, equipment, rules, and other somewhat universal data will be required after the faction data is updated.
    
    - Faction Data
        - Operator names have been updated to remove brackets.
        - A new file has been created and all operative data will be migrated to this single data source. Comments will be heavily used to aid in readability.
        - Faction data is currently being updated to match the new framework design.
        - All updates to the new operatives file are to be listed under "Operatives".

v0.03.04.24

    -Framework
        - Framework has been designed to accomodate all information listed on data slates. Updates will be required as the project advances and Games Workshop adjusts their game rules.

    - Faction Data
        - All factions have been added from the core rulebook. Additional factions have been released and need to be added.
