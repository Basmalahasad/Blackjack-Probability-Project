import random
import pygame
import os

pygame.init()

window_width = 900
window_height = 700
screen = pygame.display.set_mode((window_width, window_height))
background_image = pygame.image.load("background.png")
pygame.display.set_caption("Blackjack")
font1 = pygame.font.Font('freesansbold.ttf', 36)
font2 = pygame.font.Font('freesansbold.ttf', 24)
font3 = pygame.font.Font('freesansbold.ttf', 16)

rect_width = 300
rect_height = 80
rect_x = (window_width - rect_width) // 2
rect_y = (window_height - rect_height) // 2
deal_text = font1.render('DEAL HAND', True, 'black')

second_rect_width = 120
second_rect_height = 40
second_rect_padding = 150
rect1 = pygame.Rect((window_width / 2 - second_rect_width / 2) - second_rect_padding / 2,
                    window_height - second_rect_height
                    - 10, second_rect_width, second_rect_height)
rect2 = pygame.Rect((window_width / 2 - second_rect_width / 2) + second_rect_padding / 2,
                    window_height - second_rect_height
                    - 10, second_rect_width, second_rect_height)
rect3 = pygame.Rect(875, 675, 20, 20)
label1 = font2.render("STAND", True, 'black')
label2 = font2.render("HIT", True, 'black')
label1_rect = label1.get_rect(center=rect1.center)
label2_rect = label2.get_rect(center=rect2.center)

active = False

suits = ['hearts', 'diamonds', 'spades', 'clubs']
ranks = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
initial_deal = False
player_hand = []
dealer_hand = []
player_cards_drawn = []
dealer_cards_drawn = []
dealer_label = font2.render("Dealer's hand", True, 'yellow')
player_label = font2.render("Player's hand", True, 'yellow')

CARD_FOLDER = "card_images"
card_images = {}
player_card_images = []
dealer_card_images = []
card_width = 75
card_spacing = 20
card_height = 150
final_hand = False
second_deal = False

for suit in suits:
    for rank in ranks:
        file_name = "{}_{}.png".format(rank, suit)
        image_path = os.path.join(CARD_FOLDER, file_name)
        card_images[(rank, suit)] = pygame.image.load(image_path).convert_alpha()


def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck


def draw_card(deck, hand):
    if deck:
        card = random.choice(deck)
        deck.remove(card)
        hand.append(card)
        return card


def get_value(card):
    rank = card[0]
    if rank in ['jack', 'queen', 'king']:
        return 10
    elif rank == 'ace':
        return 11
    else:
        return rank


def total(hand):
    total = 0
    num_aces = 0
    for card in hand:
        value = get_value(card)
        if value == 11:
            num_aces += 1
        total += int(value)
    while total > 21 and num_aces > 0:
        total -= 10
        num_aces -= 1
    return total


def count_cards(deck, hand):
    count = 0
    for card in deck:
        if card not in hand:
            count += 1
    return count


def count_aces(hand):
    return sum(1 for card in hand if card[0] == 'ace')


player_aces = count_aces(player_hand)
my_deck = create_deck()
random.shuffle(my_deck)


def count_cards_comparison(deck, cards_drawn, n, comparison, hand_total_dealer):
    count = 0
    for card in deck:
        if card not in cards_drawn:
            if get_value(card) == 11:
                if hand_total_dealer < 11:
                    card_value = 11
                else:
                    card_value = 1
            else:
                card_value = get_value(card)
            if comparison == "greater":
                if card_value > n:
                    count += 1
            elif comparison == "less":
                if card_value < n:
                    count += 1
            elif comparison == "equal":
                if card_value == n:
                    count += 1
    return count


def count_cards_between(deck, cards_drawn, n, l, comparison, hand_total_dealer):
    count = 0
    for card in deck:
        if card not in cards_drawn:
            if get_value(card) == 11:
                if hand_total_dealer < 11:
                    card_value = 11
                else:
                    card_value = 1
            else:
                card_value = get_value(card)
            if comparison == "greater":
                if n < card_value < l:
                    count += 1
            elif comparison == "less":
                if card_value < n and card_value < l:
                    count += 1
            elif comparison == "equal":
                if card_value == n:
                    count += 1
    return count


