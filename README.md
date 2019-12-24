# Linux guidelines

Linux is an Unix-like operating system consisting of free/libre and open source software (FLOSS). The Linux kernel was written by Linus Torvalds and the first release was in 1991 for the x86 platform. Since then, a big community rose around this project and it was ported to an impressive number of platforms.<sup>[1](#fn1)</sup> There are many variants of Linux available today due to the open nature of the development. While this greatly improves diversity it can also be a energy waste since there are many applications that basically do the same thing. A Linux distribution is a full Linux package (with many software and utilities) which can run or be installed on a computer.

# Table of Contents

1. [Getting started](#GettingStarted)
2. [Distributions](#Distributions)

# Getting Started <a name="GettingStarted"></a>

In order to get familiar with Linux one must have access to a Linux distribution to work on. Due to the fact that there are many distributions available many users find it difficult to chose one distribution over the other. Each Linux distribution has its own [package manager](http://en.wikipedia.org/wiki/Package_manager) and utilities for handling the way software is installed/removed/updated.

# Distributions

[Debian](http://debian.org/) It is the base distribution for Ubuntu, Linux Mint, Knoppix, etc. It uses [dpkg](https://en.wikipedia.org/wiki/Dpkg) package manager with .deb packages. There are many other .dpkg utilities which make it easy to install software on these Linux distributions. One such utility is [apt-get](https://linux.die.net/man/8/apt-get).

Red-Hat Is a commercial distribution released by Red Hat Inc. It uses the RPM package manager(.rpm). Other distros that use this type of package management include Fedora, CentOS, Oracle Linux. There are also many frontends for .rpm, yum being one of the most popular.

Slackware It is the oldest active Linux distribution, which is mainly a one man project. It uses the slackpkg package manager. Its aim is simplicity and stability; Because of its simplicity there are many distributions derived from it like ZenWalk, VectorLinux and Slax.

Arch Linux It is a distribution using its own package manager named pacman. One particularity of this distribution is that it doesn't have scheduled release but uses the rolling release model. This means that you get the latest software when updating.

<a name="fn1">1</a>: Linux wikipedia page https://en.wikipedia.org/wiki/Linux
