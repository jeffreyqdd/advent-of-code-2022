#!/usr/bin/env python
from sys import stdin
import tqdm

master = 1

class Monkey:
    def __init__(self, id, starting_items, operation, test, monkey):
        self.id = id
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.monkey = monkey
        self.inspections = 0

    def throw_to_which_monkey(self):
        self.inspections += 1
        # looks at first item
        #print(f'monkey{self.id} inspects item {self.items[0]}')
        self.items[0] = self.operation(self.items[0])
        #print(f'monkey{self.id} new worry {self.items[0]}')
        #self.items[0] = int(self.items[0] / 3) # divide by three
        self.items[0] %= master
        #print(f'monkey{self.id} new worry {self.items[0]}')
        result = self.items[0] % self.test == 0
        if result:
            #print(f'throw to {self.monkey[0]}')
            return self.monkey[0]
        else:
            #print(f'throw to {self.monkey[1]}')
            return self.monkey[1]

    def has_item(self):
        return len(self.items) > 0

data = []
for _ in stdin:
    data.append(_.strip('\n'))

monkeys = []
for idx in range(0, int(len(data) / 7)):
    monkey_id = int(data[0 + idx * 7].split(' ')[1].replace(':',''))# {{{
    starting_items = list(map(int, list(
            data[1 + idx * 7].replace('Starting items: ', '').split(','))))
    #print(f'id: {monkey_id}')
    #print(f'items: {starting_items}')

    op = eval(
            f"lambda old: {data[2 + idx * 7].replace('Operation: new = ', '')}"
            )# pray it's right
    test = int(data[3 + idx * 7].split(' ')[-1])
    master *= test
    #print(f'divisible by: {test}')
    true_monkey = int(data[4+idx*7].split(' ')[-1])
    false_monkey = int(data[5+idx*7].split(' ')[-1])
    #print(f'true: {true_monkey}, false: {false_monkey}')

    monkeys.append(Monkey(
        idx, starting_items, op, test, [true_monkey, false_monkey]))# }}}

for round_num in tqdm.tqdm(range(0, 10_000)): # number of rounds

    for idx, monkey in enumerate(monkeys):# go though all monkies
        while monkey.has_item():
            target_monkey = monkey.throw_to_which_monkey()
            worry_item = monkey.items.pop(0)
            monkeys[target_monkey].items.append(worry_item)

    #for monkey in monkeys:
    #    print(monkey.items, monkey.inspections)
monkeys = sorted(monkeys, key=lambda x: -x.inspections)
print(monkeys[0].inspections * monkeys[1].inspections)
