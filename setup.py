import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kafka_splunk_connector-sathishsathi500@gmail.com",
    version="0.0.1",
    author="Sathish",
    author_email="sathishsathi500@gmail.com",
    description="Library that connects the kafka topic to splunk",
    long_description=long_description,
    install_requires=[
	'kafka-python',
	'requests',
	'logging',
	'splunk_hec_handler'
    ]
    long_description_content_type="text/markdown",
    url="https://github.com/Sathishsathi/kafka_splunk_connector",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
)
