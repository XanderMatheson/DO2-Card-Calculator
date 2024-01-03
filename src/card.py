'''
Decked Out Cards

Each Card includes every attribute to enable easy counting of
'''

from math import inf


class Card:
    def __init__(self, name):
        self.name = name
        self.ember_cost = 0
        self.crown_cost = 0
        self.clank_block = 0
        self.hazard_block = 0
        self.treasure_drops = 0
        self.ember_drops = 0
        self.sprint = 0
        self.regen = 0
        self.jump = 0

    def __repr__(self):
        return self.name + " card"


class Sneak(Card):
    name = "\033[90mSneak\033[0m"

    def __init__(self):
        super().__init__(Sneak.name)
        self.ember_cost = 7
        self.clank_block = 2


class Stability(Card):
    name = "\033[90mStability\033[0m"

    def __init__(self):
        super().__init__(Stability.name)
        self.ember_cost = 8
        self.hazard_block = 2


class TreasureHunter(Card):
    name = "\033[90mTreasure Hunter\033[0m"

    def __init__(self):
        super().__init__(TreasureHunter.name)
        self.ember_cost = 9
        self.treasure_drops = 4


class EmberSeeker(Card):
    name = "\033[90mEmber Seeker\033[0m"

    def __init__(self):
        super().__init__(EmberSeeker.name)
        self.ember_cost = 10
        self.ember_drops = 2


class MomentOfClarity(Card):
    name = "\033[90mMoment of Clarity\033[0m"

    def __init__(self):
        super().__init__(MomentOfClarity.name)
        self.ember_cost = 6
        self.clank_block = 2
        self.hazard_block = 2
        self.treasure_drops = 4
        self.ember_drops = 2


class Evasion(Card):
    name = "\033[92mEvasion\033[0m"

    def __init__(self):
        super().__init__(Evasion.name)
        self.ember_cost = 16
        self.clank_block = 4


class TreadLightly(Card):
    name = "\033[92mTread Lightly\033[0m"

    def __init__(self):
        super().__init__(TreadLightly.name)
        self.ember_cost = 18
        self.hazard_block = 4


class FrostFocus(Card):
    name = "\033[92mFrost Focus\033[0m"

    def __init__(self):
        super().__init__(FrostFocus.name)
        self.ember_cost = 20
        self.ember_drops = 4


class LootAndScoot(Card):
    name = "\033[92mLoot & Scoot\033[0m"

    def __init__(self):
        super().__init__(LootAndScoot.name)
        self.ember_cost = 20
        self.treasure_drops = 7
        self.sprint = 15


class SecondWind(Card):
    name = "\033[92mSecond Wind\033[0m"

    def __init__(self):
        super().__init__(SecondWind.name)
        self.ember_cost = 22
        self.regen = 15
        self.sprint = 15


class BeastSense(Card):
    name = "\033[92mBeast Sense\033[0m"

    def __init__(self):
        super().__init__(BeastSense.name)
        self.ember_cost = 24
        self.clank_block = -1


class BoundingStrides(Card):
    name = "\033[92mBounding Strides\033[0m"

    def __init__(self):
        super().__init__(BoundingStrides.name)
        self.ember_cost = 26
        self.hazard_block = 2
        self.jump = 120


class RecklessCharge(Card):
    name = "\033[92mReckless Charge\033[0m"

    def __init__(self):
        super().__init__(RecklessCharge.name)
        self.ember_cost = 28
        self.clank_block = -1  # Assumes the shrieker is activated
        self.hazard_block = -2
        self.ember_drops = 10


class Sprint(Card):
    name = "\033[92mSprint\033[0m"

    def __init__(self):
        super().__init__(Sprint.name)
        self.ember_cost = 30
        self.sprint = 60


class NimbleLooting(Card):
    name = "\033[92mNimble Looting\033[0m"

    # todo - implement treasure for each clank blocked
    def __init__(self):
        super().__init__(NimbleLooting.name)
        self.ember_cost = 32
        self.clank_block = 1


class SmashAndGrab(Card):
    name = "\033[92mSmash & Grab\033[0m"

    def __init__(self):
        super().__init__(SmashAndGrab.name)
        self.ember_cost = 34
        self.clank_block = -2
        self.treasure_drops = 13


class Quickstep(Card):
    name = "\033[92mQuickstep\033[0m"

    def __init__(self):
        super().__init__(Quickstep.name)
        self.ember_cost = 36
        self.clank_block = 2
        self.sprint = 15
        self.quickdraw = 1


class SuitUp(Card):
    name = "\033[92mSuit Up\033[0m"

    def __init__(self):
        super().__init__(SuitUp.name)
        self.ember_cost = 38


class AdrenalineRush(Card):
    name = "\033[92mAdrenaline Rush\033[0m"

    def __init__(self):
        super().__init__(AdrenalineRush.name)
        self.ember_cost = 40
        self.hazard_block = -1


