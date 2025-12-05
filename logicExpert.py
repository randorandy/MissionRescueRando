from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

#worked on Arion, Base Zero 2, Messadon 2

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    GravitySuit, Varia, Wave, SpeedBooster, Spazer, Ice, Grapple,
    Plasma, Screw, Charge, SpaceJump, Energy, Reserve, Xray, Walljump
) = items_unpackable


energy200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 1
))

energy300 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy)  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy)  >= 14
))


hellrun1 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy200 in loadout)
))
hellrun2 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy300 in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy500 in loadout)
))
hellrun5 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))
hellrun6 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy700 in loadout)
))
hellrun8 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy900 in loadout)
))
hellrun9 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1000 in loadout)
))
hellrun11 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1200 in loadout)
))
hellrun14 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1500 in loadout)
))

missile2 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) >= 2
))
missile5 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) >= 5
))
missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) >= 10
))
missile15 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) >= 15
))
missile20 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) >= 20
))
super2 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) >= 2
))
super3 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) >= 3
))
super4 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) >= 4
))
super6 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) >= 6
))
super10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) >= 10
))
super20 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) >= 20
))
powerBomb2 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 2
))
powerBomb3 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 3
))
powerBomb4 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 4
))
powerBomb10 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 10
))
powerBomb15 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) >= 15
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canHop = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (Bombs in loadout) or
        (Springball in loadout)
    )
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout)
))
hiJumpOr = LogicShortcut(lambda loadout: (
    (HiJump in loadout) or
    (SpaceJump in loadout) or
    (canUseBombs in loadout) or
    (
        (Morph in loadout) and
        (Springball in loadout)
    )
))
dangerousHiJumpOr = LogicShortcut(lambda loadout: (
    (HiJump in loadout) or
    (SpaceJump in loadout) #no IBJ or SBJ
))
doubleHiJumpOr = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) or
    (
        (SpaceJump in loadout) and
        (
            (HiJump in loadout) or
            (Screw in loadout)
        )
    ) or
    (
        (HiJump in loadout) and
        (
            (Morph in loadout) and
            (Springball in loadout)
        )
    )
))
dangerousDoubleHiJumpOr = LogicShortcut(lambda loadout: (
    (SpaceJump in loadout) and
    (
        (HiJump in loadout) or
        (Screw in loadout)
    ) #no IBJ or SBJ
))
highestJump = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) or
    (
        (SpaceJump in loadout) and
        (HiJump in loadout) and
        (Screw in loadout)
    )
))


bgarnowrHint = LogicShortcut(lambda loadout: (
    (GravitySuit in loadout) and
    (canUseBombs in loadout)
))
se26 = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) and 
    (Ice in loadout)
))
se66 = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) and
    (canUsePB in loadout) and
    (Missile in loadout)
))
se4 = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) and
    (Super in loadout)
))
se67 = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) and
    (canUsePB in loadout) and
    (Super in loadout)
))
se13 = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) and
    (
        (se4 in loadout) or #Arion 1 map return
        (se26 in loadout) or #Intended Ice return
        (se66 in loadout) or #SE66 right of ship return
        (bgarnowrHint in loadout) #Return via Bgarnowr hint room
    )
))
ship = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) or
    (hiJumpOr in loadout)
))
se30 = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) and
    (Ice in loadout)
))
centralArion2 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (Ice in loadout) or
        (
            (super2 in loadout) and
            (hiJumpOr in loadout) and
            (canUseBombs in loadout)
        )
    )
))
se32 = LogicShortcut(lambda loadout: (
    (centralArion2 in loadout) and
    (Missile in loadout) and
    (canUseBombs in loadout)
))
arionToWadaria = LogicShortcut(lambda loadout: (
    (se32 in loadout) and
    (hiJumpOr in loadout)
))
upperMessadonToWadaria = LogicShortcut(lambda loadout: (
    (
        (canUseBombs in loadout) and
        (
            (SpeedBooster in loadout) or
            (Walljump in loadout) or
            (
                (Ice in loadout) and
                (Wave in loadout)
            )
        )
    ) or
    (
        (arionToWadaria in loadout) and
        (Super in loadout) and
        (Wave in loadout) and
        (Ice in loadout)
    )
))
se28 = LogicShortcut(lambda loadout: (
    (upperMessadonToWadaria in loadout) and
    (Wave in loadout)
))
se37 = LogicShortcut(lambda loadout: (
    (Wave in loadout) and
    (Missile in loadout) and
    (upperMessadonToWadaria in loadout)
    # or from the other side which needs highestjump
))
se65 = LogicShortcut(lambda loadout: (
    (
        (se13 in loadout) and
        (canUsePB in loadout) and
        (
            (Super in loadout) or
            (Ice in loadout)
        )
    ) or
    (
        (canUsePB in loadout) and
        (Missile in loadout) and
        (ship in loadout) and
        (
            (highestJump in loadout) or
            (Walljump in loadout)
        )
    )
))
bgarnowrWS17top = LogicShortcut(lambda loadout: (
    (se13 in loadout)
))
sporePrize = LogicShortcut(lambda loadout: (
    (   #get there
        (
            (se30 in loadout) and
            (hiJumpOr in loadout) and
            (
                (Missile in loadout) or
                (
                    (Super in loadout) and
                    (HiJump in loadout)
                )
            )
        )
    ) and
    ( #get back
        (
            (Wave in loadout) and
            (se30 in loadout)
        ) or
        (
            (Super in loadout) and
            (Varia in loadout) and
            (canUseBombs in loadout)
        )
    )
))
earlyIce = LogicShortcut(lambda loadout: (
    (se13 in loadout) and 
    (canUseBombs in loadout) and
    (Missile in loadout) and
    (
        (Ice in loadout) or  #Intended Return
        (GravitySuit in loadout) or #Bgarnowr Hint Room Return
        (Charge in loadout) #Base Zero Hint Room Return
    )
))

chaudBayHint = LogicShortcut(lambda loadout: (
    (Varia in loadout)
))
chaudBayHintLeft = LogicShortcut(lambda loadout: (
    (
        (Varia in loadout) and
        (Morph in loadout) and
        (Wave in loadout)
    )
    #or SE43
    #or another way
))

messadonHint = LogicShortcut(lambda loadout: (
    (Varia in loadout) and
    (hiJumpOr in loadout) and
    (Morph in loadout)
))
wadariaHint = LogicShortcut(lambda loadout: (
    (hiJumpOr in loadout) and
    (Wave in loadout)
))
baseZeroHint = LogicShortcut(lambda loadout: (
    (hiJumpOr in loadout) and
    (Morph in loadout) and
    (Charge in loadout)
))
baseZero2topElevator = LogicShortcut(lambda loadout: (
    (
        (
            (baseZeroHint in loadout) and
            (Missile in loadout)
        ) or
        (bgarnowrHint in loadout) or
        (
            (se26 in loadout) and
            (Missile in loadout)
        )
    )
))
baseZero2hub = LogicShortcut(lambda loadout: (
    (
        (baseZeroHint in loadout) and
        (canUseBombs in loadout)
    ) or
    (
        (baseZero2topElevator in loadout) and
        (Missile in loadout) and
        (canUseBombs in loadout)
    )
))


