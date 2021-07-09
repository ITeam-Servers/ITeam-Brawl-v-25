from random import *
from Database.DatabaseManager import DataBase
from Logic.Boxes import Boxes

from Utils.Writer import Writer


class ClaimShopGems(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.BoxData = Boxes.boxes

    def encode(self):
    	self.writeVint(203) # CommandID
    	self.writeVint(0)   # Unknown
    	self.writeVint(1)   # Unknown
    	self.writeVint(10)  # BoxID
        # Box info end

        # Reward start
    	self.writeVint(1) # Reward count
    	
    	self.writeVint(60)                           # Reward 1 amount
    	self.writeScId(16, 8)  # CsvID
    	self.writeVint(8)                           # RewardID
    	self.writeHexa('''00 00 00''')              # Reward end
            # Box end
    	for i in range(13):
    		self.writeVint(0)