from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.visualization import plot_state_qsphere
from qiskit import QuantumCircuit
import time

def q_teleportation():
    start_time = time.time()
    ckt = QuantumCircuit(3, 3)
    
    ckt.x(0)
    ckt.barrier()

    ckt.h(1)
    ckt.cx(1, 2)
    ckt.cx(0, 1)
    ckt.h(0)

    ckt.barrier()
    ckt.measure([0, 1], [0, 1])

    ckt.barrier()
    ckt.cx(1, 2)
    ckt.cz(0, 2)
    
    ckt.measure(2, 2)

    end_time = time.time()
    return ckt, ckt.draw(output='mpl'), end_time - start_time