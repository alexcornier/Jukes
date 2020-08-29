# "Jukes Cantor 1969" Project

Master's Project, Bio-Computing, University of Bordeaux, 2019-2020

Phylogenetics is the study of evolutionary relationships between organisms. The main purpose is to reconstruct correct phylogenetics tree while estimating the time of divergence between organisms and knowing the sequence of events along evolutionary lineages.

So, to build phylogenetics tree it’s necessary to calculate the genetic distance between two homologous sequences. Which is the number of substitutions accumulated between them since they diverged from their common ancestor. The Challenge is not simply count the number of position at which the two sequence differ but to calculate the genetic distance while taking into account the fact that there may be several substitutions on the same site

For this, many probabilistic models vary according to the parameters used to describe the velocities at which one nucleotide replaces another during evolution. As part of my project, I worked on the Jukes Cantor 1969 model to show how this model of substitution is the simplest and fastest one as it provides results in one single pass. Also this model specifies that the equilibrium frequencies of the four nucleotides are 25% each and has the same probability to be replaces by any other during the evolution.

## To start

This code was developed using Python with few common libraries like MathPlotLib.
A good start is reading first the document **[Jukes.pdf](Jukes.pdf)** provided in this repository.

### Requirements

The following knowledges and environment are required to run this code:

* Python 3.7 with modules Random, Math, MathPlotLib
* IDE, for instance PyCharm, VSCode with Python module, Jypiter...

### Installation

Recommended step by step is:

* Prepare the Python environement
  * creating a specific venv is a good idea (see Python best practices on the Internet
* Clone the repository
* Run jukes.py and enjoy

## Build with

Products below where used to build this application:

* [Anaconda](https://www.anaconda.com/products/individual) - Python environment
* [Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown) - VS Code with modules Python for the program and markdown to create this README.md

## Versions

Available versions:

* **Last version :** 1.0

## Author

Application developed by:

* **Alexandre Cornier** _alias_ [@alexcornier](https://github.com/alexcornier/)

## License

This project is under ``MIT License`` License - Cf. file [LICENSE.md](./LICENSE.md) for any further details.
