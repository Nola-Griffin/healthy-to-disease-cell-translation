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

 added: 
    print("test run")

    cells = ["healthy", "healthy", "diseased"]

    for cell in cells: 
        print(cell)

 (then the code was deleted once the folder was determined to hold functions. (chatgpt suggested that I do this))

main.py: used as the main file to upload/create cell datasets and to call upon functions.
 added: 
 def main():
    print("Diseased Cell Translator starting...")

 if __name__ == "__main__":
        main()

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
 


