# Web Services and applications

#### A repository for learning web services and applications


![Computer Infrastructure](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Faspwv.com%2Fwp-content%2Fuploads%2F2019%2F11%2F1024WebService.jpg&f=1&nofb=1&ipt=0cc90b39487c94187bb222d300d44a2bb70ce8d1935ab372707a84336792ce64)


** by Roberto Gomez Garcia ** Email: G00438875@atu.ie



## Overview

The goal of this repository is to apply and demonstrate knowledge of web services and applications by building a web application using Python, AJAX, and SQL.

This project focuses on managing supplier information. It allows users to create, read, update, and delete (CRUD) supplier records through a web interface connected to a backend server and database. There are 7 different files each of them have their own function.

1)  Supplier DAO - Contains the code for connecting to the database and performing CRUD operations on supplier data.
2)  Rest Server - A Python-based server built with Flask that manages the connection between the database and the website, mapping data between them.
3)  Database configuration - Stores the settings needed to connect to the SQL database (added to .gitignore)
4)  Supplier interface(HTML, CSS for style) - The frontend part of the application that sends AJAX requests to the REST server and displays supplier data.
5)  Supplier DAO Skeleton- A simplified version of the DAO used for testing the REST API during development.
6)  SQL database creation script. 
6)  SQL table script - Instructions or script to create the supplier table in the database.


## Getting started

1)  Clone the repository:
Clone the repository to your local machine using the following command: git clone <repository-url>
More information on [Git_clone](https://git-scm.com/docs/git-clone)
2)  Run the code: check section running the project.

## Prerequisite 

Jupiter notebook and the code can be run in two different ways.

1.  Locally using  [Anaconda](https://www.anaconda.com/download) and [Visual_Studio](https://code.visualstudio.com/?wt.mc_id=vscom_downloads)
2.  Install a Windows web development environment like WampServer if you don’t already have one. It includes MySQL, which is needed to create and manage the database for this project.
3.  If not available, install flask and mysql.connector.
4.  Previous knowledge in python, SQL, AJAX and HTML recomended but not mandatory.

### Running the project locally

Follow the next steps to run the project locally.
1)	Set Up the Project Folder and place all project files in the same directory.
2)  Connect to SQL database and create table.
    - Ensure your SQL database server is running.
    - Update the database connection settings in dbconfig.py (host, user, password, database).
    - Run createdatabase.py to create the data base.
    - Run the createtable.py script to create the sql table.
5)  Launch the REST server(python restserversupplier.py). Use visual code terminal to navigate to the correct folder.
5)  In your browser, go to: http://127.0.0.1:5000/supplierinterface.html
6)  You can now create. Once the first supplier is added, user will be able to update and delete.

## Assistance

The base code for this project is derived from Andrew Beatty's WSAA Course Material 2024.
ChatGPT was used to enhance the style and design of the supplierinterface.html file. to get the enhancement I copy the base code and ask chatGPT to improve the style with a student level.

## Issues

The first part of the project (web server + mock DAO) was developed on my laptop. However, I encountered issues connecting to WAMPServer and MySQL, which prevented the project from functioning correctly. As a result, I switched to using the remote system provided by the university, where the connection worked as expected. Once the project was completed, I copied the files back to my laptop and uploaded them to GitHub.

## Getting Help
For any issue with this repository, please use the issues section of the repository. To create a new issue, follow these steps:

Go to the Issues section.
Click on New issue and provide a detailed description of the problem.
For more information on creating and managing issues, see the GitHub Issues documentation.[github_issues](https://docs.github.com/en/issues)

## Contributing

If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Please include a detail description. if any issue is encouter please feel free to open an issue.

---------------------------
**END**