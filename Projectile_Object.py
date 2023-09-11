from math import *
from math import pi
from multiprocessing.connection import answer_challenge
import matplotlib.pyplot as plt

class object:
    def __init__(self, angle, initial_height, initial_velocity, initial_coordinate):
        self._angle = angle * pi / 180
        self._initial_height = initial_height
        self._initial_velocity = initial_velocity
        self._initial_coordinate = initial_coordinate

    def case(self):
        if self._initial_velocity != 0:
            if self._angle == 0:
                return 'Mô phỏng vật ném ngang'
            elif self._angle == pi / 2:
                return 'Mô phỏng ném thẳng đứng'
            else:
                return 'Mô phỏng ném xiên'
        elif self._initial_height != 0:
            return 'Mô phỏng thả vật rơi tự do'

    def highestpoint(self):  # Tính độ cao cực đại
        return pow(self._initial_velocity, 2) * pow(sin(self._angle), 2) / (2 * 9.8) + self._initial_height
    
    def length(self):  # Tính tầm bay xa
        return abs(pow(self._initial_velocity, 2) * sin(2 * self._angle) / (2 * 9.8) + self._initial_velocity * 
                   cos(self._angle) * sqrt(2 * (self.highestpoint() + self._initial_height) / 9.8))
    
    def time_1stper(self):  # Tính khoảng thời gian từ lúc ném đến lúc đạt độ cao cực đại
        return self._initial_velocity * sin(self._angle) / 9.8

    def time_2ndper(self):  # Tính khoảng thời gian từ lúc đạt độ cao cực đại đến lúc chạm đất
        return sqrt(2 * (self.highestpoint() + self._initial_height) / 9.8)

    def totaltime(self):  # Tính khoảng thời gian từ lúc ném đến lúc chạm đất
        return self._initial_velocity * sin(self._angle) / 9.8 + sqrt(2 * (self.highestpoint() + 
                                                                           self._initial_height) / 9.8)



    def x_left(self):
        if -1 < cos(self._angle) < 0:
            return (self._initial_coordinate - int(self.length()) - 50)
        else:
            return 0
        
    def x_right(self):
        if -1 < cos(self._angle) < 0:
            return (self._initial_coordinate + 50)
        else:
            return ((self._initial_coordinate + int(self.length()) + 50))
        
        
        
    def simulation(self):
        g = -9.8
        listy = [self._initial_height]
        listx = [self._initial_coordinate]
        t_step = 0.05
        vx = self._initial_velocity * cos(self._angle)
        vy = self._initial_velocity * sin(self._angle)

        plt.xlim(self.x_left(), self.x_right())
        plt.ylim(0, (int(self.highestpoint()) + 10))
        plt.xlabel('Tầm xa')
        plt.ylabel('Độ cao')
        plt.title(self.case())

        while listy[-1] >= 0:
            listx.append(listx[-1] + vx * t_step)
            listy.append(listy[-1] + vy * t_step)

            plt.scatter(listx, listy)

            vy = vy + g * t_step

            plt.pause(0.0000001)

        plt.plot(listx, listy, 'go-')
        plt.show()

