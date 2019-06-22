## Basics > Outputs

#### stdout
  - print('this will be printed')

#### formatting
There are quite a few different way to format strings
```python
var = 3
var_string = f"The variable is: {var}"
var_string = "The variable is: {0}".format(var)
var_string = "The variable is: %r" % (var)
print("",var,"")
```

### files
  - write()
  ```python
  with open('filename', 'w') as open_file:
    open_file.write('this goes into the file')
  ```
  - opening a file with 'w' will overwrite anything that was in the file before
  - use 'a' to open the file and add to the existing contents
  - use 'w+' to create the file if it doesn't already exist