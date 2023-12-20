Using a package manager
You can install the crawler as a package: Using pip:

pip install example_data_crawler
Or using poetry:

poetry add example_data_crawler
Cloning the repository
You can also clone the repository and install the dependencies. Using poetry:

git clone https://github.com/Foxicution/data_crawler_examples
cd data_crawler_examples
poetry install
Afterwards you can checkout and run some example scripts, e.g.:


Usage
As a module
from example_data_crawler import crawl

print(crawl("gintarine", "df", query="vaikams" )
For more examples look in the examples directory.

Structure
The project is structured as follows:

example_data_crawler/: Main package directory.
__init__.py: Package initialization file.
crawler/: Directory containing individual crawler scripts.
__init__.py: Initialization file for crawlers module.
gintarine.py: Crawler for the gintarine website.
__init__.py: Initialization file for tests.
License
This project is licensed under the MIT license.