from setuptools import find_packages, setup
from typing import List

hy_e = "-e ."
def get_requirements(file_path:str)->List[str]:
  with open(file_path) as file_obj:
    requirements = file_obj.readlines()
    requirements = [req.replace("\n","") for req in requirements]

    if hy_e in requirements:
      requirements.remove(hy_e)
  return requirements

setup(
name="mlproject1",
version="0.0.1",
author="Anmol",
author_email="ianmolyadav16@gmail.com",
packages=find_packages(),
requires=get_requirements("requirements.txt")
)