# deckard

A pythonic playing card game library.

## Install

```
pip install deckards
```

## Usage

The most common way to generate cards is by creating a `Deck` object.

```py
>>> from deckard import Deck
>>> deck = Deck()
```

Decks of course have 52 cards.

```py
>>> len(deck)
52
```

You can draw cards from the deck. Notice how this decreases the size of the deck.

```py
>>> deck.draw()
[Card<K♦️>]
>>> len(deck)
51
```

You can draw multiple cards at once.

```py
>>> first, second = deck.draw(2)
>>> first, second
(Card<7♥️>, Card<T♥️>)
```

Cards can be compared to each other.

```py
>>> second > first
True
```

You can inspect the `suit` and `rank` of a card.

```py
>>> first.suit, second.suit
(<Suit.HEARTS: 0>, <Suit.HEARTS: 0>)
>>> first.rank, second.rank
(<Rank.SEVEN: 7>, <Rank.TEN: 10>)
```

And you can compare the suits and ranks of cards as well.

```py
>>> first.suit == second.suit
True
>>> first.rank < second.rank
True
```
