import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    raise RuntimeError("AioFizzBuzz requires the latest and greatest version of python (3.6)"
                       " with support for pep 492, pep 525 and pep 530")

version = __import__("aiofizzbuzz").__version__


setup(name="aiofizzbuzz",
      version=version,
      description="Asynchronous fizzbuzz.",
      long_description="An implementation of the classic whiteboard problem「𝑭𝒊𝒛𝒛𝑩𝒖𝒛𝒛」",
      url="https://github.com/nitros12/aiofizzbuzz",
      author="Ben Simms",
      author_email="ben@bensimms.moe",
      license="BSD",
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Framework :: AsyncIO",
          "Intended Audience :: Religion",
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python :: 3.6"
      ],
      keywords="Fizz Buzz FizzBuzz",
      packages=find_packages(exclude=["tests"]))
