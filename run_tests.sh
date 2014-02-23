#!/bin/sh
coverage run --source=marvel/ -m unittest marvel.tests.PyMarvelTestCase
coverage html -d ./reports/coverage_html
coverage -r -m >./reports/coverage_report.txt