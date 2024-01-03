def print_deck_attributes(deck):
    print()
    if len(deck) <= 0:
        print("Your deck is empty")
    else:
        print("Your deck includes " + str(len(deck)) + " cards (plus " + str(deck.get_total_cards() - len(deck)) + " stumble cards):\n" + str(deck))

        ember_cost, crown_cost = deck.get_card_costs()
        print("Your deck costs " + str(ember_cost) + " frost embers and " + str(crown_cost) + " crowns.")
        print_attribute(name="frost ember", subtext=" drop rate", color_num=96, attributes=deck.get_ember_drops())
        print_attribute(name="treasure", subtext=" drop rate", color_num=93, attributes=deck.get_treasure_drops())
        print_attribute(name="clank", subtext=" block", color_num=94, attributes=deck.get_clank_block())
        print_attribute(name="hazard", subtext=" block", color_num=91, attributes=deck.get_hazard_block())
        print_attribute(name="sprint", subtext=" duration", color_num=95, units=" seconds", attributes=deck.get_sprint_duration())
        print_attribute(name="jump", subtext=" duration", color_num=92, units=" seconds", attributes=deck.get_jump_duration())
    print()


def print_attribute(name="", subtext="", color_num=0, units="", attributes=(0, 0)):
    print("The average \033[" + str(color_num) + "m" + name + "\033[0m" + subtext + " of your deck is \033[" + str(color_num) + "m" + str(attributes[1]) + "\033[0m" + units + " per card (\033[" + str(color_num) + "m" + str(attributes[0]) + "\033[0m in total)")
