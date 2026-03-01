# Cool Quantum BB84 Protocol

Goal 1: Share a secret key  
Goal 2: Eavesdrop  <!-- spacebar twice at end for newline -->  
Goal 3: Noise

## Theory

1) Alice generates random sequence of bits and independently selects corresponding basis, see below. Similarly, Bob selects his measurement bases at random.
2) Alice encodes each bit into a qubit using quantum bits:
    - Rectilinear basis |0> and |1>
    - Diagonal basis $\frac{1}{\sqrt{2}}$(|0> + |1>) and $\frac{1}{\sqrt{2}}$(|0> - |1>)
3) Bob measures qubits using his randomly chosen basis. Alice and Bob publicly share their bases choices and discard bits that don't match
4) Can confirm whether there was an eavedropper based on error rates

