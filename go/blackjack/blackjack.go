package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {

	var point int ;

	switch card {
	case "ace":
		point = 11
	case "two":
		point = 2
	case "three":
		point = 3
	case "four":
		point = 4
	case "five":
		point = 5
	case "six":
		point = 6
	case "seven":
		point = 7
	case "eight":
		point = 8
	case "nine":
		point = 9
	case "ten":
		point = 10
	case "jack":
		point = 10
	case "queen":
		point = 10
	case "king":
		point = 10
	case "joker":
		point = 0
	}
	return point
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {

	var point int = ParseCard(card1) + ParseCard(card2)
	var dp int = ParseCard(dealerCard)

	var decision string;

	switch {
	case point < 12:
		decision = "H"
	case 12 <= point && point <= 16:
		if dp >= 7 {
			decision = "H"
		} else {
			decision = "S"
		}
	case 17 <= point && point <= 20:
		decision = "S"
	case point == 21:
		if dealerCard == "ace" ||dealerCard == "jack" || dealerCard == "queen" || dealerCard == "king"|| dealerCard == "joker"{
			decision = "S"
		} else {
			decision = "W"
		}
	case card1 == "ace" && card2 == "ace":
		decision = "P"
	}
	return decision
}
