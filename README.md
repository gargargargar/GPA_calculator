# GPA_calculator (THIS PROJECT IS INCOMPLETE. PLEASE COME BACK SOON.)
This is a tiny project created by Garcia (Hung-Wei) Lu (who, coincidentally, happens to me) to resolve a common high school student's and potentially college student's problem: calculating your GPA.

If you're a random Internet lurker without knowledge of how to utilize/execute/run this at all, no fear! I'll be explaining the instructions below in as much detail as possible.

## Executing the Program
Feel free to download the [python code](https://github.com/gargargargar/GPA_calculator/blob/master/GPA_calculator.py) for your own use. (Doubt this is worth any business value, but if that's legitimately what you're thinking, go find a better version of this. Seriously.)

The command line command for executing the program is as follows:
```
python3 GPA_calculator.py [--filename FILENAME] [--boost_filename BOOST_FILENAME] [--maximum MAXIMUM] [--decimal DECIMAL] [--entrytype ENTRYTYPE]
```
(You can obtain this line by typing `python3 GPA_calculator.py -h` in command line/terminal)

Here's an example of an execution:
```
python3 GPA_calculator.py --filename grade_testfile.csv --boost_filename boost_testfile.csv --maximum 4.0 --decimal 2 --entrytype letter
```

If you've downloaded every file (including the csv files) in this repo, the above code should be executable and should work.


### Parameter Explanation

If any option marked "OPTIONAL" does not apply to you, simply leave out the argument.

`--filename FILENAME`: REQUIRED. This is your csv file containing your actual grades. When using it, replace `FILENAME` with the name of your file. Further explanation in the "Creating CSV Files" section below.

`--boost_filename BOOST_FILENAME`: OPTIONAL. This is a second csv file that would indicate the GPA boosts corresponding to the course type, such as honors, AP, advanced, etc. When using it, replace `BOOST_FILENAME` with your file name.

`--maximum MAXIMUM`: OPTIONAL. This is the maximum UNWEIGHTED GPA of your GPA system, i.e. the corresponding GPA of an A+. When using it, replace `MAXIMUM` with a GPA value, such as `4.0`. Default value is `4.0`.

`--decimal DECIMAL`: OPTIONAL. Number of digits after the decimal point you would like to display. When using it, replace `DECIMAL` with an integer such as `3`. Default value is `2`.

`--entrytype ENTRYTYPE`: OPTIONAL. `ENTRYTYPE` is replaced with EITHER `LETTER` or `GPA`. `--entrytype LETTER` would indicate that your csv file stores grades as letter grades. `--entrytype LETTER` would indicate that your csv file stores grades as numerical GPA values.

### Creating CSV Files
There is one required csv files and one optional csv file.

The following csv file examples CAN BE EDITED WITH MICROSOFT EXCEL or GOOGLE SHEETS

Please download [grade_testfile.csv](https://github.com/gargargargar/GPA_calculator/blob/master/grade_testfile.csv) for an example of the `--filename FILENAME` argument. Feel free to edit the downloaded copy directly. Using this file as an example, your command line execution would look like
```
python3 GPA_calculator.py --filename grade_testfile.csv
```

Please download [boost_testfile.csv](https://github.com/gargargargar/GPA_calculator/blob/master/boost_testfile.csv) for an example of the `--boost_filename BOOST_FILENAME` argument. Feel free to edit the downloaded copy directly. Using this file (and the previous) as an example, your command line execution would look like
```
python3 GPA_calculator.py --filename grade_testfile.csv --boost_filename boost_testfile.csv
```

INSTRUCTIONS TO BE ADDED. PLEASE COME BACK SOON.

## Future Work
Portions of the main code `GPA_calculator.py` contains multiple `#TODO` comments that indicate several pending future improvements.

Future possibilities also including integrating this into an app, taking Excel/Google Sheets files as inputs, and making the execution more user-friendly.
