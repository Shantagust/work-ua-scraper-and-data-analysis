# work-ua-scraper-and-data-analysis
This project create for parsing required skills for python developer

## Project description:
This project was created for analyze 


## How to copy project from git and create virtual environment

```
git clone https://github.com/Shantagust/work-ua-scraper-and-data-analysis.git
cd work-ua-scraper-and-data-analysis
py -m venv venv
.\venv\Script\Active
pip install -r requirements.txt
```

## Run Work.ua parsing
run in console `scrape crawl skills -O skills.csv`

## Get skills ranks
You can see ranks [here](data_analyze/analyze_staticstics.ipynb)

### Requirements: 
- numpy==1.26.4
- pandas==2.2.2
- Scrapy==2.11.1
- matplotlib==3.8.4
- jupyter==1.0.0