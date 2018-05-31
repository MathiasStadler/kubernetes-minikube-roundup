# -*- mode: ruby -*-
# vi: set ft=ruby :

# from here https://github.com/fdemmer/vagrant-stretch64-docker/blob/master/Vagrantfile

plugins = ["vagrant-disksize",
"vagrant-vbguest",
"vagrant-scp",
"vagrant-proxyconf"]
puts plugins.length

# Install vagrant plugin
#
# @param: plugin type: Array[String] desc: The desired plugin to install
def ensure_plugins(plugins)
    logger = Vagrant::UI::Colored.new
    logger.info("Start Installing plugin #{plugins}")
    result = false
    plugins.each do |p|
      pm = Vagrant::Plugin::Manager.new(
        Vagrant::Plugin::Manager.user_plugins_file
      )
      plugin_hash = pm.installed_plugins
      next if plugin_hash.has_key?(p)
      result = true
      logger.warn("Installing plugin #{p}")
      pm.install_plugin(p)
    end
    if result
      logger.warn('Re-run vagrant up now that plugins are installed')
      exit
    else
      logger.info('Not additional plugins installed')
    end
    logger.info("Finish Installing plugin #{plugins}")
  end


ensure_plugins(plugins)


DOCKER_VERSION = "17.09.0~ce-0~debian"
COMPOSE_VERSION = "1.16.1"

$script = <<SCRIPT

export DEBIAN_FRONTEND=noninteractive

apt-get update && apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common \
    vim

echo "Installing docker via apt repo..."
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo apt-key add -
apt-key fingerprint 0EBFCD88

add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
    $(lsb_release -cs) \
    stable"

apt-get update && apt-get install -y --no-install-recommends \
    docker-ce=#{DOCKER_VERSION}

echo "Installing docker-compose from source..."
curl -fsSL https://github.com/docker/compose/releases/download/#{COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

echo "Adding vagrant user to docker and adm groups..."
groupadd docker &> /dev/null
usermod -aG docker vagrant
usermod -aG adm vagrant

echo "Writing docker aliases..."
cat > /etc/profile.d/00-aliases.sh <<EOF
alias d="docker"
alias dc="docker-compose"
EOF

echo "Install kernel check-config script"
wget https://github.com/docker/docker/raw/master/contrib/check-config.sh
chmod +x check-config.sh

echo "Enojy! :)"

SCRIPT

require "open3"
#set internet device name to the world
worldwideinterfaces=%x(ip route get  $(dig +short google.com | tail -1) | grep $(dig +short google.com | tail -1)| awk '{print $5}').chomp
ENV["LC_ALL"] = "en_US.UTF-8"
Vagrant.require_version ">= 1.8"
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
# network
    # What box should we base this build on?
    config.vm.box = "debian/contrib-stretch64"
    config.disksize.size = '20GB'
    # Add 2nd network adapter
    config.vm.network "public_network", type:"dhcp" ,bridge: "#{worldwideinterfaces}"
    config.ssh.insert_key = false
    #######################################################################
    # THIS REQUIRES YOU TO INSTALL A PLUGIN. RUN THE COMMAND BELOW...
    #
    #   $ vagrant plugin install vagrant-disksize
    #
    # Default images are not big enough to build .
    # config.disksize.size = '8GB'
    # forward terminal type for better compatibility with Dialog - disabled on Ubuntu by default
    config.ssh.forward_env = ["TERM"]
    # default user name is "ubuntu", please do not change it

    # SSH password auth is disabled by default, uncomment to enable and set the password
    #config.ssh.password = "armbian"
    config.vm.provider "virtualbox" do |vb|
        #name of VM in virtualbox
        vb.name = "vagrant-stretch64-docker-jenkins"
        # uncomment this to enable the VirtualBox GUI
        #vb.gui = true
        # Tweak these to fit your needs.
        vb.memory = "8192"
        vb.cpus = "4"
     end

    config.vm.provision "shell", inline: $script

    # Set the name of the VM. See: http://stackoverflow.com/a/17864388/100134
    config.vm.define :jenkins do |jenkins|
    end

    # # Ansible provisioner.
    # config.vm.provision "ansible" do |ansible|
    #    ansible.playbook = "provisioning/main.yml"
    #    ansible.verbose = "v"
    # end

end
