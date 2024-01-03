from deck import Deck
from printer import print_deck_attributes


def main():
    deck = create_deck()
    while True:
        print_deck_attributes(deck)
        answer = input("Would you like to modify the cards in your deck (Y/N)? ")
        if answer.lower() in ["n", "no", "nope", "naw", "nah"]:
            break
        deck = modify_deck(deck)


def create_deck():
    deck = Deck()
    add_cards(deck)
    return deck


def modify_deck(deck):
    keep_modifying = True
    while keep_modifying:
        action = input("Would you like to add (A) cards, remove (R) cards, or be done (D)? ")
        if action.lower() in ["a", "add", "m", "modify", "mod"]:
            add_cards(deck)
        elif action.lower() in ["r", "remove", "delete"]:
            remove_cards(deck)
        else:
            keep_modifying = False

    return deck


def add_cards(deck):
    if len(deck) >= 40:
        print("Your deck is full.")
    while len(deck) < 40:
        deck_list = deck.to_list(full=True)
        for i in range(len(deck_list)):
            print(str(i + 1) + ") " + deck_list[i + 1][0] + " x" + str(deck_list[i + 1][1]))

        print("\nYou have " + str(len(deck)) + " cards in your deck.")
        answer = input("Which type of card would you like to add (1-" + str(len(deck_list)) + ")? Enter \"D\" if you're done. ")
        if not answer.isdigit() or not 1 <= int(answer) <= len(deck_list):
            break
        card_type = int(answer)

        max_allowable_cards = deck.get_allowable_sum(deck_list[card_type][0]) - deck_list[card_type][1]
        if max_allowable_cards <= 0:
            print("You're full on " + deck_list[card_type][0] + " cards")
            continue

        answer = input("How many " + deck_list[card_type][0] + " cards would you like (0-" + str(min(40 - len(deck), max_allowable_cards)) + ")? ")
        while not answer.isdigit() or not (0 <= int(answer) <= min(40 - len(deck), max_allowable_cards)):
            answer = input("Please enter an integer in the range of (0-" + str(min(40 - len(deck), max_allowable_cards)) + "): ")

        for i in range(int(answer)):
            deck.add_card(deck_list[card_type][0])
        if len(deck) >= 40:
            print("Your deck is full.")


def remove_cards(deck):
    if len(deck) <= 0:
        print("Your deck is empty.")
    while len(deck) > 0:
        deck_list = deck.to_list(full=False)
        for i in range(len(deck_list)):
            print(str(i + 1) + ") " + deck_list[i + 1][0] + " x" + str(deck_list[i + 1][1]))

        print("\nYou have " + str(len(deck)) + " cards in your deck.")
        answer = input("Which type of card would you like to remove (1-" + str(len(deck_list)) + ")? Enter \"D\" if you're done. ")
        if not answer.isdigit() or not 1 <= int(answer) <= len(deck_list):
            break
        card_type = int(answer)

        max_removable_cards = deck_list[card_type][1]
        if max_removable_cards <= 0:
            print("You don't have any " + deck_list[card_type][0] + " cards")
            continue

        answer = input("How many " + deck_list[card_type][0] + " cards would you like to remove (0-" + str(max_removable_cards) + ")? ")
        while not answer.isdigit() or not (0 <= int(answer) <= min(40 - len(deck), max_removable_cards)):
            answer = input("Please enter an integer in the range of (0-" + str(min(40 - len(deck), max_removable_cards)) + "): ")

        for i in range(int(answer)):
            deck.remove_card(deck_list[card_type][0])
        if len(deck) <= 0:
            print("Your deck is empty.")


main()
