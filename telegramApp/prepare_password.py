import keyring as kr

with open('bot-api.txt') as f:
    contents = f.read()
    kr.set_password("AlphonsesBar", #serviceName 
                "Alphonse",  	    #username
                contents) 	    #password