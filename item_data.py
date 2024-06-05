from typing import Iterable

Item = tuple[str, bytes, bytes, bytes, bytes]
""" Name, Visible, Chozo, Hidden, AmmoQty """


class Items:
    Missile = ("Missile",
               b"\xdb\xee",
               b"\x2f\xef",
               b"\x83\xef",
               b"\x00")
    Super = ("Super Missile",
             b"\xdf\xee",
             b"\x33\xef",
             b"\x87\xef",
             b"\x00")
    PowerBomb = ("Power Bomb",
                 b"\xe3\xee",
                 b"\x37\xef",
                 b"\x8b\xef",
                 b"\x00")
    Morph = ("Morph Ball",
             b"\x77\xef",
             b"\x77\xef",
             b"\x77\xef",
             b"\x00")
    Springball = ("Springball",
                 b"\x57\xef",
                 b"\x57\xef",
                 b"\x57\xef",
                 b"\x00")
    Bombs = ("Bombs",
             b"\x3b\xef",
             b"\x3b\xef",
             b"\x3b\xef",
             b"\x00")
    HiJump = ("HiJump",
              b"\x47\xef",
              b"\x47\xef",
              b"\x47\xef",
              b"\x00")
    Varia = ("Varia Suit",
             b"\x5b\xef",
             b"\x5b\xef",
             b"\x5b\xef",
             b"\x00")
    GravitySuit = ("Gravity Suit",
                   b"\x5f\xef",
                   b"\x5f\xef",
                   b"\x5f\xef",
                   b"\x00")
    Wave = ("Wave Beam",
            b"\xa3\xef",
            b"\xa3\xef",
            b"\xa3\xef",
            b"\x00")
    SpeedBooster = ("Speed Booster",
                    b"\x4b\xef",
                    b"\x4b\xef",
                    b"\x4b\xef",
                    b"\x00")
    Spazer = ("Spazer",
              b"\x53\xef",
              b"\x53\xef",
              b"\x53\xef",
              b"\x00")
    Ice = ("Ice Beam",
           b"\x43\xef",
           b"\x43\xef",
           b"\x43\xef",
           b"\x00")
    Grapple = ("Grapple Beam",
               b"\x17\xef",
               b"\x17\xef",
               b"\x17\xef",
               b"\x00")
    Plasma = ("Plasma Beam",
              b"\x67\xef",
              b"\x67\xef",
              b"\x67\xef",
              b"\x00")
    Screw = ("Screw Attack",
             b"\x73\xef",
             b"\x73\xef",
             b"\x73\xef",
             b"\x00")
    Charge = ("Charge Beam",
              b"\x3f\xef",
              b"\x3f\xef",
              b"\x3f\xef",
              b"\x00")
    SpaceJump = ("Space Jump",
                 b"\x6f\xef",
                 b"\x6f\xef",
                 b"\x6f\xef",
                 b"\x00")
    Energy = ("Energy Tank",
              b"\xd7\xee",
              b"\x2b\xef",
              b"\x7f\xef",
              b"\x00")
    Reserve = ("Reserve Tank",
              b"\x7b\xef",
              b"\x7b\xef",
              b"\x7b\xef",
              b"\x00")
    Xray = ("Xray",
            b"\x63\xef",
            b"\x63\xef",
            b"\x63\xef",
            b"\x00")
    Walljump = ("Walljump Boots",
              b"\x00\xf8",
              b"\x00\xf8",
              b"\x00\xf8",
              b"\x00")

items_unpackable: Iterable[Item] = (
    Items.Missile, Items.Super, Items.PowerBomb, Items.Morph, Items.Springball, Items.Bombs,
    Items.HiJump, Items.GravitySuit, Items.Varia, Items.Wave, Items.SpeedBooster, Items.Spazer,
    Items.Ice, Items.Grapple, Items.Plasma, Items.Screw, Items.Charge,
    Items.SpaceJump, Items.Energy, Items.Reserve, Items.Xray, Items.Walljump
)

all_items: dict[str, Item] = {
    item[0]: item
    for item in items_unpackable
}
