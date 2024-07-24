#--------------------------------------------------------------------------------------------
# Quantum simulation of a quantum field lens coding algorithm with entanglement scaling
# between a multi-well (barrier) interaction potential of internal system B interacting and 
# external system A.
# Created by: Philip B. Alipour, Supervisor: T. A. Gulliver, at the University of Victoria,
# Dept. ECE, Victoria BC, Canada. 
# Code updated based on Qiskit 2023--2024 changes specified in code comments below. 
# Side-notes: You can also run code with the right packages installed in pipx or python.
# Examples of changes can be found on e.g., 
# https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-installation and 
# https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features  
# follow the link to fix 'deprecated release' lines, use 
# <pip install "qiskit-aer>=0.11.0"> 
# and <pip install qiskit-ibm-provider> after activating your qiskit virtual environment in 
# shell.
#--------------------------------------------------------------------------------------------
# Import the QISKit SDK... INstall Qiskit v.1 and update older ones < v.0.1 from above notes.  
import termplotlib as tpl # To draw plots on circuit results during/after experiment. 
import numpy as np
import sys
import re  # For search and spot regular expressions in {text, metadata, binary,...} I/O files.
from time import sleep
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import *
from qiskit_aer import Aer  # 2024 update... from its deprecated release.
from colorama import Fore, Back, Style  # For colored text messages.
#-----------------------------------------------------------------------------------------
# Newly added package in 2023/2024, the U3 gate has been renamed the U gate.
# from https://quantum-computing.ibm.com/composer/docs/iqx/operations_glossary
# and for cu1 gate to recreate this gate, add the control modifier to the phase gate 
# (formerly the U1 gate); (older version of Qiskit cu1, now cp)
# U3 should be renamed just U as it is an arbitrary single-qubit gate.
# CU1 should be renamed Cphase or CP depending on the above. For more, visit
# https://github.com/Qiskit/qiskit-terra/issues/4106
#-----------------------------------------------------------------------------------------
from math import pi
from qiskit.compiler import transpile, assemble # In 2024, execute now is renamed to transpile. 
from qiskit.visualization import *
from qiskit.providers.backend import Backend # Specify backend device for data processing
from qiskit_ibm_provider import IBMProvider  # 2024 update... from its deprecated release. 

