class Node:

    def __init__(self, qnt_m1, qnt_c1, qnt_mb, qnt_cb, qnt_m2, qnt_c2, flag, prev):
        self.side1 = [qnt_m1, qnt_c1]
        self.boat = [qnt_mb, qnt_cb]
        self.side2 = [qnt_m2, qnt_c2]
        self.sons = []
        self.flag = flag
        self.prev = prev