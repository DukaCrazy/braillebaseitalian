from braillebase import BrailleBase

class BrailleBaseItalian(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules_uppercase("⠨", "⠨⠨", "⠐") 
        #lowercase
        self.append_braille_letter("à", ["⠷"])
        self.append_braille_letter("è", ["⠮"])
        self.append_braille_letter("ì", ["⠌"])
        self.append_braille_letter("ò", ["⠬"])
        self.append_braille_letter("ù", ["⠾"])
        self.append_braille_letter("â", ["⠡"])
        self.append_braille_letter("ê", ["⠣"])
        self.append_braille_letter("î", ["⠩"])
        self.append_braille_letter("ô", ["⠹"])
        self.append_braille_letter("û", ["⠱"])
        self.append_braille_letter("ä", ["⠜"])
        self.append_braille_letter("ë", ["⠫"])
        self.append_braille_letter("ï", ["⠻"])
        self.append_braille_letter("ö", ["⠪"])
        self.append_braille_letter("ü", ["⠳"])
        self.append_braille_letter("é", ["⠿"])
        self.append_braille_letter("ñ", ["⠻"])
        self.append_braille_letter("ç", ["⠯"])
        #uppercase
        self.append_braille_letter("À", ["⠷"],1)
        self.append_braille_letter("È", ["⠮"],1)
        self.append_braille_letter("Ì", ["⠌"],1)
        self.append_braille_letter("Ò", ["⠬"],1)
        self.append_braille_letter("Ù", ["⠾"],1)
        self.append_braille_letter("Â", ["⠡"],1)
        self.append_braille_letter("Ê", ["⠣"],1)
        self.append_braille_letter("Î", ["⠩"],1)
        self.append_braille_letter("Ô", ["⠹"],1)
        self.append_braille_letter("Û", ["⠱"],1)
        self.append_braille_letter("Ä", ["⠜"],1)
        self.append_braille_letter("Ë", ["⠫"],1)
        self.append_braille_letter("Ï", ["⠻"],1)
        self.append_braille_letter("Ö", ["⠪"],1)
        self.append_braille_letter("Ü", ["⠳"],1)
        self.append_braille_letter("É", ["⠿"],1)
        self.append_braille_letter("Ñ", ["⠻"],1)
        self.append_braille_letter("Ç", ["⠯"],1)

        self.append_braille_letter("&", ["⠯"])
        self.append_braille_letter("-", ["⠤"])
        self.append_braille_letter("…", ["⠄"])
