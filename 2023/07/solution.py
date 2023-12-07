from collections import Counter
from enum import Enum
import sys


class HandType(Enum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

    def __lt__(self, other) -> bool:
        return self.value < other.value


CARD_TO_VALUE = {
    'A': 1,
    'K': 2,
    'Q': 3,
    'J': 4,
    'T': 5,
    '9': 6,
    '8': 7,
    '7': 8,
    '6': 9,
    '5': 10,
    '4': 11,
    '3': 12,
    '2': 13
}


class Hand:

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.hand_type = self.determine_hand_type(cards)

    def __repr__(self) -> str:
        return self.cards

    def __lt__(self, other) -> bool:
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        else:
            for i, j in zip(self.cards, other.cards):
                if i != j:
                    return CARD_TO_VALUE[i] < CARD_TO_VALUE[j]
        raise Error("Shouldn't have happened")

    def determine_hand_type(self, cards: str) -> HandType:
        most_common_list = Counter(self.cards).most_common()
        if len(most_common_list) == 1:
            return HandType.FIVE_OF_A_KIND

        most_common = most_common_list[0]
        second_most_common = most_common_list[1]

        if most_common[1] == 4:
            return HandType.FOUR_OF_A_KIND
        elif most_common[1] == 3:
            if second_most_common[1] == 2:
                return HandType.FULL_HOUSE
            else:
                return HandType.THREE_OF_A_KIND
        elif most_common[1] == 2:
            if second_most_common[1] == 2:
                return HandType.TWO_PAIRS
            else:
                return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD


with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

hands = []
for line in lines:
    cards, bid = line.split()
    hands.append(Hand(cards, int(bid)))

winnings = 0
for i, hand in enumerate(sorted(hands)):
    rank = len(hands)-i
    winnings += rank * hand.bid

print(winnings)


# Task 2

CARD_TO_VALUE2 = {
    'A': 1,
    'K': 2,
    'Q': 3,
    'T': 5,
    '9': 6,
    '8': 7,
    '7': 8,
    '6': 9,
    '5': 10,
    '4': 11,
    '3': 12,
    '2': 13,
    'J': 14,
}


class Hand2:

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.hand_type = self.determine_hand_type(cards)

    def __repr__(self) -> str:
        return self.cards

    def __lt__(self, other) -> bool:
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        else:
            for i, j in zip(self.cards, other.cards):
                if i != j:
                    return CARD_TO_VALUE2[i] < CARD_TO_VALUE2[j]
        raise Error("Shouldn't have happened")

    def determine_hand_type(self, cards: str) -> HandType:
        most_common_tuples = Counter(self.cards).most_common()

        most_common_list = []
        for t in most_common_tuples:
            if t[1] != "J":
                most_common_list.append([t[0], t[1]])
        most_common_list = list(filter(lambda entry: entry[0] != "J", most_common_list))

        if len(most_common_list) <= 1:
            return HandType.FIVE_OF_A_KIND

        most_common = most_common_list[0]
        second_most_common = most_common_list[1]
        num_of_j = cards.count("J")
        most_common[1] += num_of_j

        if most_common[1] == 4:
            return HandType.FOUR_OF_A_KIND
        elif most_common[1] == 3:
            if second_most_common[1] == 2:
                return HandType.FULL_HOUSE
            else:
                return HandType.THREE_OF_A_KIND
        elif most_common[1] == 2:
            if second_most_common[1] == 2:
                return HandType.TWO_PAIRS
            else:
                return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD


hands = []
for line in lines:
    cards, bid = line.split()
    hands.append(Hand2(cards, int(bid)))

winnings = 0
for i, hand in enumerate(sorted(hands)):
    rank = len(hands)-i
    winnings += rank * hand.bid

print(winnings)
