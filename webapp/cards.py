import random


# does what it says on the tin
def shuffle_deck(deck):
    random.shuffle(deck)


# pick card(s) - call this method multiple times to draw multiple unique cards from the deck
def get_card(deck):
    num = random.randint(0, len(deck) - 1)  # the minus 1 fixes the zero indexed array out-of-range error
    card = deck[num]
    del (deck[num])  # so we don't get the same card twice if we're calling this multiple times for the same hand
    rev = random.randint(-1, 1)  # is card reversed? zero (false) or 1 (true)
    drawn = (card, rev)  # tuple of card dictionary + 1 or zero for reversal
    return drawn


# array of dicts for each card
def get_deck():
    deck = [
        {"name": "Sun", "url": "sun", "image": "images/1.jpg",
         "desc": "Creativity,Consciousness,Brilliance",
         "rdesc": "Stale, Selfish, Immaturity",
         "cbd_desc": "Freedom from conventions and norms. Something or someone unique and exceptional. Options kept open. Giving up control, spontaneity. Uncertainty, attention to the here and now. Going on a trip.",
         "sequence": 1},

        {"name": "Moon", "url": "moon", "image": "images/2.jpg",
         "desc": "Care, Intuition, Gentleness",
         "rdesc": "Indecision, Negligence, Harshness",
         "cbd_desc": "The start of something. Beginner’s luck. Having various tools and means at our disposal. Use of supernatural forces. Creating reality with mind power. Training and acquisition of practical skills. Improvisation. Display or show for other people.",
         "sequence": 2},

        {"name": "Mercury", "url": "mercury", "image": "images/3.jpg",
         "desc": "Learn, Speaking, Moving",
         "rdesc": "Ignore, Silence, Stuck",
         "cbd_desc": "Wisdom combining intellect and intuition. A spiritual mother. A woman hiding her strengths in a world of men. Modesty. Secrets, something hidden, mystery. Getting a hint of something which remains largely unknown. Impossible to give a definite answer now.",
         "sequence": 3},

        {"name": "Venus", "url": "venus", "image": "images/4.jpg",
         "desc": "Beauty, Manners, Balance",
         "rdesc": "Vanity, Rudeness, Unbalanced",
         "cbd_desc": "Abundance, growth, productivity. Natural or human touch within an artificial framework. Emotional intelligence. Protection and care. Motherhood. A powerful female figure. Strong feminine identity.",
         "sequence": 4},

        {"name": "The Emperor", "url": "the_emperor", "image": "images/5.jpg",
         "desc": "Stability. Power. Being in control of yourself/situation. Ambition. Leadership. Firmness of purpose. A dominant male person.",
         "rdesc": "Loss of control. Emotional immaturity and bondage to parents. Possibility of being defrauded of one's inheritance. Ill-temper. Stubbornness. Fall. Loss of wealth. Megalomaniac.",
         "cbd_desc": "Practical and material achievements. Matters relating to the workplace or source of income. Authority and control, a commanding position. A protective father figure, patron or sponsor. Assertiveness. Military affairs.",
         "sequence": 5},

        {"name": "The Pope", "url": "the_pope", "image": "images/6.jpg",
         "desc": "Wisdom, endurance, persistence, patience, help from superiors, good advice, a good teacher, organization, peace, goodness of heart.",
         "rdesc": "Tendency to over criticize or being unduly concerned with the morals of others. Incapable of dealing efficiently with practical matters, especially finances. Unconventionality, illogical, superstitious, unable to behave coherently.",
         "cbd_desc": "Teacher, instructor, or counselor. Education and knowledge, academic expertise. Organized religion, conventional medicine or psychology. Spiritual father. Consultation or treatment by a specialist. Marriage.",
         "sequence": 6},

        {"name": "The Lover", "url": "the_lover", "image": "images/7.jpg",
         "desc": "Union, decision, choice, marriage, love, the union of opposites, attraction. Balance, openness to inspiration. Harmony of the inner and outer aspect of life.",
         "rdesc": "Disorder, failure, danger of a broken relationship or a wrong choice, quarrels, infidelity. Emotional instability. Dangerous temptation.",
         "cbd_desc": "Love, amorous relationship. Emotional entanglement. Need to make a choice, or to disengage oneself from past influences. Inclinations of the heart correspond to the will of heaven. Small steps actually taken are the visible signs of inner desire.",
         "sequence": 7},

        {"name": "The Chariot", "url": "the_chariot", "image": "images/8.jpg",
         "desc": "Triumph of the will, to surmount opposition, success. Self-control, ability to determinate the own destiny. Good news. Great physical and mental strength. Swiftness. The transitory power. Travel.",
         "rdesc": "Generalized disorder. Illness. Dangerous restlessness. Danger of a violent accident.",
         "cbd_desc": "Victory or an achievement putting the querent in a strong and protected position. Ambition, energy, motivation to move forward. Public honor. Power and high status.",
         "sequence": 8},

        {"name": "Justice", "url": "justice", "image": "images/9.jpg",
         "desc": "Conformity to moral rightness in action or attitude. The power to maintain equilibrium between the necessities and responsibilities of life. Justice, balance, adjustment. In order to keep things balanced certain things must be sacrificed. May refer to law matters, trials, marriages, divorces, etc. Integrity, moderation.",
         "rdesc": "Fanaticism, injustice, inequality, legal complications. Harsh judgment. Insecurity, imbalance.",
         "cbd_desc": "Law and order, legal and court issues. A fair and balanced judgment. A developed conscience. Rationality, reasoning by clear rules and common norms. Touch of grace and humanity beyond the objective considerations.",
         "sequence": 9},

        {"name": "The Hermit", "url": "the_hermit", "image": "images/10.jpg",
         "desc": "Prudence, wisdom, patience, silence, spiritual advance, divine inspiration, circumspection, retirement from participation in current events, solitude. Pilgrimage. Quest for wisdom. Could be a teacher. A period of spiritual and intellectual personal development.",
         "rdesc": "Immaturity, viciousness, darkness, stubbornness, deception, betrayal, too much or insufficient prudence. Misanthrope, misogyny, celibacy, excessively shy person. Hidden enemies.",
         "cbd_desc": "A quest for truth or for spiritual understanding. Concentrating on a clear purpose. Caution, careful examination. Self-privation for the sake of a meaningful cause. Loyalty to principles, strong faith.",
         "sequence": 10},

        {"name": "The Wheel of Fortune", "url": "the_wheel_of_fortune", "image": "images/10.jpg",
         "desc": "Change, evolution, success, good fortune, fate. Happiness, abundance. New conditions.",
         "rdesc": "Retarded progress. Delays, setbacks.",
         "cbd_desc": "Change in circumstances and position. A rise after a fall. Gambling, putting faith in capricious luck. Life cycles, closure of circles. Adapting to the routine of everyday life. A hint to previous incarnations.",
         "sequence": 11},

        {"name": "Strength", "url": "strength", "image": "images/11.jpg",
         "desc": "Sublimation or regulation of the passions and lower instincts. Power, energy, great love. Spirit ruling over matter. Action, courage. Success. Powerful will and great physical strength. The inner strength to tame the lust.",
         "rdesc": "Discord, ruin, stubbornness, abuse of power. Weakness.",
         "cbd_desc": "Power and courage to face challenges. Controlled expression of creative urges, drives and desires. Mobilization of inner resources towards a common goal. Taking risks.",
         "sequence": 12},

        {"name": "The Hanged Man", "url": "the_hanged_man", "image": "images/12.jpg",
         "desc": "Fortitude, wisdom. Self-imposed limitations. Voluntary sacrifice leading to new insight or initiation through tribulations and ordeals. Redemption through sacrifice, loss. Prophetic power. Suspended decisions. Choice requiring contemplation.",
         "rdesc": "Arrogance, egotism, resistance to spiritual influences. Absorption in physical matters. Wasted effort. False prophecy. Failure.",
         "cbd_desc": "Seeing things from a unique point of view. Enduring difficulties for a worthy cause. A period of deep self examination. Passivity, acceptance of reality even if it is the opposite of what one expects.",
         "sequence": 13},

        {"name": "Death", "url": "death", "image": "images/13.jpg",
         "desc": "Complete transformation. Death and rebirth. The end of something. Evolution from one state to another.",
         "rdesc": "Stagnation, death, petrification. Incurable ill person. Broken marriage.",
         "cbd_desc": "The end of something whose time has come. Cutting off past influences or attachment to dominant figures. Giving up the superfluous and keeping only the essential. Disintegration of the old makes room for the new.",
         "sequence": 14},

        {"name": "Temperance", "url": "temperance", "image": "images/14.jpg",
         "desc": "Careful consideration, patience, moderation, adaptation, tempering, self-control. To temper, to combine, to exercise self-restraint. Patience, bringing together two opposites carefully blending them. Good marriage. Working in harmony with others, good management. Something is brewing. Great talent and creative involvement. Striving for Transcendence through works. Alchemy. The union of opposites refined by the fire of the Will.",
         "rdesc": "Disorder, conflict, unfortunate combinations, quarrels. Possibility of shipwreck.",
         "cbd_desc": "Reconciliation, compromise, relaxation of tensions. Integration of opposites. Ability to do the seemingly impossible. A slow process of distillation and improvement. Patience, perseverance. Self-improvement.",
         "sequence": 15},

        {"name": "The Devil", "url": "the_devil", "image": "images/15.jpg",
         "desc": "Fate (wrong or good). Seductive power, blind impulse. Temptation, obsession. Sexual deviation. A disturbed mental state. Earthly passions are turning you inside and out.",
         "rdesc": "Harmful, fate, wrong use of force, weakness, blindness, disorder. Malefic effects. The pathetic human condition of choosing illusion over truth.",
         "cbd_desc": "A burst of creativity. Paradoxes and contradictions. Irony and mocking of common norms. Acting from desires, passions and impulses. Moving on from a past family trauma.",
         "sequence": 16},

        {"name": "The House of God (The Tower)", "url": "the_house_of_god", "image": "images/16.jpg",
         "desc": "Sudden changes without choice, collapse, escape from prison or bondage, accident. Plans will fall, intentions will break down. Bankruptcy. Sudden death. Enlightenment.",
         "rdesc": "Complete confusion. The gain of freedom at great cost. False accusations, oppression.",
         "cbd_desc": "Breaking up of solid structures. Getting free from confinement. Sudden breakthrough after long preparations. Sparkling sexual encounter. Success lies in simplicity and modesty.",
         "sequence": 17},

        {"name": "The Star", "url": "the_star", "image": "images/17.jpg",
         "desc": "Hope, unexpected help, insight and clarity of vision, inspiration, flexibility. Great love will be given and received. Good health.",
         "rdesc": "Arrogance, pessimism, stubbornness. Illness. Error of judgment.",
         "cbd_desc": "Openness, simplicity, return to nature. Purity, honesty. Showing yourself “as you are,” accepting one’s body and desires. Generosity. Luck from heaven. Intuitive feeling of guidance or energy coming from a higher plane.",
         "sequence": 18},

        {"name": "The Moon", "url": "the_moon", "image": "images/18.jpg",
         "desc": "Intuition, threshold of an important change, arduous and obscure path, development of psychic powers.",
         "rdesc": "Unforeseen perils, secret foes, hallucination, self-deception, hysteria, disorientation. Blackmailer.",
         "cbd_desc": "Deep emotions, perhaps related to a mother or feminine figure. A different experience of reality. Longing for the unreachable. Finding one’s hidden strengths. Occupation with the remote past. A hidden treasure.",
         "sequence": 19},

        {"name": "The Sun", "url": "the_sun", "image": "images/19.jpg",
         "desc": "Glory. Material happiness. Happy marriage or relationship, collaboration. Success. Pleasure. Energy, motivation, inspiration to others.",
         "rdesc": "Annoyances, disguise. Arrogance. Broken engagement or lost job.",
         "cbd_desc": "Light and warmth, abundance, blessings. Pleasant feeling, emotional or physical healing. Partnership, trust, sharing, brotherhood. Human touch. An ideal father figure. Matters relating to children. Setting limits in a moderate and non-oppressive way.",
         "sequence": 20},

        {"name": "Judgement", "url": "judgement", "image": "images/20.jpg",
         "desc": "Radical change, resurrection to a new life. A work (or life) well done. Willingness to try something new. Good judgment and discernment. Creative power and influence over family and career. Forgiveness. Awakening. Legal judgments, in one's favor.",
         "rdesc": "Spiritual vacillation, weakness, wrong judgment. Illness. Separation. Adverse legal judgment.",
         "cbd_desc": "Revelation, enlightenment, a new understanding. A turning point in a therapy process. Healing of a family relationship. Disclosure, secrets revealed, publicity. Birth of a baby or of a new thing.",
         "sequence": 21},

        {"name": "The World", "url": "the_world", "image": "images/21.jpg",
         "desc": "Success granted. Rewards. Travel, emigration, change of residence.",
         "rdesc": "Hindrances, stagnation. Hard work to bring success.",
         "cbd_desc": "Completion of a process. Balanced activity and achievements in various domains. Contact with far places. Harmony and correspondence between different planes. Pregnancy, something new is about to be born. The Dance of Life.",
         "sequence": 22},

        {"name": "King of Swords", "url": "king_of_swords", "image": "images/22.jpg",
         "desc": "A very good ally or counselor - clever and self-controlled with some authority. Also they can be modern, analytical and very strong. The card may also mean a lawsuit.",
         "rdesc": "Deceitful and malicious person. They may be a dangerous enemy, violent and powerful.",
         "cbd_desc": "",
         "sequence": 23},

        {"name": "Queen of Swords", "url": "queen_of_swords", "image": "images/23.jpg",
         "desc": "A graceful but stern person. They have keen insight and good judgment. May be a dancer, a widow/er or a childless person. This card also means privation and mourning.",
         "rdesc": "Playfully mischievous. Dangerous enemy. Jealous and narrow-minded person.",
         "cbd_desc": "",
         "sequence": 24},

        {"name": "Knight of Swords", "url": "knight_of_swords", "image": "images/24.jpg",
         "desc": "Audacious, clever and gallant; spirited young person. They may be domineering and unstable but they have the better intentions.",
         "rdesc": "Harsh, fanatic, extravagant. Tyrannic and aggressive. Dangerous enemy.",
         "cbd_desc": "",
         "sequence": 25},

        {"name": "Page of Swords", "url": "page_of_swords", "image": "images/25.jpg",
         "desc": "Logic and penetrating young person. Mentally and physically dexterous. Spying. Messages.",
         "rdesc": "Frivolous, revengeful and cunning person. Indiscretion. Impotence. Unforeseen perturbation.",
         "cbd_desc": "",
         "sequence": 26},

        {"name": "Ace of Swords", "url": "ace_of_swords", "image": "images/26.jpg",
         "desc": "Conquest. Triumph through trouble. Intense activity. Gestation or parturition.",
         "rdesc": "Disaster or conquest followed by disaster. Great loss. Violent death. Infertility.",
         "cbd_desc": "",
         "sequence": 27},

        {"name": "Two of Swords", "url": "two_of_swords", "image": "images/27.jpg",
         "desc": "Peace. Balanced forces. Indecision. Strength. Friendship.",
         "rdesc": "Disloyalty. Change, sometimes in the wrong direction. Quarrel",
         "cbd_desc": "",
         "sequence": 28},

        {"name": "Three of Swords", "url": "three_of_swords", "image": "images/28.jpg",
         "desc": "Sorrow. Separation, quarrel, tears. Delay. Absence.", "rdesc": "Confusion, loss, error.",
         "cbd_desc": "",
         "sequence": 29},

        {"name": "Four of Swords", "url": "four_of_swords", "image": "images/29.jpg",
         "desc": "Truce. Solitude. Stagnation. Recovering from illness. Exile. Retreat.",
         "rdesc": "Renewed activity. Surprise. Prudence and economy are advised.",
         "cbd_desc": "",
         "sequence": 30},

        {"name": "Five of Swords", "url": "five_of_swords", "image": "images/30.jpg",
         "desc": "Defeat. Failure. Loss. Powerlessness. Separation. Lies. Death.",
         "rdesc": "Risk of loss or defeat. Funeral. Weakness.",
         "cbd_desc": "",
         "sequence": 31},

        {"name": "Six of Swords", "url": "six_of_swords", "image": "images/31.jpg",
         "desc": "Science. Journey by water, revelation, study. Intelligent effort. Success after anxiety.",
         "rdesc": "Stagnation. Unfavorable result. Intellectual pride.",
         "cbd_desc": "",
         "sequence": 32},

        {"name": "Seven of Swords", "url": "seven_of_swords", "image": "images/32.jpg",
         "desc": "Futility. Partial or unpredictable result. Dreams, vacillation. Travel by land.",
         "rdesc": "Quarrels. Slanders. Disenchantment in family or friendship.",
         "cbd_desc": "",
         "sequence": 33},

        {"name": "Eight of Swords", "url": "eight_of_swords", "image": "images/33.jpg",
         "desc": "Interference. Restriction. Temporal sickness or captivity. Indecision.",
         "rdesc": "New beginnings. Freedom from the past bondage.",
         "cbd_desc": "",
         "sequence": 34},

        {"name": "Nine of Swords", "url": "nine_of_swords", "image": "images/34.jpg",
         "desc": "Cruelty. Suffering. Misery. Sickness. Martyrdom. Burden. May be death of a loved one.",
         "rdesc": "Patience, faithfulness, unselfishness.",
         "cbd_desc": "",
         "sequence": 35},

        {"name": "Ten of Swords", "url": "ten_of_swords", "image": "images/35.jpg",
         "desc": "Ruin. Total defeat. Death. The end of an illusion.", "rdesc": "Transitory success. Improvement.",
         "cbd_desc": "",
         "sequence": 36},

        {"name": "King of Disks", "url": "king_of_disks", "image": "images/36.jpg",
         "desc": "A married person, wealthy and clever in money matters. Patient and laborious, they are an experienced chief and a reliable ally.",
         "rdesc": "Vicious and greedy person. Beware of gamblers or speculators. Easy to bribe, possibly a dangerous person.",
         "cbd_desc": "",
         "sequence": 37},

    ]
    return deck
