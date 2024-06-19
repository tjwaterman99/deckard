from deckard import Suit, Rank, Card, Deck
from deckard.core import _all_cards, suit_emojis, rank_emojis


def test_suit_ordering():
    assert Suit.SPADES > Suit.CLUBS > Suit.DIAMONDS > Suit.HEARTS
    assert Suit.SPADES == Suit.SPADES


def test_rank_ordering():
    assert Rank.ACE > Rank.TWO
    assert Rank.ACE == Rank.ACE


def test_rank_emojis():
    assert Rank.ACE.emoji == rank_emojis[Rank.ACE.name]


def test_suit_hash():
    hashes = [hash(c) for c in Suit.__members__]
    assert len(hashes) == len(Suit.__members__)


def test_rank_hash():
    hashes = [hash(c) for c in Rank.__members__]
    assert len(hashes) == len(Rank.__members__)


def test_suit_emojis():
    assert Suit.SPADES.emoji == suit_emojis[Suit.SPADES.name]


def test_card_ordering():
    ace_spades = Card(rank=Rank.ACE, suit=Suit.SPADES)
    king_spades = Card(rank=Rank.KING, suit=Suit.SPADES)
    king_hearts = Card(rank=Rank.KING, suit=Suit.HEARTS)
    two_hearts = Card(rank=Rank.TWO, suit=Suit.HEARTS)
    assert ace_spades > king_spades > king_hearts > two_hearts
    assert ace_spades == ace_spades


def test_card_str():
    ace_spades = Card(rank=Rank.ACE, suit=Suit.SPADES)
    assert Rank.ACE.emoji in str(ace_spades)
    assert Suit.SPADES.emoji in str(ace_spades)


def test_card_repr():
    ace_spades = Card(rank=Rank.ACE, suit=Suit.SPADES)
    assert Rank.ACE.emoji in repr(ace_spades)
    assert Suit.SPADES.emoji in repr(ace_spades)


def test_cards_hash():
    for card in _all_cards:
        assert hash(card) is not None


def test_all_cards():
    assert len(_all_cards) == 52
    assert len(set(_all_cards)) == 52


def test_deck_length():
    assert len(Deck()) == 52


def test_deck_getitem():
    d = Deck()
    assert d[0] is not None


def test_deck_iter():
    d = Deck()
    assert next(iter(d)) is not None


def test_duck_shuffle():
    d = Deck()
    d.sort()
    assert d[0].rank == Rank.ACE
    assert d[0].suit == Suit.SPADES


def test_deck_draw():
    d = Deck()
    r = d.draw(5)
    assert len(r) == 5
    assert len(d) == len(Deck()) - len(r)
    d.draw()
    assert len(d) == len(Deck()) - len(r) - 1