earlyBase0 = LogicShortcut(lambda loadout: (
    ( #from early arion
        (se13 in loadout) and
        (Missile in loadout) and
        (Ice in loadout)
    ) or
    ( #from prize room
        (Charge in loadout) and
        (Morph in loadout) and
        (hiJumpOr in loadout)
    )
))
earlyBase02 = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) and
    (
        ( #from early arion
            (se13 in loadout) and
            (Missile in loadout) and
            (Ice in loadout)
        ) or
        ( #from hint room
            (Charge in loadout) and
            (hiJumpOr in loadout)
        )
    )
))
phantoon = LogicShortcut(lambda loadout: (
    (earlyBase02 in loadout) and
    (Walljump in loadout) and
    (Super in loadout) and
    (
        (SpeedBooster in loadout) or
        (
            (Wave in loadout) and
            (Grapple in loadout)
        )
    )
))
arion3TopRight = LogicShortcut(lambda loadout: (
    #use this to get over the wall
    (
        (hiJumpOr in loadout) or
        (canUseBombs in loadout)
    ) and
    (Missile in loadout) and
    (
        (Walljump in loadout) or
        (canUseBombs in loadout) or
        (
            (HiJump in loadout) and
            (SpaceJump in loadout) and
            (Screw in loadout)
        )
    )
))
messadonDiagonal = LogicShortcut(lambda loadout: (
    #when you can get to the Messadon1-Arion elevator
    #and take the "diagonal" path down to Kraid
    #and leave somehow
    #maybe thinking of this as a diagonal is wrong, since a lot of it is
    #accessible from below but not the stuff above it
    (hiJumpOr in loadout) and 
    (
        (earlyIce in loadout) and
        (Varia in loadout) and
        
        (
            (Reserve in loadout) or
            (
                (missile20 in loadout) and
                (super3 in loadout)
            )
        )
        #think about entring messadonDiagonal from Messadon GT
        #and leaving through wave-locked Messadon 3 top route
    )
))

easyChaudFix = LogicShortcut(lambda loadout: (
    (phantoon in loadout) and
    (SpeedBooster in loadout) and
    (Varia in loadout) and
    (Wave in loadout)
))
easyMahaganFix = LogicShortcut(lambda loadout: (
    (messadonDiagonal in loadout) and
    (HiJump in loadout) and
    (SpaceJump in loadout) and
    (Ice in loadout) and
    (Wave in loadout)
))
wadariaEntry = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) and
    (Missile in loadout) and
    (hiJumpOr in loadout) and
    (
        (super2 in loadout) or
        (Ice in loadout)
    )
))
easyWadariaFix = LogicShortcut(lambda loadout: (
    (se13 in loadout) and
    (Ice in loadout) and
    (Super in loadout) and
    (doubleHiJumpOr in loadout)
))
upperWadaria2 = LogicShortcut(lambda loadout: (
    (wadariaEntry in loadout) and
    (Wave in loadout)
))
wadaria3 = LogicShortcut(lambda loadout: (
    (
        (upperWadaria2 in loadout) and
        (energy900 in loadout) and
        (Plasma in loadout) and
        (canUsePB in loadout)
    ) or
    (
        (easyWadariaFix in loadout) and
        (Reserve in loadout) and
        (Screw in loadout)
    )
    
))

allProgression = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout) and
    (Varia in loadout) and
    (GravitySuit in loadout) and
    (Springball in loadout) and
    (Screw in loadout) and
    (SpaceJump in loadout) and
    (SpeedBooster in loadout) and
    (HiJump in loadout) and
    (Charge in loadout) and
    (Ice in loadout) and
    (Wave in loadout) and
    (Spazer in loadout) and
    (Plasma in loadout) and
    (missile10 in loadout) and
    (super10 in loadout) and
    (powerBomb4 in loadout) and
    (Grapple in loadout) and
    (Xray in loadout) and
    (energy400 in loadout) and
    (Reserve in loadout) and
    (Walljump in loadout)
))

area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            (allProgression in loadout)
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            (allProgression in loadout)
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            (allProgression in loadout)
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            (allProgression in loadout)
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


