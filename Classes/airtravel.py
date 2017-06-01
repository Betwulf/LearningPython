""" Model for aircraft travel """


class Flight:

    def __init__(self, number, aircraft):
        self._validate(number)
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def _validate(self, number):
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code in {}".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number in {}".format(number))

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):

        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("{} is not a valid seat letter".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("{} is not a valid number".format(row_text))

        if row not in rows:
            raise ValueError(" {} is not a valid row on this plane".format(row))

        return row, letter

    def seats_available(self):
        avail = sum(sum(1 for seat in row.values() if seat is None)
                    for row in self._seating if row is not None)
        return avail

    def allocate_seat(self, seat, passenger):
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is None:
            self._seating[row][letter] = passenger
        else:
            raise ValueError("Seat {} is already taken by {}".format(seat, self._seating[row][letter]))

    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        to_row, to_letter = self._parse_seat(to_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError("no one in seat {}".format(from_seat))

        if self._seating[to_row][to_letter] is not None:
            raise ValueError("{} already has seat {}".format(self._seating[to_row][to_letter], to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows+1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


if __name__ == '__main__':

    a = Aircraft("CD-3482", "Airbus A319", 21, 7)
    print(a.seating_plan())

    f = Flight("AC369", a)
    print(f.aircraft_model())

    for s in f._seating:
        print(s)

    f.allocate_seat("15A", "Bob Smith")
    f.allocate_seat("15C", "Susan Smith")
    f.allocate_seat("15F", "Madonna")
    f.allocate_seat("16A", "Jojo McFlargen")
    f.relocate_passenger("16A", "16B")

    for s in f._seating:
        print(s)

    print("Seats available:", f.seats_available())