def qdf_circuit():  # Function to compose/build a QDF circuit.
 global qc    # Instantiate qc as a global variable to represent the quantum circuit.  
 # Set your API Token. IBMQ.enable_account ('API Token') Create a Quantum Register with 
 # 4 qubits.
 q = QuantumRegister(4)
 
 # Create a Classical Register with 4 bits.
 c = ClassicalRegister(4) # as _b in Fig. 6 of Ref. [1]
 
 # Create a Quantum Circuit.
 qc = QuantumCircuit(q, c)

 #-----------------------------------------------------------------------------------------
 # Implementation of Superdense Coding
 #-----------------------------------------------------------------------------------------
 # State initialization on 4 qubits in the z-basis in the |0> state.
 qc.reset(q[0])
 qc.reset(q[1])
 qc.reset(q[2])
 qc.reset(q[3])
 qc.x(q[0])
 qc.x(q[2]) 
 qc.barrier(range(4)) # Barrier to indicate physical barriers between systems A and B
                     # particles in communication.
 qc.h(q[1]) 
 qc.cx(q[1], q[2])
 qc.barrier(range(4))
 qc.z(q[1])   # Current state and encoded in the message through QFT.
 #qc.x(q[1])  # Current message encoded in the superdense coding scheme
 qc.barrier(range(4))
 
 # Time step = 1. Time evolution of potential energy part of the Ising model (spin
 # configuration tending to ground state or magnetization M>0) relative to kappaPhi
 # implementation.
 qc.h(q[2])
 qc.u(5,-pi/2,pi/2,q[2])
 qc.h(q[2])
 
 #---------------------------------------------------------------------------------------
 # Entanglement Encoder Implementation
 #---------------------------------------------------------------------------------------
 # Two-qubit Inverse Quantum Fourier Transform (QFT^-1)
 qc.h(q[1])
 qc.cp(pi/2, q[2], q[1])
 qc.h(q[2])
 
 # Time evolution of kinetic Ising model (kinetic energy part satisfying magnetization
 # value M=0)
 qc.p(pi/2, q[1])
 qc.h(q[1])
 qc.u(-(pi**2)/30, -pi/2, pi/2, q[1])
 qc.h(q[1])
 qc.h(q[2])
 qc.u(-(pi**2)/8, -pi/2, pi/2, q[2])
 qc.h(q[2])
 qc.cp((pi**2)/8, q[2], q[1])
 
 # Two-qubit Quantum Fourier Transform (QFT)
 qc.h (q[2])
 qc.cp (-pi/2, q[2], q[1])
 qc.h (q[1])
 
 # Time evolution of potential energy part 
 qc.p(3*pi/4, q[1])
 qc.h (q[2])
 qc.u (5, -pi/2, pi/2, q[2])
 qc.h (q[2])
 qc.barrier(range(4))
 
 #------------------------------------------------------------------------------------
 # Continuation of the superdense code algorithm. Remove IF statement for real quantum
 # computers when enabling one of the backends after 'qasm_simulator' below
 #------------------------------------------------------------------------------------
 qc.x(q[1]).c_if(c, 1)  # IF statement , as if the prize is spotted via Eve or the
 # audience, ask Bob to decide to win the prize or a prize of lesser quality or energy
 # value; flipping condition for Alice to cloak the prize is 0 as opposed to 1 or 2 in
 # decimal. Remove IF statement when testing on a quantum computer and not a simulator.
 qc.barrier(range(4))
 qc.cx(q[1], q[2])
 qc.h(q[1])
 qc.barrier(range(4))
 qc.measure(q[2], c[0])  # Qubit 2 is in state |0>
 qc.measure(q[1], c[1])  # Qubit 1 is in state |1>
 
 # Remove IF statement for real quantum computers when enabling one of the backends after
 # 'qasm_simulator' below qc.swap(q[1],q[2]).c_if(c, 1) # SWAP gate is used if
 # condition c=1 or 01 in binary.
 qc.swap(q[1],q[2]).c_if(c, 2)   # SWAP gate is used if condition c=2 or 10 in binary
 qc.measure(q, c)  # Map the quantum measurement to the classical bits
 qc.barrier(range(4))
 
 global hline
 hline = "=================================================================================================================================="
 print(f"{Fore.LIGHTGREEN_EX + hline}\
 \nQuantum simulation of a quantum field lens coding algorithm with entanglement scaling between a\
 \nmulti-well (barrier) interaction potential of internal system B interacting and external system A\
 from the method article: \
 \n{Fore.LIGHTCYAN_EX}https://www.sciencedirect.com/science/article/pii/S221501612300136X{Fore.LIGHTGREEN_EX} \
 \n*- QDF Circuit Built and Simulator generates its realtime datasets from\
 {Fore.LIGHTYELLOW_EX}{{ Qiskit Aer, IBMQ }} Qasm_Simulator{Fore.LIGHTGREEN_EX}\
 \n   Workspace and/or Virtual Environment on user's computer in Python. \
 \n*- Created by: Philip B. Alipour, Supervisor: T. A. Gulliver, at the University of Victoria,\
 \n   Dept. ECE, Victoria BC, Canada. \
 \n*- Code updated based on Qiskit 2023--2024 changes specified in code comments of this simulator. \
 \n*- {Fore.LIGHTRED_EX}\033[4m\033[1mSidenotes:\033[0m{Fore.LIGHTGREEN_EX} You can also run code with\
 the right packages installed in pipx or python.\
 \n   Examples of package installation changes and features can be found on: \
 \n   {Fore.LIGHTCYAN_EX}https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-installation and \
 \n   https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features{Fore.LIGHTGREEN_EX} \
 \n{hline + Fore.YELLOW}")
 print(f"{Fore.LIGHTGREEN_EX}Press any key to continue...")
 os.system("pause >nul")
 print(f"\033[F{Fore.LIGHTMAGENTA_EX + hline}")
 print(Back.LIGHTGREEN_EX + Fore.YELLOW + 
       "\033[1m<--- {{ Qiskit Aer, IBM }} QDF CIRCUIT SIMULATION BEGINS --->\033[0m" + Back.RESET) 

 #The following lines plot the P of measurements from the QDF circuit and draws the circuit. 
 global counts_exp   # Used to plot P results for N shots run on the QDF circuit.
 #------------------------------------------------------------------------------------
 # Choose backend, number of shots and the plotting of histogram.
 #------------------------------------------------------------------------------------
 #my_provider = IBMProvider() # Previously was IBMQ.load_account().
 #print(Fore.LIGHTMAGENTA_EX + f"{hline + Fore.GREEN}\nIBMQ Providers:" + Fore.YELLOW, my_provider.backends())
 #ibmq_pick = my_provider.get_backend('ibmq_qasm_simulator') # To run on without dynamic support.
 dyn_pick = Aer.get_backend('qasm_simulator') # The device to run on dynamically... 2024 update. 
 print(Fore.LIGHTMAGENTA_EX + f"{hline + Fore.GREEN}\nDynamic Providers:"+ Fore.YELLOW, dyn_pick)
 #ibmq_pick = provider.get_backend('simulator_statevector')
 #ibmq_pick = my_provider.get_backend('ibmq_athens') # This machine was recently retired.
 #ibmq_pick = my_provider.get_backend('ibmq_16_melbourne') # This machine was recently retired.
 shots = 8192 # Number of shots to run the program (experiment); maximum is 8192 shots.
 job_exp = dyn_pick.run(qc, shots = shots) # 2024 update... Qiskit package v.1.0 (see heading)
 result = job_exp.result()
 print(Fore.GREEN + f'Counts for Qubit Pairs out of {shots} shots:' + Fore.RED, 
       result.get_counts(qc), Fore.LIGHTGREEN_EX)
 counts_exp = (result.get_counts(qc))
 
 #--- The above code snippet is the old version limited to counts ratio to maximum number 
 # of shots = 8192 resulting to plot probabilities in older Qiskit versions (as 
 # presented in our method article, Ref. [1]). 
 # New version to plot probabilities require further computation included for printing 
 # out the same probabilities based on Maximum of counts/total number of shots = 
 # a list of P(qubit pairs). 
 # The observed probabilities are computed by taking the respective counts and dividing 
 # by the total number of shots as follows.
 #---------------------------------------------------------------------------------------
 #---------------------------------------------------------------------------------------
 # The following lines calculate P values and plot them for the 'counts_exp' above after 
 # being recorded as expected measurement outcome from the QDF circuit.
 #--------------------------------------------------------------------------------------
 #N[P(kappa Phi to Psi)]
 P = 1 # The total probability of QDF circuit events relative to classical states or 
       # denoting the system's Hamiltonian (total energy). 

 file = "ibm-qdf-shell_output.bin" # I/O bin or metadata file to binary file to read/write.
 with open(file, 'w') as file_to_write:
    file_to_write.write(str(counts_exp))
    file_to_write.close() # End write counts_exp metadata to the file. 

 n_list = []  # Create an empty list for numbers to store. 
 bin_list = []  # Create an empty list for binaries to store. 
 
 with open(file, 'r') as file:
        
        # Read the contents of the file
        content = file.read()
        
        # Extract all the digits from the content and convert to int.
        N = re.findall(r'\d+', content) 
        n_list = list(map(int, N)) 

        # Convert all the metadata digits to str to sort out binaries.
        bin_list = list(map(str, N)) 

        # Calculate quantum event p's for the total P.
        p1 = n_list[1]/shots # 1st p result is stored to the p_list.
        p2 = n_list[3]/shots # 2nd p result is stored to the p_list.
        p3 = n_list[5]/shots # 3rd p result is stored to the p_list.
 
 # This prepares a list of event p's summing up to P in total from the shots. 
 # Counts for QDF pairwise qubits:
 print(f'{Fore.YELLOW} Σ ({n_list[1]}, {n_list[3]}, {n_list[5]}) = {shots} shots ⟶  \
 ⟨P(b|ij⟩)⟩ = {{ ({{n1, n2, n3}}/{shots})b|ij⟩ }} \
 \n = {Fore.LIGHTCYAN_EX}{{ p1({bin_list[0]}) = {p1} }} {Fore.YELLOW}+{Fore.LIGHTCYAN_EX}\
 {{ p2({bin_list[2]}) = {p2} }} {Fore.YELLOW}+{Fore.LIGHTCYAN_EX}\
 {{ p3({bin_list[4]}) = {p3} }} {Fore.YELLOW}= {P}'), sleep(3)

 # Set the default p color codes to 'white' as defined below in the p_color list until an if condition applies.
 p_color = [Style.BRIGHT + Fore.WHITE, Style.BRIGHT + Fore.WHITE, Style.BRIGHT + Fore.WHITE]
 
 # Set the high & low p's color-coded conditions of the p_color list against the total P color, set to LIGHTGREEN_EX.
 if p1 < 0.5 and p1 >= 0.33:
     p_color[0] = Style.BRIGHT + Fore.WHITE
 if p2 < 0.5 and p2 >= 0.33:
     p_color[1] = Style.BRIGHT + Fore.WHITE
 if p3 < 0.5 and p3 >= 0.33:
     p_color[2] = Style.BRIGHT + Fore.WHITE

 if p1 < 0.33 and p1 >= 0.25:
     p_color[0] = Style.DIM + Fore.YELLOW
 if p2 < 0.33 and p2 >= 0.25:
     p_color[1] = Style.DIM + Fore.YELLOW
 if p3 < 0.33 and p3 >= 0.25:
     p_color[2] = Style.DIM + Fore.YELLOW

 if p1 < 0.25:
     p_color[0] = Style.DIM + Fore.RED
 if p2 < 0.25:
     p_color[1] = Style.DIM +  Fore.RED
 if p3 < 0.25:
     p_color[2] = Style.DIM + Fore.RED

 if p1 > 0.5 and p1 < P:
     p_color[0] = Style.BRIGHT + Fore.LIGHTCYAN_EX
 if p2 > 0.5 and p2 < P:
     p_color[1] = Style.BRIGHT + Fore.LIGHTCYAN_EX
 if p3 > 0.5 and p3 < P:
     p_color[2] = Style.BRIGHT + Fore.LIGHTCYAN_EX

 if ((p1 <= 0.5 and p1 >= 0.4) 
     or (p2 <= 0.5 and p2 >= 0.4) 
     or (p3 <= 0.5 and p3 >= 0.4)):  # This condition implies to superposition as discussed in Refs. [1, 2], 
                                     # as the main discussion around state ⟨2⟩ of qubit pairs from a single  
                                     # field vs. a QDF transformation.
     p_color[:] = Style.BRIGHT + Fore.LIGHTMAGENTA_EX # Any color in the p_list is set to that successful event p as magenta. 
 if p1 == P or p2 == P or p3 == P:  # This only occurs when a p ⟶ ⟨P_success⟩ = P = 1, as
                                    # 100% success probability of the expected measurement outcome.
                                    # See Ref. [2] publication for more details. 
     p_color[:] = Style.BRIGHT + Fore.LIGHTGREEN_EX # Any color in the p_list is set to that successful event p as green. 
 
 # Plot QDF pairwise qubits p's relative to P:
 print(f"{Fore.LIGHTMAGENTA_EX}{hline}\n Plot = [{Fore.LIGHTGREEN_EX}Experimented n of N counts\
 {Fore.LIGHTYELLOW_EX} ∝ {Fore.LIGHTGREEN_EX} p of total circuit events P on pairwise\
 qubits {Fore.LIGHTYELLOW_EX}= P(b|ij⟩){Fore.LIGHTMAGENTA_EX}]; {Fore.LIGHTYELLOW_EX}|ij⟩ ≡ |q_i q_j⟩ ≡ |qᵢqⱼ⟩{Fore.LIGHTMAGENTA_EX}.\
 \n{hline}")      

 fig = tpl.figure()
 fig.barh([P, p1, p2, p3], [Style.BRIGHT + Fore.LIGHTGREEN_EX+f"P(b|ij⟩)", p_color[0]+f"p1(b|ij⟩) = p1({bin_list[0]})", 
                            p_color[1]+f"p2(b|ij⟩) = p2({bin_list[2]})", p_color[2]+f"p3(b|ij⟩) = p3({bin_list[4]})"], 
          force_ascii=False)
 fig.show()

 # Store the P's for simulation use by the QFLCC program for dataset analysis and QDF circuit predictions.
 with open('ibm-qdf-stats.txt', 'w') as file_to_write:
    file_to_write.write(f"{P}, {p1}, {p2}, {p3}\nP, p({bin_list[0]}), p({bin_list[2]}), p({bin_list[4]})")
    file_to_write.close() # End write counts_exp metadata to the file. 
 
 print(Fore.LIGHTMAGENTA_EX +
       "\n\033[4m<<-- IBM QDF Circuit Measurement Results by Qiskit Aer Simulator Plotted Successfully! End of Task... -->>\033[0m\n"
       + Style.BRIGHT + Fore.LIGHTGREEN_EX + f"\033[1m")
 
 print(f"{Fore.LIGHTGREEN_EX}Press any key to continue...")
 os.system("pause >nul")
 print(f"\033[F{Fore.LIGHTGREEN_EX + hline}")
 
