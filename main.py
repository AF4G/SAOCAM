#Define the imports
import twitch
import keypresser
t = twitch.Twitch();
k = keypresser.Keypresser();

#Twitch username and key
username = "prabhjotbot";
key = "oauth:bnfb9s8ttairhiv4wabglb4lpoaius";
t.twitch_connect(username, key);

while True:
    #Check for new messages
    new_messages = t.twitch_recieve_messages();

    if not new_messages:
        #No new messages
        continue
    else:
        for message in new_messages:
            #display message info
            msg = message['message'].lower()
            username = message['username'].lower()
            print(username + ": " + msg);

            
            #input from chat bar 
        
            k.key_press(msg)
            
            #check twitch messages for the following characters
            
            """
            if msg == "q": k.key_press("q");
            if msg == "w": k.key_press("w");
            

            if msg == "i": k.key_press("i");
            if msg == "o": k.key_press("o");
     
            if msg == "a": k.key_press("a");
            if msg == "s": k.key_press("s");
       
            if msg == "k": k.key_press("k");
            if msg == "l": k.key_press("l");
       
            
            """
            
            
            
            
            
            
            