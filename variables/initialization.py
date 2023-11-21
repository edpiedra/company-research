import time 
start_time = time.time()

#CHECK FOR REQUIRED DIRECTORIES
import os 

folder = "./downloads"

if not(os.path.exists(folder)):
    os.makedirs(folder)

print("[INFO] {:.2f}...loading libraries".format(
    time.time()-start_time
))

import json, requests  
import datetime as dt 
import pandas as pd 

import finnhub 

from finnlp.data_sources.news.finnhub_date_range import Finnhub_Date_Range 
from finnlp.data_sources.social_media.stocktwits_streaming import Stocktwits_Streaming

#import pandas_datareader.data as web 
import yfinance as yf 


#FOR SEEKING ALPHA MODULE
import re
#from pathlib import Path
#from random import random
#from time import sleep
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from furl import furl
from selenium import webdriver

import textblob 

import string 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from nltk.corpus import wordnet, stopwords 
from nltk import pos_tag 
from nltk.stem import WordNetLemmatizer 

import spacy 
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np 

import sys 

os.environ["TRANSFORMERS_CACHE"] = "u:/huggingface/cache/"

from transformers import AutoModel, AutoTokenizer 
from peft import PeftModel
import torch 
