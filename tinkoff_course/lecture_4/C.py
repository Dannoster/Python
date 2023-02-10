class Deck:

    

    def __init__(self, file_name=None):
        self.cards = []
        if file_name:
            self.__make_from_file(file_name)

    def __make_from_file(self, file_name):
        with open(file_name) as file:
            file_line = file.readline().strip()
            while file_line and not self.__check_errors():
                if file_line[0] == "+" and len(file_line) == 3:
                    self.__add_card(file_line[1:])
                elif file_line[0] == "^" and len(file_line) == 1:
                    self.__remove_upper_card()
                elif file_line[0] == "#" and len(file_line) == 3:
                    self.__add_to_bottom(file_line[1:])
                elif file_line[0] == "/" and len(file_line) == 1:
                    self.__remove_bottom_card()
                else:
                    self.__err()
                file_line = file.readline().strip()

    def __add_card(self, card_name):
        if Card(card_name) in self.cards:
            self.__err()
        else:
            try:
                self.cards.append(Card(card_name))
            except AssertionError:
                self.__err()

    def __add_to_bottom(self, card_name):
        if Card(card_name) in self.cards:
            self.__err()
        else:
            try:
                self.cards.insert(0, Card(card_name))
            except AssertionError:
                self.__err()

    def __remove_upper_card(self):
        if self.cards:
            self.cards.pop()
        else:
            self.__err()

    def __remove_bottom_card(self):
        if self.cards:
            self.cards.pop(0)
        else:
            self.__err()

    def __err(self):
        self.cards = ["ERROR"]

    def __check_errors(self):
        return "ERROR" in self.cards

    def show(self, file_name=None):
        if file_name:
            with open(file_name, "w") as file:
                if len(self.cards):
                    out_list = [str(card) for card in self.cards[::-1]]
                    file.write(" ".join(out_list))
                else:
                    file.write("EMPTY")
        else:
            if self.cards:
                print(*self.cards[::-1])
            else:
                print("EMPTY") 


class Card:
    

    def __init__(self, name):
        ACCEPTED_SUIT_SYMBOLS = "CSHD"
        ACCEPTED_RANK_SYMBOLS = "A23456789TJQK"
        assert name[0] in ACCEPTED_SUIT_SYMBOLS 
        assert name[1] in ACCEPTED_RANK_SYMBOLS 
        self.suit = name[0] # suit - масть
        self.rank = name[1] # rank - ранг (стоимость)

    def __eq__(self, other):
        if isinstance(other, Card):
            return str(self) == str(other)
        elif isinstance(other, str):
            return str(self) == other
        else:
            return False

    def __str__(self):
        return self.suit + self.rank


a = Deck("input.txt")
a.show("output.txt")
