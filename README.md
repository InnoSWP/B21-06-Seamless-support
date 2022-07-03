Seamless Support System
=======================
This is an implementation of a support service on Python, Django and React that can be easily integrated to different platforms. The service provides fast and efficient communication between user and volunteers in case of any questions. It is mainly based on implicitly connected telegram bot to the web page.

The repository includes:
Linter
Django App folder with front-end (React) and back-end part (Python)
Config file with constant data

The code is documented and designed to be easy to extend. If you use it in your research, please consider citing this repository (bibtex below). 

Functionality 
-------------
Users can refer to our integrated platform if they have some questions. The process is the following: user enters the QA field and in case of noticing the necessary question among the most frequently asked ones just click on it and get a fast answer. In another case, the user just types his/her question in a specific window and gets redirected to a dialog page, where can see all the answers below the questions. From the inner side, the process is more detailed and consists of resending the user’s question from the server to the common telegram chat with all the volunteers. There they can accept or reject the question, after this there forms a chat in telegram with a specific volunteer and a user. In the chat volunteer types the answer, pushes the “send” button and the message gets redirected back to the service and published on the page. 

![](IMG_2756.gif)

Installation
-------------
Install Node.js
```bash
npm install
```

*Optional:*
This is optional, because it is only needed for the front-end part to work, but you can write the front-end yourself
In order to run the code on your device, go to the front-end folder and write the following in the terminal: 
```bash
npm run build
```

Integration
-----------
Our project is divided into parts, each of which is very easy to integrate into the system. The platform consists of a front-end part, two telegram bots and a data base.<br>
<br>
**Front end part:**
You can use our front-end part or attach your own to the platform.<br>
<br>
**Back end part:**
To integrate bots, you just need to register your bot token. These parameters are configured in the config.by file.<br>
<br>
**Database:**
For adding a database, you need to create a new class that will be inherited from abstract one in CloudDatabase.py. It is also important to understand that the structure of your database should be as follows (sheets and field attributes should match those listed below).<br>
*Optional:* If you want to use GoogleSheets for this, please follow the instruction from https://docs.gspread.org/en/latest/oauth2.html and change the database name in config.py.

<img src = "screenshot1.png" width="900"/> 
<img src = "screenshot2.png" width=900"/>
<img src = "screenshot3.png" width="900"/> 
<img src = "screenshot4.png" width="900"/>
<img src = "screenshot5.png" width="500"/>

Additional information
-----------------------
**Linter:**
[![Build](https://github.com/InnoSWP/05-DocPdf-Converter/actions/workflows/build.yml/badge.svg)](https://github.com/InnoSWP/B21-06-Seamless-support/actions/workflows/build.yml)


Licence
---------
MIT License

Copyright (c) 2022 Gleb Kirillov, Leonid Zelensky, Dilyara Farkhutdinova, Ali Mahmoud Mansour, Ernest Matskevich 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



