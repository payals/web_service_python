RESTful Web Service 
===================

RESTful web service example in python.

Dependencies
---

* Python 2.7 or higher
* web.py module
  * `sudo pip install web.py`
* Apache Tomcat
  * `sudo apt-get install apache2`

Start service
---

Use the following command to start service on default port 8080: 
`python fibonacci_service.py`

Usage
---

The following URL will take you to the homepage:
`localhost:8080/`

To input the length of the series to be generated, say n, the URL will be:
`localhost:8080/fibonacci/n`


Testing
---

Tests can be run with the following command:
`sh ./run_tests.sh`