def show_results():
    if total(player_hand) > 21:
        score_label = font2.render("Player busts! Dealer wins", True, 'red')
        screen.blit(score_label, ((window_width  - score_label.get_width()) / 2, 600))

    elif total(dealer_hand) > 21:
        score_label = font2.render("Dealer busts! Player wins", True, 'red')
        screen.blit(score_label, ((window_width - score_label.get_width()) / 2, 600))

    elif total(dealer_hand) < total(player_hand):
        score_label = font2.render("Player wins!", True, 'red')
        screen.blit(score_label, ((window_width - score_label.get_width()) / 2, 600))

    elif total(dealer_hand) > total(player_hand):
        score_label = font2.render("Dealer wins!", True, 'red')
        screen.blit(score_label, ((window_width - score_label.get_width()) / 2, 600))

    else:
        score_label = font2.render("It's a tie!", True, 'red')
        screen.blit(score_label, ((window_width - score_label.get_width()) / 2, 600))


def draw_game(act):
    button_list = []
    if not act:
        deal = pygame.draw.rect(screen, 'white', (rect_x, rect_y, rect_width, rect_height), 0, 10)
        label_x = rect_x + rect_width // 2 - deal_text.get_width() // 2
        label_y = rect_y + rect_height // 2 - deal_text.get_height() // 2
        screen.blit(deal_text, (label_x, label_y))
        button_list.append(deal)
    else:
        stand = pygame.draw.rect(screen, 'white', rect1, 0, 5)
        screen.blit(label1, label1_rect)
        button_list.append(stand)
        hit = pygame.draw.rect(screen, 'white', rect2, 0, 5)
        screen.blit(label2, label2_rect)
        button_list.append(hit)
        again = pygame.draw.rect(screen, 'white', rect3, 0, 5)
        button_list.append(again)
    return button_list


