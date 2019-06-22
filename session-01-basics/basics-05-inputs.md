## Basics > Inputs

#### stdin
 - input()
 ```python
 name = input('What is your name? ')
 age = int(input('How old are you? '))
 ```
 - getpass()
 ```python
 from getpass import getpass
 secret = getpass('Tell me a secret: ')
 ```

 > We'll talk about importing modules more later. :)
 > If you're curious about what all you can import you can open ipython and type
 > ```help('modules')```, then use help() to dig into what each modules does remember to use '' around modules names in help().

#### files
 - open()
 ```python
 f = open('file_name', 'r')
 # f is now a file descritor, aka it holds information about the open file
 ```
 - read()
 ```python
 d = f.read()
 # d now contains all the contents of the file
 ```
 - readline()
 ```python
 l = f.readline()
 # l now contains the first line of the file
 ```
 - readlines()
 ```python
 ls = f.readline()
 # ls now contains a list of all the lines of the file
 ```

With each of the above examples you would be responsible for closing the file after you are done with it.
```python
f.close()
```
That can be hard to remember to do sometimes if you have lots of operations to perform on a single file.
So python has a nice syntax for hanlding that for you. When you leave scope of the with block the file is automatically closed.

 - with/as
 ```python
 with open('filename','r') as open_file:
    ls = open_file.readlines()
    # Note the white spacing here, this line is tabbed underneath the with statement to creat the new scope
 ```
 - for/in
```python
 with open('filename','r') as open_file:
    for l in open_file.readline():
        print(l)
        # Note how there are two tab groups here, there are two scopes happening at the same time
        # Everything tabbed in under for has access to l now
 ```