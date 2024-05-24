from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """function for return a list of requirements

    Args:
        file_path (str):

    Returns:
        List[str]: list of requirements
    """
    with open(file_path, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name="end-to-end-ml-project",
    version="0.0.1",
    author="tinapyp",
    author_email="fathinafiff@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
