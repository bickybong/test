class stone:
    lstones = []
    def __init__(self,name):
        self.name = name
        if len(stone.lstones) < 5:
            stone.lstones.append(self)
        else:
            del stone.lstones[0]
            stone.lstones.append(self)
    
    def showStone(self):
        for sto in stone.lstones:
            print(sto.name)
        print()
        


preciousStoneOne  = stone("Ruby")
preciousStoneTwo  = stone("Emerald")
preciousStoneThree  = stone("Sapphire")
preciousStoneFour  = stone("Diamond")
preciousStoneFive  = stone("Amber")
preciousStoneFive.showStone()
preciousStoneSix = stone("Onyx")
# Print all the stones after deleting the first stone
preciousStoneSix.showStone()
