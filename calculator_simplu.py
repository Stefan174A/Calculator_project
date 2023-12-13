

'''Se dorește implementarea unei aplicații de tip mini - calculator în mod text în Python. La pornire aplicația afișează valoarea inițială care este
implicit 0. Valoarea inițială se poate seta prin intermediul unui parametru din linia de comanda. Apoi aplicația așteaptă o operație de la utilizator și
afișează rezultatul acestuia.
Operațiile posibile sunt:
● +număr - adună la valoarea curentă numărul respectiv
● -număr - scade din valoarea curentă numărul respectiv
● *număr - înmulțește valoarea curentă numărul respectiv
● /număr - împarte valoarea curentă la numărul respectiv
● =număr - setează valoarea curentă cu numărul respectiv
● x - ieșire din program
După fiecare operație se va afișa valoarea curentă și se așteaptă din nou un input de la utilizator. Linia pe care se așteaptă input-ul de la utilizator
începe cu semnul "> ".'''

# Definim o clasă nouă numită Calculator
class Calculator:

# Metoda __init__: -Este un constructor care inițializează un obiect Calculator cu o valoare inițială pentru rezultat
# (implicit 0, dar poate fi modificată la crearea obiectului).
    def __init__(self, valoare_initiala=0):
        self.rezultat = valoare_initiala

# Scriem metodele care efectuează operațiile matematice de adunare, scădere, înmulțire și împărțire.
#  Fiecare metodă primește doi parametri a și b și întoarce rezultatul operației.
    def aduna(self, a, b):
        return a + b

    def scade(self, a, b):
        return a - b

    def inmulteste(self, a, b):
        return a * b

    def imparte(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Nu se poate împărți la zero!"

# Metoda executa_operatie primește un șir de caractere operatie, analizează tipul operației și, dacă este validă,
# execută operația corespunzătoare pe self.rezultat.
    def executa_operatie(self, operatie):
        if operatie == 'x':
            return False

        if operatie.startswith(('+', '-', '*', '/', '=')):
            if len(operatie) > 1 and operatie[1:].replace('.', '', 1).isdigit():
                operand = float(operatie[1:])
                if operatie.startswith('+'):
                    self.rezultat = self.aduna(self.rezultat, operand)
                elif operatie.startswith('-'):
                    self.rezultat = self.scade(self.rezultat, operand)
                elif operatie.startswith('*'):
                    self.rezultat = self.inmulteste(self.rezultat, operand)
                elif operatie.startswith('/'):
                    self.rezultat = self.imparte(self.rezultat, operand)
                elif operatie.startswith('='):
                    self.rezultat = operand
            else:
                print("Invalid operation")
        else:
            print("Invalid operation")

        return True

# Această metodă începe interacțiunea cu utilizatorul, afișând rezultatul curent și așteptând input pentru a efectua operațiile.
# Ciclul rulează în continuu până când se introduce comanda de ieșire (x).
    def start(self):
        while True:
            print(f"{self.rezultat}")
            operatie = input("> ")
            executie = self.executa_operatie(operatie)
            if not executie:
                break

# Aici se efectuează acțiunile atunci când acest fișier este rulat ca un script (nu importat ca modul). Se primește o valoare inițială
# de la utilizator și se inițializează un obiect de tip Calculator cu acea valoare, apoi se pornește interacțiunea cu utilizatorul prin metoda start.

def main():
    valoare_initiala = 0

    valoare_initiala_input = input("Introduceți valoarea inițială sau apăsați Enter pentru valoarea implicită (0): ")
    if valoare_initiala_input:
        valoare_initiala = float(valoare_initiala_input)

    calc = Calculator(valoare_initiala)
    calc.start()

if __name__ == "__main__":
    main()

