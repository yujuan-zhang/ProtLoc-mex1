from setuptools import setup, find_packages

setup(
    name='protloc_mex1',
    version_format='{tag}',
    author='Ze Yu Luo',
    author_email='1024226968@qq.com',
    description='...',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.9',
    install_requires=[
        'biopython',
        'numpy',
        'pandas',
        'scikit-learn',
        'seaborn',
        'matplotlib',
        'shap'
    ],
    # generate source distribution package
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    zip_safe=False,
    # generate binary distribution package
    entry_points={
        'console_scripts': [
            'protloc_mex1 = protloc_mex1.cli:main',
        ],
    },
)

