1 Title: WarPairsPoker by John Sileo 

2 Description: WarPairsPoker is written in python using pygame to represent a card game. 

2.1 Installation: Latest Version of Python, latest version of Pygame 

3 Rules 

3.1: Objective: Get rid of your hand before your opponent gets rid of their hand. 

3.2 General: If it is your turn and there are no cards played yet this hand, you may choose which mode to play: Either a single card, a pair, or a poker hand. Further plays are restricted to that mode. Furthermore, whatever is played after the first play of each hand, must be of higher rank than whatever was played before it. If a player cannot beat or decline to play on whatever was played last, they can draw one or two cards from the deck, or one of the face-up cards from the pile on the side. 

3.3 Suit Hierarchy: There is a suit hierarchy which from lowest to highest is: diamonds, clubs, hearts and then spades. For singles, the higher suit means a higher rank so a seven of spades is higher than a seven of clubs, but not higher than and eight of clubs. When determining rank for pairs, whichever pair has the spade in it is higher rank than the one that does not. For rank of a straight, flush, or straight flush the value is based on the last card numerically, so a straight of 45678 with the 8 of clubs will beat a straight of 45678 with the 8 of diamonds. Both of these straights are lower value than any straight of 56789 or higher or a higher poker hand. Full houses, and three of a kind use the value of whatever is in the three of a kind so suit hierarchy will never matter for determining rank of which three of a kind or full house is higher. Two pair uses the value of the highest pair when determining value of the two pair.  

3.4 Start of the game/Mulligan: 

To start the game, you are dealt 16 cards and must get rid of three, known as the ‘mulligan’.  The three cards you mulliganed, and the three cards your opponent mulligans, go face-up on the side known as the ‘pile’. Instead of drawing random cards from the deck either player may draw one of these cards in the pile instead of their normal draw. 

3.5 Drawing/Re-draws: 

If you cannot beat something your opponent played, or do not want to beat something your opponent played you may draw one or two cards from the deck, or one card from the face-up pile. Each player also gets one re-draw per game, where they can put the cards that they drew that turn into the face-up pile to draw the same number of cards to replace them. 
 

3.6 All Twos beat all Aces: 

A 2 is the lowest card in the game and has a lower value than all of the other cards, but as the title reads, all 2’s beat all Aces. If you play the Ace of Spades, the highest card in the game, in singles, the only way you can play on it is if you play any 2 on top of it. Additionally, Aces also cannot be played on 2 in every mode of play, so if you play a full house of Twos, your opponent cannot play a full house of Aces. Four of a kind Aces is, however playable because it is a higher rank hand. 

 

3.7 Wrap-Around Straights: 

The highest rank straight in the game would be 10JQKA, but Twos beat Aces, so a straight of JQKA2 is a legal straight that has a higher value. The value of this straight would be a two-high because wrap-around straights always use the value of last card numerically which, in this case would be the 2. Even though the 2 is technically the lowest card in the straight, it is the high-end of this wrap-around straight which makes the straights value a 2-high straight. 

 

3.8 Four of a Kind kicker: 

Four of a kind is a special hand where you can pitch a free card to go with the four of a kind to make a five-card poker hand. You still may play a four of a kind as a four-card poker hand but strategically getting rid your worst card to make a five-card poker hand is very valuable. Also worth mentioning, two pair does not get this option to make a five-card hand and will always play as four cards. Similarly, three of a kind will also always play as three cards. 

3.9 Pass the turn 

If you do not what to play anything and nothing else has been played, you may choose to pass the turn and give your opponent the ability to lead with whatever they want. If the turn was passed to you in this way, you may not pass the turn back. 

4 Features 

4.1 Buttons: Each card has a button with an image of the card on it. The cards in hand are sorted by their value. The middle play area is a display of what was played last and therefore, does not have buttons on them. The game-action buttons are black with gold trim and will only show up if that option is available to you in-game. The teal arrow pointing up or down depicts which player is to act. The options menu is on the left side in the middle of the screen. The options are not necessary to play the game, but contains features to enhance the game experience.  

4.2 Functionality: If you select a card, it will stick out to show that it is selected. Select all the cards you want to select then click play. If the cards you selected are in the middle display area and the arrow is pointing in the opposite direction then your play worked. If not, the play was not a legal play for one reason or another. Check the rules to figure out why, or maybe you have a card selected that you forgot about. Each time a game action is made, new buttons will show what game actions can be taken for the next play. 

4.3 Options Menu 

4.31 Auto-Mull: This option being on means that the AI of the game will calculate the mulligan for both players. The AI is very smart, so if you are trying to learn how to mulligan see what the AI does and try to figure out why the AI mulligans the way that it does. 

