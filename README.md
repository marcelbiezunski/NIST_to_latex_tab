# NIST_to_latex_tab

NIST Test Results Converter for LaTeX

This application converts statistical test results from NIST, stored as text files, into a format suitable for LaTeX tables.
How It Works

To use the functionality, place all folders that may contain the "finalAnalysisReport.txt" in the "nist_folders" folder (which you store in the same directory where your application and library are located). These folders can include, for example, the default sts-2.1.2 folders found in cygwin64.

After running the application, it performs the following three operations:

    Collecting Reports
        The program searches all folders inside "nist_folders" for "finalAnalysisReport.txt" files.
        It copies all found reports into a newly created directory called "all_finalAnalysisReport".

    Converting Data for LaTeX Tables
        The first function in "latexlibrary.py" replaces spaces with "&" characters, which define table columns in LaTeX.
        The modified version of the file is saved with the "_modified" suffix.

    Translating and Formatting Test Names
        The second function translates NIST statistical test names from English to Polish (this dictionary can be customized for any language).
        To improve table readability, test names are moved to the beginning of each row, and decimal points are replaced with commas.
        The final version of the file is saved with the "_modified2" suffix.

This tool automates the conversion process, making it easier to format NIST test results for LaTeX documents.
