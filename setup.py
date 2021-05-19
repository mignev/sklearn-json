import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='th-sklearn-json',
     version='0.1.0',
     author="Marian Ignev",
     author_email="dev@teachablehub.com",
     description="A safe, transparent way to share and deploy scikit-learn models. Original by Mathieu Rodrigue",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mignev/sklearn-json",
     packages=setuptools.find_packages(),
     install_requires=[
          'scikit-learn>=0.21.3',
      ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3.5',
 )
