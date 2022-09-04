[![aa-ag](https://circleci.com/gh/aa-ag/csvs.svg?style=shield)](https://circleci.com/gh/aa-ag/csvs)

[![aa-ag](https://dl.circleci.com/insights-snapshot/gh/aa-ag/csvs/main/workflow/badge.svg?window=30d)](https://app.circleci.com/insights/github/aa-ag/csvs?branches=main&workflows=workflowy&reporting-window=last-30-days&insights-snapshot=true)


## CSVs

This project started as a repo to practice handling CSV files, and turned into an app to analyse CSV files.

# Checks

`Checks` is a Single-Page Application to let users upload CSV files and check (a) their encoding, (b) their metadata, and (c) generate a sample file with 25 random rows + their original headers.

### Stack

`Check`'s backend is Django, Python.

And it's frontend is set up with Bootstrap & Jinja.

Deployed to AWS using Docker.


#### Docker

`sudo docker-compose build`
`sudo docker-compose up `