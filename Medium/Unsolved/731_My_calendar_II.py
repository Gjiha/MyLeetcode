class MyCalendarTwo:

    def __init__(self):
        self.booking = {}

    def overlap(self, start, end, startOver, endOver):
        if start < endOver and end > startOver:
            return True
        return False

    def book(self, start: int, end: int) -> bool:
        forest = list(self.booking.keys())
        forest.sort()

        listToAdd = []
        i = 0
        while i < len(forest):
            restart = False
            bookedStart, bookedEnd = forest[i]

            # Interno
            if start >= bookedStart and end < bookedEnd:
                for (childStart, childEnd) in self.booking[(bookedStart, bookedEnd)]:
                    if self.overlap(start, end, childStart, childEnd):
                        return False
                self.booking[(bookedStart, bookedEnd)].append((start, end))
                return True

            # Esterno da destra
            elif start >= bookedStart and start < bookedEnd and end > bookedEnd:
                newInterval = (bookedEnd, end)
                for (childStart, childEnd) in self.booking[(bookedStart, bookedEnd)]:
                    if self.overlap(start, bookedEnd, childStart, childEnd):
                        return False
                listToAdd.append(((bookedStart, bookedEnd), (start, bookedEnd)))
                start, end = newInterval
                restart = True

            # Esterno da sinistra
            elif start < bookedStart and end > bookedStart and end <= bookedEnd:
                newInterval = (start, bookedStart)
                for (childStart, childEnd) in self.booking[(bookedStart, bookedEnd)]:
                    if self.overlap(bookedStart, end, childStart, childEnd):
                        return False
                listToAdd.append(((bookedStart, bookedEnd), (bookedStart, end)))
                start, end = newInterval
                restart = True

            # Sovrapposizione totale
            elif start <= bookedStart and end >= bookedEnd:
                if len(self.booking[(bookedStart, bookedEnd)]) > 0:
                    return False
                listToAdd.append(((start, end), (bookedStart, bookedEnd)))

            if restart:
                forest = list(self.booking.keys())  # Aggiorna la lista
                forest.sort()  # Ricontrolla dopo aver ordinato
                i = 0  # Ricomincia da capo
            else:
                i += 1

        # Aggiungi i nuovi intervalli
        for (father, child) in listToAdd:
            if child in self.booking:
                self.booking.pop(child)
            if father in self.booking:
                self.booking[father].append(child)
            else:
                self.booking[father] = []
                self.booking[father].append(child)

        if (start, end) not in self.booking:
            self.booking[(start, end)] = []

        return True

    def __str__(self) -> str:
        return f"booking: {self.booking}"

# Test
b = MyCalendarTwo()
b.book(48, 55)
b.book(55, 64)
b.book(54, 60)
b.book(49, 55)
print(b.book(23, 28))  # False expected
print(b)