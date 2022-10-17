# PMG-CSV-COMBINER
Graceful integration of 0-infinite csv's with infinite columns into a single stdout csv and a downloadable csv, while maintaining 'filename' column.


This implementation is class based so that it may be extensible, handle new features (fields and methods), and potentially be integrated better with other software in the future. 

# HOW IT WORKS

It can take either a list of files as a direct argument, or sys.argv command line input.  
Files that are valid csv's will be integrated to the combined csv.  

    - The Pandas library handles concatenation of two dataframes with different columns by aligning shared columns of data and, essentially, concatenating the rest leaving blank cells where the first csv does not have data for that column.  Those blank cells will still be comma separated when converted back to csv.  Thus, Pandas handles the integration seamlessly, and Python can delete the temporary data used in each iteration of the function call, so that cumulative data storage is not an issue.  Once, a fully combined dataframe is created, the file is converted to csv format and printed to stdout, before being returned as a verifiable csv that appears in the file directory from which the user is working. 
    
    - This code handles incorrectly formatted file input and/or missing file input by only combining valid csv input and sending error messages in response to faulty input without crashing.  
    
                - If no valid file input is provided,  the result of trying to 'combine' the missing input is simply a return value of False.
  


# BENEFITS!
  - Clean code with ample comments, easy to follow
  - Simplistic code design that avoids typical code smells such as unecessary loops, imports, formatting, etc. 
  - Written in OOP class based style, so as to accrue extra fields/methods over time as needed
  - Has built in input file validation, does not crash if files are entered errorneously or are not found
  - Integrates limitless columns seamlessly!!!



Enjoy combining CSV's !!!!
  
