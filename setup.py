from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function returns a cleaned list of requirements
    from requirements.txt (skips duplicates, empty lines, and -e .)
    """
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)

        # Remove duplicates while preserving order
        requirement_lst = list(dict.fromkeys(requirement_lst))

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Dishant Vekariya",
    author_email="Dishantpatel927@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