4.32 Comp: This option being on means that the AI will play for the top player’s hand. This will only work if you have no cards in the top player’s hand selected. If you have cards selected and click on the Comp Play button your selection will override the computer’s play. 

4.33 Replay game: This option will prompt you to replay the entire game you just played. Useful for testing out different ways of playing the game. 

4.34 Undo: This option will undo the last action taken by a player. Can undo all the way back to the start of the game. 

4.35 Back: This takes you back to the game. If you see this button, you are in the option menu screen and cannot affect the current game. 

4.36 Show This: This option shows what was played this hand. Useful for players planning their moves. 

4.37 Show Last: This option shows what was played last hand. Again, useful for seeing what was played. 

4.38 Alternate Reveal: This option being on means you only see the hand of whoever’s turn it is. This makes you able to play both players without the bias of seeing what is in the other one’s hand. 

4.39 Rules: Displays a quick reference of the rules in case they are forgotten. 

4.40 Concede: Concedes the game for whoever’s turn it is. Useful for going onto the next game if the current game is over. 

5 Technology Overview 

5.1 Python: This was my first python project and my main goal was to create an AI for a game as complicated as this one. I previously did some questions on leetcode.com to get a feel for python. Ultimately, the hardest parts of the code to get correct were the undo button, and figuring out the algorithms for the game and translating them into code for the AI. The undo button needed a lot of revisions to get done because it changes the main variables of the game. Another issue I had was one with soft-copying versus hard-copying. Basically, I did not know of the existence of deep copying and my variables were being changed seemingly out of nowhere. I was very hesitant to post of stack overflow but this was the only time I did for this project and they said that I needed to deep copy and it worked. 

5.2 Canva: This website is used to make banners. Early on into development, I knew I wanted a different look for my buttons. I made an account on canva.com and toyed around a bit with what I could do. Eventually I made a design for all of the buttons and implemented them in my game. 

5.3 Pygame: Pygame is a library used to display a game. Each button has click area of x and y coordinates where you can do a function if you click in the area. What I did first was display the image of the button that I wanted, then change the coordinates of the click area to represent the button. I also was able code hotkeys into the game using pygame. The number keys and letters underneath on the keyboard correspond to the cards in a player’s hand. The arrow keys can change the selected card left or right, and enter clicks on the play button. 

5.4 Installation: You need the most current version of python, and pygame in order to use this application. 

6 How the AI works in steps 

6.1 Mulligan: At the start of the game, you are dealt 16 cards and must get rid of 3 of them. For the mulligan section, only one straight or flush is viable per hand. King, aces and twos, may not be used to make poker hands for your mulligan. Any poker hand that breaks up three or more pairs also cannot be used. Using these rules, the AI will look for viable flushes and viable straights. Any poker hand found will be added to a list of viable poker hands, along with two other numbers. The first number, is the number of outliers. Outliers are cards that do not match any other card in the hand, but also, are not in the poker hand. The second number is the total value of the outliers added up minus the three lowest, known as the “strength of outliers”. The two numbers represent tiebreakers, with outliers being the main tiebreaker and the strength of outliers being the secondary tiebreaker. After all straights and flushes are calculated, the hand with the best tiebreakers is the hand that is chosen. There are also cases where you do not have three cards to mulligan, because all of the cards are either in your poker hand, match other cards in your hand, or they are 2’s, aces, or kings. For these instances, we use a function, which calculates what the AI will do based on each individual hand. This includes breaking up pairs, using the lowest card in a three of a kind, using all 3 cards of a three of a kind, or just choosing a 2, ace or king. Once we find our three cards, the cards get removed from the hand and then the mulligan is complete. 

6.2 Segment:  The goal of this section is to separate the hand into usable information for the AI to make proper game decisions. The segment function of the AI will work similarly to the mulligan function where the AI will not use 2’s, aces, or kings, or break up three pairs to make a poker hand. The mulligan function also only works for 16 cards, whereas the segment function will work for any number of cards. This section of code separates the hand into 8 segments and looks like this: [[2’s, Kings, Aces], [outliers], [pairs], [three of a kind], [four of a kind], [straights], [flushes], [straight flushes]]. Unlike the mulligan algorithm, for this part we may use up to two straights or flushes. Viable flushes and straights are calculated using the same tiebreaker method used in the mulligan section to find the best combination. After the best combination of poker hands are found, the poker hands are removed and put into their respective places in their segment. With the correct poker hands removed, the rest of the cards are then added to each of their respective segments. 

