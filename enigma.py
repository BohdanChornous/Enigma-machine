class Enigma:

    def __init__(self, re, r1, r2, r3, pb, kb):
        self.reflector = re
        self.rotor_1 = r1
        self.rotor_2 = r2
        self.rotor_3 = r3
        self.plugboard = pb
        self.keyboard = kb

    def set_rings(self, rings):
        self.rotor_1.set_ring(rings[0])
        self.rotor_2.set_ring(rings[1])
        self.rotor_3.set_ring(rings[2])

    def set_key(self, key):
        self.rotor_1.rotate_to_letter(key[0])
        self.rotor_2.rotate_to_letter(key[1])
        self.rotor_3.rotate_to_letter(key[2])

    def encipher(self, letter):

        # rotate the rotors
        if self.rotor_2.left[0] == self.rotor_2.notch and self.rotor_3.left[0] == self.rotor_3.notch:
            self.rotor_1.rotate()
            self.rotor_2.rotate()
            self.rotor_3.rotate()
        elif self.rotor_2.left[0] == self.rotor_2.notch:
            self.rotor_1.rotate()
            self.rotor_2.rotate()
            self.rotor_3.rotate()
        elif self.rotor_3.left[0] == self.rotor_3.notch:
            self.rotor_2.rotate()
            self.rotor_3.rotate()
        else:
            self.rotor_3.rotate()

        # pass signal through the machine
        signal = self.keyboard.forward(letter)
        path = [signal, signal]
        signal = self.plugboard.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor_3.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor_2.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor_1.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.reflector.reflect(signal)
        path.append(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor_1.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor_2.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.rotor_3.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.plugboard.backward(signal)
        path.append(signal)
        path.append(signal)
        letter = self.keyboard.backward(signal)
        return path, letter
