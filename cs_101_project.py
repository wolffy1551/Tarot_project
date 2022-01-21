import random

deck = [
	{"name": 'The Fool', 'Upright': 'Beggingings, Possibilites, Pleasure, Adventure, Opportunity',
	 'Reversed': 'Indecision, Hesitation< Injustice, Apathy, Bad Choice'},
	{"name": 'The Magician', 'Upright': 'Creativity, Self-Confidence, Dexterity, Sleight of Hand, Will Power, Skill',
	 'Reversed': 'Delay, Unimaginative, Insecurity, Lack of Self_confidence'},
	{"name": 'The Empress', 'Upright': 'Development, Accomplisment, Action, Evolution',
	 'Reversed': 'Inaction, Lack of Concentration, Vacillaton, Anxiety, Infidelity'},
	{"name": 'The Emperor', 'Upright': 'Authority, Structure, Control', 'Reversed': 'Tyranny, Rigidity, Coldness'},
	{"name": 'The High Priestess', 'Upright': 'Knowledge, Wishom, Learning, Intution, virtue, Purity',
	 'Reversed': 'Selfishness, Shallowness, Misunderstanding, Ignorance'},
	{"name": 'The Hierophan', 'Upright': 'Mercy, Conformity, Forgiveness, Inspiration',
	 'Reversed': 'Vulnerability, Foolish, Generosity, Frailty'},
	{"name": 'The Lovers', 'Upright': 'Harmony, trust, Romance, Optimism, Honor , Love',
	 'Reversed': 'Seperation, Frustration, Unreliability, Fickelness, Untrustworthy'},
	{"name": 'The Chariot', 'Upright': 'Perseverance, Rushed Decision, Turmoil,Vengeance, Adversity',
	 'Reversed': 'Vanquishment, Defeat, Failure, Unsuccessful'},
	{"name": 'The Hermit', 'Upright': 'Inner Strength, Prudence, Withdrawal, Caution, Vigilance',
	 'Reversed': 'Hastiness, Rashness, Immaturity, Imprudence, Foolishness'},
	{"name": 'Strength', 'Upright': 'Courage, Conviction, Strength, Determination, Action, Heroism',
	 'Reversed': 'Pettiness, Sickness, Unfaithfulness, Weakness'},
	{"name": 'Justice', 'Upright': 'Equality, Rightneousness, Virtue, Honor, Harmony, Balance',
	 'Reversed': 'False Accusation, Unfairness, Abuse, Biased'},
	{"name": 'The Wheel of Fortune', 'Upright': 'Unexpected events, Advancement, Destiny, Fortune, Progress',
	 'Reversed': 'Interruption. Outside, Influences, Failure, Bad Luck'},
	{"name": 'The Moon', 'Upright': 'Deception, Disillusionment, Trickery, Error, Danger, Disgrace',
	 'Reversed': 'Trifling Mistakes, Deception, Discovered Negative Advantage'},
	{"name": 'The Sun', 'Upright': 'Accomplishment, Success, Love, Joy, Happy Marriage, Satisfaction',
	 'Reversed': 'Lonleiness, Cancleled Plans, Unhappiness, Break Ups'},
	{"name": 'The Star', 'Upright': 'Balance, Pleasure, Optimism, Insight, Spirtual love, Hope, Faith',
	 'Reversed': 'Disappointment, Bad Luck, Imbalance, Broken Dreams'},
	{"name": 'The Devil', 'Upright': 'Downfall, Unexpected Failure, Controversy, Disaster, lll tempered ',
	 'Reversed': 'Release, Enlightenment, Divore, Recovery'},
	{"name": 'The Hanged Man', 'Upright': 'Change, Reversal, Broedom, Improvement, Rebirth, Suspension, Change',
	 'Reversed': 'False Prophecy, Useless Sacrifice, Unwillingess'},
	{"name": 'Death', 'Upright': 'Unexpected Change, Loss, Failure, Transformation, Death, Bad Luck',
	 'Reversed': 'Immobility, SLow changes, Cheating, Death, Stagnation'},
	{"name": 'Temperance', 'Upright': 'Patience, Good Influence, Confidecne, Moderation',
	 'Reversed': 'Conflict, Disunion, Frustration, Impatience, Discord'},
	{"name": 'The Tower', 'Upright': 'Disruption, Abandonment, Bankruptcy, Downfaill, Unexpected Events',
	 'Reversed': 'Entrapment, Imprisonment, Old Ways, Rustic'},
	{"name": 'Judgement', 'Upright': 'Awakening, Renewal, Rejuvenation, Rebirth, Improvement',
	 'Reversed': 'Indecision, Death, Failure, Ill-Health, Theft, Worry'},
	{"name": 'The World', 'Upright': 'Perfection, Recoginition, Success, Fulfillment, Eternal Life',
	 'Reversed': 'Lack of Vision, Disappointment, Imperfection'},
]

number_card = input("Hello my friend. How many cards would you like in your spread today? ")
card_amount = int(number_card)
spread = []
num = random.randint(1, len(deck)-1)
card = deck[random.randint(1, len(deck)-1)]
inverse = random.randint(-1, 0)
defs = []
names = []
collective = {}


class TarotHand():
	def __init__(self):
		pass

	def tarot_spread(self, card_amount):
		self.card_amount = card_amount

		# print()

		while len(spread) < int(card_amount):
			spread.append(deck[num])
			del deck[num]
		for object in spread:
			names.append(object["name"])
			if object["name"] in names:
				pass

		return str(names)

	def tarot_visual(self, spread):

		for object in spread:
			if inverse == -1:
				defs.append(object["Reversed"])
			else:
				defs.append(object["Upright"])
		return str(defs)

	def printable(self, defs, names):
		global collective

		for name in names:
			for things in defs:
				if things not in collective:

					collective[name] = things
				if things in collective:
					pass
		print(defs)
		return  collective


tarot = TarotHand()
print(tarot.tarot_spread(card_amount))
print(tarot.tarot_visual(spread))
print(tarot.printable(defs, names))
