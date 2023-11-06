import unittest
from modulo_three import mod_three, transition, get_remainder

class TestModuloThree(unittest.TestCase):
    def test_mod_three_with_single_0(self):
        result = mod_three("0")
        self.assertEqual(result, 0)
    
    def test_mod_three_with_single_1(self):
        result = mod_three("1")
        self.assertEqual(result, 1)

    def test_mod_three_with_multiple_0(self):
        result = mod_three("000")
        self.assertEqual(result, 0)

    def test_mod_three_with_multiple_1(self):
        result = mod_three("111")
        self.assertEqual(result, 1)

    def test_mod_three_with_multiple_1_and_0(self):
        result = mod_three("1010")
        self.assertEqual(result, 1)

    def test_mod_three_with_largest_unsigned_32_bit_binary_number(self):
        result = mod_three("11111111111111111111111111111111")
        self.assertEqual(result, 0)

    def test_mod_three_with_empty_string(self):
        result = mod_three("")
        self.assertEqual(result, 0)

    def test_mod_three_with_non_string_input(self):
        self.assertRaises(TypeError, mod_three, 1110)

    def test_mod_three_with_non_binary_string(self):
        self.assertRaises(KeyError, mod_three, "123")

    def test_mod_three_with_none(self):
        self.assertRaises(TypeError, mod_three, None)

    def test_transition_from_S0_when_input_0(self):
        result = transition("S0", "0")
        self.assertEqual(result, "S0")

    def test_transition_from_S0_when_input_1(self):
        result = transition("S0", "1")
        self.assertEqual(result, "S1")

    def test_transition_from_S1_when_input_0(self):
        result = transition("S1", "0")
        self.assertEqual(result, "S2")

    def test_transition_from_S1_when_input_1(self):
        result = transition("S1", "1")
        self.assertEqual(result, "S0")

    def test_transition_from_S2_when_input_0(self):
        result = transition("S2", "0")
        self.assertEqual(result, "S1")

    def test_transition_from_S2_when_input_1(self):
        result = transition("S2", "1")
        self.assertEqual(result, "S2")

    def test_transition_with_non_existing_state(self):
        self.assertRaises(KeyError, transition, "non-existing state", "0")

    def test_transition_with_non_existing_bit(self):
        self.assertRaises(KeyError, transition, "S0", "non-existing bit")

    def test_get_remainder_for_final_state_S0(self):
        result = get_remainder("S0")
        self.assertEqual(result, 0)

    def test_get_remainder_for_final_state_S1(self):
        result = get_remainder("S1")
        self.assertEqual(result, 1)

    def test_get_remainder_for_final_state_S2(self):
        result = get_remainder("S2")
        self.assertEqual(result, 2)

    def test_get_remainder_for_non_existing_state(self):
        self.assertRaises(KeyError, get_remainder, "non-existing state")

if __name__ == '__main__':
    # To run these tests, run the following while in the modulo-three-exercise directory: python3 -m unittest -v tests.test_modulo_three
    unittest.main()