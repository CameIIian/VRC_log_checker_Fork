###### English | [日本語](./README-ja.md)
# Introduction 
This python script can export world and user name from VRChat log file.

# Getting Started
1. Prepare Python 3.7.X or later and set environment variables.<br/>
Python Official: https://www.python.org/downloads/ <br/>
Microsoft Store: https://apps.microsoft.com/detail/9ncvdn91xzqp

2. Find VRChat log file available at:<br/>
 C:/Users/"${username}"/AppData/LocalLow/VRChat/VRChat/output\_log_yyyy-mm-dd_hh-mm-ss.txt

3. Copy it to the script file.<br/>

4. Open terminal in the script file and run python program as follows:<br/>
```
python vrc_world_user_checker.py log_yyyy-mm-dd_hh-mm-ss.txt
```

5. See VRChat\_usrlog.txt at the same directory of the log file.<br/>

# Output example
```
2025.03.28 17:26:24 World: Camellian's World
2025.03.28 17:26:42  User: Camellian
...
```

# License

These codes are licensed under CC0 based on the forked source.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

