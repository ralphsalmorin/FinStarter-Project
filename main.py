from Website import create_app

app = create_app()

#only if main.py run, it will run the web server
if __name__ == '__main__': 
    app.run(debug=True) #Debug = true meaning it will automaticall rerun if i make changes to the code
                        #can turn this off in production. 