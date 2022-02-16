from django.shortcuts import render, HttpResponse

from selenium import webdriver
import json
import time

# wd = webdriver.Chrome()
# wd.get("https://www.powerlanguage.co.uk/wordle/")
# localStorage=wd.execute_script("return window.localStorage;")
# x= json.loads(localStorage['gameState'])
# print(x['solution'])

def show(request):
    wd = webdriver.Chrome()
    wd.get("https://www.powerlanguage.co.uk/wordle/")
    localStorage=wd.execute_script("return window.localStorage;")
    wd.quit()
    main_dict= json.loads(localStorage['nyt-wordle-state'])
    x=main_dict['solution']
    return render(request,'result.html',{'ans':x})
    
