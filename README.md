[Add project details here]

# Enviornment Setup 
## Environment variables
1. This project used `direnv` to manage API keys as environment variables. Follow installation instructions here https://direnv.net

2. If you are on a Mac, you will need to add the following config to your `~/.bash_profile`

    ```eval "$(direnv hook bash)"```

    After saving the file, run 
    
    ```source ~/.bash_profile```

3. Copy the contents of `.envrc.example` to a new file called `.envrc`. Copy your API keys into the file.

4. Set environment variables by running 

    ``` direnv allow``` 

## Install dependencies
Install dependencies by running the following command from the root directory 

 `pip install -r requirements.txt`


 # Documentation
 ## Twitter
 Query language: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query