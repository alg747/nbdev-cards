# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_cards.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_cards.ipynb 3
from fastcore.test import *
from fastcore.utils import *  # for @patch

# %% ../nbs/00_cards.ipynb 4
suits = ["♣️","♦️","❤️","♠️"]
ranks = [None, "A"] + [str(x) for x in range(2,11)] + ["J", "Q", "K"]

# %% ../nbs/00_cards.ipynb 13
class Card:
    "A playing card" 
    def __init__(self,
                 suit:int, # An index into `suits`
                 rank:int): # An index into `ranks`
        self.suit,self.rank = suit,rank
                     
    def __str__(self): return f"{ranks[self.rank]}{suits[self.suit]}"
    __repr__ = __str__

    # def __eq__(self, a:'Card'): return (self.suit,self.rank)==(a.suit,a.rank) # check patched version below

# %% ../nbs/00_cards.ipynb 20
@patch
def __eq__(self:Card, a:Card): return (self.suit,self.rank)==(a.suit,a.rank)

@patch
def __lt__(self:Card, a:Card): return (self.suit,self.rank)<(a.suit,a.rank)

@patch
def __gt__(self:Card, a:Card): return (self.suit,self.rank)>(a.suit,a.rank)
