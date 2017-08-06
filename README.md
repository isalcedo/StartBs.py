# StartBs.py
# Tool to simplify the start of BrowserSync.io

This is a simple tool for lazy developers. This assume that you have installed BrowserSync in your system.
I do work with Joomla and Yii2 mostly.

*Example:*
If you are using Joomla:

        $ python startbs.py joomla local.example.com -tn template_name

BrowserSync will look for any .scss file inside the template_name/css folder, the same for .js inside template_name/js folder and the index.php file on template_name/index.php

If you are using Yii2:

        $ python startbs.py yii2-a local.example.com

  *yii2-a means Advanced Template.*

BrowserSync will look for any .scss file inside frontend/web/css folder, the same for .js inside frontend/web/js folder and any php file inside of frontend/views/*/*.php, same for backend (backend/web/css, backend/web/js, backend/views/*/*.php)

        $ python startbs.py yii2-b local.example.com

  *yii2-b means Basic Template.*

BrowserSync will look for any .scss file inside web/css folder, the same for .js inside web/js folder and any php file inside of views/*/*.php

Attributes:
    tool (string): The name of the tool: joomla, yii2-a or yii2-b
    domain (string): Local domain name of your application
    -tn (string, optional): Mandatory for joomla, the name of the template folder that you are building
