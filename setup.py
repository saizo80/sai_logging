import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="sai_logging",
    version="0.2.0",
    author="saizo",
    author_email="saizo@simplemail.is",
    description="personal logger used for cronjobs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.saizo.gay/saizo/sai_logging",
    packages=setuptools.find_packages(),
)
