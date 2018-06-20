class Vehicle:
    def __init__(self,wheelnum,shushixing,shuliang):
        self.wheelnum=wheelnum
        self.shushixing=shushixing
        self.shuliang=shuliang
    def huoqu_wheel_num(self):
        return self.wheelnum
    def chongzhi_wheelnum(self,new_wheelnum):
        self.wheelnum=new_wheelnum




car=Vehicle(4,'五星','500kg')
car.chongzhi_wheelnum(6)
print(car.wheelnum)