from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

circuit = QuantumCircuit(2,2)

circuit.h(0)

circuit.cx(0,1)

# Step 3: Measure both qubits
circuit.measure([0, 1], [0, 1])
# Optional: Save the circuit diagram
circuit.draw(output='mpl', filename='bell_circuit.png')

# Simulation using QASM simulator
simulator = AerSimulator()
transpiled_circuit = transpile(circuit, simulator)
job = simulator.run(transpiled_circuit)
result = job.result()
counts = result.get_counts()
# Display results
print("Result:", result)
print("Counts:", counts)
plot_histogram(counts, filename='bell_histogram.png')
plt.show()
