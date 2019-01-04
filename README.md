# Aim
Check the records (rows) of csv lookupData in which contains key contained in csv sourceData.
*All the lines with same key in lookupData are captured, but the keys in sourceData must be unique.*

# Setup requirements
The following instructions might set up all of the development steps needed to use this script. The steps consider a Debian-like system.

## Python
If you do not have the latest version of Python:

```$ sudo apt-get install python3```


## Pip
And if you don't have the latest version of the Python's package manager `(pip)`:

```$ python3 -m pip install --upgrade pip```


## Pandas
If you don't have the latest version of the [Pandas library](https://pandas.pydata.org/):

```$ python3 -m pip install pandas```


## Numpy
If you don't have the latest version of the [Numpy package](http://www.numpy.org/):

```$ python3 -m pip install numpy```


# Running
## Before...
- Copy and paste the script files to the folder where the csv source data and csv lookup data are.
- If some of your database files (source or lookup) is huge (> 1 million entries), be sure to just do this task and in command-line environment (like tty).
- Be aware of the amount of lines your files have:

```wc -l <file.csv>```

## How to run
In terminal, type the command:

```python3 csv_match_files_keys.py <sourceData.csv> <lookupData.csv> <outputData.csv>```


E.g.:

```python3 csv_match_files_keys.py source.csv lookup.csv output.csv```

### Input the field indexes
The script will ask you for the column field index of both files. Consider the first column as index=0.

# A small example case
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

Know see the script behavior typing on the terminal:

```python3 cross_vlookup.py srcData.csv lookupData.csv outputData.csv```

The outputData.csv will have this content at the end:
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
