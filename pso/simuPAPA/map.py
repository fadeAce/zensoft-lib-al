# considering 100 players as a unite program and there is no distinguish between among players.
# players do behavior in considering their E-val.
class player:
    seq = 0
    rect_length_air = 20
    rect_length_land = 5

    def route(self):
        print("routing :" + self.seq)

    def fire(self):
        print("fire :" + self.seq)