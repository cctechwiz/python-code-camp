## Basics > Control Flow

#### Branching
  - if
  ```python
  height = 42
  if height < 45:
    print('sorry, too short to ride')
  ```
  - if/else
  ```python
  height = 42
  if height < 30:
    print('sorry, too short to ride')
  else:
    print('welcome aboard!')
  ```
  - if/elif/else
  ```python
  height = 42
  if height < 30:
    print('sorry, too short to ride')
  elif height < 45:
    print('you have to ride with an adult')
  else:
    print('welcome aboard!')
  ```
  - if/in
  ```python
  heights = [45, 34, 37, 30, 44, 50]
  if 30 in heights:
    print('someone is too short to ride')
  ```

#### Looping
  - for/in
  ```python
  heights = [45, 34, 37, 30, 44, 50]
  for height in heights:
    if height < 31:
        print(f'{height} is too short to ride')
  ```
  - for/in/else
  ```python
  heights = [45, 34, 37, 30, 44, 50]
  for height in heights:
    if height < 31:
        print(f'{height} is too short to ride')
  else:
    print('nothing to iterator over in that list')
  ```
  - while
  ```python
  x = 0
  while x < 7:
      print(x)
      x = x + 1
  ```
  > Warning: while loops can create ```infinite loops``` and destroy the universe... ok not really, but your program will be stuck for there forever unless you give it a way out.
  > You can use Ctrl-c to kill your program and get out of infinite loops.

  ```python
  while True:
    print('stuck in here forever')
  ```

  > Or you can give your loops a way out with ```break```

  ```python
  while True:
    command = input("Enter a command (type q to exit): ")
    print(f'you entered {command}')
    if command == 'q':
      break
  ```