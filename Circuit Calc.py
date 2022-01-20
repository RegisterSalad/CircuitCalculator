import math

resistor_names = {}

class Circuit:
    def __int__(self):
        self.name = self

class Component:
    def __init__(self, R, V, I, P, name):
        self.R = R
        self.V = V
        self.I = I
        self.P = P
        self.name = name

    def print_stats(self):
        print("\n")
        print(f"{self.name} ----")
        print(f"Resistance: {self.R:.2f}\u03A9", end="\t")
        print(f"\t Voltage: {self.V:.2f}V", end="\n")
        print(f"Current: {self.I:.2f}A", end="\t")
        print(f"\t\t\t Power: {self.P:.2f}W", end="\n\n")

    def solve_for_power(self):
        if self.R == 0:
            self.P = self.I * self.V
        elif self.V == 0:
            self.P = self.R * math.pow(self.I, 2)
        elif self.I == 0:
            self.P = math.pow(self.V, 2) / self.R
        else:
            self.P = self.I * self.V

    def solve_for_current(self):
        if self.R == 0:
            self.I = self.P / self.V
        elif self.V == 0:
            self.I = math.sqrt(self.P / self.R)
        elif self.P == 0:
            self.I = self.V / self.R
        else:
            self.I = self.V / self.R

    def solve_for_resistance(self):
        if self.I == 0:
            self.R = math.pow(self.V, 2) / self.P
        elif self.V == 0:
            self.R = self.P / math.pow(self.I, 2)
        elif self.P == 0:
            self.R = self.V / self.I
        else:
            self.R = self.V / self.I

    def solve_for_voltage(self):
        if self.I == 0:
            self.V = self.R * self.I
        elif self.R == 0:
            self.V = self.P / self.I
        elif self.P == 0:
            self.V = math.sqrt(self.P*self.R)
        else:
            self.V = self.R * self.I


def main():
    resistor_counter = 0
    while True:
        while True:
            print(f"Entering resistor addition module.\nThere are currently {resistor_counter}"
                  f" resistors in the circuit\n")
            var = input("Press any key to add new a resistor,  enter 'exit' to exit: ")
            if var == 'exit':
                print("Exiting component addition module")
                break
            else:
                input_name = input("Enter the name of the resistor: ")
                r = int(input("Resistance (0 for unknown): "))
                v = int(input("Voltage (0 for unknown): "))
                c = int(input("Current (0 for unknown): "))
                p = int(input("Power (0 for unknown): "))
                if r + v + c + p == 0:
                    print("INVALID VALUES -------- ")
                    break
                new_resistor = Component(r,v,c,p,input_name)
                resistor_counter += 1
                resistor_names[new_resistor.name] = new_resistor
                new_resistor.print_stats()
        if resistor_counter == 0:
            return 0
        while True:
            print(f"Entering resistor access module.\nThere are currently {resistor_counter}"
                  f" resistors in the circuit\n")
            var = input( "Press any key to access a resistor,  enter 'exit' to exit: " )
            if var == 'exit':
                print( "Exiting component access module" )
                break
            access_resistor = resistor_names[input("Input the name of the resistor you want to access: ")]
            access_resistor.print_stats()
            while True:
                var = input(f"What do you want solve for {access_resistor.name}? "
                            f"(current, voltage, power or resistance): ")
                if access_resistor.I and access_resistor.V and access_resistor.P and access_resistor.P != 0:
                    print("All resistor values: solved")
                    access_resistor.print_stats()
                    break
                if var == 'current':
                    access_resistor.solve_for_current()
                    print(f"The current for {access_resistor.name} is: {access_resistor.I:.2f}A")
                elif var == 'voltage':
                    access_resistor.solve_for_voltage()
                    print(f"The voltage for {access_resistor.name} is: {access_resistor.V:.2f}V" )
                elif var == 'power':
                    access_resistor.solve_for_power()
                    print(f"The power for {access_resistor.name} is: {access_resistor.P:.2f}W")
                elif var == 'resistance':
                    access_resistor.solve_for_resistance()
                    print(f"The resistance for {access_resistor.name} is: {access_resistor.R:.2f}\u03A9")

main()