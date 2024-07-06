# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:17:50 2024

@author: Personal
"""

# Diccionarios con líderes, starters y ligas.
import pandas as pd

pokedex_completa = pd.read_csv("data\Pokemon.csv")

#Función

def index_pokemon(ID, forma = 0):
    numero = [pokedex_completa.loc[pokedex_completa['ID'] == ID].index[forma]]
    return int(numero[0])


## Kanto

starter_kanto = [0, 3, 6]

kanto = {
    'Brock': [73, 94],
    'Misty': [119, 120],
    'Lt. Surge': [99, 24, 25],
    'Erika': [70, 113, 44],
    'Koga': [108, 108, 88, 109],
    'Sabrina': [63, 48, 121, 64],
    'Blaine': [57, 76, 77, 58],
    'Giovanni': [110, 50, 33, 30, 110],
    'Lorelei': [86, 90, 79, 123, 130],
    'Bruno': [94, 94, 105, 106, 67],
    'Agatha': [93, 41, 92, 23, 93],
    'Lance': [129, 147, 147, 141, 148]
}

## Johto   
starter_johto = [151, 154, 158]

johto = {
    'Falkner': [15, 16],
    'Bugsy': [10, 13, 122],
    'Whitney': [34, 240],
    'Morty': [93, 91, 92, 92],
    'Chuck': [61, 58],
    'Jasmine': [207, 80, 80],
    'Pryce': [86, 85, 220],
    'Clair': [129, 147, 147, 229],
    'Will': [177, 123, 80, 102, 177],
    'Koga': [168, 204, 88, 48, 168],
    'Bruno': [236, 94, 105, 106, 67],
    'Karen': [196, 44, 197, 93, 228],
    'Lance': [129, 5, 148, 141, 148, 148]
}

johto_kanto = {
    'Lt. Surge': [index_pokemon(100), index_pokemon(82), index_pokemon(26)],  # Lt. Surge (Electric Type)
    'Sabrina': [index_pokemon(122), index_pokemon(103), index_pokemon(65)],  # Sabrina (Psychic Type)
    'Erika': [index_pokemon(71), index_pokemon(182), index_pokemon(45)],  # Erika (Grass Type)
    'Janine': [index_pokemon(110), index_pokemon(49), index_pokemon(168)],  # Janine (Poison Type)
    'Misty': [index_pokemon(121), index_pokemon(91), index_pokemon(134)],  # Misty (Water Type)
    'Brock': [index_pokemon(112), index_pokemon(95), index_pokemon(76)],  # Brock (Rock Type)
    'Blaine': [index_pokemon(126), index_pokemon(78), index_pokemon(38)],  # Blaine (Fire Type)
    'Blue': [index_pokemon(65), index_pokemon(103), index_pokemon(59), index_pokemon(134), index_pokemon(31), index_pokemon(6)],  # Blue (Mixed Types)
    'Will': [index_pokemon(196), index_pokemon(124), index_pokemon(178), index_pokemon(103)],  # Elite Four (Psychic Type)
    'Koga': [index_pokemon(89), index_pokemon(110), index_pokemon(168), index_pokemon(169)],  # Elite Four (Poison Type)
    'Bruno': [index_pokemon(95), index_pokemon(107), index_pokemon(106), index_pokemon(237)],  # Elite Four (Fighting Type)
    'Karen': [index_pokemon(229), index_pokemon(197), index_pokemon(45), index_pokemon(94)],  # Elite Four (Dark Type)
    'Lance': [index_pokemon(130), index_pokemon(149), index_pokemon(148), index_pokemon(230), index_pokemon(149), index_pokemon(6)]  # Champion (Dragon and Mixed Types)
}

## Hoenn
starter_hoenn = [251, 254, 257]
hoenn = {
    'Roxanne': [73, 73, 298],
    'Brawly': [65, 306, 295],
    'Wattson': [81, 99, 308, 309],
    'Flannery': [321, 217, 322, 323],
    'Norman': [328, 263, 287, 288],
    'Winona': [332, 356, 278, 226, 333],
    'Tate & Liza': [343, 177, 336, 337],
    'Wallace': [320, 72, 339, 271, 129, 349],  # Campeón de la Liga Pokémon
    'Sidney': [261, 331, 274, 318, index_pokemon(259)],
    'Phoebe': [index_pokemon(356), index_pokemon(354), index_pokemon(354), index_pokemon(302), index_pokemon(356)],
    'Glacia': [index_pokemon(362), index_pokemon(364), index_pokemon(362), index_pokemon(364), index_pokemon(365)],
    'Drake': [index_pokemon(372), index_pokemon(334), index_pokemon(330), index_pokemon(230), index_pokemon(373)],
    'Steven': [index_pokemon(227), index_pokemon(346), index_pokemon(344), index_pokemon(348), index_pokemon(306), index_pokemon(376)]  # Campeón de la Región Hoenn
}



## Corregir con numero de pokédex
## Sinnoh
starter_sinnoh = [index_pokemon(387), index_pokemon(390), index_pokemon(393)]
sinnoh = {
    'Roark': [index_pokemon(74), index_pokemon(95), index_pokemon(408)],
    'Gardenia': [index_pokemon(420), index_pokemon(387), index_pokemon(407)],
    'Maylene': [index_pokemon(307), index_pokemon(67), index_pokemon(448)],
    'Crasher Wake': [index_pokemon(130), index_pokemon(419), index_pokemon(195)],
    'Fantina': [index_pokemon(429), index_pokemon(426), index_pokemon(94)],
    'Byron': [index_pokemon(82), index_pokemon(208), index_pokemon(411)],
    'Candice': [index_pokemon(215), index_pokemon(221), index_pokemon(460), index_pokemon(478)],
    'Volkner': [index_pokemon(135), index_pokemon(26), index_pokemon(405), index_pokemon(466)],
    'Aaron': [index_pokemon(496), index_pokemon(416), index_pokemon(212), index_pokemon(214), index_pokemon(452)],
    'Bertha': [index_pokemon(340), index_pokemon(472), index_pokemon(76), index_pokemon(464), index_pokemon(450)],
    'Flint': [index_pokemon(229), index_pokemon(136), index_pokemon(78), index_pokemon(392), index_pokemon(467)],
    'Lucian': [index_pokemon(122), index_pokemon(196), index_pokemon(437), index_pokemon(65), index_pokemon(475)],
    'Cynthia': [index_pokemon(442), index_pokemon(407), index_pokemon(468), index_pokemon(448), index_pokemon(350), index_pokemon(445)]
}


## Unova
starter_unova = [index_pokemon(495), index_pokemon(498), index_pokemon(501)]
## BW
unova = {
    'Cilan, Chili, Cress': [index_pokemon(506), index_pokemon(511), index_pokemon(513), index_pokemon(515)],  # Cilan (Gym Leader Trio - Grass), Chili (Gym Leader Trio - Fire), Cress (Gym Leader Trio - Water)    
    'Lenora': [index_pokemon(505), index_pokemon(507)],  # Lenora (Normal Type)
    'Burgh': [index_pokemon(542), index_pokemon(544), index_pokemon(557)],  # Burgh (Bug Type)
    'Elesa': [index_pokemon(587), index_pokemon(587), index_pokemon(523)],  # Elesa (Electric Type)
    'Clay': [index_pokemon(552), index_pokemon(530), index_pokemon(536)],  # Clay (Ground Type)
    'Skyla': [index_pokemon(528), index_pokemon(521), index_pokemon(581)],  # Skyla (Flying Type)
    'Brycen': [index_pokemon(583), index_pokemon(615), index_pokemon(614)],  # Brycen (Ice Type)
    'Drayden or Iris': [index_pokemon(611), index_pokemon(612), index_pokemon(621)],  # Drayden (Dragon Type) or Iris depending on version
    'Shauntal': [index_pokemon(563), index_pokemon(593), index_pokemon(623), index_pokemon(609)],  # Elite Four (Ghost Type)
    'Grimsley': [index_pokemon(560), index_pokemon(510), index_pokemon(553), index_pokemon(625)],  # Elite Four (Dark Type)
    'Caitlin': [index_pokemon(576), index_pokemon(518), index_pokemon(579), index_pokemon(561)],  # Elite Four (Psychic Type)
    'Marshal': [index_pokemon(534), index_pokemon(538), index_pokemon(539), index_pokemon(620)],  # Elite Four (Fighting Type)
    'N': [index_pokemon(644), index_pokemon(565), index_pokemon(584), index_pokemon(567), index_pokemon(571), index_pokemon(601)],  # Champion (Mixed Types)
    'Shauntal_RM': [index_pokemon(563), index_pokemon(593), index_pokemon(478), index_pokemon(426), index_pokemon(623), index_pokemon(609)],  # Elite Four (Ghost Type)
    'Grimsley_RM': [index_pokemon(560), index_pokemon(510), index_pokemon(319), index_pokemon(452), index_pokemon(553), index_pokemon(625)],  # Elite Four (Dark Type)
    'Caitlin_RM': [index_pokemon(576), index_pokemon(518), index_pokemon(579), index_pokemon(561), index_pokemon(437), index_pokemon(376)],  # Elite Four (Psychic Type)
    'Marshal_RM': [index_pokemon(534), index_pokemon(538), index_pokemon(539), index_pokemon(620), index_pokemon(286), index_pokemon(454)],  # Elite Four (Fighting Type)
    'Alder': [index_pokemon(617), index_pokemon(626), index_pokemon(621), index_pokemon(584), index_pokemon(589), index_pokemon(637)]  # Champion (Mixed Types)
}


## BW2

unova_bw2 = {
    'Cheren': [index_pokemon(504), index_pokemon(506)],  # Cheren (Normal Type)
    'Roxie': [index_pokemon(109), index_pokemon(544)],  # Roxie (Poison Type)
    'Burgh': [index_pokemon(541), index_pokemon(542), index_pokemon(557)],  # Burgh (Bug Type)
    'Elesa': [index_pokemon(587), index_pokemon(180), index_pokemon(523)],  # Elesa (Electric Type)
    'Clay': [index_pokemon(552), index_pokemon(28), index_pokemon(530)],  # Clay (Ground Type)
    'Skyla': [index_pokemon(581), index_pokemon(528), index_pokemon(227)],  # Skyla (Flying Type)
    'Drayden': [index_pokemon(621), index_pokemon(612), index_pokemon(330)],  # Drayden (Dragon Type)
    'Marlon': [index_pokemon(593), index_pokemon(321), index_pokemon(565)],  # Marlon (Water Type)
    'Shauntal': [index_pokemon(563), index_pokemon(426), index_pokemon(623), index_pokemon(609)],  # Elite Four (Ghost Type)
    'Grimsley': [index_pokemon(560), index_pokemon(510), index_pokemon(553), index_pokemon(625)],  # Elite Four (Dark Type)
    'Caitlin': [index_pokemon(576), index_pokemon(518), index_pokemon(579), index_pokemon(561)],  # Elite Four (Psychic Type)
    'Marshal': [index_pokemon(534), index_pokemon(538), index_pokemon(539), index_pokemon(620)],  # Elite Four (Fighting Type)
    'Iris': [index_pokemon(612), index_pokemon(635), index_pokemon(621), index_pokemon(306), index_pokemon(567), index_pokemon(131)]  # Champion (Dragon and Mixed Types)
}



## Kalos

starter_kalos = [index_pokemon(650), index_pokemon(653), index_pokemon(656)]

kalos = {
    'Viola': [index_pokemon(283), index_pokemon(666)],  # Viola (Bug Type)
    'Grant': [index_pokemon(698), index_pokemon(696)],  # Grant (Rock Type)
    'Korrina': [index_pokemon(619), index_pokemon(67), index_pokemon(701)],  # Korrina (Fighting Type)
    'Ramos': [index_pokemon(189), index_pokemon(70), index_pokemon(673)],  # Ramos (Grass Type)
    'Clemont': [index_pokemon(587), index_pokemon(695), index_pokemon(82)],  # Clemont (Electric Type)
    'Valerie': [index_pokemon(122), index_pokemon(303), index_pokemon(700)],  # Valerie (Fairy Type)
    'Olympia': [index_pokemon(561), index_pokemon(199), index_pokemon(678)],  # Olympia (Psychic Type)
    'Wulfric': [index_pokemon(460), index_pokemon(615), index_pokemon(713)],  # Wulfric (Ice Type)
    'Malva': [index_pokemon(663), index_pokemon(609), index_pokemon(668), index_pokemon(324)],  # Elite Four (Fire Type)
    'Siebold': [index_pokemon(689), index_pokemon(693), index_pokemon(121), index_pokemon(130)],  # Elite Four (Water Type)
    'Wikstrom': [index_pokemon(681), index_pokemon(707), index_pokemon(212), index_pokemon(476)],  # Elite Four (Steel Type)
    'Drasna': [index_pokemon(691), index_pokemon(334), index_pokemon(715), index_pokemon(621)],  # Elite Four (Dragon Type)
    'Diantha': [index_pokemon(701), index_pokemon(699), index_pokemon(706), index_pokemon(697), index_pokemon(711), index_pokemon(282)]  # Champion (Mixed Types)
}

## Alola

starter_alola = [722, 725, 729]

alola = {
    'Ilima': [index_pokemon(235), index_pokemon(735)],  # Ilima (Normal Type)
    'Lana': [index_pokemon(170), index_pokemon(90), index_pokemon(752)],  # Lana (Water Type)
    'Kiawe': [index_pokemon(58), index_pokemon(662), index_pokemon(105, 1)],  # Kiawe (Fire Type)
    'Mallow': [index_pokemon(708), index_pokemon(756), index_pokemon(762)],  # Mallow (Grass Type)
    'Chris': [index_pokemon(777), index_pokemon(738), index_pokemon(76, 1)],  # Sophocles (Electric Type)
    'Acerola': [index_pokemon(92), index_pokemon(778)],  # Acerola (Ghost Type)
    'Mina': [index_pokemon(707), index_pokemon(210), index_pokemon(756), index_pokemon(40), index_pokemon(743)],
    'Kahili': [index_pokemon(51, 1), index_pokemon(423), index_pokemon(330), index_pokemon(750)],  # Kahili (Flying Type)
    'Hapu': [index_pokemon(748), index_pokemon(423), index_pokemon(530), index_pokemon(750)],  # Hapu (Ground Type)
    'Olivia': [index_pokemon(703), index_pokemon(745), index_pokemon(526), index_pokemon(689)],  # Elite Four (Rock Type)
    'Nanu': [index_pokemon(553), index_pokemon(302), index_pokemon(53, 1)],  # Elite Four (Dark Type)
    'Acerola': [index_pokemon(778), index_pokemon(426), index_pokemon(623), index_pokemon(609)],  # Elite Four (Ghost Type)
    'Kukui': [index_pokemon(724), index_pokemon(727), index_pokemon(730), index_pokemon(745), index_pokemon(796), index_pokemon(735)]  # Champion (Mixed Types)
}


## Galar

starter_galar = [811, 814, 818]

galar = {
    'Milo': [index_pokemon(829), index_pokemon(830)],  # Milo (Grass Type)
    'Nessa': [index_pokemon(833), index_pokemon(834), index_pokemon(834)],  # Nessa (Water Type)
    'Kabu': [index_pokemon(850), index_pokemon(851), index_pokemon(837)],  # Kabu (Fire Type)
    'Bea': [index_pokemon(852), index_pokemon(853), index_pokemon(871)],  # Bea (Fighting Type)
    'Allister': [index_pokemon(854), index_pokemon(855), index_pokemon(623)],  # Allister (Ghost Type)
    'Opal': [index_pokemon(861), index_pokemon(862), index_pokemon(869)],  # Opal (Fairy Type)
    'Gordie': [index_pokemon(874), index_pokemon(875), index_pokemon(712)],  # Gordie (Rock Type)
    'Melony': [index_pokemon(875), index_pokemon(713), index_pokemon(871)],  # Melony (Ice Type)
    'Piers': [index_pokemon(863), index_pokemon(862), index_pokemon(865)],  # Piers (Dark Type)
    'Raihan': [index_pokemon(884), index_pokemon(885), index_pokemon(621), index_pokemon(330)],  # Raihan (Dragon Type)
    'Leon': [index_pokemon(809), index_pokemon(851), index_pokemon(889), index_pokemon(815), index_pokemon(809), index_pokemon(812)]  # Champion (Mixed Types)
}


## Paldea

starter_paldea = [822, 825, 829]

paldea = {
    'Katy': [index_pokemon(916), index_pokemon(922), index_pokemon(921)],  # Katy (Bug Type)
    'Brassius': [index_pokemon(941), index_pokemon(947), index_pokemon(941)],  # Brassius (Grass Type)
    'Iono': [index_pokemon(948), index_pokemon(949), index_pokemon(949)],  # Iono (Electric Type)
    'Kofu': [index_pokemon(952), index_pokemon(953), index_pokemon(954)],  # Kofu (Water Type)
    'Larry': [index_pokemon(962), index_pokemon(981), index_pokemon(923)],  # Larry (Normal Type)
    'Ryme': [index_pokemon(944), index_pokemon(945), index_pokemon(946)],  # Ryme (Ghost Type)
    'Tulip': [index_pokemon(966), index_pokemon(967), index_pokemon(968)],  # Tulip (Psychic Type)
    'Grusha': [index_pokemon(971), index_pokemon(972), index_pokemon(973)],  # Grusha (Ice Type)
    'Rika': [index_pokemon(982), index_pokemon(983), index_pokemon(984)],  # Elite Four (Ground Type)
    'Poppy': [index_pokemon(984), index_pokemon(969), index_pokemon(970)],  # Elite Four (Steel Type)
    'Larry': [index_pokemon(931), index_pokemon(932), index_pokemon(934)],  # Elite Four (Flying Type)
    'Hassel': [index_pokemon(990), index_pokemon(991), index_pokemon(992)],  # Elite Four (Dragon Type)
    'Geeta': [index_pokemon(997), index_pokemon(998), index_pokemon(999), index_pokemon(1000), index_pokemon(1001), index_pokemon(1002)]  # Champion (Mixed Types)
}
