
# class TV():

#     def __init__(self):
#         self.channel = 1
#         self.volume_level = 1
#         self.turn_on = False
        
#     def turn_on(self):
#         self.turn_on = True

#     def TurnOff(self):
#         self.turn_on = False
    
#     def Channel_up(self):
#         if self.turn_on:
#             self.channel = min(self.channel + 1, 100)
    
#     def Channel_down(self):
#         if self.turn_on:
#             self.channel = max(self.channel -1, 1)
    
#     def Volume_up(self):
#         if self.turn_on:
#             self.volume_level= min(self.volume_level + 1, 10)
    
#     def Volume_down(self):
#         self.volume_level = max(self.volume_level -1, 10)
    
#     def setChannel(self, new_channel):
#         self.channel = max(1,min(100,new_channel))



class TV:
    def __init__(self, channel =1,volume_level=1,turned_on = False):
        self.channel = channel
        self.volume_level = volume_level
        self.turned_on = turned_on

    def turn_on(self):
        self.turned_on = True
        print('TV is turned on')

    def turn_off(self):
        self.turned_on = False
        print('TV is turned off')
        
    def channel_up(self):
        if self.turned_on:
            print('tv is apparently on. you can channel up ') 
            if self.channel >= 100:
               self.channel = 0
            else:
                self.channel +=1
                print('i cant change channels cuz your tv is off')

    def channel_down(self):
        if self.turned_on:
            print('tv is apparently on. you can channel up ') 
            self.channel -= 1
        if  self.channel == 100:
            self.channel = 10
            print(f'the channel number is: {self.channel}')
        else:
                
            print('i cant change channels cuz your tv is off')


    # def set_channel(self,channel_number):
    #     if channel_number <= 0 and channel_number >=100:
    #         print('Please set the channel number between 1 and 100')
    #     else:
    #         self.channel = channel_number
    #         print('your new ')