# Contributing Guidelines 

### To contribute you need to setup a virtual environment !!!
### Prerequisites
- Python must be installed in your system
- Basic knowledge of python modeles
## Get Started

1. Fisrt install the `virtualenv` python module
```bash
pip install virtualenv
```
2. Now fork the project and clone it in your local machine.
```bash
git clone <url of the repo>
```
3. Open the root dir in the project and create an virtual environment with a name of `env`. ***Make sure to to give the name `env` to the virtual environment.***

```bash
virtualenv env
```
The virtual enviroment is created.
4. Now activate the virtual environment
```bash
env\Scripts\activate
```
This is for windows system.
```bash
source env/bin/activate
```
This is for linux.
4. Now install all the required modules
```bash
pip install -r requirements.txt
```
This command will install all the modules mentioned in the requirements.txt.

5. Now make changes and contribute as much as possible.

### Warning !! This is an unfinished prototype project and it is in the start of the development stage so it is unreliable. 