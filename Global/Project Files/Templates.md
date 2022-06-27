# Templates

## Faction Templates

### Operative Template

```py

operatives = [
    {   # Unit Template
        "opname":"",
        "stats":{
            "move":"",
            "apl":"",
            "gpact":"",
            "def":"",
            "save":"",
            "wounds":"",
        },
        "rweaps":[
            {   # Weapon Template
                "wname":"",
                "profiles":[
                    {
                        "pname":"",
                        "atts":"",
                        "bskill":"",
                        "dmg":"",
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
                        "atts":"",
                        "wskill":"",
                        "dmg":"",
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
