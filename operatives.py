operatives = [
    # --- Brood Coven ---
    {   # Neophyte Hybrid Trooper
        "opname":"Neophyte Hybrid Trooper",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":2,
            "def":3,
            "save":5,
            "wounds":7,
        },
        "rweaps":[
            {   # Autogun
                "wname":"Autogun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Shotgun
                "wname":"Shotgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Neophyte Hybrid",
            "Trooper"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Neophyte Hybrid Gunner
        "opname":"Neophyte Hybrid Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":7,
        },
        "rweaps":[
            {   # Flamer
                "wname":"Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Grenade Launcher
                "wname":"Grenade Launcher",
                "profiles":[
                    {
                        "pname":"Frag",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":4,
                        "srule":[
                            "Blast 2\""
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Krak",
                        "atts":4,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Webber
                "wname":"Webber",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                            "Lethal 5+"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Neophyte Hybrid",
            "Gunner"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Neophyte Hybrid Heavy Gunner
        "opname":"Neophyte Hybrid Heavy Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Heavy Stubber
                "wname":"Heavy Stubber",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Heavy"
                            "Ceaseless"
                            "Fusillade"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Mining Laser
                "wname":"Mining Laser",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Heavy"
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Seismic Cannon
                "wname":"Seismic Cannon",
                "profiles":[
                    {
                        "pname":"Long-wave",
                        "atts":6,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Heavy"
                            "Blast 1\""
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                    {
                        "pname":"Short-wave",
                        "atts":4,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":4,
                        "srule":[
                            "Heavy"
                            "Range 6\""
                        ],
                        "crits":[
                            "Stun"
                            "P 1"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Neophyte Hybrid",
            "Heavy Gunner"
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Neophyte Hybrid Icon Bearer
        "opname":"Neophyte Hybrid Icon Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":7,
        },
        "rweaps":[
            {   # Autogun
                "wname":"Autogun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Shotgun
                "wname":"Shotgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Icon Bearer"
        ],
        "uacts":[
            "Cult Icon"
        ],
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Neophyte Hybrid",
            "Icon Bearer"
        ],
        "specials":[
            "Staunch"
        ]
    },
    {   # Neophyte Hybrid Leader
        "opname":"Neophyte Hybrid Leader",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Autogun
                "wname":"Autogun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Bolt Pistol
                "wname":"Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Shotgun
                "wname":"Shotgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Web Pistol
                "wname":"Web Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Maul
                "wname":"Power Maul",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Power Pick
                "wname":"Power Pick",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Neophyte Hybrid",
            "Leader"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ]
    },
    {   # Acolyte Hybrid Trooper
        "opname":"Acolyte Hybrid Trooper",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Cult Knife and Claw
                "wname":"Cult Knife and Claw",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Balanced"
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Acolyte Hybrid",
            "Trooper"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Acolyte Hybrid Gunner
        "opname":"Acolyte Hybrid Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Hand Flamer
                "wname":"Hand Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                            "Torrent 1\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Cult Knife & Claw
                "wname":"Cult Knife & Claw",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Balanced"
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Acolyte Hybrid",
            "Gunner"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ]
    },
    {   # Acolyte Hybrid Fighter
        "opname":"Acolyte Hybrid Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Heavy Rock Cutter
                "wname":"Heavy Rock Cutter",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":4,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Heavy Rock Drill
                "wname":"Heavy Rock Drill",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":7,
                        "srule":[
                            "Brutal"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Heavy Rock Saw
                "wname":"Heavy Rock Saw",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":5,
                        "dmg2":6,
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
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Acolyte Hybrid",
            "Fighter"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Acolyte Hybrid Icon Bearer
        "opname":"Acolyte Hybrid Icon Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Cult Knife & Claw
                "wname":"Cult Knife & Claw",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Balanced"
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Icon Bearer"
        ],
        "uacts":[
            "Cult Icon"
        ],
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Acolyte Hybrid",
            "Icon Bearer"
        ],
        "specials":[
            "Staunch"
        ]
    },
    {   # Acolyte Hybrid Leader
        "opname":"Acolyte Hybrid Leader",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":9,
        },
        "rweaps":[
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Hand Flamer
                "wname":"Hand Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                            "Torrent 1\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Lash Whip
                "wname":"Lash Whip",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 2\""
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Cult Bonesword & Claw
                "wname":"Cult Bonesword & Claw",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced"
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Cult Knife & Claw
                "wname":"Cult Knife & Claw",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Balanced"
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Lash Whip"
        ],
        "uacts":[
        ],
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Acolyte Hybrid",
            "Leader"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Hybrid Metamorph Fighter
        "opname":"Hybrid Metamorph Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Metamorph Mutations
                "wname":"Metamorph Mutations",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced"
                            "Brutal"
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Hybrid Metamorph",
            "Fighter"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Hybrid Metamorph Gunner
        "opname":"Hybrid Metamorph Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Hand Flamer
                "wname":"Hand Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                            "Torrent 1\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Metamorph Mutations
                "wname":"Metamorph Mutations",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced"
                            "Brutal"
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Hybrid Metamorph",
            "Gunner"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ]
    },
    {   # Hybrid Metamorph Icon Bearer
        "opname":"Hybrid Metamorph Icon Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Metamorph Mutations
                "wname":"Metamorph Mutations",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced"
                            "Brutal"
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Icon Bearer"
        ],
        "uacts":[
            "Cult Icon"
        ],
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Hybrid Metamorph",
            "Icon Bearer"
        ],
        "specials":[
            "Staunch"
        ]
    },
    {   # Hybrid Metamorph Leader
        "opname":"Hybrid Metamorph Leader",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":9,
        },
        "rweaps":[
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Hand Flamer
                "wname":"Hand Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                            "Torrent 1\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Cult Bonesword & Metamorph Mutations
                "wname":"Cult Bonesword & Metamorph Mutations",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced"
                            "Lethal 5+"
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
            {   # Metamorph Mutations
                "wname":"Metamorph Mutations",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced"
                            "Brutal"
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Brood Coven",
        "faction":[
            "Genestealer Cults"
        ],
        "house":"",
        "keywords":[
            "Hybrid Metamorph",
            "Leader"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    # --- Cadre Mercenary ---
    {   # Kroot Carnivore Warrior
        "opname":"Kroot Carnivore Warrior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
            {   # Kroot Rifle
                "wname":"Kroot Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Rifle Blades
                "wname":"",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Masters of Camouflage"
        ],
        "uacts":[
        ],
        "fackey":"Cadre Mercenary",
        "faction":[
            "T'au Empire"
        ],
        "house":"T'au Auxiliary",
        "keywords":[
            "Kroot"
            "Carnivore"
            "Warrior"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ]
    },
    {   # Kroot Carnivore Leader
        "opname":"Kroot Carnivore Leader",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":9,
        },
        "rweaps":[
            {   # Kroot Rifle
                "wname":"Kroot Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Rifle Blades
                "wname":"",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Masters of Camouflage"
        ],
        "uacts":[
        ],
        "fackey":"Cadre Mercenary",
        "faction":[
            "T'au Empire"
        ],
        "house":"T'au Auxiliary",
        "keywords":[
            "Kroot"
            "Carnivore"
            "Leader"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ]
    },
    {   # Kroot Hound
        "opname":"Kroot Hound",
        "stats":{
            "move":8,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Ripping Fangs
                "wname":"Ripping Fangs",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Hunting Beast"
            "Masters of Camouflage"
        ],
        "uacts":[
        ],
        "fackey":"Cadre Mercernary",
        "faction":[
            "T'au Empire"
        ],
        "house":"T'au Auxiliary",
        "keywords":[
            "Kroot"
            "Hound"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Krootox
        "opname":"Krootox",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":16,
        },
        "rweaps":[
            {   # Kroot Gun
                "wname":"Kroot Gun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Krootox Fists
                "wname":"",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Brutal"
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
        "fackey":"Cadre Mercenary",
        "faction":[
            "T'au Empire"
        ],
        "house":"T'au Auxiliary",
        "keywords":[
            "Kroot"
            "Krootox"
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman"
        ]
    },
    # --- Chaos Daemon ---
    {   # Bloodletter Fighter
        "opname":"Bloodletter Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":9,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Hellblade
                "wname":"Hellblade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon"
        ],
        "uacts":[
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Khorne",
        "keywords":[
            "Bloodletter",
            "Fighter"
        ],
        "specials":[
            "Combat"
        ]
    },
    {   # Bloodletter Icon Bearer
        "opname":"Bloodletter Icon Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":9,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Hellblade
                "wname":"Hellblade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon",
            "Icon Bearer"
        ],
        "uacts":[
            "Daemonic Icon"
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Khorne",
        "keywords":[
            "Bloodletter",
            "Icon Bearer"
        ],
        "specials":[
            "Combat"
        ]
    },
    {   # Bloodletter Horn Bearer
        "opname":"Bloodletter Horn Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":9,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Hellblade
                "wname":"Hellblade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon"
        ],
        "uacts":[
            "Instrument of Chaos"
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Khorne",
        "keywords":[
            "Bloodletter",
            "Horn Bearer"
        ],
        "specials":[
            "Combat"
        ]
    },
    {   # Bloodreaper
        "opname":"Bloodreaper",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":10,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Hellblade
                "wname":"Hellblade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon"
        ],
        "uacts":[
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Khorne",
        "keywords":[
            "Leader",
            "Bloodletter",
            "Bloodreaper"
        ],
        "specials":[
            "Combat"
        ]
    },
    {   # Daemonette Fighter
        "opname":"Daemonette Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Claws
                "wname":"Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon"
        ],
        "uacts":[
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Slaanesh",
        "keywords":[
            "Daemonette",
            "Fighter"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Daemonette Icon Bearer
        "opname":"Daemonette Icon Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Claws
                "wname":"Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon",
            "Icon Bearer"
        ],
        "uacts":[
            "Daemonic Icon"
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Slaanesh",
        "keywords":[
            "Daemonette",
            "Icon Bearer"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Daemonette Horn Bearer
        "opname":"Daemonette Horn Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Claws
                "wname":"Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon"
        ],
        "uacts":[
            "Instrument of Chaos"
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Slaanesh",
        "keywords":[
            "Daemonette",
            "Horn Bearer"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Alluress
        "opname":"Alluress",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":9,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Claws
                "wname":"Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon"
        ],
        "uacts":[
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Slaanesh",
        "keywords":[
            "Leader",
            "Daemonette",
            "Alluress"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Plaguebearer Fighter
        "opname":"Plaguebearer Fighter",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Plaguesword
                "wname":"Plaguesword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon",
            "Disgustingly Resilient"
        ],
        "uacts":[
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Nurgle",
        "keywords":[
            "Plaguebearer",
            "Fighter"
        ],
        "specials":[
            "Staunch"
        ]
    },
    {   # Plaguebearer Icon Bearer
        "opname":"Plaguebearer Icon Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Plaguesword
                "wname":"Plaguesword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon",
            "Disgustingly Resilient",
            "Icon Bearer"
        ],
        "uacts":[
            "Daemonic Icon"
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Nurgle",
        "keywords":[
            "Plaguebearer",
            "Icon Bearer"
        ],
        "specials":[
            "Staunch"
        ]
    },
    {   # Plaguebearer Horn Bearer
        "opname":"Plaguebearer Horn Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Plaguesword
                "wname":"Plaguesword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon",
            "Disgustingly Resilient"
        ],
        "uacts":[
            "Instrument of Chaos"
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Nurgle",
        "keywords":[
            "Plaguebearer",
            "Horn Bearer"
        ],
        "specials":[
            "Staunch"
        ]
    },
    {   # Plagueridden
        "opname":"Plagueridden",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":9,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Plaguesword
                "wname":"Plaguesword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon",
            "Disgustingly Resilient"
        ],
        "uacts":[
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Nurgle",
        "keywords":[
            "Leader",
            "Plaguebearer",
            "Plagueridden"
        ],
        "specials":[
            "Staunch"
        ]
    },
    {   # Pink Horror Fighter
        "opname":"Pink Horror Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
            {   # Coruscating Flames
                "wname":"Coruscating Flames",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon"
        ],
        "uacts":[
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Tzeentch",
        "keywords":[
            "Pink Horror",
            "Fighter"
        ],
        "specials":[
            "Marksman"
        ]
    },
    {   # Pink Horror Icon Bearer
        "opname":"Pink Horror Icon Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
            {   # Coruscating Flames
                "wname":"Coruscating Flames",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon",
            "Icon Bearer"
        ],
        "uacts":[
            "Daemonic Icon"
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Tzeentch",
        "keywords":[
            "Pink Horror",
            "Icon Bearer"
        ],
        "specials":[
            "Marksman"
        ]
    },
    {   # Pink Horror Horn Bearer
        "opname":"Pink Horror Horn Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
            {   # Coruscating Flames
                "wname":"Coruscating Flames",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon"
        ],
        "uacts":[
            "Instrument of Chaos"
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Tzeentch",
        "keywords":[
            "Pink Horror",
            "Horn Bearer"
        ],
        "specials":[
            "Marksman"
        ]
    },
    {   # Pink Horror Iridescent
        "opname":"Pink Horror Iridescent",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":9,
        },
        "rweaps":[
            {   # Coruscating Flames
                "wname":"Coruscating Flames",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Daemon"
        ],
        "uacts":[
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Tzeentch",
        "keywords":[
            "Leader",
            "Pink Horror",
            "Iridescent"
        ],
        "specials":[
            "Marksman"
        ]
    },
    {   # Blue Horror
        "opname":"Blue Horror",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":2,
            "def":3,
            "save":6,
            "wounds":6,
        },
        "rweaps":[
            {   # Fizzing Flames
                "wname":"Fizzing Flames",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Ephemeral Daemon"
        ],
        "uacts":[
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Tzeentch",
        "keywords":[
            "Blue Horror"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Brimstone Horrors
        "opname":"Brimstone Horrors",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":2,
            "def":2,
            "save":6,
            "wounds":5,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":2,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Ephemeral Daemon",
            "Insignificant"
        ],
        "uacts":[
        ],
        "fackey":"Chaos Daemon",
        "faction":[
            "Chaos",
            "Daemon"
        ],
        "house":"Tzeentch",
        "keywords":[
            "Brimstone Horrors"
        ],
        "specials":[
        ]
    },
    # --- Commorrite ---
    {   # Kabalite Warrior
        "opname":"Kabalite Warrior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Splinter Rifle
                "wname":"Splinter Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":2,
                        "dmg2":4,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Array of Blades
                "wname":"Array of Blades",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Commorrite",
        "faction":[
            "Aeldari",
            "Drukhari"
        ],
        "house":"",
        "keywords":[
            "Kabalite",
            "Warrior"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Sybarite
        "opname":"Sybarite",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":9,
        },
        "rweaps":[
            {   # Blast Pistol
                "wname":"Blast Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\"",
                            "AP 2"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Splinter Pistol
                "wname":"Splinter Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":4,
                        "srule":[
                            "Lethal 5+",
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Splinter Rifle
                "wname":"Splinter Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":4,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Agoniser
                "wname":"Agoniser",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":3,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5",
                            "Brutal"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Array of Blades
                "wname":"Array of Blades",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
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
        "fackey":"Commorrite",
        "faction":[
            "Aeldari",
            "Drukhari"
        ],
        "house":"",
        "keywords":[
            "Kabalite",
            "Leader",
            "Sybarite"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ]
    },
    {   # Kabalite Gunner
        "opname":"Kabalite Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Blaster
                "wname":"Blaster",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP 2"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Shredder
                "wname":"Shredder",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "Blast 2\""
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Array of Blades
                "wname":"Array of Blades",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Commorrite",
        "faction":[
            "Aeldari",
            "Drukhari"
        ],
        "house":"",
        "keywords":[
            "Kabalite",
            "Gunner"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Kabalite Heavy Gunner
        "opname":"Kabalite Heavy Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Dark Lance
                "wname":"Dark Lance",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":6,
                        "dmg2":7,
                        "srule":[
                            "Heavy",
                            "Unwieldy",
                            "AP 2"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Splinter Cannon
                "wname":"Splinter Cannon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                            "Heavy",
                            "Lethal 5+",
                            "Fussilade"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Array of Blades
                "wname":"Array of Blades",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Commorrite",
        "faction":[
            "Aeldari",
            "Drukhari"
        ],
        "house":"",
        "keywords":[
            "Kabalite",
            "Heavy Gunner"
        ],
        "specials":[
            "Marksman"
        ]
    },
    {   # Wych Warrior
        "opname":"Wych Warrior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
            {   # Splinter Pistol
                "wname":"Splinter Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":2,
                        "dmg2":4,
                        "srule":[
                            "Lethal 5+",
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Hekatarii Blade
                "wname":"Hekatarii Blade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Dodge",
        ],
        "uacts":[
        ],
        "fackey":"Commorrite",
        "faction":[
            "Aeldari",
            "Drukhari"
        ],
        "house":"",
        "keywords":[
            "Wych",
            "Warrior"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Hekatrix
        "opname":"Hekatrix",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":9,
        },
        "rweaps":[
            {   # Blast Pistol
                "wname":"Blast Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\"",
                            "AP 2"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Splinter Pistol
                "wname":"Splinter Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":4,
                        "srule":[
                            "Lethal 5+",
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Agoniser
                "wname":"Agoniser",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":3,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5",
                            "Brutal"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Hekatarii Blade
                "wname":"Hekatarii Blade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Dodge",
        ],
        "uacts":[
        ],
        "fackey":"Commorrite",
        "faction":[
            "Aeldari",
            "Drukhari"
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Wych",
            "Hekatrix"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Wych Fighter
        "opname":"Wych Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Hydra Gauntlets
                "wname":"Hydra Gauntlets",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Razorflails
                "wname":"Razorflails",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless",
                            "Brutal"
                        ],
                        "crits":[
                            "Reap 1"
                        ],
                    },
                ]
            },
            {   # Shardnet and Impaler
                "wname":"Shardnet and Impaler",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Dodge",
            "Shardnet and Impaler"
        ],
        "uacts":[
        ],
        "fackey":"Commorrite",
        "faction":[
            "Aeldari",
            "Drukhari"
        ],
        "house":"",
        "keywords":[
            "Wych",
            "Fighter"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    # --- Craftworld ---
    {   # Guardian Defender Warrior
        "opname":"Guardian Defender Warrior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Shuriken Catapult
                "wname":"Shuriken Catapult",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Guardian Defender",
            "Warrior",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Guardian Defender Heavy Gunner
        "opname":"Guardian Defender Heavy Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Shuriken Catapult
                "wname":"Shuriken Catapult",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
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
            "Control Platform",
        ],
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Guardian Defender",
            "Heavy Gunner",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Guardian Defender Heavy Weapon Platform
        "opname":"Guardian Defender Heavy Weapon Platform",
        "stats":{
            "move":4,
            "apl":0,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Aeldari Missile Launcher
                "wname":"Aeldari Missile Launcher",
                "profiles":[
                    {
                        "pname":"Sunburst",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                            "Heavy",
                            "Blast 2\"",
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Starshot",
                        "atts":4,
                        "bskill":3,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Heavy",
                            "AP 1",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Bright Lance
                "wname":"Bright Lance",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":6,
                        "dmg2":7,
                        "srule":[
                            "Heavy",
                            "AP 2",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Scatter Laser
                "wname":"Scatter Laser",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Heavy",
                            "Ceaseless",
                            "Fusillade",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Shuriken Cannon
                "wname":"Shuriken Cannon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Heavy",
                            "Fusilade",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Starcannon
                "wname":"Starcannon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Heavy",
                            "AP 1",
                        ],
                        "crits":[
                            "P2",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
        ],
        "abs":[
            "Platform Controller",
        ],
        "uacts":[
            "Gun Platform",
        ],
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Guardian Defender",
            "Heavy Weapon Platform",
        ],
        "specials":[
        ]
    },
    {   # Guardian Defender Leader
        "opname":"Guardian Defender Leader",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":9,
        },
        "rweaps":[
            {   # Shuriken Catapult
                "wname":"Shuriken Catapult",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":2,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Guardian Defender",
            "Leader",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Storm Guardian Warrior
        "opname":"Storm Guardian Warrior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Shuriken Pistol
                "wname":"Shuriken Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Storm Guardian Blades
                "wname":"Storm Guardian Blades",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Storm Guardian",
            "Warrior",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Storm Guardian Gunner
        "opname":"Storm Guardian Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Flamer
                "wname":"Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\"",
                            "Torrent 2\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fusion Gun
                "wname":"Fusion Gun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":6,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                            "AP 2",
                        ],
                        "crits":[
                            "MW 4",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Storm Guardian",
            "Gunner",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Storm Guardian Leader
        "opname":"Storm Guardian Leader",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":9,
        },
        "rweaps":[
            {   # Shuriken Pistol
                "wname":"Shuriken Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Storm Guardian Blades
                "wname":"Storm Guardian Blades",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Storm Guardian",
            "Leader",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Ranger Warrior
        "opname":"Ranger Warrior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Ranger Long Rifle
                "wname":"Ranger Long Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":3,
                        "srule":[
                            "Heavy",
                            "Silent",
                        ],
                        "crits":[
                            "MW 1",
                        ],
                    },
                ]
            },
            {   # Shuriken Pistol
                "wname":"Shuriken Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Camo Cloak",
        ],
        "uacts":[
        ],
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Ranger",
            "Warrior",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Ranger Leader
        "opname":"Ranger Leader",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":9,
        },
        "rweaps":[
            {   # Ranger Long Rifle
                "wname":"Ranger Long Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":3,
                        "srule":[
                            "Heavy",
                            "Silent",
                            "Balanced",
                        ],
                        "crits":[
                            "MW 1",
                        ],
                    },
                ]
            },
            {   # Shuriken Pistol
                "wname":"Shuriken Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Camo Cloak",
        ],
        "uacts":[
        ],
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Ranger",
            "Leader",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Dire Avenger Warrior
        "opname":"Dire Avenger Warrior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Avenger Shuriken Catapult
                "wname":"Avenger Shuriken Catapult",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Balanced",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Defence Tactics",
        ],
        "uacts":[
        ],
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Dire Avenger",
            "Warrior",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Dire Avenger Exarch
        "opname":"Dire Avenger Exarch",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":9,
        },
        "rweaps":[
            {   # Avenger Shuriken Catapult
                "wname":"Avenger Shuriken Catapult",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Balanced",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Shuriken Pistol
                "wname":"Shuriken Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Twin Avenger Shuriken Catapult
                "wname":"Avenger Shuriken Catapult",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Relentless",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Diresword
                "wname":"Diresword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Lethal 5+",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Defence Tactics",
            "Shimmershield",
        ],
        "uacts":[
            "Shuriken Storm",
        ],
        "fackey":"Craftworld",
        "faction":[
            "Aeldari",
            "Asuryani",
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Dire Avenger",
            "Exarch",
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ]
    },
    # --- Death Guard ---
    {   # Plague Marine [Warrior]
        "opname":"Plague Marine [Warrior]",
        "stats":{
            "move":4,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Plague Knife
                "wname":"Plague Knife",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Disgustingly Resilient"
        ],
        "uacts":[
        ],
        "fackey":"Death Guard",
        "faction":[
            "Chaos",
            "Bubonic Astartes"
        ],
        "house":"",
        "keywords":[
            "Plague Marine",
            "Warrior"
        ],
        "specials":[
        ],
    },
    {   # Plague Marine [Gunner]
        "opname":"Plague Marine [Gunner]",
        "stats":{
            "move":4,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Meltagun
                "wname":"Meltagun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":6,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                            "AP 2"
                        ],
                        "crits":[
                            "MW 4"
                        ],
                    },
                ]
            },
            {   # Plague Belcher
                "wname":"Plague Belcher",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Plasma Gun
                "wname":"Plasma Gun",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP 2",
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Plague Knife
                "wname":"Plague Knife",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Disgustingly Resilient"
        ],
        "uacts":[
        ],
        "fackey":"Death Guard",
        "faction":[
            "Chaos",
            "Bubonic Astartes"
        ],
        "house":"",
        "keywords":[
            "Plague Marine",
            "Gunner"
        ],
        "specials":[
        ],
    },
    {   # Plague Marine [Heavy Gunner]
        "opname":"Plague Marine [Heavy Gunner]",
        "stats":{
            "move":4,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Blight Launcher
                "wname":"Blight Launcher",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Plague Spewer
                "wname":"Plague Spewer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Plague Knife
                "wname":"Plague Knife",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Disgustingly Resilient"
        ],
        "uacts":[
        ],
        "fackey":"Death Guard",
        "faction":[
            "Chaos",
            "Bubonic Astartes"
        ],
        "house":"",
        "keywords":[
            "Plague Marine",
            "Heavy Gunner"
        ],
        "specials":[
        ],
    },
    {   # Plague Marine [Fighter]
        "opname":"Plague Marine [Fighter]",
        "stats":{
            "move":4,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Bolt Pistol
                "wname":"Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Bubotic Axe
                "wname":"Bubotic Axe",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
            {   # Flail of Corruption
                "wname":"Flail of Corruption",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Reap 2"
                        ],
                    },
                ]
            },
            {   # Great Plague Cleaver
                "wname":"Great Plague Cleaver",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":4,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
            {   # Mace of Contagion
                "wname":"Mace of Contagion",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Plague Knives
                "wname":"Plague Knives",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Disgustingly Resilient"
        ],
        "uacts":[
        ],
        "fackey":"Death Guard",
        "faction":[
            "Chaos",
            "Bubonic Astartes"
        ],
        "house":"",
        "keywords":[
            "Plague Marine",
            "Fighter"
        ],
        "specials":[
        ],
    },
    {   # Plague Marine [Icon Bearer]
        "opname":"Plague Marine [Icon Bearer]",
        "stats":{
            "move":4,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Plague Knife
                "wname":"Plague Knife",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Disgustingly Resilient",
            "Icon Bearer"
        ],
        "uacts":[
            "Icon of Decay"
        ],
        "fackey":"Death Guard",
        "faction":[
            "Chaos",
            "Bubonic Astartes"
        ],
        "house":"",
        "keywords":[
            "Plague Marine",
            "Icon Bearer"
        ],
        "specials":[
        ],
    },
    {   # Plague Marine Champion
        "opname":"Plague Marine Champion",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":13,
        },
        "rweaps":[
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Bolt Pistol
                "wname":"Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Plasma Pistol
                "wname":"Plasma Pistol",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 2",
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Plague Knife
                "wname":"Plague Knife",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Plague Sword
                "wname":"Plague Sword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Fist
                "wname":"Power Fist",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Brutal"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Disgustingly Resilient"
        ],
        "uacts":[
        ],
        "fackey":"Death Guard",
        "faction":[
            "Chaos",
            "Bubonic Astartes"
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Plague Marine",
            "Champion"
        ],
        "specials":[
        ],
    },
    {   # Poxwalker
        "opname":"Poxwalker",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":2,
            "def":3,
            "save":6,
            "wounds":7,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Improvised Weapon
                "wname":"Improvised Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Mindless",
            "Disgustingly Resilient"
        ],
        "uacts":[
        ],
        "fackey":"Death Guard",
        "faction":[
            "Chaos"
        ],
        "house":"",
        "keywords":[
            "Poxwalker"
        ],
        "specials":[
        ],
    },
    # --- Ecclesiarchy ---
    {   # Battle Sister Warrior
        "opname":"Battle Sister Warrior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":8,
        },
        "rweaps":[
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Icon Bearer"
        ],
        "uacts":[
            "Icon of Purity"
        ],
        "fackey":"Ecclesiarchy",
        "faction":[
            "Imperium",
            "Adeptus Ministorum",
            "Adepta Sororitas"
        ],
        "house":"",
        "keywords":[
            "Battle Sister",
            "Warrior"
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ],
    },
    {   # Battle Sister Icon Bearer
        "opname":"Battle Sister Icon Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":8,
        },
        "rweaps":[
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Icon Bearer"
        ],
        "uacts":[
            "Icon of Purity"
        ],
        "fackey":"Ecclesiarchy",
        "faction":[
            "Imperium",
            "Adeptus Ministorum",
            "Adepta Sororitas"
        ],
        "house":"",
        "keywords":[
            "Battle Sister",
            "Icon Bearer"
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ],
    },
    {   # Battle Sister Gunner
        "opname":"Battle Sister Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":8,
        },
        "rweaps":[
            {   # Meltagun
                "wname":"Meltagun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":6,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                            "AP 2"
                        ],
                        "crits":[
                            "MW 4"
                        ],
                    },
                ]
            },
            {   # Ministorum Flamer
                "wname":"Ministorum Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Storm Bolter
                "wname":"Storm Bolter",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Ecclesiarchy",
        "faction":[
            "Imperium",
            "Adeptus Ministorum",
            "Adepta Sororitas"
        ],
        "house":"",
        "keywords":[
            "Battle Sister",
            "Gunner"
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ],
    },
    {   # Battle Sister Heavy Gunner
        "opname":"Battle Sister Heavy Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":8,
        },
        "rweaps":[
            {   # Heavy Bolter
                "wname":"Heavy Bolter",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Heavy",
                            "Fusillade"
                        ],
                        "crits":[
                            "P1"
                        ],
                    },
                ]
            },
            {   # Ministorum Heavy Flamer
                "wname":"Ministorum Heavy Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Heavy",
                            "Range 6\"",
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Ecclesiarchy",
        "faction":[
            "Imperium",
            "Adeptus Ministorum",
            "Adepta Sororitas"
        ],
        "house":"",
        "keywords":[
            "Battle Sister",
            "Heavy Gunner"
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ],
    },
    {   # Battle Sister Superior
        "opname":"Battle Sister Superior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":9,
        },
        "rweaps":[
            {   # Bolt Pistol
                "wname":"Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Combi-melta
                "wname":"Combi-melta",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":6,
                        "dmg2":3,
                        "srule":[
                            "Combi",
                            "Range 6\"",
                            "AP 2",
                            "Limited"
                        ],
                        "crits":[
                            "MW 4"
                        ],
                    },
                ]
            },
            {   # Combi-plasma
                "wname":"Combi-plasma",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Combi",
                            "AP 1",
                            "Limited"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Overcharge",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Combi",
                            "AP 2",
                            "Hot",
                            "Limited"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Condemnor Boltgun
                "wname":"Condemnor Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":3,
                        "srule":[
                            "Combi",
                            "Silent",
                            "Limited"
                        ],
                        "crits":[
                            "MW 1",
                            "P 1"
                        ],
                    },
                ]
            },
            {   # Inferno Pistol
                "wname":"Inferno Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":3,
                        "srule":[
                            "Range 3\"",
                            "AP 2"
                        ],
                        "crits":[
                            "MW 3"
                        ],
                    },
                ]
            },
            {   # Ministorum Combi-flamer
                "wname":"Ministorum Combi-flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Combi",
                            "Range 6\"",
                            "Torrent 2\"",
                            "Limited"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Ministorum Hand Flamer
                "wname":"Ministorum Hand Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                            "Torrent 1\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Plasma Pistol
                "wname":"Plasma Pistol",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 2",
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Maul
                "wname":"Power Maul",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Combi"
        ],
        "uacts":[
        ],
        "fackey":"Ecclesiarchy",
        "faction":[
            "Imperium",
            "Adeptus Ministorum",
            "Adepta Sororitas"
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Battle Sister",
            "Superior"
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman"
        ],
    },
    {   # Sister Repentia
        "opname":"Sister Repentia",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":7,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Penitent Eviscerator
                "wname":"Penitent Eviscerator",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Brutal"
                        ],
                        "crits":[
                            "Reap 2"
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Solace in Anguish"
        ],
        "uacts":[
        ],
        "fackey":"Ecclesiarchy",
        "faction":[
            "Imperium",
            "Adeptus Ministorum",
            "Adepta Sororitas"
        ],
        "house":"",
        "keywords":[
            "Sister",
            "Repentia"
        ],
        "specials":[
            "Combat",
            "Scout"
        ],
    },
    {   # Repentia Superior
        "opname":"Repentia Superior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":9,
        },
        "rweaps":[
            {   # Neural Whips
                "wname":"Neural Whips",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Letahl 5+"
                            "Range 3\""
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Neural Whips
                "wname":"Neural Whips",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Letahl 5+"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
            "Whip Into Fury"
        ],
        "fackey":"Ecclesiarchy",
        "faction":[
            "Imperium",
            "Adeptus Ministorum",
            "Adepta Sororitas"
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Repentia",
            "Superior"
        ],
        "specials":[
            "Combat",
            "Staunch"
        ],
    },
    {   # Arco-Flagellant
        "opname":"Arco-Flagellant",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":10,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Arco-flails
                "wname":"Arco-flails",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless"
                        ],
                        "crits":[
                            "Reap 1"
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Berserk Killing Machine"
        ],
        "uacts":[
        ],
        "fackey":"Ecclesiarchy",
        "faction":[
            "Imperium",
            "Adeptus Ministorum"
        ],
        "house":"",
        "keywords":[
            "Arco-flagellant"
        ],
        "specials":[
            "Combat",
            "Scout"
        ],
    },
    # --- Forge World ---
    {   # Skitarii Ranger Trooper
        "opname":"Skitarii Ranger Trooper",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
            {   # Galvanic Rifle
                "wname":"Galvanic Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Heavy"
                        ],
                        "crits":[
                            "P1"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Forge World",
        "faction":[
            "Imperium",
            "Adeptus Mechanicus"
        ],
        "house":"",
        "keywords":[
            "Skitarii",
            "Ranger",
            "Trooper"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ],
    },
    {   # Skitarii Ranger Gunner
        "opname":"Skitarii Ranger Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
            {   # Arc Rifle
                "wname":"Arc Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "AP1"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Plasma Caliver
                "wname":"Plasma Caliver",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP2",
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Transuranic Arquebus
                "wname":"Transuranic Arquebus",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":4,
                        "srule":[
                            "AP1",
                            "Heavy",
                            "Unwieldly"
                        ],
                        "crits":[
                            "MW2"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Forge World",
        "faction":[
            "Imperium",
            "Adeptus Mechanicus"
        ],
        "house":"",
        "keywords":[
            "Skitarii",
            "Ranger",
            "Gunner"
        ],
        "specials":[
            "Marksman"
        ],
    },
    {   # Skitarii Ranger Alpha
        "opname":"Skitarii Ranger Alpha",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Arc Pistol
                "wname":"Arc Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\"",
                            "AP1"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Galvanic Rifle
                "wname":"Galvanic Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Heavy"
                        ],
                        "crits":[
                            "P1"
                        ],
                    },
                ]
            },
            {   # Phosphor Blast Pistol
                "wname":"Phosphor Blast Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\"",
                            "Blast 1\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Radium Pistol
                "wname":"Radium Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Arc Maul
                "wname":"Arc Maul",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Taser Goad
                "wname":"Taser Goad",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Letahl 5+"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Forge World",
        "faction":[
            "Imperium",
            "Adeptus Mechanicus"
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Skitarii",
            "Ranger",
            "Alpha"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ],
    },
    {   # Skitarii Vanguard Trooper
        "opname":"Skitarii Vanguard Trooper",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
            {   # Radium Carbine
                "wname":"Radium Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Forge World",
        "faction":[
            "Imperium",
            "Adeptus Mechanicus"
        ],
        "house":"",
        "keywords":[
            "Skitarii",
            "Vanguard",
            "Trooper"
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ],
    },
    {   # Skitarii Vanguard Gunner
        "opname":"Skitarii Vanguard Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
            {   # Arc Rifle
                "wname":"Arc Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "AP1"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Plasma Caliver
                "wname":"Plasma Caliver",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP2",
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Transuranic Arquebus
                "wname":"Transuranic Arquebus",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":4,
                        "srule":[
                            "AP1",
                            "Heavy",
                            "Unwieldly"
                        ],
                        "crits":[
                            "MW2"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Forge World",
        "faction":[
            "Imperium",
            "Adeptus Mechanicus"
        ],
        "house":"",
        "keywords":[
            "Skitarii",
            "Vanguard",
            "Gunner"
        ],
        "specials":[
            "Marksman"
        ],
    },
    {   # Skitarii Vanguard Alpha
        "opname":"Skitarii Vanguard Alpha",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Arc Pistol
                "wname":"Arc Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\"",
                            "AP1"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Phosphor Blast Rifle
                "wname":"Phosphor Blast Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\"",
                            "Blast 1\""
                        ],
                        "crits":[
                            "P1"
                        ],
                    },
                ]
            },
            {   # Radium Carbine
                "wname":"Radium Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
            {   # Radium Pistol
                "wname":"Radium Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Arc Maul
                "wname":"Arc Maul",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Taser Goad
                "wname":"Taser Goad",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Letahl 5+"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Forge World",
        "faction":[
            "Imperium",
            "Adeptus Mechanicus"
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Skitarii",
            "Ranger",
            "Alpha"
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman"
        ],
    },
    {   # Sicarian Ruststalker Trooper
        "opname":"Sicarian Ruststalker Trooper",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":10,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Chordclaw and Transonic Razor
                "wname":"Chordclaw and Transonic Razor",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Balanced"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Transonic Blades
                "wname":"Transonic Blades",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Forge World",
        "faction":[
            "Imperium",
            "Adeptus Mechanicus"
        ],
        "house":"",
        "keywords":[
            "Skitarii",
            "Sicarian",
            "Ruststalker",
            "Trooper"
        ],
        "specials":[
            "Combat",
            "Scout"
        ],
    },
    {   # Sicarian Ruststalker Princeps
        "opname":"Sicarian Ruststalker Princeps",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":11,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Chordclaw and Transonic Razor
                "wname":"Chordclaw and Transonic Razor",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Balanced"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Transonic Blades
                "wname":"Transonic Blades",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Forge World",
        "faction":[
            "Imperium",
            "Adeptus Mechanicus"
        ],
        "house":"",
        "keywords":[
            "Skitarii",
            "Leader",
            "Sicarian",
            "Ruststalker",
            "Princeps"
        ],
        "specials":[
            "Combat",
            "Scout"
        ],
    },
    {   # Sicarian Infiltrator Trooper
        "opname":"Sicarian Infiltrator Trooper",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":10,
        },
        "rweaps":[
            {   # Flechette Blaster
                "wname":"Flechette Blaster",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Relentless",
                            "Fusilade",
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Stubcarbine
                "wname":"Stubcarbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Taser Goad
                "wname":"Taser Goad",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Forge World",
        "faction":[
            "Imperium",
            "Adeptus Mechanicus"
        ],
        "house":"",
        "keywords":[
            "Skitarii",
            "Sicarian",
            "Infiltrator",
            "Trooper"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ],
    },
    {   # Sicarian Infiltrator Princeps
        "opname":"Sicarian Infiltrator Princeps",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":11,
        },
        "rweaps":[
            {   # Flechette Blaster
                "wname":"Flechette Blaster",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Relentless",
                            "Fusilade",
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Stubcarbine
                "wname":"Stubcarbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Taser Goad
                "wname":"Taser Goad",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Forge World",
        "faction":[
            "Imperium",
            "Adeptus Mechanicus"
        ],
        "house":"",
        "keywords":[
            "Skitarii",
            "Leader",
            "Sicarian",
            "Infiltrator",
            "Princeps"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ],
    },
    # --- Greenskin ---
    {   # Boy Fighter
        "opname":"Boy Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":10,
        },
        "rweaps":[
            {   # Shoota
                "wname":"Shoota",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":5,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Slugga
                "wname":"Slugga",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":5,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Choppa
                "wname":"Choppa",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Greenskin",
        "faction":[
            "Ork",
        ],
        "house":"",
        "keywords":[
            "Boy",
            "Fighter",
        ],
        "specials":[
            "Combat",
            "Marksman"
        ]
    },
    {   # Boss Nob
        "opname":"Boss Nob",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":13,
        },
        "rweaps":[
            {   # Kombi-rokkit
                "wname":"Kombi-rokkit",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":5,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Kombi",
                            "Limited",
                            "AP1",
                        ],
                        "crits":[
                            "Splash 1",
                        ],
                    },
                ]
            },
            {   # Kombi-skorcha
                "wname":"Kombi-skorcha",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Kombi",
                            "Limited",
                            "Range 6\"",
                            "Torrent 2\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Shoota
                "wname":"Shoota",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":5,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Slugga
                "wname":"Slugga",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":5,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Big Choppa
                "wname":"Big Choppa",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Choppa
                "wname":"Choppa",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Killsaw
                "wname":"Killsaw",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Power Klaw
                "wname":"Power Klaw",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Brutal",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Kombi",
        ],
        "uacts":[
        ],
        "fackey":"Greenskin",
        "faction":[
            "Ork",
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Boy",
            "Boss Nob",
        ],
        "specials":[
            "Comabt",
            "Staunch"
        ]
    },
    {   # Boy Gunner
        "opname":"Boy Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":10,
        },
        "rweaps":[
            {   # Big Shoota
                "wname":"Big Shoota",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "bskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Fusillade",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Rokkit Launcha
                "wname":"Rokkit Launcha",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":5,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "AP 1",
                        ],
                        "crits":[
                            "Splash 1",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Greenskin",
        "faction":[
            "Ork",
        ],
        "house":"",
        "keywords":[
            "Boy",
            "Gunner",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Gretchin
        "opname":"Gretchin",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":2,
            "def":3,
            "save":6,
            "wounds":5,
        },
        "rweaps":[
            {   # Gretchin Blasta
                "wname":"Gretchin Blasta",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gretchin Knife
                "wname":"Gretchin Knife",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":1,
                        "dmg2":2,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Runt",
        ],
        "uacts":[
        ],
        "fackey":"Greenskin",
        "faction":[
            "Ork",
        ],
        "house":"",
        "keywords":[
            "Boy",
            "Gretchin",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Clan Kommando Fighter
        "opname":"Clan Kommando Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":10,
        },
        "rweaps":[
            {   # Slugga
                "wname":"Slugga",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":5,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Choppa
                "wname":"Choppa",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
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
        "fackey":"Greenskin",
        "faction":[
            "Ork",
        ],
        "house":"",
        "keywords":[
            "Clan Kommando",
            "Fighter",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Clan Kommando Nob
        "opname":"Clan Kommando Nob",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":13,
        },
        "rweaps":[
            {   # Slugga
                "wname":"Slugga",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Choppa
                "wname":"Choppa",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Klaw
                "wname":"Power Klaw",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Brutal",
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
        "fackey":"Greenskin",
        "faction":[
            "Ork",
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Clan Kommando",
            "Kommando Nob",
        ],
        "specials":[
            "Combat",
            "Staunch"
        ]
    },
    {   # Burna Boy
        "opname":"Burna Boy",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":10,
        },
        "rweaps":[
            {   # Burna
                "wname":"Burna",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\"",
                            "Torrent 2\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Greenskin",
        "faction":[
            "Ork",
        ],
        "house":"",
        "keywords":[
            "Speshulist",
            "Burna Boy",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Loota
        "opname":"Loota",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":10,
        },
        "rweaps":[
            {   # Deffgun
                "wname":"Deffgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":5,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Greenskin",
        "faction":[
            "Ork",
        ],
        "house":"",
        "keywords":[
            "Speshulist",
            "Loota",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Spanner
        "opname":"Spanner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":11,
        },
        "rweaps":[
            {   # Big Shoota
                "wname":"Big Shoota",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Fusillade",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Kustom Mega-blasta
                "wname":"Kustom Mega-blasta",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP 2",
                            "Hot",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Rokkit Launcha
                "wname":"Rokkit Launcha",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "AP 1",
                        ],
                        "crits":[
                            "Splash 1",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Greenskin",
        "faction":[
            "Ork",
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Speshulist",
            "Spanner",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    # --- Grey Knights ---
    {   # Grey Knight Warrior
        "opname":"Grey Knight Warrior",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":11,
        },
        "rweaps":[
            {   # Storm Bolter
                "wname":"Storm Bolter",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Nemesis Daemon Hammer
                "wname":"Nemesis Daemon Hammer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Nemesis Falchions
                "wname":"Nemesis Falchions",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Nemesis Force Weapon
                "wname":"Nemesis Force Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Nemesis Warding Stave
                "wname":"Nemesis Warding Stave",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
            "Manifest Psychic Power [Grey Knight]"
        ],
        "fackey":"Grey Knight",
        "faction":[
            "Imperium"
            "Sanctic Astartes"
        ],
        "house":"",
        "keywords":[
            "Psyker"
            "Warrior"
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman"
        ]
    },
    {   # Grey Knight Gunner
        "opname":"Grey Knight Gunner",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":11,
        },
        "rweaps":[
            {   # Incinerator
                "wname":"Incinerator",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Heavy"
                            "Range 6\""
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Psilencer
                "wname":"Psilencer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Heavy"
                            "Fusillade"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Psycannon
                "wname":"Psycannon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Heavy"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
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
            "Manifest Psychic Power [Grey Knight]"
        ],
        "fackey":"Grey Knight",
        "faction":[
            "Imperium"
            "Sanctic Astartes"
        ],
        "house":"",
        "keywords":[
            "Psyker"
            "Gunner"
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Grey Knight Justicar
        "opname":"Grey Knight Justicar",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Storm Bolter
                "wname":"Storm Bolter",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Nemesis Daemon Hammer
                "wname":"Nemesis Daemon Hammer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Nemesis Falchions
                "wname":"Nemesis Falchions",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Nemesis Force Weapon
                "wname":"Nemesis Force Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Nemesis Warding Stave
                "wname":"Nemesis Warding Stave",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
            "Manifest Psychic Power [Grey Knight]"
        ],
        "fackey":"Grey Knight",
        "faction":[
            "Imperium"
            "Sanctic Astartes"
        ],
        "house":"",
        "keywords":[
            "Psyker"
            "Leader"
            "Justicar"
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman"
        ]
    },
    # --- Hive Fleet ---
    {   # Genestealer Fighter
        "opname":"Genestealer Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":9,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Double Rending Claws
                "wname":"Double Rending Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Rending Claws
                "wname":"Rending Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Scything Talons
                "wname":"Scything Talons",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Synapse",
            "Lightning Reflexes",
            "Hidden Horror",
        ],
        "uacts":[
        ],
        "fackey":"Hive Fleet",
        "faction":[
            "Tyranid",
        ],
        "house":"",
        "keywords":[
            "Genestealer",
            "Fighter",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Genestealer Leader
        "opname":"Genestealer Leader",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":10,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Double Rending Claws
                "wname":"Double Rending Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless",
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Rending Claws
                "wname":"Rending Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Scything Talons
                "wname":"Scything Talons",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Synapse",
            "Lightning Reflexes",
            "Hidden Horror",
        ],
        "uacts":[
        ],
        "fackey":"Hive Fleet",
        "faction":[
            "Tyranid",
        ],
        "house":"",
        "keywords":[
            "Genestealer",
            "Fighter",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Tyranid Warrior Fighter
        "opname":"Tyranid Warrior Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":18,
        },
        "rweaps":[
            {   # Deathspitter
                "wname":"Deathspitter",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Devourer
                "wname":"Devourer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Lash Whip
                "wname":"Lash Whip",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 3\"",
                        ],
                        "crits":[
                            "Stun",
                        ],
                    },
                ]
            },
            {   # Spinefists
                "wname":"Spinefists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Bonesword
                "wname":"Bonesword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Boneswords
                "wname":"Boneswords",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Rending Claws
                "wname":"Rending Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Scything Talons
                "wname":"Scything Talons",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Synapse",
            "Weaponbeast",
            "Lash Whip",
        ],
        "uacts":[
        ],
        "fackey":"Hive Fleet",
        "faction":[
            "Tyranid",
        ],
        "house":"",
        "keywords":[
            "Synapse",
            "Tyranid Warrior",
            "Warrior",
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman"
        ]
    },
    {   # Tyranid Warrior Heavy Gunner
        "opname":"Tyranid Warrior Heavy Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":18,
        },
        "rweaps":[
            {   # Barbed Strangler
                "wname":"Barbed Strangler",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Heavy",
                            "Blast 2\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Lash Whip
                "wname":"Lash Whip",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 3\"",
                        ],
                        "crits":[
                            "Stun",
                        ],
                    },
                ]
            },
            {   # Venom Cannon
                "wname":"Venom Cannon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Heavy",
                            "AP 1",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Bonesword
                "wname":"Bonesword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Boneswords
                "wname":"Boneswords",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Rending Claws
                "wname":"Rending Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Scything Talons
                "wname":"Scything Talons",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Synapse",
            "Lash Whip",
        ],
        "uacts":[
        ],
        "fackey":"Hive Fleet",
        "faction":[
            "Tyranid",
        ],
        "house":"",
        "keywords":[
            "Synapse",
            "Tyranid Warrior",
            "Heavy Gunner",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Tyranid Warrior Leader
        "opname":"Tyranid Warrior Leader",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":19,
        },
        "rweaps":[
            {   # Deathspitter
                "wname":"Deathspitter",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Devourer
                "wname":"Devourer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Lash Whip
                "wname":"Lash Whip",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 3\"",
                        ],
                        "crits":[
                            "Stun",
                        ],
                    },
                ]
            },
            {   # Spinefists
                "wname":"Spinefists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Bonesword
                "wname":"Bonesword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Boneswords
                "wname":"Boneswords",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Rending Claws
                "wname":"Rending Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
            {   # Scything Talons
                "wname":"Scything Talons",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Balanced",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Synapse",
            "Weaponbeast",
            "Lash Whip",
        ],
        "uacts":[
        ],
        "fackey":"Hive Fleet",
        "faction":[
            "Tyranid",
        ],
        "house":"",
        "keywords":[
            "Synapse",
            "Tyranid Warrior",
            "Leader",
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman"
        ]
    },
    {   # Termagant
        "opname":"Termagant",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":2,
            "def":3,
            "save":6,
            "wounds":7,
        },
        "rweaps":[
            {   # Devourer
                "wname":"Devourer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fleshborer
                "wname":"Fleshborer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Spinefists
                "wname":"Spinefists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Claws
                "wname":"Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Synapse",
        ],
        "uacts":[
        ],
        "fackey":"Hive Fleet",
        "faction":[
            "Tyranid",
        ],
        "house":"",
        "keywords":[
            "Tyranid Swarm",
            "Termagant",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Hormagaunt
        "opname":"Hormagaunt",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":2,
            "def":3,
            "save":6,
            "wounds":7,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Scything Talons
                "wname":"Scything Talons",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":4,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                            "Relentless",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Synapse",
        ],
        "uacts":[
        ],
        "fackey":"Hive Fleet",
        "faction":[
            "Tyranid",
        ],
        "house":"",
        "keywords":[
            "Tyranid Swarm",
            "Hormagaunt",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    # --- Hunter Cadre ---
    {   # Fire Warrior Shas'la
        "opname":"Fire Warrior Shas'la",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
            {   # Pulse Blaster
                "wname":"Pulse Blaster",
                "profiles":[
                    {
                        "pname":"Close Range",
                        "atts":4,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\""
                            "Armour Penetration 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Long Range",
                        "atts":4,
                        "bskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Pulse Carbine
                "wname":"Pulse Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Pulse Rifle
                "wname":"Pulse Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Fire Warrior"
            "Shas'la"
        ],
        "specials":[
            "Marksman"
        ]
    },
    {   # Fire Warrior Shas'ui
        "opname":"Fire Warrior Shas'ui",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Pulse Blaster
                "wname":"Pulse Blaster",
                "profiles":[
                    {
                        "pname":"Close Range",
                        "atts":4,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\""
                            "Armour Penetration 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Long Range",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Pulse Carbine
                "wname":"Pulse Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Pulse Rifle
                "wname":"Pulse Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Leader"
            "Fire Warrior"
            "Shas'ui"
        ],
        "specials":[
            "Marksman"
        ]
    },
    {   # Pathfinder Shas'la
        "opname":"Pathfinder Shas'la",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":7,
        },
        "rweaps":[
            {   # Pulse Carbine
                "wname":"Pulse Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
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
            "Markerlight"
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Pathfinder"
            "Shas'la"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Pathfinder Heavy Gunner
        "opname":"Pathfinder Heavy Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":7,
        },
        "rweaps":[
            {   # Ion Rifle
                "wname":"Ion Rifle",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":5,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Piercing 1"
                        ],
                    },
                    {
                        "pname":"Overcharge",
                        "atts":5,
                        "wskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Armour Penetration 1"
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Rail Rifle
                "wname":"Rail Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":4,
                        "srule":[
                            "Armour Penetration 1"
                            "Lethal 5+"
                        ],
                        "crits":[
                            "Mortal Wounds 2"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Pathfinder"
            "Heavy Gunner"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Pathfinder Shas'ui
        "opname":"Pathfinder Shas'ui",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Pulse Carbine
                "wname":"Pulse Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
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
            "Markerlight"
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Leader"
            "Pathfinder"
            "Shas'la"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Stealth Battlesuit Shas'ui
        "opname":"Stealth Battlesuit Shas'ui",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":10,
        },
        "rweaps":[
            {   # Burst Cannon
                "wname":"Burst Cannon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "bskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless"
                            "Fusillade"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fusion Blaster
                "wname":"Fusion Blaster",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":5,
                        "dmg1":6,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                            "Armour Penetration 2"
                        ],
                        "crits":[
                            "Mortal Wounds 4"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Camouflage Field"
        ],
        "uacts":[
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Fly"
            "Stealth Battlesuit"
            "Shas'ui"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Stealth Battlesuit Shas'vre
        "opname":"Stealth Battlesuit Shas'vre",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":11,
        },
        "rweaps":[
            {   # Burst Cannon
                "wname":"Burst Cannon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless"
                            "Fusillade"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fusion Blaster
                "wname":"Fusion Blaster",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":6,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                            "Armour Penetration 2"
                        ],
                        "crits":[
                            "Mortal Wounds 4"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Camouflage Field"
        ],
        "uacts":[
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Leader"
            "Fly"
            "Stealth Battlesuit"
            "Shas'vre"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # MV1 Gun Drone
        "opname":"MV1 Gun Drone",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
            {   # Twin Pulse Carbine
                "wname":"Twin Pulse Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Ram
                "wname":"Ram",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Artificial Intelligence"
            "Saviour Protocols"
        ],
        "uacts":[
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Drone"
            "Fly"
            "MV1 Gun Drone"
        ],
        "specials":[
            "Marksman"
        ]
    },
    {   # MV4 Shield Drone
        "opname":"MV4 Shield Drone",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Ram
                "wname":"Ram",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Artificial Intelligence"
            "Saviour Protocols"
            "Shield Generator"
        ],
        "uacts":[
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Drone"
            "Fly"
            "MV4 Shield Drone"
        ],
        "specials":[
            "Staunch"
        ]
    },
    {   # MV36 Guardian Drone
        "opname":"MV36 Guardian Drone",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Ram
                "wname":"Ram",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Artificial Intelligence"
            "Saviour Protocols"
            "Guardian Shield Generator"
        ],
        "uacts":[
            "Guardian Field"
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Drone"
            "Fly"
            "MV36 Guardian Drone"
        ],
        "specials":[
            "Staunch"
        ]
    },
    {   # MV31 Pulse Accelerator Drone
        "opname":"MV31 Pulse Accelerator Drone",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Ram
                "wname":"Ram",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Artificial Intelligence"
            "Saviour Protocols"
            "Pulse Accelerator"
        ],
        "uacts":[
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Drone"
            "Fly"
            "MV31 Pulse Accelerator Drone"
        ],
        "specials":[
            "Staunch",
            "Scout"
        ]
    },
    {   # MV33 Grav-Inhibitor Drone
        "opname":"MV33 Grav-Inhibitor Drone",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Ram
                "wname":"Ram",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Artificial Intelligence"
            "Saviour Protocols"
            "Grav-inhibitor"
        ],
        "uacts":[
            "Grav-wave"
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Drone"
            "Fly"
            "MV33 Grav-Inhibitor Drone"
        ],
        "specials":[
            "Staunch",
            "Scout"
        ]
    },
    {   # MV7 Marker Drone
        "opname":"MV7 Marker Drone",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":7,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Ram
                "wname":"Ram",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Artificial Intelligence"
            "Saviour Protocols"
        ],
        "uacts":[
            "Markerlight"
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Drone"
            "Fly"
            "MV7 Marker Drone"
        ],
        "specials":[
            "Staunch",
            "Scout"
        ]
    },
    {   # MB3 Recon Drone
        "opname":"MB3 Recon Drone",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":4,
            "save":4,
            "wounds":12,
        },
        "rweaps":[
            {   # Burst Cannon
                "wname":"Burst Cannon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "bskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Heavy"
                            "Ceaseless"
                            "Fusillade"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Ram
                "wname":"Ram",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":5,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Artificial Intelligence"
            "Saviour Protocols"
        ],
        "uacts":[
            "Analyse"
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Drone"
            "Fly"
            "MB3 Recon Drone"
        ],
        "specials":[
            "Staunch",
            "Marksman",
            "Scout"
        ]
    },
    {   # DS8 Tactical Support Turret
        "opname":"DS8 Tactical Support Turret",
        "stats":{
            "move":"",
            "apl":1,
            "gpact":1,
            "def":4,
            "save":4,
            "wounds":9,
        },
        "rweaps":[
            {   # Missile Pod
                "wname":"Missile Pod",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Heavy"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Smart Missile System
                "wname":"Smart Missile System",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "bskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Heavy"
                            "Smart Targeting"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
        ],
        "abs":[
            "Artificial Intelligence"
            "Saviour Protocols"
            "Smart Targeting"
            "Support Turret"
        ],
        "uacts":[
        ],
        "fackey":"Hunter Cadre",
        "faction":[
            "T'au Empire"
        ],
        "house":"",
        "keywords":[
            "Drone"
            "DS8 Tactical Support Turret"
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    # --- Imperial Guard ---
    {   # Guardsman Trooper
        "opname":"Guardsman Trooper",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":2,
            "def":3,
            "save":5,
            "wounds":7,
        },
        "rweaps":[
            {   # Lasgun
                "wname":"Lasgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Bayonet
                "wname":"Bayonet",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Imperial Guard",
        "faction":[
            "Imperium",
            "Astra Militarum"
        ],
        "house":"",
        "keywords":[
            "Guardsman",
            "Trooper"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Guardsman Comms
        "opname":"Guardsman Comms",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":7,
        },
        "rweaps":[
            {   # Lasgun
                "wname":"Lasgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Bayonet
                "wname":"Bayonet",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Relay Orders"
        ],
        "uacts":[
            "Signal"
        ],
        "fackey":"Imperial Guard",
        "faction":[
            "Imperium",
            "Astra Militarum"
        ],
        "house":"",
        "keywords":[
            "Guardsman",
            "Comms"
        ],
        "specials":[
            "Staunch",
            "Scout"
        ]
    },
    {   # Guardsman Gunner
        "opname":"Guardsman Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":7,
        },
        "rweaps":[
            {   # Flamer
                "wname":"Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Grenade Launcher
                "wname":"Grenade Launcher",
                "profiles":[
                    {
                        "pname":"Frag",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":4,
                        "srule":[
                            "Blast 2\""
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Krak",
                        "atts":4,
                        "bskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Meltagun
                "wname":"Meltagun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":6,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                            "AP 2"
                        ],
                        "crits":[
                            "MW 4"
                        ],
                    },
                ]
            },
            {   # Plasma Gun
                "wname":"Plasma Gun",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "bskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "bskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP 2"
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Sniper Rifle
                "wname":"Sniper Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":3,
                        "srule":[
                            "Heavy"
                            "Silent"
                        ],
                        "crits":[
                            "MW 1"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Bayonet
                "wname":"Bayonet",
                "profiles":[
                    {
                        "pname":"",
                        "atts":"3",
                        "wskill":"4+",
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Imperial Guard",
        "faction":[
            "Imperium",
            "Astra Militarum"
        ],
        "house":"",
        "keywords":[
            "Guardsman",
            "Gunner"
        ],
        "specials":[
            "Marksman"
        ]
    },
    {   # Guardsman Sergeant
        "opname":"Guardsman Sergeant",
        "stats":{
            "move":"6\"",
            "apl":"2",
            "gpact":"1",
            "def":"3",
            "save":"5+",
            "wounds":"8",
        },
        "rweaps":[
            {   # Bolt Pistol
                "wname":"Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Laspistol
                "wname":"Laspistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Plasma Pistol
                "wname":"Plasma Pistol",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "wskill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\""
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "wskill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\""
                            "AP 2"
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":4,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
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
        "fackey":"Imperial Guard",
        "faction":[
            "Imperium",
            "Astra Militarum"
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Guardsman",
            "Sergeant"
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman"
        ]
    },
    {   # Tempestus Scion Trooper
        "opname":"Tempestus Scion Trooper",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Hot-shot Lasgun
                "wname":"Hot-shot Lasgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
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
            "Signal"
        ],
        "fackey":"Imperial Guard",
        "faction":[
            "Imperium",
            "Astra Militarum"
        ],
        "house":"",
        "keywords":[
            "Tempsestus Scion",
            "Trooper"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Tempestus Scion Comms
        "opname":"Tempestus Scion Comms",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Hot-shot Lasgun
                "wname":"Hot-shot Lasgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":4,
                        "dmg1":2,
                        "dmg2":3,
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
            "Signal"
        ],
        "fackey":"Imperial Guard",
        "faction":[
            "Imperium",
            "Astra Militarum"
        ],
        "house":"",
        "keywords":[
            "Tempsestus Scion",
            "Comms"
        ],
        "specials":[
            "Staunch",
            "Scout"
        ]
    },
    {   # Tempestus Scion Gunner
        "opname":"Tempestus Scion Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":8,
        },
        "rweaps":[
            {   # Flamer
                "wname":"Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Grenade Launcher
                "wname":"Grenade Launcher",
                "profiles":[
                    {
                        "pname":"Frag",
                        "atts":4,
                        "bskill":3,
                        "dmg1":2,
                        "dmg2":4,
                        "srule":[
                            "Blast 2\""
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Krak",
                        "atts":4,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Hot-shot Volley Gun
                "wname":"Hot-shot Volley Gun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Fusillade"
                        ],
                        "crits":[
                            "P 4"
                        ],
                    },
                ]
            },
            {   # Meltagun
                "wname":"Meltagun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\""
                            "AP 2"
                        ],
                        "crits":[
                            "MW 4"
                        ],
                    },
                ]
            },
            {   # Plasma Gun
                "wname":"Plasma Gun",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "bskill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "bskill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP 2"
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Imperial Guard",
        "faction":[
            "Imperium",
            "Astra Militarum"
        ],
        "house":"",
        "keywords":[
            "Tempsestus Scion",
            "Gunner"
        ],
        "specials":[
            "Marksman"
        ]
    },
    {   # Tempestor
        "opname":"Tempestor",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":9,
        },
        "rweaps":[
            {   # Bolt Pistol
                "wname":"Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Hot-shot Laspistol
                "wname":"Hot-shot Laspistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Plasma Gun
                "wname":"Plasma Gun",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "bskill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\""
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":"4",
                        "bskill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\""
                            "AP 2"
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Fist
                "wname":"Power Fist",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":4,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Accomplished Leader"
        ],
        "uacts":[
        ],
        "fackey":"Imperial Guard",
        "faction":[
            "Imperium",
            "Astra Militarum"
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Tempsestus Scion",
            "Tempestor"
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman"
        ]
    },
    # --- Space Marine ---
    {   # Intercessor [Warrior]
        "opname":"Intercessor [Warrior]",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":13,
        },
        "rweaps":[
            {   # Auto Bolt Rifle
                "wname":"Auto Bolt Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Bolt Rifle
                "wname":"Bolt Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "P 1"
                        ],
                    },
                ]
            },
            {   # Stalker Bolt Rifle
                "wname":"Stalker Bolt Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Heavy",
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Space Marine",
        "faction":[
            "Imperium",
            "Adeptus Astartes"
        ],
        "house":"",
        "keywords":[
            "Primaris",
            "Intercessor",
            "Warrior"
        ],
        "specials":[
        ],
    },
    {   # Intercessor Sergeant
        "opname":"Intercessor Sergeant",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":14,
        },
        "rweaps":[
            {   # Auto Bolt Rifle
                "wname":"Auto Bolt Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Ceaseless"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Bolt Pistol
                "wname":"Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Bolt Rifle
                "wname":"Bolt Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "P 1"
                        ],
                    },
                ]
            },
            {   # Hand Flamer
                "wname":"Hand Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\"",
                            "Torrent 1\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Plasma Pistol
                "wname":"Plasma Pistol",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 2",
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Stalker Bolt Rifle
                "wname":"Stalker Bolt Rifle",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Heavy",
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Fist
                "wname":"Power Fist",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Brutal"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Thunder Hammer
                "wname":"Thunder Hammer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Space Marine",
        "faction":[
            "Imperium",
            "Adeptus Astartes"
        ],
        "house":"",
        "keywords":[
            "Primaris",
            "Leader",
            "Intercessor",
            "Sergeant"
        ],
        "specials":[
        ],
    },
    {   # Assault Intercessor [Warrior]
        "opname":"Assault Intercessor [Warrior]",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":13,
        },
        "rweaps":[
            {   # Heavy Bolt Pistol
                "wname":"Heavy Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                            "P 1"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":5,
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
        "fackey":"Space Marine",
        "faction":[
            "Imperium",
            "Adeptus Astartes"
        ],
        "house":"",
        "keywords":[
            "Primaris",
            "Assault Intercessor",
            "Warrior"
        ],
        "specials":[
        ],
    },
    {   # Assault Intercessor Sergeant
        "opname":"Assault Intercessor Sergeant",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":14,
        },
        "rweaps":[
            {   # Hand Flamer
                "wname":"Hand Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\"",
                            "Torrent 1\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Heavy Bolt Pistol
                "wname":"Heavy Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                            "P 1"
                        ],
                    },
                ]
            },
            {   # Plasma Pistol
                "wname":"Plasma Pistol",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 2",
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Fist
                "wname":"Power Fist",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Brutal"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Thunder Hammer
                "wname":"Thunder Hammer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "abs":[
        ],
        "uacts":[
        ],
        "fackey":"Space Marine",
        "faction":[
            "Imperium",
            "Adeptus Astartes"
        ],
        "house":"",
        "keywords":[
            "Primaris",
            "Leader",
            "Assault Intercessor",
            "Sergeant"
        ],
        "specials":[
        ],
    },
    {   # Infiltrator [Warrior]
        "opname":"Infiltrator [Warrior]",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Marksman Bolt Carbine
                "wname":"Marksman Bolt Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Lethal 5"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Space Marine",
        "faction":[
            "Imperium",
            "Adeptus Astartes"
        ],
        "house":"",
        "keywords":[
            "Primaris",
            "Infiltrator",
            "Warrior"
        ],
        "specials":[
        ],
    },
    {   # Infiltrator Sergeant
        "opname":"Infiltrator Sergeant",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":13,
        },
        "rweaps":[
            {   # Marksman Bolt Carbine
                "wname":"Marksman Bolt Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Lethal 5"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Space Marine",
        "faction":[
            "Imperium",
            "Adeptus Astartes"
        ],
        "house":"",
        "keywords":[
            "Primaris",
            "Leader",
            "Infiltrator",
            "Sergeant"
        ],
        "specials":[
        ],
    },
    {   # Incursor [Warrior]
        "opname":"Incursor [Warrior]",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Occulus Bolt Carbine
                "wname":"Occulus Bolt Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "No Cover"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Combat Knife
                "wname":"Combat Knife",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":5,
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
        "fackey":"Space Marine",
        "faction":[
            "Imperium",
            "Adeptus Astartes"
        ],
        "house":"",
        "keywords":[
            "Primaris",
            "Incursor",
            "Warrior"
        ],
        "specials":[
        ],
    },
    {   # Incursor Sergeant
        "opname":"Incursor Sergeant",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":13,
        },
        "rweaps":[
            {   # Occulus Bolt Carbine
                "wname":"Occulus Bolt Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "No Cover"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Combat Blade
                "wname":"Combat Blade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":5,
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
        "fackey":"Space Marine",
        "faction":[
            "Imperium",
            "Adeptus Astartes"
        ],
        "house":"",
        "keywords":[
            "Primaris",
            "Leader",
            "Incursor",
            "Sergeant"
        ],
        "specials":[
        ],
    },
    {   # Reiver [Warrior]
        "opname":"Reiver [Warrior]",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Bolt Carbine
                "wname":"Bolt Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Special Issue Bolt Pistol
                "wname":"Special Issue Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Combat Knife
                "wname":"Combat Knife",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Space Marine",
        "faction":[
            "Imperium",
            "Adeptus Astartes"
        ],
        "house":"",
        "keywords":[
            "Primaris",
            "Reiver",
            "Warrior"
        ],
        "specials":[
        ],
    },
    {   # Reiver Sergeant
        "opname":"Reiver Sergeant",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":13,
        },
        "rweaps":[
            {   # Bolt Carbine
                "wname":"Bolt Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Special Issue Bolt Pistol
                "wname":"Special Issue Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Combat Knife
                "wname":"Combat Knife",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Bladesman"
        ],
        "uacts":[
        ],
        "fackey":"Space Marine",
        "faction":[
            "Imperium",
            "Adeptus Astartes"
        ],
        "house":"",
        "keywords":[
            "Primaris",
            "Leader",
            "Reiver",
            "Sergeant"
        ],
        "specials":[
        ],
    },
    # --- Talons of the Emperor ---
    {   # Custodian Guard Warrior
        "opname":"Custodian Guard Warrior",
        "stats":{
            "move":6,
            "apl":4,
            "gpact":1,
            "def":3,
            "save":2,
            "wounds":18,
        },
        "rweaps":[
            {   # Guardian Spear
                "wname":"Guardian Spear",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "P 1"
                        ],
                    },
                ]
            },
            {   # Sentinel Blade
                "wname":"Sentinel Blade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                            "P 1"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Guardian Spear
                "wname":"Guardian Spear",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Sentinel Blade
                "wname":"Sentinel Blade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "The Emperor's Chosen"
            "Storm Shield"
        ],
        "uacts":[
        ],
        "fackey":"Talons of the Emperor",
        "faction":[
            "Imperium"
            "Adeptus Custodes"
        ],
        "house":"",
        "keywords":[
            "Custodian Guard"
            "Warrior"
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman",
            "Scout"
        ]
    },
    {   # Custodian Guard Leader
        "opname":"Custodian Guard Leader",
        "stats":{
            "move":6,
            "apl":4,
            "gpact":1,
            "def":3,
            "save":2,
            "wounds":19,
        },
        "rweaps":[
            {   # Guardian Spear
                "wname":"Guardian Spear",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "P 1"
                        ],
                    },
                ]
            },
            {   # Sentinel Blade
                "wname":"Sentinel Blade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                            "P 1"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Guardian Spear
                "wname":"Guardian Spear",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Sentinel Blade
                "wname":"Sentinel Blade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "The Emperor's Chosen"
            "Storm Shield"
        ],
        "uacts":[
        ],
        "fackey":"Talons of the Emperor",
        "faction":[
            "Imperium"
            "Adeptus Custodes"
        ],
        "house":"",
        "keywords":[
            "Custodian Guard"
            "Leader"
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman",
            "Scout"
        ]
    },
    {   # Sister of Silence Prosecutor
        "opname":"Sister of Silence Prosecutor",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":8,
        },
        "rweaps":[
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Psychic Abomination"
        ],
        "uacts":[
        ],
        "fackey":"Talons of the Emperor",
        "faction":[
            "Imperium"
            "Anathema Psykana"
        ],
        "house":"",
        "keywords":[
            "Sister of Silence"
            "Prosecutor"
        ],
        "specials":[
            "Staunch",
            "Marksman",
            "Scout"
        ]
    },
    {   # Sister of Silence Witchseeker
        "opname":"Sister of Silence Witchseeker",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":8,
        },
        "rweaps":[
            {   # Flamer
                "wname":"Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Psychic Abomination"
        ],
        "uacts":[
        ],
        "fackey":"Talons of the Emperor",
        "faction":[
            "Imperium"
            "Anathema Psykana"
        ],
        "house":"",
        "keywords":[
            "Sister of Silence"
            "Witchseeker"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Sister of Silence Vigilator
        "opname":"Sister of Silence Vigilator",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Executioner Greatblade
                "wname":"Executioner Greatblade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Psychic Abomination"
        ],
        "uacts":[
        ],
        "fackey":"Talons of the Emperor",
        "faction":[
            "Imperium"
            "Anathema Psykana"
        ],
        "house":"",
        "keywords":[
            "Sister of Silence"
            "Vigilator"
        ],
        "specials":[
            "Combat",
            "Staunch"
        ]
    },
    {   # Sister of Silence Superior
        "opname":"Sister of Silence Superior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":9,
        },
        "rweaps":[
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Flamer
                "wname":"Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\""
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Executioner Greatblade
                "wname":"Executioner Greatblade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Psychic Abomination"
        ],
        "uacts":[
        ],
        "fackey":"Talons of the Emperor",
        "faction":[
            "Imperium"
            "Anathema Psykana"
        ],
        "house":"",
        "keywords":[
            "Sister of Silence"
            "Superior"
            "Leader"
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    # --- Thousand Sons ---
    {   # Rubric Marine Warrior
        "opname":"Rubric Marine Warrior",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Inferno Boltgun
                "wname":"Inferno Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "AP 1",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Favoured By Change",
            "All Is Dust",
        ],
        "uacts":[
        ],
        "fackey":"Thousand Sons",
        "faction":[
            "Chaos",
            "Arcana Astartes",
        ],
        "house":"",
        "keywords":[
            "Rubric Marine",
            "Warrior",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Rubric Marine Gunner
        "opname":"Rubric Marine Gunner",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Soulreaper Cannon
                "wname":"Soulreaper Cannon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":6,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "AP 1",
                            "Fusillade",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Warpflamer
                "wname":"Warpflamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                            "Torrent 2\"",
                            "AP 1",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Favoured By Change",
            "All Is Dust",
        ],
        "uacts":[
        ],
        "fackey":"Thousand Sons",
        "faction":[
            "Chaos",
            "Arcana Astartes",
        ],
        "house":"",
        "keywords":[
            "Rubric Marine",
            "Gunner",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Rubric Marine Icon Bearer
        "opname":"Rubric Marine Icon Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Inferno Boltgun
                "wname":"Inferno Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "AP 1",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Favoured By Change",
            "All Is Dust",
            "Icon Bearer",
            "Icon Of Flame",
        ],
        "uacts":[
        ],
        "fackey":"Thousand Sons",
        "faction":[
            "Chaos",
            "Arcana Astartes",
        ],
        "house":"",
        "keywords":[
            "Rubric Marine",
            "Icon Bearer",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Aspiring Sorcerer
        "opname":"Aspiring Sorcerer",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":13,
        },
        "rweaps":[
            {   # Inferno Bolt Pistol
                "wname":"Inferno Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\"",
                            "AP 1",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Plasma Pistol
                "wname":"Plasma Pistol",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "bskill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 1",
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "bskill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 2",
                            "Hot",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Warpflame Pistol
                "wname":"Warpflame Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                            "Torrent 1\"",
                            "AP 1",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Force Stave
                "wname":"Force Stave",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Stun",
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Favoured By Change",
        ],
        "uacts":[
            "Manifest Psychic Power [Thousand Sons]",
        ],
        "fackey":"Thousand Sons",
        "faction":[
            "Chaos",
            "Arcana Astartes",
        ],
        "house":"",
        "keywords":[
            "Psyker",
            "Leader",
            "Rubric Marine",
            "Aspiring Sorcerer",
        ],
        "specials":[
            "Combat",
            "Staunch",
            "Marksman"
        ]
    },
    {   # Tzaangor Fighter
        "opname":"Tzaangor Fighter",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Tzaangor Blades
                "wname":"Tzaangor Blades",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":4,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Favoured By Change",
        ],
        "uacts":[
        ],
        "fackey":"Thousand Sons",
        "faction":[
            "Chaos",
        ],
        "house":"",
        "keywords":[
            "Tzaangor",
            "Fighter",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Tzaangor Icon Bearer
        "opname":"Tzaangor Icon Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Dagger
                "wname":"Dagger",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Favoured By Change",
            "Icon Bearer",
        ],
        "uacts":[
            "Herd Banner",
        ],
        "fackey":"Thousand Sons",
        "faction":[
            "Chaos",
        ],
        "house":"",
        "keywords":[
            "Tzaangor",
            "Icon Bearer",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Tzaangor Horn Bearer
        "opname":"Tzaangor Horn Bearer",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Dagger
                "wname":"Dagger",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Favoured By Change",
        ],
        "uacts":[
            "Brayhorn",
        ],
        "fackey":"Thousand Sons",
        "faction":[
            "Chaos",
        ],
        "house":"",
        "keywords":[
            "Tzaangor",
            "Horn Bearer",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Twistbray
        "opname":"Twistbray",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":9,
        },
        "rweaps":[
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Tzaangor Blades
                "wname":"Tzaangor Blades",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Relentless",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Favoured By Change",
        ],
        "uacts":[
        ],
        "fackey":"Thousand Sons",
        "faction":[
            "Chaos",
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Tzaangor",
            "Twistbray",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    # --- Tomb World ---
    {   # Necron Warrior
        "opname":"Necron Warrior",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":9,
        },
        "rweaps":[
            {   # Gauss Flayer
                "wname":"Gauss Flayer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Gauss Reaper
                "wname":"Gauss Reaper",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\"",
                        ],
                        "crits":[
                            "P 1",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Bayonet
                "wname":"Bayonet",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Living Metal",
        ],
        "uacts":[
        ],
        "fackey":"Tomb World",
        "faction":[
            "Necron",
        ],
        "house":"",
        "keywords":[
            "Necron Warrior",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Immortal Warrior
        "opname":"Immortal Warrior",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":10,
        },
        "rweaps":[
            {   # Gauss Blaster
                "wname":"Gauss Blaster",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "AP 1",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Tesla Carbine
                "wname":"Tesla Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Splash 1",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Bayonet
                "wname":"Bayonet",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Living Metal",
        ],
        "uacts":[
        ],
        "fackey":"Tomb World",
        "faction":[
            "Necron",
        ],
        "house":"",
        "keywords":[
            "Immortal",
            "Warrior",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Immortal Leader
        "opname":"Immortal Leader",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":11,
        },
        "rweaps":[
            {   # Gauss Blaster
                "wname":"Gauss Blaster",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "AP 1",
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Tesla Carbine
                "wname":"Tesla Carbine",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                            "Splash 1",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Bayonet
                "wname":"Bayonet",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "wskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Living Metal",
        ],
        "uacts":[
        ],
        "fackey":"Tomb World",
        "faction":[
            "Necron",
        ],
        "house":"",
        "keywords":[
            "Immortal",
            "Leader",
        ],
        "specials":[
            "Staunch",
            "Marksman"
        ]
    },
    {   # Flayed One Warrior
        "opname":"Flayed One Warrior",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":9,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Flayer Claws
                "wname":"Flayer Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Living Metal",
        ],
        "uacts":[
        ],
        "fackey":"Tomb World",
        "faction":[
            "Necron",
        ],
        "house":"",
        "keywords":[
            "Flayed One",
            "Warrior",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Flayed One Leader
        "opname":"Flayed One Leader",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":4,
            "wounds":10,
        },
        "rweaps":[
        ],
        "mweaps":[
            {   # Flayer Claws
                "wname":"Flayer Claws",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                            "Rending",
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Living Metal",
        ],
        "uacts":[
        ],
        "fackey":"Tomb World",
        "faction":[
            "Necron",
        ],
        "house":"",
        "keywords":[
            "Flayed One",
            "Leader",
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Deathmark Warrior
        "opname":"Deathmark Warrior",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":10,
        },
        "rweaps":[
            {   # Synaptic Disintegrator
                "wname":"Synaptic Disintegrator",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":4,
                        "dmg2":4,
                        "srule":[
                            "Heavy",
                            "AP 1",
                        ],
                        "crits":[
                            "MW 1",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Living Metal",
        ],
        "uacts":[
        ],
        "fackey":"Tomb World",
        "faction":[
            "Necron",
        ],
        "house":"",
        "keywords":[
            "Deathmark",
            "Warrior",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    {   # Deathmark Leader
        "opname":"Deathmark Leader",
        "stats":{
            "move":4,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":11,
        },
        "rweaps":[
            {   # Synaptic Disintegrator
                "wname":"Synaptic Disintegrator",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":4,
                        "dmg2":4,
                        "srule":[
                            "Heavy",
                            "AP 1",
                            "Balanced",
                        ],
                        "crits":[
                            "MW 1",
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "wskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Living Metal",
        ],
        "uacts":[
        ],
        "fackey":"Tomb World",
        "faction":[
            "Necron",
        ],
        "house":"",
        "keywords":[
            "Deathmark",
            "Leader",
        ],
        "specials":[
            "Marksman",
            "Scout"
        ]
    },
    # --- Traitor Space Marine ---
    {   # Chaos Space Marine [Warrior]
        "opname":"Chaos Space Marine [Warrior]",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Bolt Pistol
                "wname":"Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Traitor Space Marine",
        "faction":[
            "Chaos",
            "Heretic Astartes"
        ],
        "house":"",
        "keywords":[
            "Chaos Space Marine",
            "Warrior"
        ],
        "specials":[
        ],
    },
    {   # Chaos Space Marine [Gunner]
        "opname":"Chaos Space Marine [Gunner]",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Flamer
                "wname":"Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\"",
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Meltagun
                "wname":"Meltagun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":6,
                        "dmg2":3,
                        "srule":[
                            "Range 6\"",
                            "AP 2"
                        ],
                        "crits":[
                            "MW 4"
                        ],
                    },
                ]
            },
            {   # Plasma Gun
                "wname":"Plasma Gun",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "AP 2",
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Traitor Space Marine",
        "faction":[
            "Chaos",
            "Heretic Astartes"
        ],
        "house":"",
        "keywords":[
            "Chaos Space Marine",
            "Gunner"
        ],
        "specials":[
        ],
    },
    {   # Chaos Space Marine [Heavy Gunner]
        "opname":"Chaos Space Marine [Heavy Gunner]",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Heavy Bolter
                "wname":"Heavy Bolter",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Heavy",
                            "Fusillade"
                        ],
                        "crits":[
                            "P 1"
                        ],
                    },
                ]
            },
            {   # Missile Launcher
                "wname":"Missile Launcher",
                "profiles":[
                    {
                        "pname":"Frag",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":5,
                        "srule":[
                            "Heavy",
                            "Blast 2\""
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Krak",
                        "atts":4,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Heavy",
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
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
        "fackey":"Traitor Space Marine",
        "faction":[
            "Chaos",
            "Heretic Astartes"
        ],
        "house":"",
        "keywords":[
            "Chaos Space Marine",
            "Heavy Gunner"
        ],
        "specials":[
        ],
    },
    {   # Chaos Space Marine [Icon Bearer]
        "opname":"Chaos Space Marine [Icon Bearer]",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":12,
        },
        "rweaps":[
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Bolt Pistol
                "wname":"Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Icon Bearer"
        ],
        "uacts":[
            "Icon of Vegeance"
        ],
        "fackey":"Traitor Space Marine",
        "faction":[
            "Chaos",
            "Heretic Astartes"
        ],
        "house":"",
        "keywords":[
            "Chaos Space Marine",
            "Icon Bearer"
        ],
        "specials":[
        ],
    },
    {   # Chaos Space Marine Aspiring Champion
        "opname":"Chaos Space Marine Aspiring Champion",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":3,
            "wounds":13,
        },
        "rweaps":[
            {   # Boltgun
                "wname":"Boltgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Bolt Pistol
                "wname":"Bolt Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Plasma Pistol
                "wname":"Plasma Pistol",
                "profiles":[
                    {
                        "pname":"Standard",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 1"
                        ],
                        "crits":[
                        ],
                    },
                    {
                        "pname":"Supercharge",
                        "atts":4,
                        "skill":2,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                            "Range 6\"",
                            "AP 2",
                            "Hot"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Chainsword
                "wname":"Chainsword",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Fists
                "wname":"Fists",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Fist
                "wname":"Power Fist",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":3,
                        "dmg1":5,
                        "dmg2":7,
                        "srule":[
                            "Brutal"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
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
        "fackey":"Traitor Space Marine",
        "faction":[
            "Chaos",
            "Heretic Astartes"
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Chaos Space Marine",
            "Aspiring Champion"
        ],
        "specials":[
        ],
    },
    {   # Chaos Cultist [Fighter]
        "opname":"Chaos Cultist [Fighter]",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":2,
            "def":3,
            "save":5,
            "wounds":7,
        },
        "rweaps":[
            {   # Autogun
                "wname":"Autogun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Brutal Assault Weapon
                "wname":"Brutal Assault Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Traitor Space Marine",
        "faction":[
            "Chaos"
        ],
        "house":"",
        "keywords":[
            "Cultist",
            "Fighter"
        ],
        "specials":[
        ],
    },
    {   # Chaos Cultist [Gunner]
        "opname":"Chaos Cultist [Gunner]",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":7,
        },
        "rweaps":[
            {   # Flamer
                "wname":"Flamer",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":2,
                        "dmg1":2,
                        "dmg2":2,
                        "srule":[
                            "Range 6\"",
                            "Torrent 2\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Heavy Stubber
                "wname":"Heavy Stubber",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "skill":4,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Heavy",
                            "Ceaseless",
                            "Fusillade"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":4,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Traitor Space Marine",
        "faction":[
            "Chaos"
        ],
        "house":"",
        "keywords":[
            "Cultist",
            "Gunner"
        ],
        "specials":[
        ],
    },
    {   # Chaos Cultist Champion
        "opname":"Chaos Cultist Champion",
        "stats":{
            "move":6,
            "apl":2,
            "gpact":1,
            "def":3,
            "save":5,
            "wounds":8,
        },
        "rweaps":[
            {   # Autogun
                "wname":"Autogun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Autopistol
                "wname":"Autopistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Shotgun
                "wname":"Shotgun",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":2,
                        "dmg1":3,
                        "dmg2":3,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Brutal Assault Weapon
                "wname":"Brutal Assault Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "skill":3,
                        "dmg1":2,
                        "dmg2":3,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Gun Butt
                "wname":"Gun Butt",
                "profiles":[
                    {
                        "pname":"",
                        "atts":3,
                        "skill":3,
                        "dmg1":2,
                        "dmg2":3,
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
        "fackey":"Traitor Space Marine",
        "faction":[
            "Chaos"
        ],
        "house":"",
        "keywords":[
            "Leader",
            "Cultist",
            "Champion"
        ],
        "specials":[
        ],
    },
    # --- Troupe ---
    {   # Player Warrior
        "opname":"Player Warrior",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
            {   # Shuriken Pistol
                "wname":"Shuriken Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Harlequin's Blade
                "wname":"Harlequin's Blade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Balanced"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Harlequin's Caress
                "wname":"Harlequin's Caress",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Harlequin's Embrace
                "wname":"Harlequin's Embrace",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Brutal"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Harlequin's Kiss
                "wname":"Harlequin's Kiss",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":7,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Holo-suit"
            "Flip Belt"
        ],
        "uacts":[
        ],
        "fackey":"Troupe",
        "faction":[
            "Aeldari"
            "Harlequins"
        ],
        "house":"",
        "keywords":[
            "Player"
            "Warrior"
        ],
        "specials":[
            "Combat",
            "Scout"
        ]
    },
    {   # Player Gunner
        "opname":"Player Gunner",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":8,
        },
        "rweaps":[
            {   # Fusion Pistol
                "wname":"Fusion Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":5,
                        "dmg2":3,
                        "srule":[
                            "Range 3\""
                            "AP 2"
                        ],
                        "crits":[
                            "MW 3"
                        ],
                    },
                ]
            },
            {   # Neuro Disruptor
                "wname":"Neuro Disruptor",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\""
                            "AP 1"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Harlequin's Blade
                "wname":"Harlequin's Blade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Balanced"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Harlequin's Caress
                "wname":"Harlequin's Caress",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":4,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Harlequin's Embrace
                "wname":"Harlequin's Embrace",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Brutal"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Harlequin's Kiss
                "wname":"Harlequin's Kiss",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":3,
                        "dmg2":7,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Holo-suit"
            "Flip Belt"
        ],
        "uacts":[
        ],
        "fackey":"Troupe",
        "faction":[
            "Aeldari"
            "Harlequins"
        ],
        "house":"",
        "keywords":[
            "Player"
            "Gunner"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ]
    },
    {   # Player Leader
        "opname":"Player Leader",
        "stats":{
            "move":6,
            "apl":3,
            "gpact":1,
            "def":3,
            "save":6,
            "wounds":9,
        },
        "rweaps":[
            {   # Fusion Pistol
                "wname":"Fusion Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":5,
                        "dmg2":3,
                        "srule":[
                            "Range 3\""
                            "AP 2"
                        ],
                        "crits":[
                            "MW 3"
                        ],
                    },
                ]
            },
            {   # Neuro Disruptor
                "wname":"Neuro Disruptor",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Range 6\""
                            "AP 1"
                        ],
                        "crits":[
                            "Stun"
                        ],
                    },
                ]
            },
            {   # Shuriken Pistol
                "wname":"Shuriken Pistol",
                "profiles":[
                    {
                        "pname":"",
                        "atts":4,
                        "bskill":2,
                        "dmg1":3,
                        "dmg2":4,
                        "srule":[
                            "Range 6\""
                        ],
                        "crits":[
                            "Rending"
                        ],
                    },
                ]
            },
        ],
        "mweaps":[
            {   # Harlequin's Blade
                "wname":"Harlequin's Blade",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Balanced"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Harlequin's Caress
                "wname":"Harlequin's Caress",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":3,
                        "dmg1":5,
                        "dmg2":6,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Harlequin's Embrace
                "wname":"Harlequin's Embrace",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":5,
                        "srule":[
                            "Brutal"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Harlequin's Kiss
                "wname":"Harlequin's Kiss",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":3,
                        "dmg2":7,
                        "srule":[
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
            {   # Power Weapon
                "wname":"Power Weapon",
                "profiles":[
                    {
                        "pname":"",
                        "atts":5,
                        "wskill":2,
                        "dmg1":4,
                        "dmg2":6,
                        "srule":[
                            "Lethal 5+"
                        ],
                        "crits":[
                        ],
                    },
                ]
            },
        ],
        "abs":[
            "Holo-suit"
            "Flip Belt"
        ],
        "uacts":[
        ],
        "fackey":"Troupe",
        "faction":[
            "Aeldari"
            "Harlequins"
        ],
        "house":"",
        "keywords":[
            "Player"
            "Leader"
        ],
        "specials":[
            "Combat",
            "Marksman",
            "Scout"
        ]
    },
]