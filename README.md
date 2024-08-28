# QFLCS: Quantum Field Lens Coding Simulator  

This repository contains the code for the QFLCS (Quantum Field Lens Coding Simulator) as part of its algorithm, QFLCA (Quantum Field Lens Coding Algorithm) project.
The project repositories are available at https://data.mendeley.com/datasets/gf2s8jkdjf/3 and https://doi.org/10.24433/CO.9905505.v2, which include the code, project website documentation and demo video files.

<kbd> ![1D-circuit-01](https://github.com/user-attachments/assets/df63a875-46fa-42fc-a498-6e780666718e) </kbd> 

The QFLCS program analyzes the measurement outcome probability ($\cal P$) data from datasets generated by Quantum Double-field (QDF) Circuits. The datasets are compared between ES and GS states as a $\cal P$ indicator generated for measurement samples. Small dataset samples denote: 

<kbd> ![QDF_Demo Line](QDF_demo_line.gif) </kbd>

a. A particle pair’s energy state in a QDF (different GS states or sublevels of a GS, or see Sec. 3 of the published article), <br>
b. a particle state in an SF, an ES relative to a GS from (a.), prior to its transform into a QDF, and, <br>
c. the expected transformation of fields (ES $\longleftrightarrow$ GS) and their $⟨{\frak M}(\cal{P}, \psi_{ij})⟩$, as in Sec. 3 of the published article.

<kbd> ![k-trans-QDF-P-measure-IN](k-trans-QDF-P-measure-IN.png) </kbd>

This repository's file structure is a sample mirror of the Mendeley repository file structure of v3+ at https://data.mendeley.com/datasets/gf2s8jkdjf/3, but with a much smaller file size for efficient download and use of the QFLCA project's code without the documentation (website) and demo video files. Certain small updates have been made in the main python file uploaded on Code Ocean for minor debugging purposes at https://doi.org/10.24433/CO.9905505.v2. 

* QFLCA project's code without the documentation (website) and demo video files can be found under the <code></code/root/lab/sim/QFLCC classifiers></code> directory in <code></code/root/lab/sim/QFLCC classifiers/docs></code> and <code></code/root/lab/sim/QFLCC classifiers/site></code> folders at https://doi.org/10.24433/CO.9905505.v2. 

<kbd> ![QDF_Circuit_and Dataset Analysis](QDF_circuit_screenshot.jpg) </kbd>
* The main file is <code></code/root/lab/sim/QFLCC classifiers/QAI-LCode_QFLCC.py></code> which imports and executes the <code></code/root/lab/sim/QFLCC classifiers/QDF-LCode_IBMQ-2024-codable.py></code> or <code>QDF-LCode_IBMQ-2024.py</code> code for the simulation under Win OS or Linux OS. 

* We recommend downloading the entire <code> root </code> directory according to the folder structure and run <code>QAI-LCode_QFLCC.py</code> in VSC with python latest packages installed for Windows OS (the QDF game is developed for Windows OS, yet parts of the code for sound and display can be rewritten for Linux OS), e.g. <code>"winsound"</code> package as a compatible option. 
Other packages are needed to be installed or code rewritten for <code>"sound"</code> and <code>"display"</code> compatibility under other operating systems. 

<kbd> <img src="https://github.com/user-attachments/assets/a6e1eece-0292-441b-a752-928f56f19928" style="border: 2px solid green" /> </kbd>
 
* The <code>QAI-LCode_QFLCC.py</code> file has a Pygame GUI and other packages suited for local machine runs, rather than running this file on the Code Ocean platform which could take hours to compile and run a compatible program/game with packages. 
However, the <code>QDF-LCode_IBMQ-2024-codable.py</code> can be run here as the core of the simulation program simulating the QDF circuit. 
A short presentation explaining these points are given in the <code></site/assets/video></code> directory as the <code>QAI-COcean-Demo.mp4</code> file.

<kbd> ![QDF Game Scores Screenshot](QDF_game_screenshot.jpg) </kbd>

* The User and Developer's documentation/manual/demo is found under the <code></code/root/lab/sim/QFLCC classifiers></code> directory, as <code> site-prints </code> and <code> site </code> contents.

* In each folder <code><QFLCC classifiers/IBMQ>, <.../sim/QAI>, </QFLCC classifiers></code> and <code> QI </code> under <code></code/root/lab/sim></code>, <code>Tips.txt</code> and/or <code>ReadMe.txt</code> files exist to explain the contents of that directory. Also, under <code></code/root/lab></code> directory, a ReadMe file exists explaining the manual computation and presentation parts of the project.

<hr />

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
