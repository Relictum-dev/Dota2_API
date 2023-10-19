Game_Modes = {
    0: 'None',
    1: 'All Pick Unranked',
    2: 'Capitans Mode Unranked',
    3: 'Random Draft',
    4: 'Single Draft',
    5: 'All Random',
    6: 'Intro',
    7: 'The Diretide',
    8: 'Reverse Capitan Mode',
    9: 'The Greeviling',
    10: 'Tutorial',
    11: 'Mid Only',
    12: 'Least Played',
    13: 'New Player Pool',
    14: 'Compendium Matchmaking',
    15: 'Custom',
    16: 'Capitans Draft Ranked',
    17: 'Balanced Draft',
    18: 'Ability Draft',
    19: 'Event',
    20: 'All Random Deathmatch',
    21: 'Solo Mid',
    22: 'All Pick Ranked',
    23: 'Turbo',
    24: 'Mutation'
}


Heroes_pool = {
    1: 'Antimage',
    2: 'Axe',
    3: 'Bane',
    4: 'Bloodseeker',
    5: 'Cristal Maiden',
    6: 'Drow_Ranger',
    7: 'Earthshaker',
    8: 'Juggernaut',
    9: 'Mirana',
    10: 'Morphling',
    11: 'Shadow Fiend',
    12: 'Phantom Lancer',
    13: 'Puck',
    14: 'Pudge',
    15: 'Razor',
    16: 'Sand King',
    17: 'Storm Spirit',
    18: 'Sven',
    19: 'Tiny',
    20: 'Vengeful Spirit',
    21: 'Windranger',
    22: 'Zeus',
    23: 'Kunkka',
    25: 'Lina',
    26: 'Lion',
    27: 'Shadow Shaman',
    28: 'Slardar',
    29: 'Tidehunter',
    30: 'Witch Doctor',
    31: 'Lich',
    32: 'Riki',
    33: 'Enigma',
    34: 'Tinker',
    35: 'Sniper',
    36: 'Necrophos',
    37: 'Warlock',
    38: 'Beastmaster',
    39: 'Queen of Pain',
    40: 'Venomancer',
    41: 'Faceless Void',
    42: 'Wraith King',
    43: 'Death Prophet',
    44: 'Phantom Assasin',
    45: 'Pugna',
    46: 'Templar Assasin',
    47: 'Viper',
    48: 'Luna',
    49: 'Dragon Knight',
    50: 'Dazzle',
    51: 'Clocwerk',
    52: 'Leshrac',
    53: "Natures's Prophet",
    54: 'Lifestealer',
    55: 'Dark Seer',
    56: 'Clinkz',
    57: 'Omniknight',
    58: 'Enchantress',
    59: 'Huskar',
    60: 'Night Stalker',
    61: 'Broodmother',
    62: 'Bounty Hunter',
    63: 'Weaver',
    64: 'Jakiro',
    65: 'Batraider',
    66: 'Chen',
    67: 'Spectre',
    68: 'Anicent Apparition',
    69: 'Doom',
    70: 'Ursa',
    71: 'Spirit Breaker',
    72: 'Gyrocopter',
    73: 'Alchemist',
    74: 'Invoker',
    75: 'Silencer',
    76: 'Outworld Destroyer',
    77: 'Lycan',
    78: 'Brewmaster',
    79: 'Shadow Demon',
    80: 'Lone Druid',
    81: 'Chaos Knight',
    82: 'Meepo',
    83: 'Treant Protecton',
    84: 'Ogre Mage',
    85: 'Undying',
    86: 'Rubick',
    87: 'Disruptor',
    88: 'Nyx Assasin',
    89: 'Naga Siren',
    90: 'Keeper of the Light',
    91: 'Io',
    92: 'Visage',
    93: 'Slark',
    94: 'Medusa',
    95: 'Troll Warlord',
    96: 'Centaur Warrunner',
    97: 'Magnus',
    98: 'Timbersaw',
    99: 'Bristleback',
    100: 'Tusk',
    101: 'Skywrath Mage',
    102: 'Abbadon',
    103: 'Elder Titan',
    104: 'Legion Commander',
    105: 'Techies',
    106: 'Ember Spirit',
    107: 'Earth Spirit',
    108: 'Underlord',
    109: 'Terrorblade',
    110: 'Phoenix',
    111: 'Oracle',
    112: 'Winter Wyvern',
    113: 'Arc Warden',
    114: 'Monkey King',
    119: 'Dark Willow',
    120: 'Pangolier',
    121: 'Grimstroke',
    123: 'Hoodwink',
    126: 'Void Spitit',
    128: 'Snapfire',
    129: 'Mars',
    135: 'Downbreaker',
    136: 'Marci',
    137: 'Primal Beast',
    138: 'Muerta'
}




