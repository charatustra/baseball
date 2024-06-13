class Game:
    def guess(self, guessNumber):
        self.assertIllegalValue(guessNumber)

    def assertIllegalValue(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        for number in guessNumber:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if self.isDuplicatedNumber(guessNumber):
            raise TypeError()

    def isDuplicatedNumber(self, guessNumber):
        return guessNumber[0] == guessNumber[1] \
            or guessNumber[0] == guessNumber[1] \
            or guessNumber[1] == guessNumber[2]
