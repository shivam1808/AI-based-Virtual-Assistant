import requests
from output_module import output
from internet import check_internet_connection   
  
def get_news(): 
    
    if check_internet_connection():
        # BBC news api 
        main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=1bf3cdcaf711482589457e06c9936aef"
      
        # fetching data in json format 
        open_bbc_page = requests.get(main_url).json() 
      
        # getting all articles in a string article 
        article = open_bbc_page["articles"] 
      
        # empty list which will  
        # contain all trending news 
        results = [] 
          
        for ar in article: 
            results.append(ar["title"]) 
              
        for i in range(len(results)): 
              
            # printing all trending news 
            print(str(i + 1) + " " + results[i])    

        return "So these were the top news from today"
    else:
        return "Please Check your internet connection"             