def mmr_rank(player_rank):
    if player_rank >= 0 and player_rank <= 149:
        player_rank = 'Рекрут 1'
        return player_rank
    elif player_rank >= 150 and player_rank <= 299:
        player_rank = 'Рекрут 2'
        return player_rank
    elif player_rank >= 300 and player_rank <= 459:
        player_rank = 'Рекрут 3'
        return player_rank
    elif player_rank >= 460 and player_rank <= 609:
        player_rank = 'Рекрут 4'
        return player_rank
    elif player_rank >= 610 and player_rank <= 769:
        player_rank = 'Рекрут 5'
        return player_rank
    elif player_rank >= 770 and player_rank <= 919:
        player_rank = 'Страж 1'
        return player_rank
    elif player_rank >= 920 and player_rank <= 1079:
        player_rank = 'Страж 2'
        return player_rank
    elif player_rank >= 1080 and player_rank <= 1229:
        player_rank = 'Страж 3'
        return player_rank
    elif player_rank >= 1230 and player_rank <= 1399:
        player_rank = 'Страж 4'
        return player_rank
    elif player_rank >= 1400 and player_rank <= 1539:
        player_rank = 'Страж 5'
        return player_rank
    elif player_rank >= 1540 and player_rank <= 1699:
        player_rank = 'Рыцарь 1'
        return player_rank
    elif player_rank >= 1700 and player_rank <= 1849:
        player_rank = 'Рыцарь 2'
        return player_rank
    elif player_rank >= 1850 and player_rank <= 1999:
        player_rank = 'Рыцарь 3'
        return player_rank
    elif player_rank >= 2000 and player_rank <= 2149:
        player_rank = 'Рыцарь 4'
        return player_rank
    elif player_rank >= 2150 and player_rank <= 2309:
        player_rank = 'Рыцарь 5'
        return player_rank
    elif player_rank >= 2310 and player_rank <= 2449:
        player_rank = 'Герой 1'
        return player_rank
    elif player_rank >= 2450 and player_rank <= 2609:
        player_rank = 'Герой 2'
        return player_rank
    elif player_rank >= 2610 and player_rank <= 2769:
        player_rank = 'Герой 3'
        return player_rank
    elif player_rank >= 2770 and player_rank <= 2929:
        player_rank = 'Герой 4'
        return player_rank
    elif player_rank >= 2930 and player_rank <= 3079:
        player_rank = 'Герой 5'
        return player_rank
    elif player_rank >= 3080 and player_rank <= 3229:
        player_rank = 'Легенда 1'
        return player_rank
    elif player_rank >= 3230 and player_rank <= 3389:
        player_rank = 'Легенда 2'
        return player_rank
    elif player_rank >= 3390 and player_rank <= 3539:
        player_rank = 'Легенда 3'
        return player_rank
    elif player_rank >= 3540 and player_rank <= 3699:
        player_rank = 'Легенда 4'
        return player_rank
    elif player_rank >= 3700 and player_rank <= 3849:
        player_rank = 'Легенда 5'
        return player_rank
    elif player_rank >= 3850 and player_rank <= 3999:
        player_rank = 'Властелин 1'
        return player_rank
    elif player_rank >= 4000 and player_rank <= 4149:
        player_rank = 'Властелин 2'
        return player_rank
    elif player_rank >= 4150 and player_rank <= 4299:
        player_rank = 'Властелин 3'
        return player_rank
    elif player_rank >= 4300 and player_rank <= 4459:
        player_rank = 'Властелин 4'
        return player_rank
    elif player_rank >= 4460 and player_rank <= 4619:
        player_rank = 'Властелин 5'
        return player_rank
    elif player_rank >= 4620 and player_rank <= 4819:
        player_rank = 'Божество 1'
        return player_rank
    elif player_rank >= 4820 and player_rank <= 5019:
        player_rank = 'Божество 2'
        return player_rank
    elif player_rank >= 5020 and player_rank <= 5219:
        player_rank = 'Божество 3'
        return player_rank
    elif player_rank >= 5220 and player_rank <= 5419:
        player_rank = 'Божество 4'
        return player_rank
    elif player_rank >= 5420 and player_rank <= 5620:
        player_rank = 'Божество 5'
        return player_rank
    else:
        player_rank = 'Immortal'
        return player_rank
                            

