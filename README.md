SENTIMENT ANALYSIS:
- finnhub news: summary
- finnlp news: summary
- finnlp stocktwits: sentiment


QUANTITATIVE:
- earnings surprises: surpricePercent
- insider sentiment: mspr
- recommendation trends: net recommendation percent of total


copy finnlp folder downloaded from https://github.com/AI4Finance-Foundation/FinNLP/tree/main into the workspace folder.

REQUIREMENTS:

pip install:
- finnhub-python
- yfinance
- parsel
- tqdm
- furl
- selenium
- textblob
- nltk
- spacy
- scikit-learn
- transformers==4.30.0
- peft
- accelerate
- bitsandbytes
- pandas
- scipy
- sentencepiece
- protobuf==3.20.0

python -m spacy download en_core_web_lg