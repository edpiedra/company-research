from variables.variables import * 

class FinNLPDownloads():
    def __init__(self):
        print("[INFO] {:.2f}...initializing finnlp downloads module".format(
            time.time()-start_time
        ))
        
        self.start_date = None 
        self.start_date_long = None 
        self.end_date = None 
        self.ticker = None 
        
        self.basic_config = {
            "max_retry"     : 5,
            "proxy_pages"   : 5,
        }
        
        self.token_config = self.basic_config | {
            "token"     : PrivateData.finnhub_api_key
        }
        
    def _company_sticktwits(self):
        print("[INFO] {:.2f}...getting finnlp company stocktwits for {}".format(
            time.time()-start_time, self.ticker
        ))
        
        downloader = Stocktwits_Streaming(self.basic_config)
        downloader.download_streaming_stock(self.ticker)
        df = downloader.dataframe

        stocktwits = df.copy()

        stocktwits.to_csv(self.folder + "/stocktwits.csv")
        
    def get_company_info(self):
        self.folder = f'./downloads/{self.ticker}/finnlp'

        if not(os.path.exists(self.folder)):
            os.makedirs(self.folder)
            
        self._company_sticktwits()
        