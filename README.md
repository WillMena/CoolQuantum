# Cool Quantum BB84 Protocol

Goal 1: Share a secret key  
Goal 2: Eavesdrop  <!-- spacebar twice at end for newline -->  
Goal 3: Noise

## Theory

1) Alice generates random sequence of bits and independently selects corresponding basis, see below. Similarly, Bob selects his measurement bases at random.
2) Alice encodes each bit into a qubit using quantum bits:
    - Rectilinear basis $|0\rangle$ and $1\rangle$
    - Diagonal basis $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ and $\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$
3) Bob measures qubits using his randomly chosen basis. Alice and Bob publicly share their bases choices and discard bits that don't match
4) Can confirm whether there was an eavedropper based on error rates

