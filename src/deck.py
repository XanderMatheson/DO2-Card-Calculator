from card import *


class Deck:
    def __init__(self):
        self.__player_cards = 0  # Does not include stumble cards
        self.__total_cards = 0  # Includes stumble cards
        self.__cards = {}
        self.__card_names = {}
        for card_name in CARD_CLASSES:
            self.__card_names[card_name[0].name] = card_name[0]
            self.__cards[card_name[0].name] = [[], card_name[1]]
        self.__quickdraw_count = 0
        self.__clank_multiplier = 1.0
        self.__adrenaline_multiplier = [0]
        self.__sneak_multiplier = 1
        self.__draw_rate = 1.0
        self.__eerie_silence_count = 0
        self.__cold_snap_count = 0
        self.__chill_step_count = 0
        self.__deepfrost_multiplier = 1
        self.__stairs_unlocked = [0, 1, 2, 3]
        self.__contains_bunny_slippers = False

    def add_card(self, card_name):
        if self.__player_cards >= 40:
            print("You already have 40 cards in your deck.")
        elif isinstance(card_name, str) and len(self.__cards[card_name][0]) < self.__cards[card_name][1]:
            self.__cards[card_name][0].append(self.__card_names[card_name]())
            self.__player_cards += 1
            self.__total_cards += 1
            if "Swagger" in card_name:
                for i in range(2):  # Add the stumble cards associated with Swagger
                    self.__cards["\033[91mStumble\033[0m"][0].append(self.__card_names["\033[91mStumble\033[0m"]())
                self.__total_cards += 2
            elif "Suit Up" in card_name:
                self.__clank_multiplier = 1.25
            elif "Adrenaline Rush" in card_name:
                # todo - verify the max and min heartbeat for this card
                self.__adrenaline_multiplier = (8, 20)
            elif "Haste" in card_name:
                # Does the draw rate increase linearly (3 cards = 1.3 draw rate) or
                # exponentially (3 cards = 1.331 draw rate)? Or does it even increase at all?
                # Todo - Someone ask Tango!!!
                self.__draw_rate += 0.1  # Increase linearly
                # self.__draw_rate *= 1.1  # Increase exponentially
            elif "Eerie Silence" in card_name:
                self.__eerie_silence_count += 1
            elif "Cold Snap" in card_name:
                self.__cold_snap_count += 1
            elif "Deepfrost" in card_name:
                self.__deepfrost_multiplier += 6
        else:
            print("Couldn't add that card to the deck.")

    def remove_card(self, card_name):
        if self.__player_cards < 0:
            print("There's nothing left to remove.")
        elif isinstance(card_name, str) and len(self.__cards[card_name][0]) > 0:
            self.__cards[card_name][0].pop()
            self.__player_cards -= 1
            self.__total_cards -= 1
            if card_name == "\033[94mSwagger\033[0m":  # Get rid of the stumble cards associated with Swagger
                self.__cards["\033[91mStumble\033[0m"][0].pop()
                self.__cards["\033[91mStumble\033[0m"][0].pop()
                self.__total_cards -= 2
        else:
            print("Couldn't remove that card from the deck.")

    def get_total_cards(self):
        return self.__total_cards

    def get_allowable_sum(self, card_name):
        return self.__cards[card_name][1]

    def get_card_costs(self):
        ember_cost = 0
        crown_cost = 0
        for card_type in self.__cards.keys():
            for card in self.__cards[card_type][0]:
                ember_cost += card.ember_cost
                crown_cost += card.crown_cost
        return ember_cost, crown_cost

    def get_ember_drops(self):
        ember_drops = 0
        for card_type in self.__cards.keys():
            for card in self.__cards[card_type][0]:
                ember_drops += card.ember_drops
        average_drop = ember_drops / (self.__total_cards - self.__cold_snap_count)  # Don't count the cold snaps themselves
        ember_drops += 3 * average_drop * self.__cold_snap_count
        return round(ember_drops), round(ember_drops / self.__total_cards, 3)

    def get_treasure_drops(self):
        treasure_drops = 0
        for card_type in self.__cards.keys():
            for card in self.__cards[card_type][0]:
                treasure_drops += card.treasure_drops
        return treasure_drops, round(treasure_drops / self.__total_cards, 3)

    def get_clank_block(self):
        clank_block = 0
        for card_type in self.__cards.keys():
            for card in self.__cards[card_type][0]:
                clank_block += card.clank_block
        clank_block /= self.__clank_multiplier
        return clank_block, round(clank_block / self.__total_cards, 3)

    def get_hazard_block(self):
        hazard_block = 0
        for card_type in self.__cards.keys():
            for card in self.__cards[card_type][0]:
                hazard_block += card.hazard_block
        return hazard_block, round(hazard_block / self.__total_cards, 3)

    def get_sprint_duration(self):
        sprint = 0
        for card_type in self.__cards.keys():
            for card in self.__cards[card_type][0]:
                sprint += card.sprint
        return sprint, round(sprint / self.__total_cards, 3)

    def get_jump_duration(self):
        jump = 0
        for card_type in self.__cards.keys():
            for card in self.__cards[card_type][0]:
                jump += card.jump
        return jump, round(jump / self.__total_cards, 3)

    def to_list(self, full=False):
        deck_list = {}
        index = 1
        for card_type in self.__cards.keys():
            if card_type == "\033[91mStumble\033[0m":
                continue
            count = len(self.__cards[card_type][0])
            if full or count > 0:
                deck_list[index] = [card_type, count]
                index += 1
        return deck_list

    def __get_clank_averages(self, total_clank_block, total_cards):
        if self.__contains_bunny_slippers:
            extra_clank_block = [0, 4, 8, 12]
            averages = []
            for i in range(len(extra_clank_block)):
                averages.append((total_clank_block + extra_clank_block[i]) / total_cards)
            return averages

    def __get_ember_averages(self, total_ember_drops, total_cards):
        if self.__contains_deepfrost:
            extra_ember_drops = [0, 4, 8, 12]
            averages = []
            for i in range(len(extra_ember_drops)):
                averages.append((total_ember_drops + extra_ember_drops[i]) / total_cards)
            return averages

    def __str__(self):
        deck_string = ""
        for card_type in self.__cards.keys():
            count = len(self.__cards[card_type][0])
            if count > 0:
                deck_string += str(count) + "x " + card_type + " cards\n"
        return deck_string

    def __len__(self):
        return self.__player_cards
