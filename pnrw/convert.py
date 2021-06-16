"""
https://nanoo.tools/unit-converter
"""

table = {"raw":1}

def _table(currency="nano"):
    if currency.lower() == "nano":
        for i, p in enumerate(["G","M","k","","m","u"]):
            inRaw = 10 ** (33-(i*3))
            table[p+currency] = inRaw
    elif currency.lower() == "ban":
        for i, p in enumerate(["Gban","Mban","kban","ban","banoshi"]):
            if p != "banoshi":
                t = 3
            else:
                t = 11
                i = 1
            inRaw = 10 ** (33-(i*t))
            table[p] = inRaw


def convert(amount, From, To):
    return amount*(table[From]/table[To])

_table()
_table("ban")