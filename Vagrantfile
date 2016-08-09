# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  # Download an Ubuntu 14.04 box with the desktop GUI
  config.vm.box = "box-cutter/ubuntu1404-desktop"
  # Download an Ubuntu 14.04 box with no GUI
  #config.vm.box = "ubuntu/trusty64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  #config.vm.synced_folder ".", "/workspace"

  def usbfilter_exists(machine_name, vendor_id, product_id)
    #
    # Determine if a usbfilter with the provided Vendor/Product ID combination
    # already exists on this VM.
    #
    # TODO: Use a more reliable way of retrieving this information.
    #
    # NOTE: The "machinereadable" output for usbfilters is more
    #       complicated to work with (due to variable names including
    #       the numeric filter index) so we don't use it here.
    #
    machine_id_filepath = ".vagrant/machines/" + machine_name + "/virtualbox/id"

    if not File.exists? machine_id_filepath
      # VM hasn't been created yet.
      return false
    end

    vm_info = `VBoxManage showvminfo $(<#{machine_id_filepath})`
    filter_match = "VendorId:         #{vendor_id}\nProductId:        #{product_id}\n"
    return vm_info.include? filter_match
  end

  def better_usbfilter_add(vb, machine_name, vendor_id, product_id, filter_name)
    #
    # This is a workaround for the fact VirtualBox doesn't provide
    # a way for preventing duplicate USB filters from being added.
    #
    # TODO: Implement this in a way that it doesn't get run multiple
    #       times on each Vagrantfile parsing.
    #
    if not usbfilter_exists(machine_name, vendor_id, product_id)
      vb.customize ["usbfilter", "add", "0",
                    "--target", :id,
                    "--name", filter_name,
                    "--vendorid", vendor_id,
                    "--productid", product_id
                    ]
    end
  end

  config.vm.hostname = "baa-serverless-config"
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = false

    vb.name = "baa-serverless-config"

    # Customize the amount of memory on the VM:
    vb.memory = 2048
    vb.cpus = 1
    # Enable USB
    vb.customize ["modifyvm", :id, "--usb", "on"]
    # Enable USB2.0
    vb.customize ["modifyvm", :id, "--usbehci", "on"]
    # Add a USB filter for the Ortec DigiBASE (VID: 2605 (0x0a2d), PID: 31 (0x001f))
    better_usbfilter_add(vb, config.vm.hostname, "0a2d", "001f", "Ortec DigiBASE")

  end
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y python-dev python-pip liblz4-dev thrift-compiler python-thrift
    sudo pip install base64
  SHELL

  config.vm.provision "shell", run: "always", inline: <<-SHELL
    echo "build"
    cd /vagrant/
    sudo pip install -t baa_messages/vendored/ -r requirements.txt
  SHELL

end
