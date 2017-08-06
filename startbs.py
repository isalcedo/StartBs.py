#!/usr/bin/python

"""Tool to simplify the start of BrowserSync.io

This is a simple tool for lazy developers. This assume that you have installed BrowserSync in your system.
I do work with Joomla and Yii2 mostly.

Example:
    If you are using Joomla:

        $ python startbs.py joomla local.example.com -tn template_name

    BrowserSync will look for any .scss file inside the template_name/css folder, the same for .js inside template_name/js
    folder and the index.php file on template_name/index.php

    If you are using Yii2:

        $ python startbs.py yii2-a local.example.com

    yii2-a means Advanced Template.

    BrowserSync will look for any .scss file inside frontend/web/css folder, the same for .js inside frontend/web/js folder
    and any php file inside of frontend/views/*/*.php, same for backend (backend/web/css, backend/web/js, backend/views/*/*.php)

        $ python startbs.py yii2-b local.example.com

    yii2-b means Basic Template.

    BrowserSync will look for any .scss file inside web/css folder, the same for .js inside web/js folder and any php file inside
    of views/*/*.php

Attributes:
    tool (string): The name of the tool: joomla, yii2-a or yii2-b
    domain (string): Local domain name of your application
    -tn (string, optional): Mandatory for joomla, the name of the template folder that you are building

Dev:     Ignacio Salcedo
WebSite: https://isalcedo.com
Email:   ignacio@isalcedo.com

"""

# Imports.
import sys
import os
import argparse

def start_bs(tool, domain, template_name = False) :
    if tool == 'joomla':
        os.system('browser-sync start --proxy "'+domain+'" --files "templates/'+template_name+'/css/*.scss" "templates/'+template_name+'/js/*.js" "templates/'+template_name+'/index.php"')
        pass
    if tool == 'yii2-a':
        os.system('browser-sync start --proxy "'+domain+'" --files "frontend/web/css/*.scss" "frontend/web/js/*.js" "frontend/views/*/*.php" "backend/web/css/*.scss" "backend/web/js/*.js" "backend/views/*/*.php"')
        pass
    if tool == 'yii2-b':
        os.system('browser-sync start --proxy "'+domain+'" --files "web/css/*.scss" "web/js/*.js" "views/*/*.php"')
        pass

# Dealing with arguments.
parser = argparse.ArgumentParser(description='Start BrowserSync for Joomla 3 site development, or Advanced Yii2 Development')
parser.add_argument('tool', action='store',  help='Define the tool (joomla, yii2-b or yii2-a)')
parser.add_argument('domain', action='store',  help='Define the local domain')
parser.add_argument('-tn', action='store',  help='(optional) For Joomla, the name of the template folder')
arguments = parser.parse_args()

# Main Script
if arguments.tool == 'joomla':
    if arguments.tn :
        start_bs(arguments.tool, arguments.domain, arguments.tn)
    else:
        parser.error("If tool is Joomla, the template name is required: startbs.py [-h] tool domain -tn template_name")
else:
    start_bs(arguments.tool, arguments.domain)