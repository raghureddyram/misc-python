import random

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")


class Drummer(Musician):
    def __init__(self):
        super().__init__(["brrrdddumPcham", "bissh", "pching"])

    def solo(self):
        print(super().solo(6), '..kaboom!') ##better way to do this?

class Band(object):
    def __init__(self):
        self.members = []

    def hire(self):
        avail_musicians = [Bassist, Guitarist, Drummer]
        choice = random.choice(avail_musicians)
        self.members.append(choice())

    def show_members(self):
        print("current memmbers are {}".format(self.members))

    def fire(self, type):
        musician_count = len(self.members)

        for musician in self.members:
            if musician == type:
                self.memmbers.remove(type)
        new_musician_count = len(self.members)

        if new_musician_count == musician_count:
            self.members.pop()

        return self.members



dan = Drummer()

pink_floyd = Band()

pink_floyd.hire()

pink_floyd.show_members()




pink_floyd.fire(Drummer)


pink_floyd.show_members()


dan.solo()