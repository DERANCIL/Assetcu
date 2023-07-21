#!/bin/bash


printf "${BOLD}${YELLOW}##########################################################\n"
printf "##### Welcome to the  installer #####\n"
printf "##########################################################\n\n${NORMAL}"

sudo apt-get -y update

printf "${BOLD}${MAGENTA}Installing programming languages\n${NORMAL}"
 
printf "${CYAN}Installing Python\n${NORMAL}"
sudo apt-get install -y python3-pip
sudo apt-get install -y python-pip
sudo apt-get install -y dnspython


printf "${CYAN}Installing GO\n\n${NORMAL}"
sudo apt install -y golang
export GOROOT=/usr/lib/go
export GOPATH=~/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH

echo "export GOROOT=/usr/lib/go" >> ~/.bashrc
echo "export GOPATH=~/go" >> ~/.bashrc
echo "export PATH=$GOPATH/bin:$GOROOT/bin:$PATH" >> ~/.bashrc

source ~/.bashrc


printf "${CYAN}Cloning TheHarvester\n${NORMAL}"
git clone https://github.com/laramies/theHarvester.git
cd theHarvester
pip3 install -r requirements.txt
cd ..








printf "${CYAN}Installing Amass\n${NORMAL}"
apt install amass -y


printf "${CYAN}Installing Subfinder\n${NORMAL}"
GO111MODULE=on go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
sudo cp ~/go/bin/subfinder /usr/local/bin 

printf "${CYAN}Installing Naabu\n${NORMAL}"
git clone https://github.com/projectdiscovery/naabu.git
cd naabu/v2/cmd/naabu
go build
cp naabu /usr/local/bin/

printf "${CYAN}Installing dnsx\n${NORMAL}"
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest


printf "${CYAN}Installing httpx\n${NORMAL}"
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