location_logic: LocationLogicType = {
    "Arion 1 Left of Ship Missile 300": lambda loadout: (
        (
            (ship in loadout) and
            (Super in loadout) and 
            (Morph in loadout) and
            (Ice in loadout) and
            (
                (hiJumpOr in loadout) or
                (
                    (HiJump in loadout) and
                    (Springball in loadout)
                )
            )
        )
    ),
    "Arion 1 Left of Ship Super Missile 551": lambda loadout: (
        (ship in loadout) and
        (Super in loadout) and
        (Morph in loadout)
    ),
    "Arion 1 Spacejumplock Super Missile 288": lambda loadout: (
        (Super in loadout) and
        (doubleHiJumpOr in loadout)
    ),
    "Arion 1 Spacejumplock Missile 345": lambda loadout: (
        (Super in loadout) and
        (doubleHiJumpOr in loadout)
    ),
    "Arion 1 by SE66 Missile 344": lambda loadout: (
        (se13 in loadout)
    ),
    "Arion 1 Triple Top Left Missile 1585": lambda loadout: (
        (se13 in loadout) and
        (
            (
                (Ice in loadout) and
                (canUseBombs in loadout) and
                (
                    (canUsePB in loadout) or
                    (Walljump in loadout) or
                    (doubleHiJumpOr in loadout)
                )
            ) or
            (
                (Super in loadout) and
                (
                    (Walljump in loadout) or
                    (Ice in loadout) or
                    (doubleHiJumpOr in loadout)
                ) 
            )
        )
    ),
    "Arion 1 Triple Top Right Missile 1584": lambda loadout: (
        (se13 in loadout) and
        (
            (
                (Ice in loadout) and
                (
                    (canUsePB in loadout) or
                    (Walljump in loadout) or
                    (doubleHiJumpOr in loadout)
                )
            ) or
            (
                (Super in loadout) and
                (canUseBombs in loadout) and
                (
                    (Walljump in loadout) or
                    (Ice in loadout) or
                    (doubleHiJumpOr in loadout)
                ) 
            )
        )
    ),
    "Arion 1 John McClain Broken Glass Super Missile 70": lambda loadout: (
        (se13 in loadout) and
        (Plasma in loadout) and
        (energy400 in loadout)
    ),
    "Arion 1 Triple Bottom Left Missile 1583": lambda loadout: (
        (se13 in loadout) and
        (
            (
                (Ice in loadout) and
                (
                    (canUsePB in loadout) or
                    (Walljump in loadout) or
                    (doubleHiJumpOr in loadout)
                )
            ) or
            (
                (Super in loadout) and
                (canUseBombs in loadout) and
                (
                    (Walljump in loadout) or
                    (Ice in loadout) or
                    (doubleHiJumpOr in loadout)
                ) 
            )
        )
    ),
    "Arion 1 Below Triple Missile 1582": lambda loadout: (
        (se13 in loadout) and
        (
            (
                (Ice in loadout) and
                (canUseBombs in loadout) and
                (
                    (canUsePB in loadout) or
                    (Walljump in loadout) or
                    (doubleHiJumpOr in loadout)
                )
            ) or
            (
                (Super in loadout) and
                (
                    (Walljump in loadout) or
                    (Ice in loadout) or
                    (doubleHiJumpOr in loadout)
                ) 
            )
        )
        
    ),
    "Arion 1 Below SE13 Power Bomb 89": lambda loadout: (
        (se13 in loadout) and
        (Super in loadout) and
        (Screw in loadout) and
        (SpeedBooster in loadout)
    ),
    "Arion 1 Left Shaft Missile 1586": lambda loadout: (
        ( 
            (se13 in loadout) and
            (Super in loadout) and
            (
                (HiJump in loadout) or
                (SpaceJump in loadout) or
                (
                    (canUseBombs in loadout) and
                    (canUsePB in loadout) and
                    (Missile in loadout)
                )
            ) and
            (
                (Walljump in loadout) or
                (dangerousHiJumpOr in loadout)
            )
        ) or
            (
                (Missile in loadout) and
                (canUseBombs in loadout) and
                (canUsePB in loadout)
            )

    ),
    "Arion 1 Beside Pair Missile 1587": lambda loadout: (
        (
            (se13 in loadout) and
            (Super in loadout) and
            (
                (HiJump in loadout) or
                (SpaceJump in loadout)
            )
        ) or
        (se65 in loadout)
    ),
    "Arion 1 Pair Missile L 1588": lambda loadout: (
        ( 
            (se13 in loadout) and
            (Super in loadout) and
            (
                (HiJump in loadout) or
                (SpaceJump in loadout) or
                (
                    (canUseBombs in loadout) and
                    (canUsePB in loadout) and
                    (Missile in loadout)
                )
            ) and
            (
                (Walljump in loadout) or
                (dangerousHiJumpOr in loadout)
            )
        ) or
        (se65 in loadout)
    ),
    "Arion 1 Pair Missile R 1589": lambda loadout: (
        ( 
            (se13 in loadout) and
            (Super in loadout) and
            (
                (HiJump in loadout) or
                (SpaceJump in loadout) or
                (
                    (canUseBombs in loadout) and
                    (canUsePB in loadout) and
                    (Missile in loadout)
                )
            ) and
            (
                (Walljump in loadout) or
                (dangerousHiJumpOr in loadout)
            )
        ) or
        (se65 in loadout)
    ),
    "Arion 1 Alpha Ridley Power Bomb 99": lambda loadout: (
        (allProgression in loadout)
        # could be calculated better for arion ridley
    ),
    "Arion 1 Bottom Right Missile 334": lambda loadout: (
        (
            #central arion 2 route
            (centralArion2 in loadout) and
            (Ice in loadout) and
            (missile10 in loadout) and
            (Super in loadout)
        ) or
        (
            #SE16 route
            (Missile in loadout) and
            (canUseBombs in loadout) and
            (powerBomb4 in loadout) and #really it's 3 pb
            (SpeedBooster in loadout) and
            (Energy in loadout) #maybe more energy
        )
    ),
    "Arion 1 Elevator to Messadon Missile 55": lambda loadout: (
        (
            (canUseBombs in loadout) and
            (canUsePB in loadout) and
            (Super in loadout)
        ) or
        (messadonDiagonal in loadout)
    ),
    "Arion 1 From SE39 Super Missile 80": lambda loadout: (
        (se65 in loadout) and
        (Wave in loadout) and
        (canUsePB in loadout) and
        (canUseBombs in loadout)
    ),
    "Arion 1 Bottom Right Super Missile 269": lambda loadout: (
        #Defeat BT for SE16 route
        (Missile in loadout) and
        (canUseBombs in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ),
    "Arion 2 Right of Ship Missile 1271": lambda loadout: (
        (Morph in loadout) and 
        (Missile in loadout) and 
        (
            (ship in loadout) or
            (se65 in loadout)
        )
    ),
    "Arion 2 from SE12 Super Missile 67": lambda loadout: (
        (se13 in loadout) and
        (doubleHiJumpOr in loadout) and
        (Wave in loadout)
    ),
     "Arion 2 by SE67 Missile 322": lambda loadout: (
        (
            (centralArion2 in loadout) and
            (SpeedBooster in loadout) and
            (powerBomb4 in loadout)
        ) or
        (se67 in loadout)

    ),
    "Arion 2 Below SE67 Missile 346": lambda loadout: (
        (
            (
                (centralArion2 in loadout) and
                (SpeedBooster in loadout)
            ) or
            (
                (se67 in loadout) and
                (powerBomb4 in loadout)
            )
        ) and
        (hiJumpOr in loadout) and
        (
            (Plasma in loadout) or
            (canUseBombs in loadout) or
            (canUsePB in loadout)
        )
    ),
    "Arion 2 Left Middle Lower Missile 323": lambda loadout: (
        (centralArion2 in loadout) and
        (Morph in loadout) and 
        (Missile in loadout) and
        (hiJumpOr in loadout)
    ),
    "Arion 2 at SE32 Missile 47": lambda loadout: (
        (centralArion2 in loadout) and 
        (Missile in loadout) and
        (canHop in loadout) and
        (
            (hiJumpOr in loadout) or
            (SpeedBooster in loadout)
        )
    ),
    "Arion 2 Central Super Missile 74": lambda loadout: (
        (centralArion2 in loadout) and
        (Super in loadout) and
        (canUseBombs in loadout)   
    ),
    "Arion 2 Ripper Missile 43": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Arion 2 Beetom Behind Missile 1591": lambda loadout: ( 
        (
            (canUseBombs in loadout) and
            (super2 in loadout)
        ) or
        (
            (Morph in loadout) and
            (Ice in loadout) and
            (hiJumpOr in loadout) and
            (Super in loadout) and
            (
                (Energy in loadout) or
                (
                    (Plasma in loadout) or
                    (Spazer in loadout) or
                    (Screw in loadout) or
                    (GravitySuit in loadout)
                )
            )    
        )
    ),
    "Arion 2 Beetom Ceiling Missile 1592": lambda loadout: (
        (
            (canUseBombs in loadout) and
            (Ice in loadout)
        ) or
        (
            (canHop in loadout) and
            (Ice in loadout) and
            (hiJumpOr in loadout) and
            (super2 in loadout) and
            (
                (Energy in loadout) or
                (
                    (Plasma in loadout) or
                    (Spazer in loadout) or
                    (Screw in loadout) or
                    (GravitySuit in loadout)
                )
            )    
        )
    ),
    "Arion 2 Below Beetom Chozo Missile 1590": lambda loadout: (
        (
            (super4 in loadout) and 
            (canUseBombs in loadout)
        ) or
        (
            (Morph in loadout) and
            (Ice in loadout) and
            (Super in loadout) and
            (hiJumpOr in loadout) and
            (
                (Energy in loadout) or
                (
                    (Plasma in loadout) or
                    (Spazer in loadout) or
                    (Screw in loadout) or
                    (Varia in loadout) or
                    (GravitySuit in loadout)
                )
            )   
        )
    ),
    "Arion 2 Below Beetom Left Super Missile 293": lambda loadout: (
        (SpeedBooster in loadout) and
        (
            (
                (hiJumpOr in loadout) or
                (Ice in loadout)
            )
        ) and
        (
            (
                (canUseBombs in loadout) and
                (super3 in loadout)
            ) or
            (
                (Morph in loadout) and
                (centralArion2 in loadout) and 
                (Super in loadout) and
                (hiJumpOr in loadout)
            ) or
            (
                (powerBomb4 in loadout) and
                (Energy in loadout)
            )
        )
    ),
    "Arion 2 Below Beetom Right Super Missile 294": lambda loadout: (
        (
            (hiJumpOr in loadout) or
            (Ice in loadout)
        ) and
        (
            (
                (canUseBombs in loadout) and
                (super3 in loadout)
            ) or
            (
                (Morph in loadout) and
                (centralArion2 in loadout) and 
                (Super in loadout) 
            )
        )
    ),
    "Arion 3 from SE66 Missile 320": lambda loadout: (
        (se13 in loadout) and
        (canUsePB in loadout)
    ),
    "Arion 3 Top Right Missile 1571": lambda loadout: (
        (se65 in loadout) and
        (Charge in loadout)
    ),
    "Arion 3 Gravitylocked Missile 321": lambda loadout: (
        (se65 in loadout) and
        (GravitySuit in loadout)
    ),
    "Arion 3 Bomb Entry Missile 37": lambda loadout: (
        (Morph in loadout)
    ),
    "Arion 3 Hidden BT Missile 335": lambda loadout: (
        (Morph in loadout) and
        (Bombs in loadout) and #BT required, also coincidentally bombs
        (Missile in loadout) #required for BT eye door
    ),
    "Arion 3 by SE19 Super Missile 69": lambda loadout: (
        (canUsePB in loadout) and
        (
            (Ice in loadout) or
            (
                (canUseBombs in loadout) and
                (super2 in loadout)
            ) or
            (highestJump in loadout)
        )
    ),
    "Arion 3 BT Power Bomb 108": lambda loadout: (
        (canUseBombs in loadout) and #bomb door
        (canUsePB in loadout)
    ),
    "Arion 3 HiJump 53": lambda loadout: (
        (canUseBombs in loadout) and
        (Ice in loadout) and
        (Missile in loadout)
    ),
    "Arion 3 BT Bottom Missile 336": lambda loadout: (
        (canHop in loadout) and
        (Ice in loadout) and
        (Missile in loadout) and
        (
            (Energy in loadout) or
            (Plasma in loadout) or
            (Spazer in loadout) or
            (Varia in loadout) or
            (GravitySuit in loadout)
        )
    ),
    "Arion 3 Bombs 7": lambda loadout: (
        (Morph in loadout) and
        (Missile in loadout)
    ),
    "Arion 3 Bomb Torizo Energy Tank 2114": lambda loadout: (
        (Morph in loadout) and
        (Missile in loadout)
    ),
    "Base0-1 by SE61 Missile": lambda loadout: (
        (phantoon in loadout) and
        (Charge in loadout)
    ),
    "Base0-1 Left Side Super Missile": lambda loadout: (
        (phantoon in loadout) and
        (
            (Screw in loadout) or
            (
                (Charge in loadout) and
                (Ice in loadout)
            )
        ) and
        (SpeedBooster in loadout)
    ),
    "Base0-1 Far Right Missile": lambda loadout: (
        (earlyBase02 in loadout) and
        (canUseBombs in loadout) and
        (Spazer in loadout)
    ),
    "Base0-1 Power Bomb": lambda loadout: (
        (phantoon in loadout) and
        (Charge in loadout) and
        (Ice in loadout) and
        (Spazer in loadout) #check pb?
    ),
    "Base0-1 Right Side Super Missile": lambda loadout: (
        (earlyBase02 in loadout) and
        (canUsePB in loadout) and
        (Walljump in loadout)
    ),
    "Base0-1 Gravity Suit": lambda loadout: (
        (phantoon in loadout) and
        (Charge in loadout) and
        (Ice in loadout) and
        (Spazer in loadout) #check pb?
    ),
    "Base0-1 Bottom Right Missile": lambda loadout: (
        (phantoon in loadout) and
        (Charge in loadout) and
        (Ice in loadout) and
        (Spazer in loadout) and
        (Screw in loadout) #pb?
    ),
    "Base0-2 Entry Hallway Power Bomb": lambda loadout: (
        (baseZero2hub in loadout) and
        (canUseBombs in loadout) and
        (powerBomb4 in loadout)
    ),
    "Base0-2 Entry Energy Tank": lambda loadout: (
        (baseZero2topElevator in loadout) and
        (
            (
                (Grapple in loadout) and
                (Super in loadout)
            ) or
            (super4 in loadout) or 
            (highestJump in loadout)
        )
    ),
    "Base0-2 Hallway Central Missile": lambda loadout: (
        (baseZero2hub in loadout) and
        (canUseBombs in loadout) and
        (
            (SpeedBooster in loadout) or
            (
                (Walljump in loadout) and
                (Screw in loadout) and
                (Super in loadout)
            )
            # TODO or a superless option from the lower right
        ) 
    ),
    "Base0-2 Left Hallway Missile": lambda loadout: (
        (baseZero2hub in loadout) and
        (SpeedBooster in loadout) and
        (canUseBombs in loadout)
    ),
    "Base0-2 Map Missile": lambda loadout: (
        (phantoon in loadout) #ws powered on only
    ),
    "Base0-2 by SE23 Missile": lambda loadout: (
        (baseZero2hub in loadout) and
        (SpeedBooster in loadout) and
        (canUseBombs in loadout)
    ),
    "Base0-2 by SE18/23/59/78 Missile": lambda loadout: (
        (baseZero2hub in loadout) and
        (canUseBombs in loadout) and
        (Plasma in loadout)
    ),
    "Base0-2 Speed Booster": lambda loadout: (
        (phantoon in loadout) and
        (
            (Grapple in loadout) or
            (GravitySuit in loadout)
        )
    ),
    "Base0-2 Bottom Right Super Missile": lambda loadout: (
        # Torizo locked
        (phantoon in loadout) and
        (Charge in loadout) and
        (Ice in loadout) and
        (Spazer in loadout) #pb to torizo?
    ),
    "Base0-3 Boss Missile": lambda loadout: (
        (phantoon in loadout)
    ),
    "Base0-3 After Map Missile": lambda loadout: (
        (phantoon in loadout) and
        (SpeedBooster in loadout)
    ),
    "Base0-3 Bottom Missile": lambda loadout: (
        (phantoon in loadout) and
        (Wave in loadout)
    ),
    "Base0-3 Bottom Super Missile": lambda loadout: (
        (phantoon in loadout) and
        (Wave in loadout) and
        (SpeedBooster in loadout)
    ),
    "Base0-3 Bottom Energy Tank": lambda loadout: (
        (phantoon in loadout) and
        (SpeedBooster in loadout) and
        (Ice in loadout) and
        (Super in loadout) and
        (Wave in loadout) #wave-or-grapple to return from base0-3?
    ),
    "Bgarnowr 1 Springball": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Ice in loadout) and
        (Grapple in loadout) and
        (Wave in loadout) and
        (Walljump in loadout) and
        (SpeedBooster in loadout) and
        (Missile in loadout) and
        (super20 in loadout) and
        (Spazer in loadout) #more?
    ),
    "Bgarnowr 1 Top Left Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Spazer in loadout) and
        (Grapple in loadout) #maybe?
    ),
    "Bgarnowr 1 by Springball Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Ice in loadout) and
        (Grapple in loadout) and
        (SpeedBooster in loadout) and
        (Springball in loadout) and 
        (Spazer in loadout) #maybe?
    ),
    "Bgarnowr 1 Below Springball Super Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (SpeedBooster in loadout) and
        (Springball in loadout)
    ),
    "Bgarnowr 1 by SE75 Power Bomb": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (canUsePB in loadout) and
        (Grapple in loadout) 
    ),
    "Bgarnowr 1 Right Side Torizolock Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (Wave in loadout) and
        (Springball in loadout) and
        (Spazer in loadout)
    ),
    "Bgarnowr 1 by SE21 Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Spazer in loadout) and
        (Grapple in loadout) 
    ),
    "Bgarnowr 1 by SE69 Super Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (missile5 in loadout) and
        (Spazer in loadout) and
        (SpeedBooster in loadout)
    ),
    "Bgarnowr 1 Bottom Left Super Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Spazer in loadout) and
        (Grapple in loadout) 
    ),
    "Bgarnowr 1 Spazer": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Spazer in loadout) and
        (Grapple in loadout) and
        (Wave in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ),
    "Bgarnowr 1 by SE63 Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) 
    ),
    "Bgarnowr 2 Top Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (SpaceJump in loadout) and
        (Screw in loadout)
    ),
    "Bgarnowr 2 Top Right Super Missile": lambda loadout: (
        #mama turtle super
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Ice in loadout) and
        (Grapple in loadout) and
        (missile5 in loadout) and
        (SpeedBooster in loadout) #idk
    ),
    "Bgarnowr 2 Top Right Power Bomb": lambda loadout: (
        #mama turtle
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Ice in loadout) and
        (Grapple in loadout) and
        (missile5 in loadout) #maybe
    ),
    "Bgarnowr 2 by SE63 Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (Screw in loadout)
    ),
    "Bgarnowr 2 Grapplelocked Super Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (Grapple in loadout)
    ),
    "Bgarnowr 2 Above Center Right Super Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (Spazer in loadout) and
        (canUsePB in loadout)
    ),
    "Bgarnowr 2 Left Side Powerbomblocked Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (powerBomb4 in loadout) and
        (SpeedBooster in loadout) and
        (Springball in loadout) and
        (Ice in loadout) 
    ),
    "Bgarnowr 2 Central Power Bomb": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (Spazer in loadout) and 
        (Wave in loadout) and
        (canUsePB in loadout)
    ),
    "Bgarnowr 2 Below Center Right Super Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (Grapple in loadout)
    ),
    "Bgarnowr 2 Central Super Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (Spazer in loadout) and 
        (Wave in loadout)
    ),
    "Bgarnowr 2 Bottom Left Super Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Spazer in loadout) and
        (Grapple in loadout) and
        (Wave in loadout) and
        (SpeedBooster in loadout)
    ),
    "Bgarnowr 2 Bottom Left Pair Left Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Spazer in loadout) and
        (Grapple in loadout) and
        (Wave in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ),
    "Bgarnowr 2 Bottom Left Pair Right Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Spazer in loadout) and
        (Grapple in loadout) and
        (Wave in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout)
    ),
    "Bgarnowr 2 Bottom Right Super Missile": lambda loadout: (
        (earlyBase0 in loadout) and
        (Spazer in loadout) and
        (GravitySuit in loadout) and
        (Wave in loadout) #more?
    ),

    "Bgarnowr 3 Bottom Left Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (canUsePB in loadout)
        #grav?
    ),
    
    "Bgarnowr 3 Top Power Bomb": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (SpeedBooster in loadout) and
        (GravitySuit in loadout) and
        (Spazer in loadout) and
        (Missile in loadout)
    ),
    
    "Bgarnowr 3 Plasma Beam": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (Wave in loadout) and
        (Plasma in loadout)
    ),
    "Bgarnowr 3 from SE22 Super Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (
            (canUsePB in loadout) or
            (
                (Spazer in loadout) and
                (GravitySuit in loadout) #??
            )
        )
        #is this expecting Bg GT? SE68 logic is...
    ),
    "Bgarnowr 3 Bottom Plasmalock Power Bomb": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (Spazer in loadout) and
        (Ice in loadout) and
        (Plasma in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (hiJumpOr in loadout) and
        (canUsePB in loadout) #idk
    ),
    "Bgarnowr 3 Central Power Bomb": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Wave in loadout) and
        (canUsePB in loadout) and
        (Grapple in loadout) #eh
    ),
    "Bgarnowr 3 Central Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Spazer in loadout) and
        (Super in loadout) and
        (canUsePB in loadout) and
        (Grapple in loadout) #huh
    ),
    "Bgarnowr 3 Top Pair Left Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (Wave in loadout) and
        (
            (Ice in loadout) or
            (HiJump in loadout) or
            (GravitySuit in loadout)
        )
    ),
    "Bgarnowr 3 Top Pair Right Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (Wave in loadout) and
        (
            (Ice in loadout) or
            (HiJump in loadout) or
            (GravitySuit in loadout)
        )

    ),
    "Bgarnowr 3 Walljumplock Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (Wave in loadout) and
        (Walljump in loadout)
    ),
    "Bgarnowr 3 Grapplelocked Cave Missile": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) 
    ),
    "Bgarnowr 3 Secret Fish Energy Tank": lambda loadout: (
        (bgarnowrWS17top in loadout) and
        (GravitySuit in loadout) and
        (Grapple in loadout) and
        (SpeedBooster in loadout) and
        (Wave in loadout)
    ),

    "Chaud Bay 1 Charge Beam": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 Left Center Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 3 Near Varia Lava Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 Killem Right Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 by SE74 Missile": lambda loadout: (
        (Varia in loadout) and
        (Screw in loadout)
        #or from the left without screw
    ),
    "Chaud Bay 1 Left Center Super Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 1 Bottom Left Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 Metroid Maze Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 Croc Super Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 3 Top Xraylocked Super Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 1 Top Left Super Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 3 Top Right Power Bomb": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 Center Power Bomb": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 Lost Caves Super Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 Speedballlocked Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 Wavelocked Super Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 Above Ridley Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 Bottom Reserve Tank": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 at SE71 Super Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 Bottom Right Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 Below Ridley Super Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 Bottom Right Power Bomb": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 Elevator Lava Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 by SE43 Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 3 Croc Maze Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 Top Left Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 Left Side Power Bomb": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 3 Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 3 Varia Suit": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 2 By Base0-3 Elevator Power Bomb": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 1 Chargelocked Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 1 Top Right Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 Bottom Reserve Tank": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 with Reserve Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 Screw Attack": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 Misdirection Copy PLM Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud bay 4 Bottom Right Energy Tank": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 4 Lost Caves Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 1 Xray": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 1 Below Xray Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Chaud Bay 1 Bottom Right Missile": lambda loadout: (
        (easyChaudFix in loadout)
    ),
    "Mahagan 1 Walljump Boots": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 1 Below Walljump Speedballlock Energy Tank": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 1 Highest Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 2 Speed-Chargelock Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 3 Below Speedballlock Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 3 Speedballlock Super Missile": lambda loadout: (
        (easyMahaganFix in loadout) and
        (SpeedBooster in loadout)
    ),
    "Mahagan 1 Right Chargeway Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 1 Lower Left Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 1 Prize Room Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 1 Leftmost Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 3 Elevator Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 3 Nearest Elevator Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 2 Bottom Right Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 2 Top Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 3 Bottom Right Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 2 Ridley Speedballlock Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 1 Prize Room Energy Tank": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 1 Wave Beam": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 1 by Wave Beam Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 2 Bottom Left Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 2 First Torizolock Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 3 Left Section Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 3 Left Section Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 2 Top Right Power Bomb": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 2 Second Torizolock Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 1 Lower Split Top Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 1 Lower Split Bottom Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 3 Top Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 3 Speedlocked Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 3 Door Open Super Missile": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Mahagan 2 Prize Room Power Bomb": lambda loadout: (
        (easyMahaganFix in loadout)
    ),
    "Messadon 1 Top Right Back Missile 1596": lambda loadout: (
        (canUseBombs in loadout) and
        (hiJumpOr in loadout) and
        (Missile in loadout) and
        (Reserve in loadout) and
        (Wave in loadout) #or from SE42, SE28+Wave
    ),
    "Messadon 1 Top Right Front Missile 1597": lambda loadout: (
        (canUseBombs in loadout) and
        (hiJumpOr in loadout) and
        (Missile in loadout) and
        (Reserve in loadout) and
        (
            (Wave in loadout) or
            (Varia in loadout) #ways to escape Spo spo prize room?
        ) #or SE42, SE28+Wave
    ),
    "Messadon 1 by Arion 2 Super Missile 297": lambda loadout: (
        (canUseBombs in loadout) and
        (Ice in loadout) and
        (hiJumpOr in loadout) and
        (Wave in loadout)
    ),
    "Messadon 1 Tall Tower Missile 1599": lambda loadout: (
        (messadonDiagonal in loadout) and
        (Super in loadout)
    ),
    "Messadon 1 by SE72 Missile 1595": lambda loadout: (
        (earlyIce in loadout) and
        (hiJumpOr in loadout) and
        (Super in loadout)
    ),
    "Messadon 1 by SE42 Missile 57": lambda loadout: (
        (sporePrize in loadout) and
        (Super in loadout)
    ),
    "Messadon 1 Central Super Missile 81": lambda loadout: (
        (messadonDiagonal in loadout) and
        (Charge in loadout) and
        (Ice in loadout)
    ),
    "Messadon 1 Ice Energy Tank 19": lambda loadout: (
        (earlyIce in loadout)
    ),
    "Messadon 1 Entry Icelocked Missile 41": lambda loadout: (
        (earlyIce in loadout) and
        (Ice in loadout)
    ),
    "Messadon 1 Ice Beam 50": lambda loadout: (
        (earlyIce in loadout) and
        (Ice in loadout) #escape the room
    ),
    "Messadon 1 Elevator to Chaud Bay Hidden Missile 1617": lambda loadout: (
        (messadonDiagonal in loadout) and
        (Reserve in loadout) and
        (Ice in loadout) and
        (HiJump in loadout) and
        (SpaceJump in loadout)
    ),
    "Messadon 1 Bottom Right Killall Super Missile 83": lambda loadout: (
        (messadonDiagonal in loadout) and
        (Reserve in loadout) and
        (Ice in loadout)
    ),
    "Messadon 1 Elevator to Chaud Bay Chozo Missile 1616": lambda loadout: (
        (messadonDiagonal in loadout) and
        (Reserve in loadout) and
        (Ice in loadout) and
        (HiJump in loadout) and
        (SpaceJump in loadout)
    ),
    "Messadon 1 Bottom Right Super Missile 553": lambda loadout: (
        (messadonDiagonal in loadout) and
        (Reserve in loadout) and
        (Ice in loadout)
    ),
    "Messadon 2 Morph Ball 26": lambda loadout: (
        (Morph in loadout) and
        (Missile in loadout)
    ),
    "Messadon 2 Outside Alpha Missile 30": lambda loadout: (
        (canUseBombs in loadout) and
        (Super in loadout)
    ),
    "Messadon 2 Alpha Missile 1 33": lambda loadout: (
        True
    ),
    "Messadon 2 Alpha Missile 2 31": lambda loadout: (
        True
    ),
    "Messadon 2 Alpha Missile 3 32": lambda loadout: (
        True
    ),
    "Messadon 2 Below Retro Top Missile 1598": lambda loadout: (
        (canUsePB in loadout) and
        (
            (
                (SpeedBooster in loadout) and
                (
                    (Energy in loadout) or
                    (Grapple in loadout) or
                    (SpaceJump in loadout)
                ) and
                (
                    (Missile in loadout) or
                    (Super in loadout) or
                    (Wave in loadout)
                )
            ) or
            (
                (se30 in loadout) and
                (Springball in loadout) and
                (HiJump in loadout) and
                (canUsePB in loadout)
            )
        )
        
    ),
    "Messadon 2 Large Below Retro Missile 46": lambda loadout: (
        (
            (
                (SpeedBooster in loadout) and
                (powerBomb3 in loadout) and
                (
                    (Energy in loadout) or
                    (Grapple in loadout) or
                    (SpaceJump in loadout)
                ) and
                (
                    (Missile in loadout) or
                    (Super in loadout) or
                    (Wave in loadout)
                )
            ) or
            (
                (se30 in loadout) and
                (Springball in loadout) and
                (HiJump in loadout)
            )
        )
        
    ),
    "Messadon 2 Above Lootroom Super Missile 75": lambda loadout: (
        (allProgression in loadout) #check
    ),
    "Messadon 2 Large Below Retro Super Missile 76": lambda loadout: (
        (SpeedBooster in loadout) and
        (Springball in loadout) and
        (Super in loadout) and
        (sporePrize in loadout)
        # revamp sporePrize

    ),
    "Messadon 2 by SE30 Missile 1569": lambda loadout: (
        (SpeedBooster in loadout) and
        (
            (se30 in loadout) or
            (
                (SpeedBooster in loadout) and
                (powerBomb3 in loadout) and
                (
                    (Energy in loadout) or
                    (Grapple in loadout) or
                    (SpaceJump in loadout)
                ) and
                (
                    (Missile in loadout) or
                    (Super in loadout) or
                    (Wave in loadout)
                )
                # from 1598
            )
        )
    ),
    "Messadon 2 Spore Spawn Missile 45": lambda loadout: (
        (canUseBombs in loadout) and
        (Ice in loadout) and
        (hiJumpOr in loadout) and
        (missile5 in loadout)
    ),
    "Messadon 2 Outside Spore Missile 44": lambda loadout: (
        (sporePrize in loadout) and
        (canUseBombs in loadout) and
        (super3 in loadout) and
        (dangerousHiJumpOr in loadout) # maybe dangerous double
    ),
    "Messadon 2 Outside Spore Reserve Tank 129": lambda loadout: (
        (sporePrize in loadout) and
        (canUsePB in loadout) and
        (doubleHiJumpOr in loadout)
    ),
    "Messadon 2 Spazerlocked Prize Power Bomb 92": lambda loadout: (
        (sporePrize in loadout) and
        (canUseBombs in loadout) and
        (Spazer in loadout)
    ),
    "Messadon 2 Gravitylocked Missile 337": lambda loadout: (
        (Missile in loadout) and
        (Morph in loadout) and
        (HiJump in loadout) and
        (
            (sporePrize in loadout) and
            (GravitySuit in loadout) and
            (Walljump in loadout)
            # left entry
        ) or
        (
            (canUseBombs in loadout) and
            (Ice in loadout) and
            (missile5 in loadout)
            # defeat spore spawn
        ) or
        (
            (
                (messadonHint in loadout) or
                (se37 in loadout)
            ) and
            (highestJump in loadout)
        )
    ),
    "Messadon 2 Outside Spazerblock Super Missile 292": lambda loadout: (
        #from left-above
        (
            (sporePrize in loadout) and
            (canUseBombs in loadout) and
            (Spazer in loadout) and
            (hiJumpOr in loadout)
        ) or
        (
            (doubleHiJumpOr in loadout) and
            (
                (
                    (messadonHint in loadout) and
                    (canUseBombs in loadout) and
                    (missile2 in loadout) and
                    (Super in loadout)
                ) # or
            ) 
            # or se41 with plasma
            # or se72 with screw
            # maybe more

        )
    ),
    "Messadon 2 Right Side Xraylocked Super Missile 291": lambda loadout: (
        (Xray in loadout) and
        (
            #from left-above
            (
                (sporePrize in loadout) and
                (canUseBombs in loadout) and
                (Spazer in loadout) and
                (doubleHiJumpOr in loadout)
            ) or
            (
                (
                    (messadonHint in loadout) and
                    (canUseBombs in loadout) and
                    (missile2 in loadout) and
                    (Super in loadout)
                ) # or
                # or se41 with plasma
                # or se72 with screw
                # maybe more
            )
        )
    ),
    "Messadon 2 Lower Left Super Missile 552": lambda loadout: (
        (
            (messadonHint in loadout) and
            (Reserve in loadout) and
            (hiJumpOr in loadout)
        ) or
        (
            (se37 in loadout) and
            (highestJump in loadout) and
            (HiJump in loadout) and
            (missile2 in loadout) and
            (Super in loadout) and
            (Reserve in loadout)
        )
        # or from chaud bay elevator
        # or from other messadon locations
    ),
    "Messadon 2 by SE37 Super Missile 82": lambda loadout: (
        (
            (messadonHint in loadout) and
            (hiJumpOr in loadout) and
            (Super in loadout) and
            (missile2 in loadout)
        ) or
        (
            (se37 in loadout) and
            (highestJump in loadout)
        )
    ),
    "Messadon 2 Lower Right Missile 56": lambda loadout: (
        (
            (messadonHint in loadout) and
            (canUseBombs in loadout) and
            (Missile in loadout)
        ) or
        (  
            (se37 in loadout) and
            (highestJump in loadout) and
            (missile2 in loadout) and
            (Super in loadout) and
            (HiJump in loadout)
        )
        # other ways?
    ),
    "Messadon 2 Lower Left Missile 1615": lambda loadout: (
        (
            (messadonHint in loadout) and
            (Reserve in loadout) and
            (hiJumpOr in loadout)
        ) or
        (
            (se37 in loadout) and
            (highestJump in loadout) and
            (HiJump in loadout) and
            (missile2 in loadout) and
            (Super in loadout)
        )
        # or from chaud bay elevator
        # or from other messadon locations
    ),



    "Messadon 3 Grapple Beam 60": lambda loadout: (
        (
            (messadonHint in loadout) or
            (
                (se37 in loadout) and
                (highestJump in loadout) and
                (Wave in loadout) and
                (
                    (missile2 in loadout) or
                    (GravitySuit in loadout)
                )
            )
        ) and
        (canUseBombs in loadout) and
        (doubleHiJumpOr in loadout) and
        (Missile in loadout) and
        (super10 in loadout) and
        (energy500 in loadout)


    ),
    "Messadon 3 Top Left Super Missile 73": lambda loadout: (
        (canUseBombs in loadout) and 
        (SpeedBooster in loadout)
    ),
    
    "Messadon 3 Speedballlocked Missile 1593": lambda loadout: (
        (canUseBombs in loadout) and
        (HiJump in loadout) and
        (SpaceJump in loadout) and
        (SpeedBooster in loadout) and
        (canUsePB in loadout) and
        (Springball in loadout)
        #probably right
    ),
    "Messadon 3 Bottom Left Missile 1570": lambda loadout: (
        #from left-above
        (
            (sporePrize in loadout) and
            (canUseBombs in loadout) and
            (Spazer in loadout) and
            (doubleHiJumpOr in loadout)
        ) or
        (
            (
                (messadonHint in loadout) and
                (canUseBombs in loadout) and
                (missile2 in loadout) and
                (Super in loadout)
            ) # or
            # or se41 with plasma
            # or se72 with screw
            # maybe more
        )
    ),
    "Messadon 3 by SE28 Super Missile 295": lambda loadout: (
        (se28 in loadout)
    ),
    "Messadon 3 Alpha Reserve Tank": lambda loadout: (
        (
            (messadonHint in loadout) and
            (Super in loadout) and
            (hiJumpOr in loadout) and
            (
                (HiJump in loadout) or
                (GravitySuit in loadout)
            )
        ) or
        (
            (se37 in loadout) and
            (highestJump in loadout) and
            (Wave in loadout) and
            (
                (missile2 in loadout) or
                (GravitySuit in loadout)
            )
        )

    ),
    'Messadon 3 "wavelocked" Missile': lambda loadout: (
        (upperMessadonToWadaria in loadout) and
        (
            (Missile in loadout) or
            (Ice in loadout)
        ) and
        (Wave in loadout)
    ),
    "Messadon 3 Grapplelocked Super Missile": lambda loadout: (
        (upperMessadonToWadaria in loadout) and
        (
            (Missile in loadout) or
            (Ice in loadout)
        ) and
        (
            (Grapple in loadout) or
            (
                (SpaceJump in loadout) and
                (Screw in loadout)
            )
        )
    ),
    "Messadon 3 Top Right Missile": lambda loadout: (
        (upperMessadonToWadaria in loadout) and
        (
            (Missile in loadout) or
            (Ice in loadout)
        ) and
        (hiJumpOr in loadout)
    ),
    "Messadon 3 Bottom Right Super Missile": lambda loadout: (
        (allProgression in loadout) #is this GT locked?
    ),
    "Messadon 3 Golden Torizo Super Missile Super Missile": lambda loadout: (
        (
            (messadonHint in loadout) or
            (
                (se37 in loadout) and
                (highestJump in loadout) and
                (Wave in loadout) and
                (
                    (missile2 in loadout) or
                    (GravitySuit in loadout)
                )
            )
        ) and
        (canUseBombs in loadout) and
        (doubleHiJumpOr in loadout) and
        (Missile in loadout) and
        (super10 in loadout) and
        (energy500 in loadout)
    ),
    "Wadaria 2 Custombosslocked Super Missile": lambda loadout: (
        (canUseBombs in loadout) and
        (Super in loadout) and
        (Missile in loadout) and
        (Ice in loadout)
    ),
    "Wadaria 2 Wavelocked Super Missile": lambda loadout: (
        (easyWadariaFix in loadout) and
        (Wave in loadout)
    ),
    "Wadaria 1 Top Left Missile": lambda loadout: (
        (easyWadariaFix in loadout) and
        (super2 in loadout)
    ),
    "Wadaria 3 Split Room Bottom Missile": lambda loadout: (
        (wadaria3 in loadout)
    ),
    "Wadaria 2 Bottom Right Grapplelocked Super Missile": lambda loadout: (
        (upperWadaria2 in loadout)
    ),
    "Wadaria 1 Right Side Missile": lambda loadout: (
        (easyWadariaFix in loadout) and
        (Wave in loadout)
        # I think
    ),
    "Wadaria 1 Warp to Messadon Energy Tank": lambda loadout: (
        (easyWadariaFix in loadout)
    ),
    "Wadaria 1 Left Side Super Missile": lambda loadout: (
        (easyWadariaFix in loadout) and
        (SpeedBooster in loadout)
    ),
    "Wadaria 3 Top Right Screwlocked Super Missile": lambda loadout: (
        (wadaria3 in loadout) and
        (Screw in loadout)
    ),
    "Wadaria 2 Space Jump": lambda loadout: (
        (upperWadaria2 in loadout)
    ),
    "Wadaria 1 Shaft Hidden Missile": lambda loadout: (
        (easyWadariaFix in loadout)
    ),
    "Wadaria 2 by SE33 Missile": lambda loadout: (
        (easyWadariaFix in loadout)
    ),
    "Wadaria 1 Speed Hallway Super Missile": lambda loadout: (
        (easyWadariaFix in loadout)
    ),
    "Wadaria 3 Farthest Right Missile": lambda loadout: (
        (wadaria3 in loadout)
    ),
    "Wadaria 2 Farthest Bottom Right Super Missile": lambda loadout: (
        (easyWadariaFix in loadout) and
        (Xray in loadout) and
        (missile2 in loadout)
        #more?
    ),
    "Wadaria 2 Alpha Top Super Missile": lambda loadout: (
        (easyWadariaFix in loadout)
    ),
    "Wadaria 2 Alpha Bottom Super Missile": lambda loadout: (
        (easyWadariaFix in loadout)
    ),
    "Wadaria 2 F Missile": lambda loadout: (
        (easyWadariaFix in loadout) and
        (Xray in loadout) and
        (Spazer in loadout)
        #maybe more?
    ),
    "Wadaria 1 Top Right Missile": lambda loadout: (
        (upperWadaria2 in loadout)
    ),
    "Wadaria 1 Bottom Left Missile": lambda loadout: (
        (
            (easyWadariaFix in loadout) and
            (Wave in loadout)
        )
        #or a backdoor from lower Messadon 3
    ),
    "Wadaria 3 Long Hallway from 2 Missile": lambda loadout: (
        (upperWadaria2 in loadout) and
        (Grapple in loadout)
        # ???
        # and an event???
    ),
    "Wadaria 3 Screwlocked Above Ridley Missile": lambda loadout: (
        (
            (upperWadaria2 in loadout) and
            (Screw in loadout) and
            (Xray in loadout)
        ) or
        (
            (wadaria3 in loadout) and
            (Screw in loadout) and
            (Spazer in loadout) and
            (Springball in loadout)
        )
        #maybe?
    ),
    "Wadaria 3 Screwlocked Above Ridley Power Bomb": lambda loadout: (
        (
            (upperWadaria2 in loadout) and
            (Screw in loadout) and
            (Xray in loadout)
        ) or
        (
            (wadaria3 in loadout) and
            (Screw in loadout) and
            (Spazer in loadout) and
            (Springball in loadout)
        )
        #maybe?
    ),
    "Wadaria 2 Highest Super Missile": lambda loadout: (
        (easyWadariaFix in loadout)
    ),
    "Wadaria 3 by SE79 Missile": lambda loadout: (
        (upperWadaria2 in loadout) and
        (canUsePB in loadout)
        #I think
    ),
    "Wadaria 1 Central Superlocked Missile": lambda loadout: (
        (easyWadariaFix in loadout)
    ),
    
}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
