# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "final-control0" do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.hostname = "final-control0"
    config.vm.network "private_network", ip: "192.168.56.10"
    config.vm.provider "virtualbox" do |vb|
      vb.name = "final-control0"
      vb.cpus = 2
      vb.memory = 3072
      if !File.exist?("disk00.vdi") 
        vb.customize ["createmedium", "disk", "--filename", "disk00.vdi", "--size", 10240]
      end
      vb.customize ["storageattach", :id, "--storagectl", "SCSI", "--port", 2, "--device", 0, "--type", "hdd", "--medium", "disk00.vdi"]
    end
  end
  config.vm.define "final-node01" do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.provider "virtualbox" do |vb|
      vb.name = "final-node01"
      vb.cpus = 1
      vb.memory = 1536
      if !File.exist?("disk01.vdi") 
        vb.customize ["createmedium", "disk", "--filename", "disk01.vdi", "--size", 10240]
      end
      vb.customize ["storageattach", :id, "--storagectl", "SCSI", "--port", 2, "--device", 0, "--type", "hdd", "--medium", "disk01.vdi"]
    end
    config.vm.hostname = "final-node01"
    config.vm.network "private_network", ip: "192.168.56.20"
    config.disksize.size = "50GB"
  end
  config.vm.define "final-node02" do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.provider "virtualbox" do |vb|
      vb.name = "final-node02"
      vb.cpus = 1
      vb.memory = 1536
      if !File.exist?("disk02.vdi") 
        vb.customize ["createmedium", "disk", "--filename", "disk02.vdi", "--size", 10240]
      end
      vb.customize ["storageattach", :id, "--storagectl", "SCSI", "--port", 2, "--device", 0, "--type", "hdd", "--medium", "disk02.vdi"]
    end
    config.vm.hostname = "final-node02"
    config.vm.network "private_network", ip: "192.168.56.30"
    config.disksize.size = "50GB"
  end
  config.vm.define "final-node03" do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.provider "virtualbox" do |vb|
      vb.name = "final-node03"
      vb.cpus = 1
      vb.memory = 1536
      if !File.exist?("disk03.vdi") 
        vb.customize ["createmedium", "disk", "--filename", "disk03.vdi", "--size", 10240]
      end
      vb.customize ["storageattach", :id, "--storagectl", "SCSI", "--port", 2, "--device", 0, "--type", "hdd", "--medium", "disk03.vdi"]
    end
    config.vm.hostname = "final-node03"
    config.vm.network "private_network", ip: "192.168.56.40"
    config.disksize.size = "50GB"
  end

  # Hostmanager plugin
  config.hostmanager.enabled = true
  config.hostmanager.manage_guest = true

  # Enable SSH Password Authentication
  config.vm.provision "shell", inline: <<-SHELL
    sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/g' /etc/ssh/sshd_config
    sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
    sed -i 's/security.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
    systemctl restart ssh
    systemctl start systemd-timesyncd
    timedatectl set-timezone UTC
  SHELL
end
