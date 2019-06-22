## Basics > Variables

### Variables
You can create variables by just typing a name = some value
 - x = 1
 - y = "hello"

### Types
#### numbers
 - ints (whole numbers without decimals)
   - 3, 5, 64563
 - floats (numbers with decimals)
   - 1.2, 3.14, 6.28

#### strings (words and sentences)
 - 'hello'
 - "hello"
 - """
   hello
   """

#### boolean
 - True
 - False

#### lists
 - [1, 2, 3, 4]
 - ['apple', 'banana', 'pear']
 - [1, 'apple', 5, False]

List can be accessed with an index (zero based counting), or with iteration (which we'll see in a bit).
 - ```x = [1, 2, 3, 4]```
 - ```x[0]``` will be 1

What happens if we don't give it an good index number?
 - ```x[12]``` will say ```list index out of range```
 - ```x[-1]``` will be 4 (last element)

What if you wanted to get some of the items from the list, not just one?
 - ```x[0:3]``` will be [1, 2, 3] (we asked for items starting at 0 and stopping before 3)
 - ```x[2:]``` will be [3, 4] (we asked for items starting at 2 and stopping at the end)
 - ```x[0:3:2]``` will be [1, 3] (we asked for items starting at 0 and stopping before 3, couting our index by 2)
 - These are called ```list slices```, you can get some more info in this [stack overflow post](https://stackoverflow.com/questions/509211/understanding-slice-notation)

You can also get fancy and nest lists inside of lists
```python
x = [
    [1, 2, 3, 4],
    ['apple', 'banana', 'pear'],
    [1, 'apple', 5, False]
]
```
- ```x[0]``` will be [1, 2, 3, 4]
- ```x[0][0]``` will be 1

Did you know that strings are just lists of characters?
```python
x = 'Hello'
```
- ```x[0]``` will be 'H'
- You can do all the same list slicing on strings as well

#### dictionaries
 - {key: value}
 - {'sunday': 'roast', 'monday': 'ham', 'tuesday': 'chicken'}
 - {'jack': 12, 'jerry': 11, 'tom': 13}

 Dictionaries can be accessed by the key, or with iteration (which we'll see in a bit).
 - ```x = {'jack': 12, 'jerry': 11, 'tom': 13}```
 - ```x['jack']``` will print 12

 You can also get fancy and nest dictionaries inside of dictionaries
```python
x = {
    'jack': {'age':12, 'hair': 'brown'},
    'jerry': {'age':11, 'hair': 'brown'},
    'tom': {'age':13, 'hair': 'brown'}
}
```
- ```x['jack']``` would be {'age': 12, 'hair': 'brown'}
- ```x['jack']['age']``` would be 12

#### type() & casting
We can use the type function to see the type of any variable
 - ```type(3)``` will tell you that 3 is an ```int``` which is short for integer
 - ```x = "hello"``` then ```type(x)``` will tell you x is a ```str``` which is short for string

You can change the type of a variable by ```casting``` it. Some things won't cast correctly
- ```float(1)``` --> 1.0
- ```int(1.2)``` --> 1
- ```str(1.2)``` --> '1.2'
- ```int('1')``` --> 1
- ```int('1.2')``` --> error, you need to do ```int(float('1.2'))``` (you can only do one cast at a time, str --> float --> int)

#### Comments
You can use the # symbol to comment out a line of code, or add a note to your code.
Nothing that starts with a # will be run when the program is executed.
```python
# The following dictionary contains the friends and their ages
friends = {'jack': 12, 'jerry': 11, 'tom': 13}
```