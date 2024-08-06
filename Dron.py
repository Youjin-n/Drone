import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random


# "fig" genel hatları oluşturan nesneyken "ax" çizim ve grafiğin yapısıyla ilgili olan nesnedir
fig, ax = plt.subplots()

x_locations = []
y_locations = []

# Butonların yerleştirileceği alanı ve boyutunu belirler
button1 = plt.axes([0.82, 0.7, 0.167, 0.07])
button2 = plt.axes([0.82, 0.6, 0.167, 0.07])
button3 = plt.axes([0.82, 0.5, 0.167, 0.07])
button4 = plt.axes([0.82, 0.4, 0.167, 0.07])
button5 = plt.axes([0.82, 0.3, 0.167, 0.07])

# Butonları oluşturur
btn1 = Button(button1, 'Üçgen')
btn2 = Button(button2, "Kare")
btn3 = Button(button3, "Yıldız")
btn4 = Button(button4, "Rastgele")
btn5 = Button(button5, "Yer değiştirme")

# Dronların özellikleri burada tutulur
class Drone:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        
    def move(self, x, y):
        self.x = x
        self.y = y


class Swarm:
    def __init__(self, number_of_drones):
        self.drones = [Drone(i, plt.cm.rainbow(i/number_of_drones)) for i in range(number_of_drones)]

    def change_formation(self, sekil):
        if sekil == "üçgen":
            # Rastgele 3 farklı dron seçer, dronları konumlandırır ve üçgen çizer
            selected_drones = random.sample(self.drones, 3)
            x_locations.extend([1, 9, 5, 1])
            y_locations.extend([1, 1, 8, 1])
            for id, drone in enumerate(selected_drones):
                if id == 0:
                    drone.move(1 , 1)
                elif id == 1:
                    drone.move(9, 1)
                elif id == 2:
                    drone.move(5, 8)

        elif sekil == "kare":
            # Rastgele 4 farklı dron seçer, dronları konumlandırır ve kare çizer
            selected_drones = random.sample(self.drones, 4)
            x_locations.extend([1, 9, 9, 1, 1])
            y_locations.extend([1, 1, 9, 9, 1])
            for id, drone in enumerate(selected_drones):
                if id == 0:
                    drone.move(1, 1)
                elif id == 1:
                    drone.move(9, 1)
                elif id == 2:
                    drone.move(9, 9)
                elif id == 3:
                    drone.move(1, 9)

        elif sekil == "yıldız":
            # Rastgele 5 farklı dron seçer, dronları konumlandırır ve yıldız çizer
            selected_drones = self.drones
            x_locations.extend([2.648, 5.0, 7.351, 1.195, 8.804, 2.648])
            y_locations.extend([1.763, 9.0, 1.763, 6.236, 6.236,1.763])
            for id, drone in enumerate(selected_drones):
                if id == 0:
                    drone.move(2.648 , 1.763)
                elif id == 1:
                    drone.move(7.351 , 1.763)
                elif id == 2:
                    drone.move(8.804, 6.236)
                elif id == 3:
                    drone.move(5.0, 9.0)
                elif id == 4:
                    drone.move(1.195, 6.236)

        else:
            return

        ax.plot(x_locations, y_locations)
  
    # dronların yer değiştirmesini sağlar
    def replace(self, drone1_id, drone2_id):
        drone1 = self.drones[drone1_id]
        drone2 = self.drones[drone2_id]

        drone1.x, drone2.x = drone2.x, drone1.x
        drone1.y, drone2.y = drone2.y, drone1.y

    # Dronların renklerini ayarlar ve dronları gösterir
    def plot(self):
        for drone in self.drones:
            ax.scatter(drone.x, drone.y, color=drone.color)
        plt.show()


# Butonlara basıldığında gerçekleşen kısımlar
def button_clicked1(event):
    global x_locations, y_locations, swarm
    ax.clear()
    x_locations = []
    y_locations = []
    
    swarm = Swarm(5)
    swarm.change_formation("üçgen")

    ax.plot(x_locations,y_locations)
    ax.set_xlim(-1, 11)  
    ax.set_ylim(-1, 11)

    swarm.plot()
    fig.canvas.draw_idle() 


def button_clicked2(event):
    global x_locations, y_locations, swarm
    ax.clear()
    x_locations = []
    y_locations = []

    swarm = Swarm(5)
    swarm.change_formation("kare")

    ax.plot(x_locations,y_locations)
    ax.set_xlim(-1, 11)  
    ax.set_ylim(-1, 11)

    swarm.plot()
    fig.canvas.draw_idle() 


def button_clicked3(event):
    global x_locations, y_locations, swarm
    ax.clear()
    x_locations = []
    y_locations = []

    swarm = Swarm(5)
    swarm.change_formation("yıldız")

    ax.plot(x_locations,y_locations)
    ax.set_xlim(-1, 11)  
    ax.set_ylim(-1, 11)

    swarm.plot()
    fig.canvas.draw_idle() 


def button_clicked4(event):
    global x_locations, y_locations, swarm
    ax.clear()
    x_locations = []
    y_locations = []

    swarm = Swarm(5)
    swarm.change_formation("a")

    ax.set_xlim(-1, 11)  
    ax.set_ylim(-1, 11)

    swarm.plot()
    fig.canvas.draw_idle() 

def button_clicked5(event):
    swarm.replace(random.randint(0,4), random.randint(0,4))
    swarm.plot()
    fig.canvas.draw_idle()


# Butonların basıldığında çalışmasını sağlayan kısım
btn1.on_clicked(button_clicked1)
btn2.on_clicked(button_clicked2)
btn3.on_clicked(button_clicked3)
btn4.on_clicked(button_clicked4)
btn5.on_clicked(button_clicked5)


fig.subplots_adjust(right=0.8) # Grafiğin konumunu düzeltir 
ax.set_xlim(-1, 11)            # Çizimin x sınırlarını ayarlar
ax.set_ylim(-1, 11)            # Çizimin y sınırlarını ayarlar 

swarm = Swarm(5)
swarm.plot()
