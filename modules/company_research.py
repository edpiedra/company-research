from modules.submodules.finnhub_data import * 
from modules.submodules.finnlp_data import * 
from modules.submodules.yahoo_data import * 
from modules.submodules.seekingalpha_data import * 
from modules.submodules.data_analysis import * 

class CompanyResearch():
    def __init__(self):
        print("[INFO] {:.2f}...initializing company research module".format(
            time.time()-start_time
        ))
        
        self.ticker = None 
        self.start_date = None 
        self.start_date_long = None 
        self.end_date = None 
        
        self.finnhub_downloads = FinnHubDownloads()
        self.finnlp_downloads = FinNLPDownloads()
        self.yahoo_downloads = YahooDownloads()
        self.seekingalpha_downloads = SeekingAlphaDownloads()
        self.data_analysis = DataAnalysis()
        
        
    def run(self):
        print("[INFO] {:.2f}...running company research module".format(
            time.time()-start_time
        ))
        
        self.ticker = "AAPL"
        self.start_date = "2023-01-01"
        self.start_date_long = "2018-01-01"
        self.end_date = "2023-03-31"
        
        folder = f'./downloads/{self.ticker}'

        if not(os.path.exists(folder)):
            os.makedirs(folder)

        
        self.finnhub_downloads.ticker           = self.ticker 
        self.finnhub_downloads.start_date       = self.start_date 
        self.finnhub_downloads.start_date_long  = self.start_date_long 
        self.finnhub_downloads.end_date         = self.end_date
        
        #self.finnhub_downloads.get_company_info()
        
        self.finnlp_downloads.ticker = self.ticker 
        self.finnlp_downloads.start_date = self.start_date 
        self.finnlp_downloads.start_date_long = self.start_date_long 
        self.finnlp_downloads.end_date = self.end_date 
        
        #self.finnlp_downloads.get_company_info()
        
        self.yahoo_downloads.start_date = self.start_date
        self.yahoo_downloads.start_date_long = self.start_date_long 
        self.yahoo_downloads.end_date = self.end_date 
        self.yahoo_downloads.ticker = self.ticker 
        
        #self.yahoo_downloads.get_company_info()
        
        self.seekingalpha_downloads.ticker = self.ticker
        self.seekingalpha_downloads.start_date_long = self.start_date_long
        self.seekingalpha_downloads.end_date = self.end_date
        
        #self.seekingalpha_downloads.get_company_info()
        
        self.data_analysis.ticker = self.ticker 
        
        self.data_analysis.data_analysis()
        