# Table of Contents

* **[Aim](#aim)**
* **[Setup requirements](#setup-requirements)**
  * [Python](#python)
  * [Pip](#pip)
  * [NumPy](#numpy)
  * [Pandas](#pandas)
* **[Running](#running)**
  * [Before...](#before)
  * [How to run](#how-to-run)
  * [Field indexes input](#field-indexes-input)
* **[Small example case](#small-example-case)**
    * [Source data](#source-data)
    * [Lookup data](#lookup-data)
    * [Run](#run)
    * [Output data](#output-data)
    * [Conclusion](#conclusion)
* **[Development](#development)**
  * [License](#license)
----

# Aim
Check the records (rows) of csv lookupData in which contains key contained in csv sourceData, generating an output (new) file at the end.

*All the lines with same key in lookupData are captured, but the keys in sourceData must be unique.*


# Setup requirements
The following instructions might set up all of the development steps needed to use this script. The steps consider a Debian-like system.

## Python
If you do not have the latest version of Python:

```$ sudo apt-get upgrade python3```

## Pip
And if you don't have the latest version of the Python's package manager `(pip)`:

```$ python3 -m pip install --upgrade pip```

## NumPy
If you don't have the latest version of the [NumPy package](http://www.numpy.org/):

```$ python3 -m pip install numpy```

## Pandas
If you don't have the latest version of the [Pandas library](https://pandas.pydata.org/):

```$ python3 -m pip install pandas```


# Running
## Before...
- Copy and paste the script files to the folder where the csv source data and csv lookup data are.
- If some of your database files (source or lookup) is huge (> 1 million entries), be sure to just do this task and in command-line environment (like tty).
- Be aware of the amount of lines your files have:

```wc -l <file.csv>```

## How to run
In terminal, type the command:

```python3 csv_vlookup.py <sourceData.csv> <lookupData.csv> <newOutputDataFile.csv>```

E.g.:

```python3 csv_match_files_keys.py source.csv lookup.csv newOutputFile.csv```

### Field indexes input
The script will ask you for the column field index of both files. Consider the first column as index=0.


# Small example case
## Source data
Consider the source file called 'srcData.csv' with this content:

```
primaryKey,value
air,aaa
smell,bbb
hand,ccc
dude,ddd
road,eee
cat,fff
```

## Lookup data
And the lookup file called 'lookupData.csv' with this content:
```
primaryKey,value1,value2
air,col01,col02
air,col11,col12
smell,col21,col22
hand,col61,col62
dude,col31,col32
road,col41,col42
cat,col51,col52	
mouse,col71,col72
```

## Run
Know see the script behavior typing on the terminal:

```python3 cross_vlookup.py srcData.csv lookupData.csv newOutputDataFile.csv```

## Output data
The newOutputDataFile.csv will have this content at the end:
```
primaryKey,value1,value2
air,col01,col02
air,col11,col12
smell,col21,col22
hand,col61,col62
dude,col31,col32
road,col41,col42
cat,col51,col52	
```

## Conclusion
Note that the register (row) `mouse,col71,col72` of `lookupData.csv` was not appended to the output, because its key `mouse` didn't exist in `srcData.csv`.


# Development
The csv_vlookup source code is [hosted on GitHub](https://github.com/igorasantos/csv_vlookup).

Please feel free to submit [pull requests](https://github.com/igorasantos/csv_vlookup/pulls) and bugs on the [issue tracker](https://github.com/igorasantos/csv_vlookup/issues).

## License
[The MIT License](LICENSE)
