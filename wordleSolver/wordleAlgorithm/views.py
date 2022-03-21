from django.shortcuts import render, HttpResponse

from selenium import webdriver
import json
import os

def show(request):
    crm_options=webdriver.ChromeOptions()
    crm_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    crm_options.add_argument("--headless")
    crm_options.add_argument("--disable-dev-shm-usage")
    crm_options.add_argument("--no-sandbox")
    wd = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=crm_options)
    wd.get("https://www.powerlanguage.co.uk/wordle/")
    localStorage=wd.execute_script("return window.localStorage;")
    wd.quit()
    main_dict= json.loads(localStorage['nyt-wordle-state'])
    x=main_dict['solution']
    return render(request,'result.html',{'ans':x})
    
