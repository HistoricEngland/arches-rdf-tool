# Arches RDF Tool

This script allows you to convert an Arches resource to an RDF format. It is very simple and does not log in so you can only access what is publically available.

## Installation

> Requires python 3.7+ (it has only been tested on 3.7). 

1. Clone the repo to your machine
1. Create a virtual environment to host the script packages. This can be done insde the repo but only if you use the name `env` as this is set in the .gitignore file.
   ```cmd
   > python -m venv env
   ```
1. Activate the virtual environment using `path\to\env\Scripts\activate`
1. Then install the required packages
   ```
   > pip install -r path\to\requirements.txt
   ```

## Usage

The script requires the following **ordered** arguments

1. Arches hostname
1. a comma seperated UUID of the resource
1. an output directory path

example with the current working directory in the repo
```
> python convert-arches.py https://www.example-arches.com 13c335be-abcd-1234-5678-177803a4ef82 C:\path\to\ouput\directory

> python convert-arches.py https://www.example-arches.com 00000171-a306-48c5-9cd0-cbe5d08a995b,00000230-0a58-4917-a88e-69bdbd8f68c9 C:\path\to\ouput\directory
```
