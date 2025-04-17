from setuptools import setup, find_packages

setup(
    name="lennar_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "flask",
        "pymongo"
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'run-part1 = part_one.main:main',  # Entry point for part 1
            'run-part2 = part_two.main:main',  # Entry point for part 2
            'run-part3 = part_two.main:main',  # Entry point for part 2
        ],
    },
)
