#Diseased Cell Translator Lab Notebook
------------------------------------------------------------------------------------------------------------------------------------------
## 06/04/2026

###Goal: 
Setup and explore the basic python program structure. Understand how basic genomics structures are modeled in computers. 

###What I did:
Downloaded and installed Git and Python into VS code.

Installed: 
 numpy, pandas, scikit-learn, matplotlib, torch, jupyter

Created the following folders: 
 data, src, tests, documents

Created the following folders: 
 data: eventually will store larger real-life datasets.
 documents: used to store long-term ideas and lessons in programming, python, biology, and machine learning. Also contains a future goals roadmap.
 src: contains the source code of the project
 tests: will contain programs that will check the validity of the code contained in src later on.


Created the following files:

README: general summary of the purpose of the program
lab_notebook.md: breif documentation of what I learned, my daily goals, and what I learned.

In the documents folder:
 biology_notes.md: used to store and document biology lessons learned.
 machine_learning.md: used to store and document machine learning lessons.
  python.md: used to store and document python lessons.
  ideas_md: used to store longterm questions and ideas that arise during exploration.
  roadmap.md: used to store next step goals for subsequent research sessions.
  LICENSE: used to indicate what other students can do with the code. 
   (chatgpt recommended it)
 .gitignore: tells githib what files to ignore.

In the src folder: 
cells.py: used to contain needed functions to be used in cell data analysis

main.py: used as the main file to upload/create cell datasets and to call upon functions.

###what I did learned;
- how to clone a repository from github into VS code instead of copy-and-pasting program files from bluebird into github.
- python projects are organized into folders for organization and split much like earlier java projects I learned on in my previous computer science class.
- How to operate and navigate basic VS code UI components like the terminal, folders, and the command prompt.
- python basics like lists, matrices, and variables.
- main.py functions exactly like the main file in java,
- GITHUB repositories usually keep README.md and LICENSE in yhe prject root instead of the documentation section.
- how to create a lab notebook
- how to install python libraries and GIT outside of a browser.

###Questions: 
- How does an actual biological matrix look like - does it look like chatgpt generated examples?
- How should I determine the rules for analyzing datasets - do I use rule-based code or machine learning?
- Is a README usually breif, or does it get added onto as the program gets improved?
- How do researchers in the field confirm these findings - do they send their hypothesis to wet labs?
- How much of a cell's stae can be predicted from looking at gene expression alone?
- Can genes with low expression levels have dispropotionately large effects on cell behavior?
-----------------------------------------------------------------------------------------------------------------------------------------
 
## 06/05/2026

###Goal: Continue learning about genomics modeling by looking at a real dataset and create a few working functions that can be used to analyze test data sets. Create another reproducible lab notebook. 

###What I did: 
- Created a count() function in cells.py: 
- Created a disease_percentage() function in cells.py:
- Created my first mock jupyter notebook that is able to test these functions on sample, mock datasets.
- Installed numpy and pandas to the jupyter file.
- Created a requirements.txt file
- Tested the functions also in main.py: 

###What I learned: 
- Installing numpy and pandas on one file does not automatically install them for all files. (The Jupyter notebook needed a seperate installation to run the kernals)\
- The lab notebook here is actually more like a lab journal, since the Jupyter notebok actually contains the reproducibility.
- How to freeze the different versions of software used and add them in a requirements.txt to simulate reusability practices for potential later research.
- How to make a juptyter lab notebook and what markdown files actually are. (I previously used kernels in browser for my summer course, so seeing the jupyter notebook layout was almost exactly like how I had to code during the summer course)
- What the pycache file that popped up in my files does and why it appears. 
- That the terminal needs a path and authentication for some actions, as the functions called in the jupyter notebook did not run until cells.py was referenced in src. 
- setting up a jupyter lab notebook takes longer than expected. i was not actually able to look or import a real biological dataset in this session. (The data used to test the functions was fake)

##Questions: 
- How big can this lab journal file get? Adding the exact code that I did in cells.py and main.py takes a lot of space and the code produced in each section may get lerger. 
- Why is there a test file included if the testing of the functions was done in main.py.
- How do programmers trust large datasets to be entered in correctly - is there a designated job where someone reviews the millions of datapoints to make sure the data is uniform before the dataset is published.
- Is there more than one method of coding in python? I coded the traditional way through syntax and loops, but chatgpt also suggested: an ifinstance shorthand command. Is that a function or another way of programming?
- After pushing the code to github, can all of the programs be retreived in the event the computer crashed or should I put my projects on a hard drive?
-----------------------------------------------------------------------------------------------------------------------------------------
