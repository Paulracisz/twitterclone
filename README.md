Twitterclone is a copy of twitter using Django technologies to implement some of the functionality of Twitter. It has authentication, server side rendering of components, the ability to make an account, login, make a tweet, follow other accounts, and has a dynamic feed organized chronologically, and filtered by whom the user follows.

<h2> Dependencies required for this project </h2>
<ul>
  <li>Python 3.8.2</li>
  <li>Poetry</li>
  <li>Linux-based or Mac operating system</li>
  <li>Bash or Zsh shell</li>
  </ul>

<h2> Installation </h2>
<ul>
<p><li>If you're running Windows 10, <a href="https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/">here</a> is a tutorial on how to get a bash terminal running on Windows.</li><p/>
<p><li><a href="https://www.geeksforgeeks.org/how-to-download-and-install-python-latest-version-on-linux/">Here</a> is a guide on how to install the latest version of Python on Linux, and <a href="https://blog.adafruit.com/2020/05/29/installing-the-latest-version-of-python-on-mac-os-catalina-python-mac-apple-catalina-letsbsocial1/">click here</a> for Mac.
  </li>
</p>
  <p><li><a href="https://pypi.org/project/poetry/">How to install Poetry with pip package manager.</a></li></p>
  </ul>
  <p> Now that everything is set up, you can move onto running this project on your machine</p>
  
  <h2> Set-Up </h2>
  
  <ol>
  <li> Fork and clone the repo.</li>
  <li> cd into your new directory, and run the command <code>poetry install</code>. This is going to install all of the dependecies required for the project.</li>
  <li> now run <code>poetry shell</code>. This will create a virtual enviornment for your terminal. From here you can run commands off of a file called manage.py. This file holds all of the information for things such as running a server. </li>
  <li> you can run the command <code> python manage.py runserver</code> to run the server. (Note that this particular project does not display anything on a webpage so it would display a blank webpage.) If you want to look at the relational data structure, do <code>code .</code> in the root folder to open it up in VS Code and you can view the data structure.

# README created by Paul Racisz.
