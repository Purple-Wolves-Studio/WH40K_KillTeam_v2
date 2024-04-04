# Templates

## Faction Templates

### Operative Template

```py

operatives = [
    {   # Unit Template
        "opname":"",
        "stats":{
            "move":,
            "apl":,
            "gpact":,
            "def":,
            "save":,
            "wounds":,
        },
        "rweaps":[
            {   # Weapon Template
                "wname":"",
                "profiles":[
                    {
                        "pname":"",
                        "atts":,
                        "skill":,
                        "dmg1":,
                        "dmg2":,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Weapon Template
                "wname":"",
                "profiles":[
                    {
                        "pname":"",
                        "atts":,
                        "skill":,
                        "dmg1":,
                        "dmg2":,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"",
        "faction":[
        ],
        "house":"",
        "keywords":[
        ],
        "specials":[
        ],
    },
]

```

--------------------------------------------------------------------

## Global Templates

### Ability Template

```py

abilities = [
    {   # Ability Template
        "abname":"",
        "abtext":"",
    },
]
        

```

### Unique Action Template

```py

uacts = [
    {   # Action Template
        "actname":"",
        "actcost":0,
        "actext":"",
    },
]

```