6.3 AI Decision Making: This section determines each game decision the AI will make. If the AI has the choice of playing anything they want, the AI will go down a list of specific things they can play in this order, stopping if one is found. The list is, in order: straight, flush, 5-card “do I win” check, three of a kind, two pair, full house, four of a kind, straight flush, pairs, single cards, and finally draw. This means that if the AI goes first and has a straight, they will always play it. The 5-card “do I win” check is a check that happens if the AI has specifically 5 cards in hand and they make a straight, a flush, or a wrap-around straight. You might notice that a full house is after three of a kind in the order of play. The explanation is that three of a kind, will be played if you have more three of a kind’s than pairs, or, no pairs at all. This means that the AI will rarely play three of a kind and will often skip over it and play the full house. Similarly, the AI will only play two pair if it has a higher poker hand to play after it. If the AI does not have the choice of what mode to play, the AI will be locked into singles, pairs or poker hands, and will only use the code from the respective mode will be used to make decisions. 

6.31 Drawing: Drawing is the last decision on the list of AI decision making and will be done if the AI has no decision based on the code. If the first card drawn is a king, an ace or a card that matches a card in the hand, or the hand has 5 or less cards in it, the AI will draw 1 card. Otherwise, the AI, will choose to draw 2 cards. The AI also has one re-draw per game, and will use it to re-draw if its 2 cards drawn that do not contain a match, and are not a 2, king, or ace. 

6.32 Playing Aggressively to win the game: The AI decision making will only use pairs in the pair section its segment, and singles in the outlier section of its segment and disregard the segment containing 2’s, kings and aces. If a situation arises where the opponent plays a pair that is higher than anything in its pair segment, the AI will figure out if it should play its 2’s, kings, and aces, in a pair. It does this based on how many cards the opponent has in hand and also how many outliers are in its current hand. If the AI decides to play, then it will choose the pair to play and play it, if not the AI will choose to draw. If single cards are the current mode, the AI may also choose to play cards from the twos, kings, and aces section. If the opponent has three or less cards in hand the AI will resort to only playing cards from the 2’s, kings, and aces section if able. 

 

7 Screenshots 

7.1 Top player plays a full house of 3’s, the teal arrow points to the bottom player. Bottom player’s action. 

 

7.2 Bottom player responds with four of a kid 7’s adding the 9 of spades to make a 5-card hand. Action goes back to the top player. Top player cannot beat a four of a kind so he has to draw. 

 

 

7.3 The options menu 

 

 

8 Appendix 

8.1 Why I made this: I have a deep background in card games featuring Pokemon, Magic the Gathering, and poker. I learned a game similar to WarPairsPoker in high school and was unhappy with the rules. I have a bunch of friends that play this game with that I would play with and test new rules. I kept changing the rules to try to make the game more fun and eventually settled on these rules. I probably have around a thousand hours playing this game probably even more including testing WarPairsPoker. My main goal with this project was to create an AI for this very complicated game. The AI is not truly perfect, but it is very capable of playing a very good game. Some of the things it cannot do are, know that it has the highest cards left and use that information, know if all aces have been played so that twos are useless to keep, and know some of the more difficult lines of play that win the game. This was also my first project in coding python. I was looking for jobs for a while after graduating college and did not really find anything that interested me. My friend, Ray, who also plays this game convinced me to learn python. I started out trying to learn on w3schools.com and then started doing some problems on Leetcode.com. I started talking to people in software development and they said that you need projects on your resume to show that you can do the job. While playing WarPairsPoker, I realized that I could just code the game in python which eventually led to making an AI to go along with it. The project took about a year and three months, with most of the time being just thinking about the algorithms to make the AI play the game optimally. 

8.2 Game strategy: The most valuable poker hands in your hand are straights or flushes that don’t use kings, aces, or 2’s. Don’t play straights or flushes that contain kings, aces, or 2’s unless you absolutely have to. You also should not play straight or flushes that break up three or more pairs or three of a kind. If you have no more poker hands, generally you want to be playing pairs. Don’t play pairs of kings or aces unless you are pretty sure you win the game if you play them. Twos are pretty valuable because they beat aces, but if you also have a lot of aces then your twos are not very useful. Twos are also the weakest of the valuable cards (the others being aces and kings) so don’t be afraid to get rid of them. There are a couple 2-card combinations of cards that will guarantee a win in singles, they are as follows: King of spades and any 2, Ace of Spades and any non-2 card or the two of spades, and the two of spades with any ace. There are a couple more combinations and some 3-card combinations that will guarantee a win so be mindful for those. Overall, WarPairsPoker is a very complex game and there are so many possibilities for each hand. There are games where you feel like you have no chance and then you just draw into four of a kind and win. I really enjoy this game and that’s why I made it for my python project. 

8.3 Poker hand value: This game uses elements of poker so the value of the poker hands is as follows: (Lowest) Two pair, Three of a kind, Straight, Flush, Full House (three of a kind and a pair), Four of a kind, Straight Flush (Highest). 

 
