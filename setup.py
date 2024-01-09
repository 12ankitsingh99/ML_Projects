from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(filepath:str)->list[str]:
    '''This function will return the list of requirements from the requirements.txt file'''
    requirements=[]
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements


setup(
    name='ML_Projects',
    version='0.0.1',
    description='END TO END MACHINE LEARNING PROJECT IMPLEMENTATIONS',
    author='ANKIT SINGH',
    author_email='12ankitsingh99@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)