#Define the imports
import twitch
import keypresser
t = twitch.Twitch();
k = keypresser.Keypresser();

#Enter your twitch username and oauth-key below, and the app connects to twitch with the details.
#Your oauth-key can be generated at http://twitchapps.com/tmi/
username = "prabhjotbot";
key = "oauth:bnfb9s8ttairhiv4wabglb4lpoaius";
t.twitch_connect(username, key);

#The main loop
while True:
    #Check for new mesasages
    new_messages = t.twitch_recieve_messages();

    if not new_messages:
        #No new messages...
        continue
    else:
        for message in new_messages:
            #Wuhu we got a message. Let's extract some details from it
            msg = message['message'].lower()
            username = message['username'].lower()
            print(username + ": " + msg);

            #This is where you change the keys that shall be pressed and listened to.
            #The code below will simulate the key q if "q" is typed into twitch by someone
            #.. the same thing with "w"
            #Change this to make Twitch fit to your game!
            """ 
            if msg == "q": k.key_press("q");
            if msg == "w": k.key_press("w");
            if msg == "e": k.key_press("e");
            if msg == "r": k.key_press("r");
            if msg == "t": k.key_press("t");
            if msg == "y": k.key_press("y");
            if msg == "u": k.key_press("u");
            if msg == "i": k.key_press("i");
            if msg == "o": k.key_press("o");
            if msg == "p": k.key_press("p");
            if msg == "a": k.key_press("a");
            if msg == "s": k.key_press("s");
            if msg == "d": k.key_press("d");
            if msg == "f": k.key_press("f");
            if msg == "g": k.key_press("g");
            if msg == "h": k.key_press("h");
            if msg == "j": k.key_press("j");
            if msg == "k": k.key_press("k");
            if msg == "l": k.key_press("l");
            if msg == "z": k.key_press("z");
            if msg == "x": k.key_press("x");
            if msg == "c": k.key_press("c");
            if msg == "v": k.key_press("v");
            if msg == "b": k.key_press("b");
            if msg == "n": k.key_press("n");
            if msg == "m": k.key_press("m");
            if msg == "space": k.key_press("space");
            """
            
            
            
            