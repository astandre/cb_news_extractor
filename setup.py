import sys
from setuptools import setup, find_packages
from cb_news.news_extractor import __version__

setup(name='news_extractor',
      description="",
      long_description=open('README.rst').read(),
      version=__version__,
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      dependency_links=["https://github.com/Runnerly/flakon.git#egg=flakon"],
      install_requires=["flask"],
      author="André Herrera",
      author_ewmail="andreherrera97@hotmail.com",
      license="MIT",
      keywords=["microservices"],
      entry_points={
          'console_scripts': [
              'news_extractor = cb_news.news_extractor.run:app',
          ],
      }
      )
