from setuptools import setup, find_packages

version = '0.1.0'

setup(name='PyMarvel',
      version=version,
      description="Python wrapper for Marvel API",
      long_description=open("README.md", "r").read(),
      classifiers=[
          "Development Status :: 1 - Planning",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='marvel api comics python',
      author='Garrett Pennington',
      author_email='garrettp@gmail.com',
      url='http://github.com/gpennington/PyMarvel',
      license='MIT',
      packages=find_packages(),
      install_requires=['requests'],
      include_package_data=True,
      zip_safe=True,
      )