run = True
while run:
    screen.blit(background_image, (0, 0))
    if initial_deal:
        for i in range(1):
            player_hand = [draw_card(my_deck, player_cards_drawn), draw_card(my_deck, player_cards_drawn)]
            dealer_hand = [draw_card(my_deck, dealer_cards_drawn), draw_card(my_deck, dealer_cards_drawn)]

            dealer_aces = count_aces(dealer_hand)
            dealer_hit = False

            if total(dealer_hand) < 17:
                dealer_hit = True
            elif total(dealer_hand) == 17 and dealer_aces > 0:
                dealer_hit = True
            else:
                dealer_hit = False

            hand_total_player = total(player_hand)
            hand_total_dealer = total(dealer_hand)

            probability_win = 0
            probability_lose = 0
            probability_tie = 0

            S = hand_total_player - hand_total_dealer
            N = 21 - hand_total_dealer


            def probability_calculator():
                global probability_win, probability_tie, probability_lose

                if hand_total_player == 21 and player_aces > 0:
                    probability_win = 1
                else:
                    if not dealer_hit:
                        if S > 0:
                            probability_win = 1
                        elif S < 0:
                            probability_lose = 1
                        else:
                            probability_tie = 1

                    else:
                        total_cards_left = count_cards(my_deck, player_hand + dealer_hand)

                        # dealer busts
                        num_cards_greater = count_cards_comparison(my_deck, player_hand + dealer_hand, N, "greater",
                                                                   hand_total_dealer)
                        prob_win_A = num_cards_greater / total_cards_left

                        # dealer reaches 21
                        num_cards_equal = count_cards_comparison(my_deck, player_hand + dealer_hand, N, "equal",
                                                                 hand_total_dealer)
                        prob_lose_B = num_cards_equal / total_cards_left

                        # dealer not busting or reach 21
                        num_cards_less = count_cards_comparison(my_deck, player_hand + dealer_hand, N, "less",
                                                                hand_total_dealer)
                        initial_prob = num_cards_less / total_cards_left

                        num_cards_greater_S = count_cards_between(my_deck, player_hand + dealer_hand, S, N, "greater",
                                                                  hand_total_dealer)
                        prob_lose_C = (num_cards_greater_S / num_cards_less) * initial_prob

                        num_cards_equal_S = count_cards_between(my_deck, player_hand + dealer_hand, S, N, "equal",
                                                                hand_total_dealer)
                        prob_tie_C = (num_cards_equal_S / num_cards_less) * initial_prob

                        num_cards_less_S = count_cards_between(my_deck, player_hand + dealer_hand, S, N, "less",
                                                               hand_total_dealer)
                        prob_win_C = (num_cards_less_S / num_cards_less) * initial_prob

                        probability_win = prob_win_A + prob_win_C
                        probability_lose = prob_lose_B + prob_lose_C
                        probability_tie = prob_tie_C

                return probability_win, probability_tie, probability_lose


            win_prob, tie_prob, lose_prob = probability_calculator()

        initial_deal = False

    if second_deal == True:
        show_results()

    if active:
        player_x = (window_width - card_width - card_width - card_spacing) / 2
        player_y = 150
        x = (window_width - card_width - card_width - card_spacing) / 2
        y = 400
        hand_total_player = total(player_hand)
        hand_total_dealer = total(dealer_hand)

        screen.blit(dealer_label, (x, window_height / 2))
        dealer_total_label = font3.render(f'Total: {hand_total_dealer}', True, 'yellow')
        screen.blit(dealer_total_label, (x, window_height / 2 + card_height + card_spacing))
        for card in player_hand:
            screen.blit(card_images[card], (player_x, player_y))
            player_x += card_width + card_spacing

        player_total_label = font3.render(f'Total: {hand_total_player}', True, 'yellow')
        screen.blit(player_total_label, (x, 100 + card_height + card_spacing))
        screen.blit(player_label, (x, 100))
        for card in dealer_hand:
            screen.blit(card_images[card], (x, y))
            x += card_width + card_spacing

        stand_probability_label = font3.render("IF YOU CHOOSE TO STAND: ", True, 'yellow')
        screen.blit(stand_probability_label, (40, 200))
        winning_probability_label = font3.render("Probability of Winning: {:.2f}%".format(win_prob * 100), True,
                                                 'yellow')
        screen.blit(winning_probability_label, (30, 250))
        tying_probability_label = font3.render("Probability of Tying: {:.2f}%".format(tie_prob * 100), True, 'yellow')
        screen.blit(tying_probability_label, (30, 300))
        losing_probability_label = font3.render("Probability of Losing: {:.2f}%".format(lose_prob * 100), True,
                                                'yellow')
        screen.blit(losing_probability_label, (30, 350))

        # hit_probability_label = font3.render("IF YOU CHOOSE TO HIT: ", True, 'yellow')
        # screen.blit(hit_probability_label, (650, 200))
        # winning_probability_label_hit = font3.render(" COMING SOON...", True, 'yellow')
        # screen.blit(winning_probability_label_hit, (650, 250))

    buttons = draw_game(active)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if not active:
                if buttons[0].collidepoint(event.pos):
                    active = True
                    initial_deal = True
                    create_deck()
            else:
                if buttons[0].collidepoint(event.pos):
                    dealer_aces = count_aces(dealer_hand)
                    while len(dealer_hand) < 3:
                        if total(dealer_hand) < 17:
                            new_card = draw_card(my_deck, dealer_hand)
                        elif total(dealer_hand) == 17 and dealer_aces > 0:
                            new_card = draw_card(my_deck, dealer_hand)
                        else:
                            break
                    second_deal = True

                if buttons[1].collidepoint(event.pos):
                    dealer_aces = count_aces(dealer_hand)
                    while len(player_hand) < 3:
                        draw_card(my_deck, player_hand)
                    while len(dealer_hand) < 3:
                        if total(dealer_hand) < 17:
                            new_card = draw_card(my_deck, dealer_hand)
                        elif total(dealer_hand) == 17 and dealer_aces > 0:
                            new_card = draw_card(my_deck, dealer_hand)
                        else:
                            break
                    second_deal = True

                if buttons[2].collidepoint(event.pos):
                    active = False
                    second_deal = False

    pygame.display.flip()
pygame.quit()
