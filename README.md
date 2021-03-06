<p align="center">
  <a href=#>
    <img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210625%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210625T160339Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=de6e8f4211025908f415455a259900aae4dc9a9815c7557e1f0859a44ca5a348" alt="Holberton School HBnB logo">
  </a>
</p>

# HBnB
_Holberton School Air BnB clone_

## Table of Contents
* [About](#about)
* [The Console](#the-console)
* [Authors](#authors)

## About
HBnB is a clone of Air BnB. The project is divided into 7 parts:
1. The console
2. HTML
3. MySQL
4. Fabric
5. Flask
6. REST API
7. Web dynamic

## The Console

The Console is the first part of the HBnB clone. In it, we wrote classes for representing users and listings, a file storage engine for saving and recalling data between interactive sessions, as well as a command interpreter for easily managing our data.

### HBnB CLI — The command interpreter

The HBnB CLI (command line interpreter) provides a convenient command line interface specifically to manage (add, delete, modify, etc.) HBnB data.
It offers an imporved workflow over alternatives such as embedding data in the source code, manually managing a data file, or using the Python interpreter to manage the data.

### Commands
* `all [CLASS]` - Show all objects.
* `create CLASS` - Create a new object.
* `destroy CLASS ID` - Destroy a specified instance.
* `help [COMMAND]` - Get information about a command.
* `quit` - Close an interactive session. Also quit with `^-D` or `EOF`.
* `show CLASS ID` - Display a single instance.
* `update CLASS ID ATTRIBUTE VALUE` - Edit attributes of an instance.

### Usage

Start an interactive HBnB CLI session by executing `console.py`:

`./console.py`

If it runs sucessfully, it will display the prompt and await input:

`(hbnb) `

Simply type any valid command(s) listed above. Type `quit` to exit the interactive session.

The HBnB CLI may also be used non-interacively by piping input to it from a shell:

`$ echo "help" | ./console.py`


### Examples
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create Place
aba364fd-8b9e-4c4b-b865-8db6a6e9bc03

(hbnb) all
["[Place] (aba364fd-8b9e-4c4b-b865-8db6a6e9bc03) {'created_at': datetime.datetime(2021, 7, 1, 13, 29, 27, 264673), 'id': 'aba364fd-8b9e-4c4b-b865-8db6a6e9bc03', 'updated_at': datetime.datetime(2021, 7, 1, 13, 29, 27, 264832)}"]
(hbnb) 
```

## Authors
Justin Masayda [@keysmusician](https://github.com/keysmusician)

Carson Stearn [@krytech](https://github.com/krytech)
