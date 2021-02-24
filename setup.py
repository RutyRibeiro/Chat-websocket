import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="keru-app", # Replace with your own username
    version="0.0.1",
    author="KeruEnterprise",
    author_email="kelvin.conego@hotmail.com",
    description="WebSocket Chat",
    long_description="Chat em WebSocket para testes",
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "",
    }
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)