#---------------------------------------------------------------------------------------------------
# <----- Display histogram results of the QDF circuit event P's and then printing the circuit ----->
#---------------------------------------------------------------------------------------------------
qdf_circuit() # Call this function to plot P results given the number of shots. 

#-------------------------------------------------------------------------------------------------------
# Visualize the Circuit in the terminal by printing the circuit... This is in python. IBMQ kernel 
# does not require print(), or simply enter qc.draw() in this case. See code from the
# 'QDF-LCode_IBMQ-2024-raw-codable.ipynb' codable file or its 'QDF-LCode_IBMQ-2024-raw.ipynb' base file.  
#-------------------------------------------------------------------------------------------------------
print(qc.draw())

fcircuit = "ibm-qdf-circuit_output.bin" # The file that the printed circuit is saved.
with open(fcircuit, 'w', encoding='utf-8') as file_to_write:
    file_to_write.write(str(qc.draw()))
    file_to_write.close() # End writing the printed circuit.

print(Back.RESET + Fore.MAGENTA+"\n\033[4m<<-- QDF Circuit BUILT & RAN Successfully! End of Task... -->>\033[0m\n"
       + Fore.LIGHTGREEN_EX), sleep(3)
print(Back.LIGHTGREEN_EX + Fore.YELLOW 
      + f"{hline}\n\033[1m<--- {{ Qiskit Aer, IBM }} QDF CIRCUIT SIMULATION CONCLUDED --->\n{hline}\033[0m" + Back.RESET) 
#########--END OF PROGRAM--#########
