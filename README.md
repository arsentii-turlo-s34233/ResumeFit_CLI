# ResumeFit_CLI

ResumeFit CLI is a simple Python command line project. It compares a resume or CV with a job description using .txt files.

The program checks hard skills, soft skills, years of experience, and education level. After analysis, it shows an overall fit score, matched skills, missing skills, and recommendations. The last result can also be exported to a JSON file.

How to run

Run the project from the main folder:

python main.py

Menu options

- 1 - Load Resume
- 2 - Load Job description
- 3 - Show loaded status
- 4 - Analyze resume fit
- 5 - Export last result to JSON
- 0 - Quit

Sample files

You can test the program with:

Data/sample_resume.txt
Data/sample_job.txt

Example test flow

Run:

python main.py

Then choose:

1 and enter Data/sample_resume.txt
2 and enter Data/sample_job.txt
4 to analyze
5 to export the result to JSON

Project structure

main.py starts the program.

The ResumeFit folder is used as a Python package. It contains an init.py file, so Python can treat this folder as a package and allow imports between modules.

The project is split into separate files:

app.py contains the command line menu.

analyzer.py contains the main analysis logic.

constants.py contains hard skills and soft skills.

decorators.py contains the custom decorator.

exceptions.py contains custom exceptions.

models.py contains the Document and AnalysisResult classes.

report.py prints the analysis report.

scoring.py contains score calculation functions.

storage.py loads .txt files and saves JSON reports.

text_tools.py contains text processing and regular expression functions.

Why some Python features were used

Classes were used to keep related data together. Document stores the file path and text. AnalysisResult stores the result of the analysis.

A decorator was used to check if both files are loaded before running the analysis.

A generator was used for recommendations. It gives recommendations one by one depending on what is missing in the resume.

Regular expressions were used to find skills, years of experience, and education level in text.

Sets were used because they make it easy to find matched and missing skills.

JSON serialization was used to save the last analysis result to a file.

Comprehensions and lambda were used in helper functions to make some operations shorter, for example formatting skills and sorting the skill summary.

Python topics used

The project uses functions, classes, modules, regular expressions, file handling, JSON serialization, custom exceptions, a decorator, a generator, lambda, comprehensions, sets, dictionaries, and a command line menu.

Note

It is not a real ATS system. The analysis is based on simple keyword matching and regular expressions.