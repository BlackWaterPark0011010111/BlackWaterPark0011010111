class Aquarium:
    def __init__(self, fish_count, Eye_color, skinColor):
        self.SkinColor = skinColor
        self.PRIVATE_SWIM_COUNT = 0
        self.eye_color = Eye_color
        self.protected_DEAD_FISH = 0
        self.fishCount = fish_count

    def _start(self):
        if self.fishCount == 0:
            print("There are no alive fish left.")
            return
        self.PRIVATE_SWIM_COUNT += 1

        print(
            str(self.fishCount)
            + " fish are swimming. Their eyes are "
            + self.eye_color
            + " and their skin is "
            + self.SkinColor
            + "."
        )
        print(
            "There are "
            + str(self.protected_DEAD_FISH)
            + " dead fish with them in the aquarium."
        )
        print(
            "The fish have now been swimming "
            + str(self.PRIVATE_SWIM_COUNT)
            + " times."
        )

    def __die_fish(__that, _number):
        if __that.fishCount == 0:
            print("All fish are dead.")
            print("GAME OVER")
            print("=====")
            return
        __that.fishCount -= _number
        __that.protected_DEAD_FISH += _number
        if _number > 1:
            print(str(_number) + " fish have died.")
        else:
            print("A fish has died.")


if __name__ == "__main__":
    MyAquariumApp = Aquarium(5, "blue", "red")
    MyAquariumApp._start()
    MyAquariumApp._Aquarium__die_fish(2)
    MyAquariumApp._start()
    MyAquariumApp._Aquarium__die_fish(1)
    MyAquariumApp._start()
    MyAquariumApp._Aquarium__die_fish(2)
    MyAquariumApp._start()
    MyAquariumApp._Aquarium__die_fish(1)