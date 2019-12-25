Linux is an Unix-like operating system consisting of free/libre and open source software (FLOSS). The Linux kernel was written by Linus Torvalds and the first release was in 1991 for the x86 platform. Since then, a big community rose around this project and it was ported to an impressive number of platforms.[1] There are many variants of Linux available today due to the open nature of the development. While this greatly improves diversity it can also be a energy waste since there are many applications that basically do the same thing. A **Linux distribution** is a full Linux package (with many software and utilities) which can run or be installed on a computer.

Getting started
---------------

In order to get familiar with Linux one must have access to a Linux distribution to work on. Due to the fact that there are many distributions available many users find it difficult to chose one distribution over the other. Each Linux distribution has its own [package manager](http://en.wikipedia.org/wiki/Package_manager) and utilities for handling the way software is installed/removed/updated.

Distributions
-------------

-   [Debian](http://debian.org) It is the base distribution for Ubuntu, Linux Mint, Knoppix, etc. It uses .dpkg package manager with .deb packages. There are many other [.dpkg utilities](https://en.wikipedia.org/wiki/Dpkg) which make it easy to install software on these Linux distributions. One such utility is [apt-get](http://linux.die.net/man/8/apt-get).
-   [Red-Hat](http://www.redhat.com/products/enterprise-linux/) Is a commercial distribution released by Red Hat Inc. It uses the [RPM package manager(.rpm)](http://en.wikipedia.org/wiki/RPM_Package_Manager). Other distros that use this type of package management include Fedora, CentOS, Oracle Linux. There are also many frontends for .rpm, [yum](http://en.wikipedia.org/wiki/Yellow_dog_Updater,_Modified) being one of the most popular.
-   [Slackware](http://www.slackware.com/) It is the oldest active Linux distribution, which is mainly a one man project. It uses the slackpkg package manager. Its aim is simplicity and stability; Because of its simplicity there are many distributions derived from it like ZenWalk, VectorLinux and Slax.
-   [Arch Linux](https://www.archlinux.org/) It is a distribution using its own package manager named [pacman](http://en.wikipedia.org/wiki/Pacman_(package_manager)). One particularity of this distribution is that it doesn't have scheduled release but uses the [rolling release model](http://en.wikipedia.org/wiki/Rolling_release). This means that you get the latest software when updating.

Package manager
---------------

We described package managers as utilities to update/install/remove software. To make an idea about what a package manager does, imagine the [Windows](http://en.wikipedia.org/wiki/Microsoft_Windows) environment. Here you install software via .msi or .exe setup packages. The software can be removed/updated from "Add remove programs". All these things are unified under Linux environment in the form of the package manager. Each package in Linux can be considered an application/library/utility. These packages, along with their dependencies are installed with the help of the package manager.

The package manager (usually):

-   keeps a list of installed packages and their version
-   it handles dependencies between packages
-   handles a global update process of all the packages
-   can remove packages and unused dependencies
-   can use repositories (will be described later) with precompiled software

One can install also software from source, bypassing this way the package manager, but this can be risky and a source of operating system failures if not done carefully. There are also installers similar to the ones from Windows which can have their own way of installation, being able to bypass the package manager of the distribution.

Repository
----------

One important thing for each Linux distribution is the [application repository](http://en.wikipedia.org/wiki/Software_repository). This is the place where you can get software for your Linux distribution. Usually the repository represents a FTP/HTTP/HTTPS link from which the package manager downloads a list of available software.

For example this is the list of a link to a Ubuntu mirrored repository:

    Index of http://ftp.astral.ro/distros/ubuntu/

    Name    Last Modified   Size    Type
    Parent Directory/       -   Directory
    dists/   2012-Oct-18 20:33:45   -   Directory
    indices/ 2012-Oct-19 14:26:10   -   Directory
    pool/    2010-Feb-27 08:30:27   -   Directory
    project/ 2008-Feb-13 16:39:51   -   Directory
    ubuntu/  2013-Jan-21 13:54:31   -   Directory
    ls-lR.gz 2013-Jan-21 13:05:40   12.4M   application/x-gzip
    lighttpd

The link to the repository is put in configuration files, which are the very popular in the Unix/Linux environment. The repository configuration file is distribution specific and can be found in the manuals of the distribution that come along with the Linux distribution. Nowadays it is rarely needed to edit configuration files by hand, since there are a lot of utilities that do this for you. However there are situations when manual editing configuration files is needed.

General information
-------------------

### Multiuser

Linux is a real multiuser system. This means that multiple users can work on a machine at the same time. This reflects in all aspects of the operating system.

### File Systems

A file system is a way to access data. A typical example from Windows world is NTFS and FAT32 filesystems. Linux supports a wide range of filesystems, [ext3](http://en.wikipedia.org/wiki/Ext3) being one of the most common. Since Linux is a multiuser system we can see this in the filesystem. For example here are few directory listings together with explanations regarding ownership and file type:

    iulian@iulian-VirtualBox:~$ ls -l /home
    total 8
    drwxr-xr-x 24 iulian iulian 4096 Jan 22 10:13 iulian
    drwxr-xr-x  2 test   test   4096 Jan 22 11:10 test

-   first **d** stands for the file type which in this case is a directory
-   the next group **<span style="color:red">rwx</span>** shows the owner rights and means that the owner has all the rights - <span style="color:red">r</span>ead, <span style="color:red">w</span>rite, e<span style="color:red">x</span>ecute
-   the next group **<span style="color:red">r-x</span>** shows the group rights. This means that users from the owning group have only <span style="color:red">r</span>ead and e<span style="color:red">x</span>ecute right (no write).
-   the last group **<span style="color:red">r-x</span>** shows the rights of others (not in the group or the owner). This means that other users have only <span style="color:red">r</span>ead and e<span style="color:red">x</span>ecute right (no write).
-   the third column shows the owner of the file (directory)
-   the fourth column shows the owning group of the file

More information about what **ls** are on [manual page of ls](http://linux.die.net/man/1/ls).

The file system offers the possibility to set rights for each file by using the following 2 commands:

-   chmod
-   chown
-   chgrp

To avoid being given the [RTFM](http://en.wikipedia.org/wiki/RTFM), be sure to **check the manual** for each of these commands in order to get familiar with the Unix/Linux documentation.

### Documentation

Besides the Internet, Linux offers a lot of documentation sources in the manual pages. These pages can be accessed via the [man command](http://linux.die.net/man/1/man). For example here is how the documentation for **mkdir** (a command used to create a directory) can be seen from a Linux console:

    iulian@iulian-VirtualBox:~$ man mkdir
    #
    # and the displayed help looks like the following
    #
    MKDIR(1)                                             User Commands                                             MKDIR(1)

    NAME
           mkdir - make directories

    SYNOPSIS
           mkdir [OPTION]... DIRECTORY...

    DESCRIPTION
           Create the DIRECTORY(ies), if they do not already exist.

           Mandatory arguments to long options are mandatory for short options too.

           -m, --mode=MODE
                  set file mode (as in chmod), not a=rwx - umask
    ...
    ...
    ...

Beside the man command you can use other commands like:

-   info
-   apropos
-   whatis

### Everything is a file

In Linux/Unix everything is seen as a file. This means that hard-drives, network interfaces, audio-devices etc can be accessed via a file.

### Mounting

As mentioned before, everything is a file. This means that every device can be found in the filesystem. All hard-drives, cd-roms, usb-sticks and other storage media are found in this filesystem. In order to access the information found on them you must [mount](http://en.wikipedia.org/wiki/Mount_(Unix)) them. Some devices are automatically mounted when you start your computer. You can find them in the configuration file */etc/fstab* file:

    % cat /etc/fstab
    /dev/sda1       /               ext2        defaults        1   1
    /dev/sda2       /usr/local      ext2        defaults        1   1
    /dev/sda4       /home           ext2        defaults        1   1
    /dev/sdb1       swap            swap        defaults        0   0
    /dev/sdb3       /export         ext2        defaults        1   1
    none            /dev/pts        devpts      gid=5,mode=620  0   0
    none            /proc           proc        defaults        0   0
    /dev/fd0        /mnt            ext2        defaults        0   0
    /dev/cdrom      /mnt/cdrom      iso9660     ro              0   0

Today, in modern distributions many mount operations are done automatically. This means that you rarely need to use the [mount command](http://linux.die.net/man/8/mount). However, it is important to know how the mount/umount command works since it can offer information. For example to find out how many mounts are there you can simply type mount:

    iulian@iulian-VirtualBox:~$ mount
    /dev/sda1 on / type ext4 (rw,errors=remount-ro)
    proc on /proc type proc (rw,noexec,nosuid,nodev)
    sysfs on /sys type sysfs (rw,noexec,nosuid,nodev)
    none on /sys/fs/fuse/connections type fusectl (rw)
    none on /sys/kernel/debug type debugfs (rw)
    none on /sys/kernel/security type securityfs (rw)
    udev on /dev type devtmpfs (rw,mode=0755)
    devpts on /dev/pts type devpts (rw,noexec,nosuid,gid=5,mode=0620)
    tmpfs on /run type tmpfs (rw,noexec,nosuid,size=10%,mode=0755)
    none on /run/lock type tmpfs (rw,noexec,nosuid,nodev,size=5242880)
    none on /run/shm type tmpfs (rw,nosuid,nodev)
    gvfs-fuse-daemon on /home/iulian/.gvfs type fuse.gvfs-fuse-daemon (rw,nosuid,nodev,user=iulian)
    iulian@iulian-VirtualBox:~$ 

There are many options that one can do with mount. [2] For example you can even mount an .iso image in order to see the contents without writing it to a CD/DVD. This is what actually happens when using software like [Daemon Tools](http://www.daemon-tools.cc/eng/downloads) on Windows.

### Directory structure

There is a unix convention about the directory structure. Here are a few examples:

-   **/** is the root of the filesystem
-   **/etc** contains configuration files.
-   **/bin** contains binaries like fundamental utilities like *cd* or *ls*.
-   **/sbin** contains super user binaries, which are mainly used for administration purposes.
-   **/tmp** it is a temporary directory, used to store temporary data
-   **/root** the home directory of the superuser (root) or the system administrator
-   **/home** the home directory for other users
-   **/media** default mount point for usb-sticks and other portable media
-   **/mnt** Contains filesystem mount points; it can be used also for network filesystems ([nfs](http://en.wikipedia.org/wiki/Network_File_System)), cd-roms, etc

Another standard is the [Linux Standard Base](http://en.wikipedia.org/wiki/Linux_Standard_Base), which goes beyond the directory structure.[3]

Directory listing of an Ubuntu installation:

    iulian@iulian-VirtualBox:~$ ls -l /
    total 92
    drwxr-xr-x   2 root root  4096 Dec 10 10:13 bin
    drwxr-xr-x   3 root root  4096 Jan 21 10:08 boot
    drwxr-xr-x   2 root root  4096 Sep 20 12:57 cdrom
    drwxr-xr-x  15 root root  4260 Jan 22 10:13 dev
    drwxr-xr-x 128 root root 12288 Jan 22 10:13 etc
    drwxr-xr-x   3 root root  4096 Sep 20 13:03 home
    lrwxrwxrwx   1 root root    33 Jan 21 10:07 initrd.img -> /boot/initrd.img-3.2.0-36-generic
    lrwxrwxrwx   1 root root    33 Dec 10 10:17 initrd.img.old -> /boot/initrd.img-3.2.0-34-generic
    drwxr-xr-x  21 root root  4096 Oct 15 15:28 lib
    drwxr-xr-x   2 root root  4096 Nov  7 13:21 lib64
    drwx------   2 root root 16384 Sep 20 12:28 lost+found
    drwxr-xr-x   2 root root  4096 Oct 18 11:31 media
    drwxr-xr-x   3 root root  4096 Oct 18 11:37 mnt
    drwxr-xr-x   2 root root  4096 Oct 16 10:39 opt
    dr-xr-xr-x 150 root root     0 Jan 22 10:13 proc
    drwx------   3 root root  4096 Sep 20 13:58 root
    drwxr-xr-x  21 root root   820 Jan 22 10:13 run
    drwxr-xr-x   2 root root  4096 Jan 21 09:43 sbin
    drwxr-xr-x   2 root root  4096 Mar  5  2012 selinux
    drwxr-xr-x   2 root root  4096 Aug 23 19:50 srv
    drwxr-xr-x  13 root root     0 Jan 22 10:13 sys
    drwxrwxrwt  12 root root  4096 Jan 22 10:44 tmp
    drwxr-xr-x  13 root root  4096 Nov  7 13:33 usr
    drwxr-xr-x  13 root root  4096 Jan 21 16:36 var
    lrwxrwxrwx   1 root root    29 Jan 21 10:07 vmlinuz -> boot/vmlinuz-3.2.0-36-generic
    lrwxrwxrwx   1 root root    29 Dec 10 10:17 vmlinuz.old -> boot/vmlinuz-3.2.0-34-generic

Installing a Linux distribution
-------------------------------

Installing a Linux distribution is nowadays an easy task compared to what it was, let's say in 2002. This is because of the software and hardware advancements. When referring to software advancements I mainly refer to virtualization software; when it comes to hardware I refer to high-speed portable drives, cheaper RAM, support for hardware virtualization. All these advancements make it possible to run Linux without the risk of losing all your information:

-   Running (without installing!) a live stick with a Linux version. It is loaded in memory and never touches any information found on the hard drives
-   Installing into a virtual machine

If you however decide to install Linux on a real machine special steps must be taken if you don't want to lose data. You can even have multi-boot support; this means you can choose at booting phase which operating system to start (Windows/Linux/etc).

### Needed partitions

Linux needs a [swap partition](http://en.wikipedia.org/wiki/Swap_space#Linux), which is a regular partition formatted as Linux Swap filesystem. Other than that it needs **at least** one partition which will be mounted as **/**. You can use multiple partitions.

For example it is wise to save configuration settings on a different partition that will have its mountpoint **/etc**.

Another example which preserves the user settings is to put **/home** on a separate partition.

This way, when reinstalling the system we invest little effort in configuration since user settings (/home and system settings /etc) are preserved.

For performance reasons one can mount some directories like **/tmp** to memory. This is an optimization for applications that create a lot of temporary files.[4]

### Partitioning

Partitioning is done with tools that are usually part of the installation kit. You can use one (or more?) of these tools:

-   fdisk
-   cfdisk
-   parted

Note that it is very possible to have graphical frontends to such tools that are similar to [Partition Magic](http://en.wikipedia.org/wiki/PartitionMagic).

### Installation

The installation process is very similar in each distribution and consists in:

-   selecting the partition you want to install your distribution to
-   selecting the list of packages you want to install
-   make minimal configurations such as:
    -   time/date and timezone
    -   keyboard settings
    -   network configuration

NOTE:

-   Since network configuration is usually a process related to Linux administration we will not go into much details about it.

#### Installing from a live medium

As mentioned earlier Linux can be tested without installing by running it first from a live medium (CD/DVD or USB Stick). This can be considered a test to see if all the peripheric equipments are detected (network card, sound card, hard drives, etc). Once you checked and everything works as expected you can proceed to the installation process which should be a step by step process.

#### Installing from an installation CD

While this was the standard method for installing a system, it is now abandoned by every major Linux distribution in favor of the live-medium install.

#### Installing to a virtual machine

<span style="color:red">**NOTE:**</span> <u>If the live distribution doesn't work on the virtual machine try searching on discussion forums for answers. For example Fedora 18 doesn't work in VMWare Player unless you disable 3D acceleration. See [this thread](https://ask.fedoraproject.org/question/3520/fedora-18-impossible-to-use-on-vmware-9) for more details.</u>

For installing into a virtual machine you need to configure your machine in such way that you at least have:

-   a hard drive with enough space to permit the installation
-   enough RAM
-   a network card (Linux is pretty extensible once connected to a network)
-   other peripheric equipment that you need (serial ports, etc)

The configuration depends on your virtual machine software and [hardware capabilities](http://en.wikipedia.org/wiki/Hardware_virtualization). More information should be found in the software's manual.

#### Installing to a real hard drive

The big difference between installing on a Virtual Machine and installing on a real hard drive is <span style="color:red">**the possibility to lose data**</span> if not careful.

#### Selecting the boot device

Linux comes with a bootloader. This is the application that starts the Linux when booting. At the end of the installation you will be prompted to install a boot loader. The bootloader is the one that makes it possible to start your system after reboot. It is also the one responsible for multiboot support. You can even boot diferent versions of kernel of the same distribution.

You will usually need to install the bootloader into the booting hard drive (which usually is /dev/sda). This is related to administration activities and thus will not be detailed.

##### So what does the bootloader do?

1.  It prompts you when booting to chose what you want to start (Windows/Linux/FreeBSD/Other Linux/Linux With other kernel version/Other OS/etc)
2.  It loads the specified kernel (leaving the kernel to start the OS Initialization)

In Linux two bootloaders are used: [Lilo](http://en.wikipedia.org/wiki/LILO_(boot_loader)) and [GRUB](http://en.wikipedia.org/wiki/GNU_GRUB), though GRUB is the default for most of the distributions nowadays.

Installation of a package
-------------------------

Installation is an administrative task and requires root privileges. This means that it should be performed by people who understand the implications. Root privileges mean that you have full rights. In other words, be careful when running tasks with such privileges.

NOTE: Since installing is an administrative task it means that everything is executed with root privileges. You can use [sudo](http://linux.die.net/man/8/sudo) to do this. Depending on your system you can use [su](http://linux.die.net/man/1/su) command to gain root access.

All the instructions below assume you have root privileges.

### Installation with the distribution's package manager

Usually you can install software once the repository link/path is configured correctly. System administrators may choose to create mirrors of a central repository locally in order to avoid network traffic. As mentioned each distribution comes with its own package manager. We will give specific instructions for each distribution. We will focus on command line since from user interfaces things are pretty intuitive.

In Debian (.deb) based systems:

-   Update of packages

<!-- -->

    apt-get update

-   Upgrade of packages

<!-- -->

    apt-get upgrade

-   Install a package

<!-- -->

    apt-get install <name_of_package>

-   Remove a package

<!-- -->

    apt-get remove <name_of_package>

-   Search for a package or keywords

<!-- -->

    apt-cache search <keywords>

In .rpm based systems (using yum):

-   Update of packages

<!-- -->

    yum update

-   Upgrade of packages

<!-- -->

    yum upgrade

-   Install a package

<!-- -->

    yum install <name_of_package>

-   Remove a package

<!-- -->

    yum remove <name_of_package>

-   Search for a package

<!-- -->

    yum search <keywords>

### Installation from source

Usually there are a few steps that are made in order to install something from source. However be careful when doing this, because you may alter the OS, as the package manager can be bypassed. Usual steps when installing from source:

1.  Getting the source
        wget http://www.example.com/example.tar.gz

    This command basically downloads a tar.gz from a website. Consult wget manual for more details.

2.  Extract the sources from the archive
        tar -xzf example.tar.gz

3.  Read instructions about how to install package
        less README

    or

        less INSTALL

    or

        more INSTALL

    or ...

4.  Follow the instructions

Typically many programs in the Unix world come together with the [gnu build system](http://en.wikipedia.org/wiki/GNU_build_system). This means that **after** we extract the sources we usually do the following:

1.  autoconf (if needed - it generates configure script)
2.  ./configure (prepares the makefiles)
3.  make (compiles with the generated makefiles)
4.  make install (installs the application)

Note that on each step you can have additional configurations. For example you can choose where to install by typing:

    ./configure --prefix=/my_install_path/

### Installing from different repositories

You can install software from different repositories. For example beside the main repository you can add other repositories and get software from there. You will use the same instructions as above after you updated you repositories paths/links.

### Installing proprietary packages

Some applications ([Skype](https://www.skype.com/en/get-skype/) is an example) provide packages for various distributions. This means that you can download the corresponding package for your distribution (.deb in case of Debian based distributions).

To install a deb package you must use [dpkg](http://en.wikipedia.org/wiki/Dpkg):

    dpkg -i debFileName

One must regard dpkg as the base command for installing packages. It is used by all package management commands, including apt-get.

The same goes for .rpm packages in .rpm based distributions:

    rpm -i rpmFileName

### Other types of installations

Some applications, mainly proprietary ones, come with their custom installers. They usually have their own compiled libraries and upon installation they are stored in the installation folders. An example is the **quake3** installer which by default installs in **/usr/local/games/quake3**. Typically such applications come with many libraries of their own that are usually stored outside the system libraries, to make sure they don't alter the OS. Of course, this type of installations can bypass the package manager.

Using the command line
----------------------

The shell is present in most of the Unix like systems. There are many things that can be automatized and, for most of them, the only way is to use a shell. A shell is an interface in which users type commands and get information. Everything that you type is interpreted and a response gets back to you.

The default shell for most of the Linux distribution is **bash**. As each interpreter, it has its own language. The bash language itself will not be detailed in this section as there are too many things to discuss. Instead of enumerating all features and syntax it is generally recommended to do different tasks with bash in order to accommodate with it.

NOTE: There are shells similar to bash: sh, csh or ksh. Depending on the shell used one may need to use slightly different syntaxes. For example here is a [comparison between csh and sh](http://en.wikipedia.org/wiki/C_shell#More_like_C).

### Environment variables

Just like in Windows, environment variables also exist in Unix like systems. They can be added/modified/removed in order to accommodate various applications that use them.

A simple example is the HOME variable which points to the user's home directory.

    iulian@iulian-VirtualBox:~$ echo $HOME
    /home/iulian
    iulian@iulian-VirtualBox:~$ 

Another example is the **PATH** variable tells what are the paths from which we can launch commands without providing the full path to the executable. For example one can launch **ls** without the need to provide full path **/bin/ls** because **/bin** directory is in PATH. This is similar to the Windows behavior of PATH.

    iulian@iulian-VirtualBox:~$ echo $PATH
    /usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
    iulian@iulian-VirtualBox:~$ ls -l /bin/ls
    -rwxr-xr-x 1 root root 105840 Nov 20 00:25 /bin/ls
    iulian@iulian-VirtualBox:~$ ls
    Desktop    Downloads         Music     Public     tests   Work
    Documents  examples.desktop  Pictures  Templates  Videos
    iulian@iulian-VirtualBox:~$ 

One difference here compared to Windows is that PATH variable uses **:** (colon) separator instead of **;** (semicolon).

There are many variables that influence the way program works. Some of them are:

-   LD\_PRELOAD
-   LD\_LIBRARY\_PATH

Other examples can be found [here](http://linux.die.net/man/8/ld.so).

Some application specific environment variable is [CLASSPATH](http://en.wikipedia.org/wiki/Classpath_(Java)#Setting_the_path_through_an_environment_variable) which is used by the java runtime.

Information about all these variables can be found in the application specific documentation.

### File system

See [File Systems](Linux_guidelines#File_Systems "wikilink") section for how the file systems permissions and useful commands for changing permissions.

You can browse through the file system inside the shell by using commands like:

-   cd - change directory
-   ls - list contents of current directory
-   mkdir - create a directory
-   rmdir - removes an empty directory
-   rm - removes a file/directory
-   pwd - prints the current directory
-   find - searches for files
-   mv - rename/move
-   cp - copy a file
-   ln - create a link
-   which - tells where an executable is found in path
-   touch - change timestamp of file or create an empty file

### Process utilities

Linux is a multitask operating system. This means that multiple processes can run in the same time. Just like in other multitask operating systems you can see which processes are running, terminate them, give them higher/low priority. Some of the commands used for process handling are:

-   ps - shows information about the running processes
-   top - shows processes while running, how much memory/cpu they use and can sort them depending on various criteria
-   pstree - shows the tree of processes with parent-&gt;child relation
-   kill - it is used to terminate processes; generally it sends a signal which by default is the terminate signal. For killing a process one can use the following commands:

<!-- -->

    kill <pid>

In case the terminate signal is ignored (this can be done programatically and some applications do it) you can send the KILL signal to the application (the KILL signal, or signal number 9, cannot be ignored):

    kill -9 <pid>
    kill -KILL <pid>
    kill -s 9 <pid>
    kill -s KILL <pid>

-   killall - it is used to terminate process by name.
-   nice - run a program with desired priority
-   renice - change priority of a running process

Read the manual page of each command for further options. For more information about signals you can check the signal manual page from section 7:

    man 7 signal

**NOTE:** You usually should try closing processes gracefully and only if this is not possible to use *kill* and related commands.

### Basic network utilities

Since networking usually falls in the hands of administrating users it will only be briefly presented here.

Here are some commands together with their description:

-   ping - send a ICMP request to a host (usually to see the response time, or to see if a host is available)
-   netstat - shows information about the current connections of the current machine
-   traceroute - shows the hops needed to reach a host
-   ifconfig - configure network interfaces (root privileges needed) or show information about the network interfaces
-   host, dig - shows DNS information
-   ssh - client application able to connect to remote sshd servers
-   telnet - the predecessor of ssh; one remarkable difference is that everything in send in clear on the network while in the case of ssh everything is encrypted

### Bash scripting

Each program has at least three open streams when started:

-   stdin - file descriptor 0 (for reading - by default it reads from the terminal)
-   stdout - file descriptor 1 (for writing - by default writes to console)
-   stderr - file descriptor 2 (for writing - by default writes to console)

#### Redirecting

-   Redirecting stdin

<!-- -->

    command < file

This way the command reads everything from **file** instead of reading from the terminal

-   Redirecting stdout

<!-- -->

    command > file

or

    command 1> file

-   Redirecting stderr

<!-- -->

    command 2> file

-   Redirecting both stderr and stdout to different files

<!-- -->

    command > stdout_file 2> stderr_file

-   Redirecting stder and stdout to same file

<!-- -->

    command &> file

-   Redirecting by appending to file

<!-- -->

    command >> file

This command appends to an existing file instead of creating a new file with the output of command.

##### tee

Sometimes we want to put the information to stdout and both to a file. This can be achieved with **tee** command. For example to display the list of files and saving it to a file you can use the following command:

    iulian@iulian-VirtualBox:~/tests$ ls . | tee ls.txt
    alias.sh
    arit.sh
    in.txt
    ls.txt
    showmyvar.sh
    iulian@iulian-VirtualBox:~/tests$ cat ls.txt 
    alias.sh
    arit.sh
    in.txt
    ls.txt
    showmyvar.sh
    iulian@iulian-VirtualBox:~/tests$ 

To append to a file option **-a** can be added to the tee command.

For more information about redirection you can consult the bash manual, section **REDIRECTING**.

#### Piping

Piping means redirecting the output of a program to the input of another program. This can be achieved in bash with the pipe operator (**|**):

    command1 | command2

In this case the stdout of **command1** is the input of **command2**. See **Pipelines** section from bash manual.

#### Processing text in bash - filters

##### grep

The unix environment provides commands that help you filter your input. For example let's say I want to know all the environment variables that contain the **proxy** keyword. I can achieve this with the *grep* command for filtering:

    iulian@iulian-VirtualBox:~/tests$ env | grep proxy
    http_proxy=http://proxy01.example.com:8000/
    ftp_proxy=ftp://proxy01.example.com:8000/
    ALL_PROXY=socks://proxy01.example.com:8000/
    all_proxy=socks://proxy01.example.com:8000/
    socks_proxy=socks://proxy01.example.com:8000/
    https_proxy=https://proxy01.example.com:8000/
    no_proxy=localhost,127.0.0.0/8,*.example.com
    iulian@iulian-VirtualBox:~/tests$ 

By default the search of *grep* is case sensitive but with the **-i** switch we can change that:

    iulian@iulian-VirtualBox:~/tests$ env | grep -i proxy
    NO_PROXY=localhost,127.0.0.0/8,*.example.com
    http_proxy=http://proxy01.example.com:8000/
    ftp_proxy=ftp://proxy01.example.com:8000/
    ALL_PROXY=socks://proxy01.example.com:8000/
    all_proxy=socks://proxy01.example.com:8000/
    socks_proxy=socks://proxy01.example.com:8000/
    UBUNTU_MENUPROXY=libappmenu.so
    https_proxy=https://proxy01.example.com:8000/
    no_proxy=localhost,127.0.0.0/8,*.example.com

You can even invert the match by using the **-v** switch. This means that it will filter everything that contains the keyword leaving everything else to be displayed:

    iulian@iulian-VirtualBox:~/tests$ env | grep -iv proxy
    SSH_AGENT_PID=2539
    GPG_AGENT_INFO=/tmp/keyring-DZ00Bc/gpg:0:1
    TERM=xterm
    SHELL=/bin/bash
    XDG_SESSION_COOKIE=c327ef6ef0f1dfd3581b09150000000b-1360071901.702413-1161824480
    WINDOWID=44040198
    GNOME_KEYRING_CONTROL=/tmp/keyring-DZ00Bc
    USER=iulian
    ............................
    iulian@iulian-VirtualBox:~/tests$ 

###### grep with regular expressions

You can use [regular expressions](Linux_guidelines#Filtering_with_regular_expressions "wikilink") when using grep. For example to remove lines that contain *only* comments from a bash script you can use the following command:

    iulian@iulian-VirtualBox:~/tests$ grep -v -E "^[ \t]*#" arit.sh 
    x="140"
    y="-98"
    z=$((x+y))
    echo $z
    iulian@iulian-VirtualBox:~/tests$ cat arit.sh 
    #!/bin/bash
    x="140"
    y="-98"
      # this comment is with space in front
    #this does an arithmetic addition
    z=$((x+y))
    echo $z
    iulian@iulian-VirtualBox:~/tests$ 

-   **-v** means to print the non-matching lines
-   **-E** means to use extended regular expressions (extended regex is the standard nowadays)
-   **^\[ \\t\]\*\#** regex means matching everything that starts with zero or more (**\***) whitespace characters (which means space or tab), and is followed by a **\#** character

##### head/tail

To retrieve only the first or the last part of an input we can use the head and tail correspondingly. As an example we retrieve the first 2 lines of a file:

    iulian@iulian-VirtualBox:~/tests$ head -n 2 alias.sh 
    #!/bin/bash
    shopt -s expand_aliases
    iulian@iulian-VirtualBox:~/tests$ 

Similarly you can retrieve the last 2 lines by using tail

    iulian@iulian-VirtualBox:~/tests$ tail -n 2 alias.sh 
    . ~/x.sh
    ll
    iulian@iulian-VirtualBox:~/tests$ 

When you want to see what is written in a log file you can use tail with **-f** option (follow):

    tail -f log_file_where_lines_are_appended

Using **tail -f** keeps **tail** executable running until the user exits by pressing CTRL+C (which by default sends a SIGINT signal to the application)

##### rev

rev is a command that reverses the text of each line. Example of usage:

    iulian@iulian-VirtualBox:~/tests$ echo xinu | rev
    unix
    iulian@iulian-VirtualBox:~/tests$ 

##### sort

Sorting input can be done with the **sort** command:

    iulian@iulian-VirtualBox:~/tests$ cat in.txt 
    b
    a
    c
    d
    iulian@iulian-VirtualBox:~/tests$ sort in.txt 
    a
    b
    c
    d
    iulian@iulian-VirtualBox:~/tests$ 

##### uniq

Filtering lines that are equal in a file can be achieved by using the **uniq** command. A condition for calling **uniq** is that the lines are sorted.

    iulian@iulian-VirtualBox:~/tests$ cat in.txt 
    b
    a
    c
    c
    b
    d
    iulian@iulian-VirtualBox:~/tests$ sort in.txt | uniq 
    a
    b
    c
    d
    iulian@iulian-VirtualBox:~/tests$ 

##### cut

**cut** can be used to extract some parts of a line based on a delimiter. For example to extract the first part (**-f1**) of a line separated by equal character (**-d=**) you can use the following command:

    iserban@bra-w10-038 ~
    $ echo -e "ABC=def\nXYZ=abc"
    ABC=def
    XYZ=abc

    iserban@bra-w10-038 ~
    $ echo -e "ABC=def\nXYZ=abc" | cut -d= -f1
    ABC
    XYZ

    iserban@bra-w10-038 ~
    $

##### tr

Using **tr** command you can replace or delete characters. For example to replace characters we provide two sets and the characters present in the first set will be replaced by characters from the second set:

    iulian@iulian-VirtualBox:~/tests$ echo "Upper case?" | tr [a-z] [A-Z]
    UPPER CASE?
    iulian@iulian-VirtualBox:~/tests$ 

To delete some characters we can use the **-d** option. For example to erase commas from a text we use the following command:

    iulian@iulian-VirtualBox:~/tests$ echo "Hi, are Jim, James and Danny here?" | tr -d ,
    Hi are Jim James and Danny here?
    iulian@iulian-VirtualBox:~/tests$ 

To keep commas we can use the complement of the set (**-c** option). This can prove useful to count the number of characters in a string (with *wc* command):

    iulian@iulian-VirtualBox:~/tests$ echo "Hi, are Jim, James and Danny here?" | tr -c -d ,
    ,,iulian@iulian-VirtualBox:~/tests$ 
    iulian@iulian-VirtualBox:~/tests$ echo "Hi, are Jim, James and Danny here?" | tr -c -d , | wc -c
    2
    iulian@iulian-VirtualBox:~/tests$ 

To squeeze characters one can use the **-s** option

    iulian@iulian-VirtualBox:~/tests$ echo "What are you doing???????????" | tr -s ?
    What are you doing?
    iulian@iulian-VirtualBox:~/tests$ 

##### sed

**sed** offers the possibility to edit the input with the use of advanced features like [regular expressions](Linux_guidelines#Filtering_with_regular_expressions "wikilink"). All the capabilities of *sed* are described in the sed manual. Here is a list of non-comprehensive features of sed:

-   search replace (with regular expressions)

In the following simple example note the **/g** in the second command which replaces all the occurrences of "John" instead of the first.

    iulian@iulian-VirtualBox:~/tests$ cat story.txt 
    John is a student. John wakes up in the morning.
    John meets with his fellows after classes.
    They always appreciate John for having a good sense of humor.
    iulian@iulian-VirtualBox:~/tests$ sed "s/John/David/" story.txt 
    David is a student. John wakes up in the morning.
    David meets with his fellows after classes.
    They always appreciate David for having a good sense of humor.
    iulian@iulian-VirtualBox:~/tests$ sed "s/John/David/g" story.txt 
    David is a student. David wakes up in the morning.
    David meets with his fellows after classes.
    They always appreciate David for having a good sense of humor.
    iulian@iulian-VirtualBox:~/tests$ 

In the next example we will swap first name with last name in a file containing two names on each line (**-r** forces the use of extended regular expressions). **\\1** and **\\2** stand for the sub-expressions matching the regular expressions (sub-expressions are delimited with **(** and **)**).

    iulian@iulian-VirtualBox:~/tests$ sed -r "s/([A-Za-z]+)[ \t]+([A-Za-z]+)/\2 \1/" names.txt 
    Doe John
    Last First
    Lastish Firstish
    Lee Bruce
    Willis Bruce
    Last The
    iulian@iulian-VirtualBox:~/tests$ cat names.txt 
    John Doe
    First Last
    Firstish Lastish
    Bruce Lee
    Bruce Willis
    The Last
    iulian@iulian-VirtualBox:~/tests$ 

As another example let's consider the [grep regular expressions](Linux_guidelines#grep_with_regular_expressions "wikilink") example and extend its functionality by removing all the comments from a bash script. This means including the comments after a command:

    iulian@iulian-VirtualBox:~/tests$ grep -v -E "^[ \t]*#" arit.sh | sed -r "s/([^#]+)#.*/\1/"
    x="140"
    y="-98"
    z=$((x+y)) 
    echo $z
    iulian@iulian-VirtualBox:~/tests$ grep -v -E "^[ \t]*#" arit.sh
    x="140"
    y="-98"
    z=$((x+y)) # comment after command
    echo $z
    iulian@iulian-VirtualBox:~/tests$ cat arit.sh 
    #!/bin/bash
    x="140"
    y="-98"
      # this comment is with space in front
    #this does an arithmetic addition
    z=$((x+y)) # comment after command
    echo $z
    iulian@iulian-VirtualBox:~/tests$ 

-   character replacement (similar to what [**tr**](Linux_guidelines#tr "wikilink") does)

<!-- -->

    iulian@iulian-VirtualBox:~/tests$ echo "ABCD" | sed "y/ABC/XYZ/"
    XYZD
    iulian@iulian-VirtualBox:~/tests$ 

##### awk

#### Filtering with regular expressions

**NOTE:** There are differences between basic regular expressions (BRE) and extended regular expressions(ERE). Since most of the systems support ERE we will make a list of the most used regular expressions. This is not intended to be a complete reference or to show an exhaustive list of regular expressions. It is the duty of each one using regular expressions to document about the supported expressions on the platform he's using. A starting point for this can be:

-   [regular expressions wikipedia page](http://en.wikipedia.org/wiki/Regular_expression)
-   [the manual page for grep](http://linux.die.net/man/1/grep)

With advanced commands like **sed, grep** or **awk** one can use regular expressions. Here is a list of regular expression metacharacters and their meaning:

| Metacharacter | Meaning                                                                                                                                                                                                                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **.**         | Any character                                                                                                                                                                                                                                                                                                                                                        |
| **[ ]**      | Matches a list of characters or character range. For example **[adm]** matches any of the letters **a**, **d** or **m**. You can also specify ranges with **-** (minus). For example **[0-9]** matches a digit or **[a-z]** matches all lowercase letters. To match all the letters you can specify 2 ranges **[a-zA-Z]**.                                   |
| **[^ ]**    | Works in opposite way compared to the previous. This means that **[^0-9]** matches everything **except** digits.                                                                                                                                                                                                                                                   |
| **^**         | Matches the beginning of the string. In line based tools this means the beginning of the line.                                                                                                                                                                                                                                                                       |
| **$**         | Matches the end of the string. In line based tools this means the end of the line.                                                                                                                                                                                                                                                                                   |
| **?**         | Matches the preceding expression at most 1 time (this means 0 or 1 times).                                                                                                                                                                                                                                                                                           |
| **\***        | Matches the preceding expression at most 0 or more times.                                                                                                                                                                                                                                                                                                            |
| **+**         | Matches the preceding expression at least one time. This means 1 or more times. For example **\[0-9\]+** matches a group of digits which has at least 1 digit (like 123 or 2).                                                                                                                                                                                       |
| **|**         | This is used to match multiple expressions. For example **black|cat** matches either **black** or **cat** words.                                                                                                                                                                                                                                                     |
| **{m,n}**     | Match the preceding expression at least **m** times but no more than **n** times. For example **\\.[a-z]{2,3}** can match a domain suffix (.com, .de, .ro, .ch). Note that **.** (the dot) is escaped in order not to be interepretted as *any character*. **{1,}** is equivalent to **+**, **{0,}** is equivalent to **\*** and **{0,1}** is equivalent to **?**. |

#### Exploring the filesystem from bash

Go to [File System](#File_system "wikilink") section for more details and related commands.

#### Process handling commands

See [Process utilities](#Process_utilities "wikilink") section for more details and commands. Be aware that while having administrative rights (eg: root) **kill**ing processes may render you system unstable.

#### Tweaking/configuring the shell (bash)

Bash offers the possibility to be configured. This can be done either by running a command each time when opening a console or by putting that command into one or more scripts that bash executes an startup. These scripts are according to the documentation:

    /etc/profile
    The systemwide initialization file, executed for login shells
    ~/.bash_profile
    The personal initialization file, executed for login shells
    ~/.bashrc
    The individual per-interactive-shell startup file
    ~/.bash_logout
    The individual login shell cleanup file, executed when a login shell exits
    ~/.inputrc
    Individual readline initialization file

#### Creating scripts for various interpreters

The first line in a script is usually the line containing the interpretter. For example in the following script the interepreter is **/bin/bash**:

    iulian@iulian-VirtualBox:~/tests$ cat showmyvar.sh 
    #!/bin/bash
    echo The value of MY_VAR is:$MY_VAR. 
    iulian@iulian-VirtualBox:~/tests$ 

To see that the first line is not just a comment (**\#** in bash is interpreted as comment) try replacing **/bin/bash** with the **cat** command (**which cat**).

    iulian@iulian-VirtualBox:~/tests$ cat showmyvar.sh
    #!/bin/cat
    echo The value of MY_VAR is:$MY_VAR. 
    iulian@iulian-VirtualBox:~/tests$ ./showmyvar.sh
    #!/bin/cat
    echo The value of MY_VAR is:$MY_VAR. 
    iulian@iulian-VirtualBox:~/tests$

##### env command

To be able to create a script that is independent of the path where the interpreter is installed (*cat* may be located in **/bin/cat** or in **/usr/bin/cat**) you can use the **env** command. *env* can be used in the following way:

    iulian@iulian-VirtualBox:~/tests$ cat my.py 
    #!/usr/bin/env python
    print "Hello Python!"
    iulian@iulian-VirtualBox:~/tests$ ./my.py 
    Hello Python!
    iulian@iulian-VirtualBox:~/tests$ 

This is the way to write scripts for the various scripting languages that available on \*nix platforms: php, python, perl, csh, ksh, bash, sh etc. When *env* receives no parameters it only prints the current environment and exits.

#### Conditional execution in bash

``` bash
#!/bin/sh
if [ $days -gt 365 ]
then
   echo This is over a year.
fi

if [ -d /my/path ]
then
   echo The dir exists
fi

if [ ! -d /my/path ]
then
   echo The dir does not exist
fi
```

To get a full list of the if syntaxes you can check the [man test manual page](http://linux.die.net/man/1/test).

#### Bash aliases and functions

##### Aliases

If you type 'alias' in a bash prompt a list will be printed:

    alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
    alias egrep='egrep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias grep='grep --color=auto'
    alias l='ls -CF'
    alias la='ls -A'
    alias ll='ls -alF'
    alias ls='ls --color=auto'

What this wants to say is that some commands are replaced when they are typed with their aliases. For example when you type **grep** it will be replaced with **grep --color=auto**. You can create aliases with the alias command also:

    iulian@iulian-VirtualBox:~$ alias e='echo "My alias"'
    iulian@iulian-VirtualBox:~$ e
    My alias
    iulian@iulian-VirtualBox:~$ 

This means that whenever you have a command you can create a sort of shorthand for it, like in the example below.

**NOTE:** By default aliases are enabled in interactive shells. But when executing a script, which is an non-interactive shell by default, they will not be expanded. For this to work **shopt -s expand\_aliases** must be put in the script before declaring **aliases**.

##### Functions

Bash also provides the ability to create functions. They can become useful inside scripts. For example you can create a function that lists all conf files in a specified directory.

    function quit {
      exit
    }
    function hello {
      echo Hello!
    }
    function showparam1and2 {
      echo Param1 $1
      echo Param2 $2
    }

Compared to aliases, functions can also be given one or more parameters making them extremely useful compared to aliases. This is because aliases only replace some command with another command. The parameters can be accesses just like in a normal bash script with **$1**, **$2** and so on.

To export functions so that they can be used to child processes you must use the **export -f** command which is bash specific.

    function hello {
      echo Hello!
    }
    export -f hello
    ./childscript.sh

#### Loops in bash

Bash provides loops like most programming languages. The syntax is the following:

    for varname [ [ in [ word ... ] ] ; ] do <list of commands> ; done

For example if we want to print the files in the current directory we can do that with the following **for** loop:

    for file in *; do
       echo $file
    done

If we want to print a list of words we can use for in the following way:

    for x in a b c d; do
    echo $x
    done

Similarly one can use also the **while** loop which has the following syntax:

    while condition; do <command list>; done

For more information one can check *Compound Commands* chapter from the bash manual.

##### Arithmetic evaluation

Bash offers also the possibility to arithmetically evaluate expressions. This can be achieved by using double parenthesis: **((** expr **))**. For example you can create a for loop similar to the one from the C language in bash using the double parenthesis:

    iulian@iulian-VirtualBox:~$ 
    for ((i=0;i<5;i++)); do 
    echo $i; 
    done
    0
    1
    2
    3
    4
    iulian@iulian-VirtualBox:~$ 

Another example is adding numbers in bash:

    iulian@iulian-VirtualBox:~/tests$ cat arit.sh 
    #!/bin/bash
    x="140"
    y="-98"
    z=$((x+y))
    echo $z
    iulian@iulian-VirtualBox:~/tests$ ./arit.sh 
    42
    iulian@iulian-VirtualBox:~/tests$ 

For more details you can check the *ARITHMETIC EVALUATION* chapter in the bash manual.

### other shells: sh,csh,ksh,bash,dash,...

As explained in the [interpreters](#Creating_scripts_for_various_interpreters "wikilink") section there can be many interpreters that can be used to write scripts. For example if some scripts use *csh* (C shell) instead of *bash* they will have a different syntax[5]:

<table>
<tr>
<td>
bash
</td>
<td>
csh (C shell)
</td>
<tr>
<td>
   <pre lang="bash">
   #!/bin/sh 
    if [ $days -gt 365 ]
    then
      echo This is over a year.
    fi
   </pre>
</td>
<td>
  <pre lang="bash">
   #!/bin/csh 
    if ( $days > 365 ) then
      echo This is over a year.
    endif
  </pre>
</td>
</tr>
</table>

Things to consider:<u>

1.  You should check the manual of each shell you want to use if you want writing/converting scripts to work with that interpreter
2.  You should check shell compatibility (there are differences between *sh*, *bash*, *dash*, *ksh* and other implementations)
3.  You should have maintainability and portability in mind (it is advisable to stick to one shell in a project)

</u>

Working remotely
----------------

### From Linux

To connect to the host named **my\_host\_name** with the user **my\_user** you must type one of the following commands:

    ssh -l my_user my_host_name
    ssh my_user@my_host_name

Transferring files from is done via **scp** command:

    scp my_user@my_host_name:path_to_remote_file path_to_local_destination

For extra information about these commands you can consult their manual page.

### From Windows

From Windows you must download a ssh client. One of the most popular is [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/). For scp you can use [WinSCP](http://winscp.net/).

### From Other operating systems

The only thing to be done is to use a ssh client for the platform you're using it.

### Running remote graphical applications

Running graphical applications in the Linux environment uses the services provided by an X server. This is usually installed on a Linux machine where a graphical environment is present. The [design](http://en.wikipedia.org/wiki/X_Window_System#Design) of this service allows it to run applications even via network as long as you have a server installed locally. This means that if you are connected on a remote machine you can use the graphical applications present on that machine. They will be however displayed on your machine provided that you:

1.  have installed an X server
2.  have configured the connection to forward the X protocol via the network

#### On Linux

On Linux machine the X server is installed and running when you are in a graphical session. You don't have to do anything except configuring the ssh connection to the remote host. To enable the forwarding of the X protocol you can use the **-X** or **-Y** option in ssh:

    ssh -Y user@host

You can check after that if the display variable is set (this is used by programs using X to connect themselves to the X server):

    echo $DISPLAY

#### On Windows

On Windows you must install a X server. There are many X servers that can be installed:

-   [VcXsrv](https://sourceforge.net/projects/vcxsrv/) this seems to be an up to date version of X server for Windows since XMing can be downloaded only after contributing to the project
-   [Cygwin/X](http://x.cygwin.com/) The X Server from the Cygwin environment (\*)
-   [XMing](https://sourceforge.net/projects/xming/) though no updates were made recently and new releases require you to donate (requires a donor password)

<!-- -->

-   ... others (you can add to this list) ...

After you have installed and started the X server you must connect with putty enabling the X11 forwarding from the following position: **Connection-&gt;SSH-&gt;X11-&gt;Enable X11 Forwarding**

**\***: you can install the full [cygwin](https://cygwin.com/install.html) stack together with Cygwin/X and use the same workflow as for remoting from linux. This is much easier to set up.

Documentation sources
---------------------

-   [Debian documentation](http://www.debian.org/doc/)
-   [Slackware book](http://www.slackbook.org/html/index.html)
-   [Ubuntu help](https://help.ubuntu.com/)
-   [Ubuntu wiki](https://wiki.ubuntu.com/)
-   [LPI Linux Certification from Wikibooks](http://en.wikibooks.org/wiki/LPI_Linux_Certification)

References
----------

<references/>
<Category:Linux> <Category:Open_Source_Software>

[1] [Wikipedia Linux Page](http://en.wikipedia.org/wiki/Linux)

[2] [Slackbook: Filesystem structure and mounting](http://www.slackbook.org/html/filesystem-structure-mounting.html)

[3] [The Unix directory structure](http://en.wikipedia.org/wiki/Unix_directory_structure)

[4] [tmpfs - a memory filesystem](http://en.wikipedia.org/wiki/Tmpfs)

[5] [The C shell Wikipedia page](http://en.wikipedia.org/wiki/C_shell#More_like_C)
