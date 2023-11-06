REMAINDERS = { "S0":0, "S1":1, "S2":2 }

INITIAL_STATE = "S0"

S0_TRANSITIONS = { "0":"S0", "1":"S1" }
S1_TRANSITIONS = { "0":"S2", "1":"S0" }
S2_TRANSITIONS = { "0":"S1", "1":"S2" }

STATES = { "S0":S0_TRANSITIONS, "S1":S1_TRANSITIONS, "S2":S2_TRANSITIONS }

def mod_three(binary_string: str) -> int:
    """Returns the mod-three of a string of ones and zeroes"""
    current_state = INITIAL_STATE

    for bit in binary_string:
        current_state = transition(current_state, bit)

    remainder = get_remainder(current_state)

    return remainder

def transition(state: str, bit: str) -> str:
    """Returns the state transition"""
    return STATES[state][bit]

def get_remainder(state: str) -> int:
    """Returns the remainder value of the state"""
    return REMAINDERS[state]

if __name__ == '__main__':
    # Here are some examples of the mod_three procedure
    # To see the results, run the following command while in the modulo-three-exercise directory: python3 modulo_three/modulo_three.py 
    print(mod_three("1101"))
    print(mod_three("1110"))
    print(mod_three("1111"))