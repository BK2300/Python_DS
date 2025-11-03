START

INITIALIZE deck with all UNO cards
SHUFFLE deck

CREATE player_list
FOR each player IN player_list DO
    DEAL 7 cards to player
END FOR

SET discard_pile = top card from deck
SET active_color = color of discard_pile
SET play_direction = "clockwise"
SET turn_index = 0

WHILE no player has an empty hand DO
    SET current_player = player at position turn_index
    DISPLAY current_player's hand
    DISPLAY "Current color: ", active_color

    IF current_player has a card that matches (active_color OR number/symbol on discard_pile) THEN
        current_player chooses a valid card
        PLAY that card
        PUSH card to discard_pile
        UPDATE active_color = color of that card

        IF the card is a special card THEN
            CASE card_type OF
                "Reverse":
                    TOGGLE play_direction
                "Skip":
                    NEXT player is skipped
                "Draw Two":
                    NEXT player draws 2 cards
                "Wild":
                    current_player chooses a new active_color
                "Wild Draw Four":
                    current_player chooses a new active_color
                    NEXT player draws 4 cards
            END CASE
        END IF

    ELSE
        current_player draws one card from deck
        IF this card can be played THEN
            PLAY that card immediately
        ELSE
            DISPLAY "No valid cards — turn ends"
        END IF
    END IF

    IF current_player has 1 card left THEN
        DISPLAY current_player's name, " says UNO!"
    END IF

    IF current_player has 0 cards left THEN
        DISPLAY current_player's name, " wins the game!"
        BREAK
    END IF

    IF play_direction == "clockwise" THEN
        turn_index = (turn_index + 1) mod number_of_players
    ELSE
        turn_index = (turn_index - 1 + number_of_players) mod number_of_players
    END IF

END WHILE

DISPLAY "Game over"

END
