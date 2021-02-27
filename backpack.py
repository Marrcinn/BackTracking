class Backpack:
    def __init__(self, cap, items):
        self.cap = cap
        self.items = items
        self.max_val = 0
        self.max_el = []

    def __str__(self):
        answer = ""
        answer += "The max value is %d \n" % self.max_val
        for el in self.max_el:
            answer += "Element of weigh %d and value %d\n" % (el.weigh, el.value)
        return answer

    def pack(self, current_el, current_val, current_weigh):
        for el in self.items:
            if el.weigh + current_weigh > self.cap:
                if current_val > self.max_val:
                    self.max_val = current_val
                    self.max_el = current_el

            else:
                current_el.append(el)
                current_val += el.value
                current_weigh += el.weigh
                self.pack(current_el, current_val, current_weigh)
                current_el.pop(-1)
                current_val -= el.value
                current_weigh -= el.weigh

    def solve(self):
        self.pack([], 0, 0)


class Item:
    def __init__(self, value, weigh):
        self.value = value
        self.weigh = weigh

def Tests():
    items = [Item(20, 10), Item(8, 5), Item(6, 4)]
    bp = Backpack(18, items)
    bp.solve()
    assert bp.max_val == 32
    items = [Item(20, 10), Item(8, 5), Item(10, 4)]
    bp = Backpack(20, items)
    bp.solve()
    assert bp.max_val == 50
    items = [Item(20, 10), Item(2, 5), Item(1, 4)]
    bp = Backpack(20, items)
    bp.solve()
    assert bp.max_val == 40

if __name__=="__main__":
    Tests()
    print("Tests passed")