class EerieSilence(Card):
    name = "\033[94mEerie Silence\033[0m"

    def __init__(self):
        super().__init__(EerieSilence.name)
        self.ember_cost = 42
        self.clank_block = 8
        self.hazard_block = 2


class DungeonRepairs(Card):
    name = "\033[94mDungeon Repairs\033[0m"

    def __init__(self):
        super().__init__(DungeonRepairs.name)
        self.ember_cost = 44
        self.clank_block = -1
        self.hazard_block = 7


class Swagger(Card):
    name = "\033[94mSwagger\033[0m"

    def __init__(self):
        super().__init__(Swagger.name)
        self.ember_cost = 46
        self.treasure_drops = 10
        self.ember_drops = 10


class ChillStep(Card):
    name = "\033[94mChill Step\033[0m"

    # todo - figure this one out
    def __init__(self):
        super().__init__(ChillStep.name)
        self.ember_cost = 48


class SpeedRunner(Card):
    name = "\033[94mSpeed Runner\033[0m"

    def __init__(self):
        super().__init__(SpeedRunner.name)
        self.ember_cost = 50
        self.ember_drops = 8


class EyesOnThePrize(Card):
    name = "\033[94mEyes on the Prize\033[0m"

    def __init__(self):
        super().__init__(EyesOnThePrize.name)
        self.ember_cost = 52


class Haste(Card):
    name = "\033[94mHaste\033[0m"

    def __init__(self):
        super().__init__(Haste.name)
        self.ember_cost = 56


class ColdSnap(Card):
    name = "\033[94mCold Snap\033[0m"

    def __init__(self):
        super().__init__(ColdSnap.name)
        self.ember_cost = 58
        self.hazard_block = -3


class SilentRunner(Card):
    name = "\033[94mSilent Runner\033[0m"

    # todo - figure this out too
    def __init__(self):
        super().__init__(SilentRunner.name)
        self.ember_cost = 60


class FuzzyBunnySlippers(Card):
    name = "\033[94mFuzzy Bunny Slippers\033[0m"

    def __init__(self):
        super().__init__(FuzzyBunnySlippers.name)
        self.ember_cost = 62


class Deepfrost(Card):
    name = "\033[94mDeepfrost\033[0m"

    def __init__(self):
        super().__init__(Deepfrost.name)
        self.ember_cost = 64


class Brilliance(Card):
    name = "\033[94mBrilliance\033[0m"

    def __init__(self):
        super().__init__(Brilliance.name)
        self.ember_cost = 66
        self.quickdraw = 2


class PayToWin(Card):
    name = "\033[93mPay to Win\033[0m"

    def __init__(self):
        super().__init__(PayToWin.name)
        self.crown_cost = 2
        self.ember_drops = 10


class TacticalApproach(Card):
    name = "\033[93mTactical Approach\033[0m"

    def __init__(self):
        super().__init__(TacticalApproach.name)
        self.crown_cost = 2
        self.clank_block = 5
        self.treasure_drops = 5


class PorkChopPower(Card):
    name = "\033[93mPork Chop Power\033[0m"

    def __init__(self):
        super().__init__(PorkChopPower.name)
        self.crown_cost = 2


class DungeonLackey(Card):
    name = "\033[93mDungeon Lackey\033[0m"

    def __init__(self):
        super().__init__(DungeonLackey.name)
        self.crown_cost = 8
        self.clank_block = 8


class Stumble(Card):
    name = "\033[91mStumble\033[0m"

    def __init__(self):
        super().__init__(Stumble.name)
        self.clank_block = -2


CARD_CLASSES = [
    # Each ordered pair contains the class itself (for easy instantiation) and the max number of that card type
    (Sneak, 5),
    (Stability, 5),
    (TreasureHunter, 5),
    (EmberSeeker, 5),
    (MomentOfClarity, 5),
    (Evasion, 3),
    (TreadLightly, 3),
    (FrostFocus, 3),
    (LootAndScoot, 3),
    (SecondWind, 3),
    (BeastSense, 3),
    (BoundingStrides, 3),
    (RecklessCharge, 3),
    (Sprint, 3),
    (NimbleLooting, 3),
    (SmashAndGrab, 3),
    (Quickstep, 3),
    (SuitUp, 1),
    (AdrenalineRush, 3),
    (EerieSilence, 3),
    (DungeonRepairs, 3),
    (Swagger, 3),
    (ChillStep, 3),
    (SpeedRunner, 1),
    (EyesOnThePrize, 3),
    (Haste, 3),
    (ColdSnap, 3),
    (SilentRunner, 1),
    (FuzzyBunnySlippers, 1),
    (Deepfrost, 3),
    (Brilliance, 3),
    (PayToWin, 3),
    (TacticalApproach, 1),
    (PorkChopPower, 1),
    (DungeonLackey, 1),
    (Stumble, inf)
]

