import os
import pandas as pd
import sys


class CsvCombiner:
    """A class that takes csv files and uses the combine_csvs method and its helper methods to
    combine csvs with unlimited csv file inputs, even with different columns"""
    def __init__(self, files):
        """Extensible as it allows user to provide a list of files or, in the absence of passed parameters,
        executes with sys.argv input, using the files provided"""
        if files is None:
            # first argument at index 0 is ignored, to focus on the files we are passing as arguments0
            self.files = sys.argv[1:]
        else:
            self.files = files

    def get_basename(self, given_file):
        """using the os.path.basename() method allows us to extract and return the basename of the file as a string"""
        basename = os.path.basename(given_file)
        return str(basename)

    def generate_filename_column(self, given_dataframe, basename):
        """This method takes arguments that are a dataframe and its basename, then
        creates a new column for that dataframe filled with the basename in each cell."""
        # make a horizontal list filled with csv's base file name,
        filename = [basename for x in range(0, len(given_dataframe))]

        # then use that data to fill a new column titled 'filename' with list
        given_dataframe['filename']=filename
        return

    def generate_dataframe(self, given_csv):
        """turns a csv into a pandas dataframe, creates new column with filename, and makes sure that
        each of the columns is lower case to assist in future concatenation before returning new df"""

        # convert csv to df
        new_dataframe = pd.read_csv(given_csv)
        base = self.get_basename(given_csv)

        # get new column based on the file basename
        self.generate_filename_column(new_dataframe, base)

        # ensure all lower case
        new_dataframe.columns = [each_col.lower()for each_col in new_dataframe.columns]

        return new_dataframe

    def combine_csvs(self, list_of_csvs):
        """uses generate_dataframe method to turn csvs into dataframes, adds requested 'filename' column with the
        generate_filename_column, and uses pandas concatenation to handle the addition of csvs that may have new
        columns that are not mentioned in the original csv(s) for extensibility.  Converts the resultant combined
        dataframe to a csv to be returned as a file, and provides print out standard output version in the terminal."""

        # start empty dataframe with which we will combine all subsequent VALID csvs.
        csv_accumulator = pd.DataFrame()

        # for unlimited valid csvs, format each with filename column as a dataframe, and concatenate to csv_accumulator
        for spreadsheet in list_of_csvs:

            # only if valid .csv
            if '.csv' in spreadsheet:
                try:
                    new_df_to_concatenate = self.generate_dataframe(spreadsheet)
                    csv_accumulator = pd.concat([csv_accumulator, new_df_to_concatenate])
                except FileNotFoundError:
                    # this would handle invalid csvs
                    print(f"File Not Found. \nCheck to ensure that the file  '{spreadsheet}'  was typed properly.")
                    continue
            else:
                # if the file was not a csv to begin with, print the message and go to the next
                print(f"{spreadsheet} does not include the correct extension.  Please provide valid .csv file")
                continue

        if csv_accumulator.empty:
            print("No valid csv provided.")
            return False

        # provide standard output print version
        stdout_combined_csv = csv_accumulator.to_csv(index=False)
        print('\nCSV STANDARD OUTPUT:\n', stdout_combined_csv)

        # convert to csv with filepath in working directory, to have an actual .csv file available
        filepath = 'combined_spreadsheets.csv'

        combined_csv = csv_accumulator.to_csv(filepath, index=False)
        # new csv file will appear in working directory
        return combined_csv


def main():
    """an example of the use of my class"""
    files = ['clothing.csv', 'accessories.csv', 'household_cleaners.csv']
    combiner = CsvCombiner(files)
    combiner.combine_csvs(files)


if __name__ == '__main__':
    main()