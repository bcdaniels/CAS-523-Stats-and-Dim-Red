# CAS 523: Statistics & Dimensionality Reduction

This repository contains coding examples and exercises for Arizona State University's course CAS 523 — Methods for Complex Systems Science: Statistics and Dimensionality Reduction.

Instructor: Bryan Daniels

## Course Description

Complex systems involve a large number of interacting components, and consequently observational studies of these systems typically generate data sets of high dimension.  It is common, for instance, to be faced with data from hundreds or thousands of distinct neurons in a brain, genes in a cell, people in a society, firms in an economy, or texts in a corpus.  To make sense of such data, a diverse set of tools has been developed that summarizes key properties at the population level (statistics) and characterizes predictable lower-dimensional patterns (dimensionality reduction).

This course will provide a guided tour of the tools of data analysis, focusing on those most relevant to complex adaptive systems.  With a solid foundation in inferential statistics, we will encounter PCA-type linear projections, nonlinear manifold techniques, topic modeling, clustering methods, network statistics, and more.  We will also explore more abstract foundations for how these methods work and when they fail, from information bottleneck theory to Bayesian model selection.  Students will hone their data skills by applying state-of-the-art open-source software to real-world datasets.

## Getting Started

This course will use coding examples and exercises written in the programming language Python.   We will typically run Python code using interactive Jupyter notebooks, a convenient format that allows for running and saving Python code along with results that the code produces.  This github repository contains a collection of Jupyter notebooks that we will use in class.

### Setting up Python and Jupyter

To run Python and Jupyter on your own computer, we recommend installing the Anaconda package, available for Windows, Mac, and Linux here: https://www.anaconda.com/products/distribution 

If you already have a different favorite way of running Python code, feel free to use what you are most comfortable with.  We will identify any dependencies on packages outside of Python and Jupyter so you will know exactly what you will need (likely standard data science packages included in Anaconda such as `numpy`, `matplotlib`, and `pandas`).

### Setting up this git repository

The _simplest_ way to access the code in this repository is to download a zip file containing all its files by clicking the green "Code" button and then "Download ZIP" on the webpage for this repository: https://github.com/bcdaniels/CAS-523-Stats-and-Dim-Red 

A perhaps _better_ way to access the code is to use `git`, a widely-used tool for version control.  This is not required for the course, but it is something you will definitely want practice using if you are aiming for a career involving any kind of collaborative coding.  Running `git clone https://github.com/bcdaniels/CAS-523-Stats-and-Dim-Red.git` at a command line will create a subdirectory containing a copy of the code as a full `git` repository, with all the version control powers that entails.  There are plenty of places to get introduced to the basics of `git`.  A good start would be to review [the basic git commands](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/) and [the popular github workflow](https://guides.github.com/introduction/flow/).