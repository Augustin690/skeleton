This file explains how to install the dependencies required to make this lab
work on your own machine. If you are working on the computers in the Télécom lab
rooms, everything you can skip this step.

The lab session is written for a Linux-based system, and is not intended to work
on Windows or Mac OS. The lab session requires a working Python 3 installation,
the Python modules `wtforms` and `flask`, and a working SQLite 3 installation.

You should first ensure that you have Python3 installed (e.g., the command
`python3` exists), and that you have SQLite 3 installed (e.g., the command
`sqlite3` exists). If not, on a Debian-based system (e.g., Ubuntu), you can run:

`sudo apt install python3 sqlite3 `

On a different distribution, you should use your distribution's package manager.

You should then install the `flask` and `wtforms` modules. There are three
options for this:

## Option 1: installing the distribution packages

On a Debian-based system (e.g., Ubuntu), you can simply run:

`sudo apt install python3-flask python3-wtforms`

On a different distribution, you should use your distribution's package manager.

## Option 2: using pip

You can simply run: `pip3 install requirements.txt`.

If you do not have the `pip3` executable, you may need to install it. On Debian
systems, this is done by:

`sudo apt install python3-pip`

On a different distribution, you should use your distribution's package manager.

This will install the requirements in your user's home directory, and `python3`
should then be able to find them.

## Option 3: create a virtual environment

A virtual environment is a way to install the Python libraries required for a
project, but only locally to a given project, instead of globally. To use it,
open a terminal and navigate to the folder of your project. Then create the
virtual environment by running:

`virtualenv venv`

This will create a folder `venv` containing the data of the virtual environment.
Next, activate the virtual environment by running:

`source venv/bin/activate`

Your terminal prompt should now indicate "venv".

Now, whevener opening a terminal to work on the project, just after navigating
to the project's directory, you should run again:

`source venv/bin/activate`

If you do not have the `virtualenv` program installed but have the `pip3`
program installed, you may install it by running:

`pip3 install virtualenv`

