# mflix

This is a short guide on setting up the system and environment
dependencies required for the MFlix application to run.

**Disclaimer:** The dependencies and versions in this project are not
maintained. This project is intended for educational purposes and is
**not** intended to be exposed in a network, so use at your own
discretion.

## Project Structure

Everything you will implement is located in the `mflix/db.py` file,
which contains all database interfacing methods. The API will make calls
to `db.py` to interact with MongoDB.

The unit tests in `tests` will test these database access methods
directly, without going through the API. The UI will run these methods
in integration tests, and therefore requires the full application to be
running.

The API layer is fully implemented, as is the UI. If you need to run on
a port other than 5000, you can edit the `index.html` file in the build
directory to modify the value of **window.host**.

Please do not modify the API layer in any way, `movies.py` and `user.py`
under the **mflix/api** directory. Doing so will most likely result in
the frontend application failing to validate some of the labs.

## Local Development Environment Configuration

### Anaconda

We\'re going to use [Anaconda] to install Python 3 and to manage our
Python 3 environment.

**Installing Anaconda for Mac**

You can download Anaconda from their [MacOS download site]. The
installer will give you the option to \"Change Install Location\", so
you can choose the path where the `anaconda3` folder will be placed.
Remember this location, because you will need it to activate the
environment.

Once installed, you will have to create and activate a `conda`
environment:

``` sh
# navigate to the mflix-python directory
cd mflix-python

# enable the "conda" command in Terminal
echo ". /anaconda3/etc/profile.d/conda.sh" >> ~/.bash_profile
source ~/.bash_profile

# create a new environment for MFlix
conda create --name mflix

# activate the environment
conda activate mflix
```

You can deactivate the environment with the following command:

``` sh
conda deactivate
```

**Installing Anaconda for Windows**

You can download Anaconda from their [Download site]. Please be careful
to select `Windows Tab` before downloading.

The Anaconda installer will prompt you to *Add Anaconda to your PATH*.
Select this option to use `conda` commands from the Command Prompt.

If you forget to select this option before installing, no worries. The
installer will let you choose an \"Install Location\" for Anaconda,
which is the directory where the `Anaconda3` folder will be placed.

Using your machine\'s location of `Anaconda3` as `<path-to-Anaconda3>`,
run the following commands to activate `conda` commands from the Comman

  [Anaconda]: https://anaconda.org/
  [MacOS download site]: https://www.anaconda.com/download/#macos
  [Download site]: https://www.anaconda.com/download/