from functools import cmp_to_key

#load input from file
production = False
parsed_input = []


with open('input_7.txt') as f:
    input = f.read()
    parsed_input = [{"hand":l.split(" ")[0], "bid": l.split(" ")[1]} for l in input.splitlines() if len(l.split(" "))==2 ]



card_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}


def sort_hand(hand):
    card_count = {x : 0 for x in card_values.keys()}
    for card in hand:
        card_count[card] = card_count[card] + 1

    card_count = sorted(card_count.items(), key=lambda kv: kv[1])
    card_count.reverse()
    # card_cout list to dict
    card_count = [{"card": x[0], "count":x[1]} for x in card_count]
    return card_count


def hand_value(sorted_hand):

    if sorted_hand[0]['count'] == 5:
        return 7
    # four of a kind
    if sorted_hand[0]['count'] == 4:
        return 6
    # full house
    if sorted_hand[0]['count'] == 3 and sorted_hand[1]['count'] == 2:
        return 5
    # three of a kind
    if sorted_hand[0]['count'] == 3:
        return 4
    # two pair
    if sorted_hand[0]['count'] == 2 and sorted_hand[1]['count'] == 2:
        return 3
    # pair
    if sorted_hand[0]['count'] == 2:
        return 2
    # high card
    for val in sorted_hand:
        if val['count'] > 1:
            print("error")
            return 0
    return 1


def compare_hands(handBid1, handBid2):
    handval1 = hand_value(handBid1['sorted_hand'])
    handval2 = hand_value(handBid2['sorted_hand'])

    if  handval1 < handval2:
        return -1
    elif handval1 > handval2:
        return 1
      
    for card1, card2 in zip(handBid1['hand'], handBid2['hand']):
        if card_values[card1] < card_values[card2]:
            return -1
        elif card_values[card1] > card_values[card2]:
            return 1
    return 0

# Convert the comparison function to a key function using cmp_to_key
key_function = cmp_to_key(compare_hands)
sorted_input = [{"sorted_hand":sort_hand(hand_bid["hand"]), "hand": hand_bid["hand"], "bid": hand_bid["bid"]} for hand_bid in parsed_input]

sorted_input = sorted(sorted_input, key=key_function)

sum = 0
for index, sorted_hand in enumerate(sorted_input):
    # print(sorted_hand['hand'])
    sum += int(sorted_hand["bid"]) * (index+1)
    
print(sum)