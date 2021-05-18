 <h2 align="center">Be-Secure</h2>
   
<p> <center> <h4 align="center"> An Powerfull secure environment provider for your works </h4> </p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#BeSman">About The Project</a>
      <ul>
        <li><a href="#Mission">Mission</a></li>
      </ul>
    </li>
    <li>
      <a href="#Command-Line-Interface">Command Line Interface</a>
    </li>
    <li><a href="#Installation-and-commands">Installation and commands</a></li>
	       <ul>
        <li><a href="#Install-commands">Install commands</a></li>
	<li><a href="#Uninstall-commands">Uninstall commands</a></li>
        <li><a href="#Version commands">Version commands</a></li>
       <li><a href="#Other useful commands">Other useful commands</a></li>	       
      </ul>
    <li><a href="#Prerequisite">Prerequisite</a></li>
    <li><a href="#Partners">Partners</a></li>
    <li><a href="#Contribution">Contribution</a></li>
    <li><a href="#Acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT  -->
# BeSman 

BeSman or Be-Secure  Manager is an umbrella of open source security projects and utilities tracked by Wipro’s open source security team and its open source partner network. The trusted open source security projects can used to create open source security testing environments and open source enterprise security platforms.


## Mission 
Establish a collaborative decentralized network of open source security organizations and service providers to create trusted , interoperable and secure open source security tools.

<!-- GETTING STARTED -->
# Command Line Interface
BeSman, (Be-Secure manager) gives you a *bes* command on your shell , you can use it to automate the setup of various development environments required for bes projects  
BeSman is a tool for providing secure environments for user. It provides a convenient command line interface for installing, removing and listing Environments.


# Prerequisite

Please use OAH commands to create Bes installed virtual machine. For moreinformation use below link.
https://github.com/jobyko/oah-installer

# Installation and commands 

1. Windows [In Gitbash] [bes with new vm]
    #####    i.   git clone https://github.com/jobyko/oah-installer
    #####    ii.  cd oah-installer && ./install.sh
    #####    iii. oah install -v oah-bes-vm 
    #####    iv.  Use VM which got created while instaling oah-bes-vm to work with bes commands. 

3. Linux  [Terminal] [bes with new vm]
Open your favourite terminal and enter the following

    #####   i.   curl -s https://raw.githubusercontent.com/openapphack/oah-installer/install.sh | bash
    #####   ii.  oah install -v oah-bes-vm
    #####   iii. Use created vm to work with bes commands
   

### Local Installation

To install BeSman locally running against your local server, run the following commands:


	$ source ~/.besman/bin/besman-init.sh


### Local environment commands

Run the following commands on the terminal to manage respective environments.

### Install commands:

        $ bes install -env [environment_name] -V [version_tag]

        Example   :
           $ bes install -env bes_dev_ansible -V 0.0.1

Please run the following command to get the list of other environments and its versions.

	   	`$ bes list`



### Uninstall commands:

        $ bes uninstall -env [environment_name] -V [version]

        Example   :
           $ bes uninstall -env  bes_dev_ansible -V 0.0.1


### Version commands:

    $ bes --version
    $ bes --version -env [environment_name]

 
____________________

### Other useful commands:        

        $ bes list
        $ bes status        
        $ bes help     

<!-- PARTNERS -->
## Partners    

 1. Indian Institute of Technology (Bombay)
 2. Wipro


<!-- CONTRIBUTING -->
## Contribution

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements  
