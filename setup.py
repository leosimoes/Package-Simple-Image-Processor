from setuptools import setup, find_packages

with open("DESCRIPTION.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simple_image_processor",
    version="0.0.1",
    author="Leonardo Simões",
    author_email="leosimoes",
    description="Simple Image Processor",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leosimoes/Package-Simple-Image-Processor",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)