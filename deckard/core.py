from random import shuffle as _shuffle
from enum import Enum
from itertools import product


suit_emojis = {
    "SPADES": "♠️",
    "CLUBS": "♣️",
    "DIAMONDS": "♦️",
    "HEARTS": "♥️",
}


rank_emojis = {
    "ACE": "A",
    "KING": "K",
    "QUEEN": "Q",
    "JACK": "J",
    "TEN": "T",
    "NINE": "9",
    "EIGHT": "8",
    "SEVEN": "7",
    "SIX": "6",
    "FIVE": "5",
    "FOUR": "4",
    "THREE": "3",
    "TWO": "2",
}


class Suit(Enum):
    SPADES = 3
    CLUBS = 2
    DIAMONDS = 1
    HEARTS = 0

    @property
    def emojis(cls):
        return suit_emojis

    @property
    def emoji(self):
        return self.emojis[self.name]

    def __gt__(self, other: "Suit"):
        return self.value > other.value

    def __eq__(self, other: "Suit"):
        return self.value == other.value

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name


class Rank(Enum):
    ACE = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2

    @property
    def emojis(self):
        return rank_emojis

    @property
    def emoji(self):
        return self.emojis[self.name]

    def __gt__(self, other: "Suit"):
        return self.value > other.value

    def __eq__(self, other: "Suit"):
        return self.value == other.value

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __gt__(self, other: "Card"):
        if self.suit > other.suit:
            return True
        else:
            return self.rank > other.rank

    def __eq__(self, other: "Card"):
        return self.suit == other.suit and self.rank == other.rank

    def __hash__(self):
        return hash((self.suit, self.rank))

    def __str__(self):
        return f"{self.rank.emoji}{self.suit.emoji}"

    def __repr__(self):
        return f"Card<{self}>"


_ranks = frozenset(Rank._member_map_.values())
_suits = frozenset(Suit._member_map_.values())
_suit_ranks = frozenset(product(_ranks, _suits))
_all_cards = list([Card(rank=r, suit=s) for r, s in _suit_ranks])


class Deck:

    def __init__(self, cards: list[Card] = _all_cards, shuffle=True):
        self.cards = cards.copy()
        if shuffle:
            self.shuffle()
        else:
            self.sort()

    def __iter__(self):
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, value: int):
        return self.cards[value]

    def shuffle(self):
        _shuffle(self.cards)

    def sort(self):
        self.cards = list(sorted(self.cards, reverse=True))

    def draw(self, num=1):
        res = list()
        for _ in range(num):
            res.append(self.cards.pop(0))
        return res
