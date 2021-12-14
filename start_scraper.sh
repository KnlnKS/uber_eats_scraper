#!/bin/bash

# Exit if any command fails
set -e

country=""

function usage() {
    echo "Scrape Uber Eats"
    echo "Usage:  ./start_scraper [options]"
    echo ""
    echo "Options:"
    echo "  --help                       Show help"
    echo "  --country                    Scrape for a specific country"
    echo ""
}

while [[ "${1}" != "" ]]; do
    param=$(echo "${1}" | awk -F= '{print $1}')
    value=$(echo "${1}" | awk -F= '{print $2}')
    case ${param} in
    --help)
        usage
        exit
        ;;
    --country)
        country="${value}"
        ;;
    *)
        echo "ERROR: unknown parameter \"${param}\""
        usage
        exit 1
        ;;
    esac
    shift
done

if [[ -z ${country} ]]
then
  echo "ERROR: country must be set."
  usage
  exit 1
fi

rm -rf output
scrapy crawl regions -o output/regions.json -a country="${country}"
scrapy crawl categories -o output/categories.json
python scripts/remove_dupe_categories.py
yarn --cwd api_scraper/ start
