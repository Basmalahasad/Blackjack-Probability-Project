# Blackjack-Probability-Project
### This project is developing a basic strategy for a modified version of blackjack using probability and simulation.
---

### What is blackjack?
Blackjack is a popular casino card game where the goal is to have a hand value of 21 or as close to 21 as possible without going over. Players are dealt two cards and can choose to "hit" to receive additional cards or "stand" to keep their current hand. The dealer also receives cards and must follow specific rules for drawing additional cards. If a player's hand exceeds 21, they "bust" and lose the game. The player with the highest hand value without busting wins the game.

### Introduction
Blackjack is a popular card game that is played in casinos worldwide. The game involves making decisions based on the cards dealt to you and the dealer's up-card. Unlike other casino games, such as roulette or slot machines, blackjack requires skill and strategy to increase your chances of winning. Our version of blackjack is different in these ways:

* The dealer and the player can have a maximum of three cards in hand, meaning that they are only allowed to perform one action each
* The player and the dealer may take another card (hit) or not take another card (stand)
* Both cards of the player and the dealer are visible
* We are playing using only one deck 

### Purpose 
*The best strategy answers the question "Is it in our best interest to hit or stand?"*

Knowing a basic strategy of blackjack will help you make better decisions at the table. The basic strategy is a mathematically calculated set of rules that tells you what to do in every possible situation in the game. This means that you don't have to rely on guesswork or hunches when playing blackjack. By following the basic strategy, you can minimize your losses and maximize your winnings. Moreover, knowing the basic strategy will help you reduce the house edge. The house edge is the advantage that the casino has over the player in any casino game. In blackjack, the house edge can be as low as 0.5% if you use the basic strategy correctly. This means that for every $100 that you bet, you can expect to lose only $0.50 on average. In contrast, if you don't use the basic strategy, the house edge can be as high as 5%, which means that you can expect to lose $5 for every $100 that you bet.

### Progress
In recent weeks, significant progress has been made in the development of our blackjack game, achieved through a series of ordered steps:

* Conducted extensive research into the game's rules 
* Studied various programming languages and chose Python for its flexibility and functionality
* Developed the game's basic framework, which included the logic for dealing cards, calculating scores, and determining winners
* Created a program to calculate the probability of winning, losing, or tying in the case where the player chooses to stand 
* Designed a simple user interface for the game

### Logic
The code creates the our modified version  of blackjack that pits the player against a computer dealer. The player is presented with the options to "hit" or "stand", meaning to draw another card or keep their current hand. The probability of winning, losing, or tying is shown for each option, and suggests what would be in the best interest of player. The current code uses theoretical probability to calculate the probability of the player winning, losing, or tying, based on the cards that have been drawn and the remaining cards in the deck. When the player opts to "stand", the program executes four primary checks: the player has a natural 21, the dealer busts, the dealer gets 21, and the dealer not busting nor reaching 21. The program determines the probability of the player or the dealer attaining each scenario and leverages these probabilities to compute the likelihood of winning, losing, or tying.

### What's next?
* Our current task involves computing the probability of winning, losing, and tying in the event that the player decides to "hit" during the game.
* Find the empirical probability of winning, losing, or tying. This can be achieved using Pandas to iterate over all possible combinations of player and dealer hands and recording the outcomes of each combination, specifically wins, ties, and losses. 
* Answer questions comparing the theoretical and empirical probability and our version of the game to the original 
* Utilize the outcomes of our analysis to create a fair game with no house edge. By analyzing the probability of each outcome and adjusting the rules of the game, we can ensure that both the player and the dealer have an equal chance of winning. 


***Support for this project was provided by The Women's Advancement Initiative's Dorothy Goodwin Scholars Program, which was made possible thanks to a generous bequest from Dorothy Goodwin. The Women's Advancement Initiative at the University of Hartford is proud to continue the legacy of advancing each woman's potential in the Hartford College for Women tradition.*** 
