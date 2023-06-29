# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:51:46 2023

@author: Jagrati Garg
"""

#import libraries
import pandas as pd
import dash
import dash_html_components as html
import webbrowser







#declare global variables
project_name=None
app=dash.Dash()



#define functions
def load_model():
    global scrappedReviews
    scrappedReviews=pd.read_csv("scrappedReviews.csv")
    
    
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")
    

def create_ui_app():
    main_layout=html.Div(
        [
            html.H1("users sentiments with insight"),
            html.H5("welcome")
            
            
            
            
            
            
            
            
            
            
            
            ]
        
        
        
        
        
        
        
        
        )
    return main_layout



#define main function
def main():
    global scrappedReviews
    global project_name
    print("start the project")
    load_model()
    project_name='sentiments analysis with insights'
    
    #print(project_name)
    #print(scrappedReviews.sample(5))
    open_browser()
    app.title=project_name
    app.layout=create_ui_app()
    app.run_server()
    print("end the project")
    project_name=None






#call the main function
if __name__=='__main__':
    main()