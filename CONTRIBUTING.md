# Contributing Guidelines 

### 🔔 To contribute you need to setup a virtual environment !!!

### 🔔  `dev` branch is our primary development branch, all works will be done on `dev` branch
### Prerequisites
- Python must be installed in your system
- Basic knowledge of python modeles
## Get Started 🏃💨

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
pip install -r src/requirements.txt
```
This command will install all the modules mentioned in the requirements.txt.

5. Now make changes and contribute as much as possible.

## Best Practices 🥇 ✅

1. Do not start making changes on the dev branch after pulling it in you local system. Make a seperate bracnh from `dev` branch and give a proper name to the branch. Then push the branch to your `origin` then make a pull request from your created branch to our `dev` branch.
2. Variable names must be in `snake case`.
3. Function name must be in `camel case`.
4. Class name must be in `pascal case`.

## Local Testing 👩‍🔬🧪
There is a `test` dir in the `src` dir. To test the code in your local machine 
```bash
python src/main_test.py
```

### Warning !! This is an unfinished prototype project and it is in the start of the development stage so it is unreliable. 