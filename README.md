Samantha. An RSS reader built with practical Domain-Driven-Design.

#### Installation

This guide assumes OSX, but can be adapted for different platforms accordingly.

First, we'll need [Virtualbox](https://www.virtualbox.org) & [Vagrant](http://www.vagrantup.com). This is a must for Mac users because Docker uses Linux-specific, so we will be running Docker from within a VM. The following commands assume [homebrew](http://brew.sh) & [cask](http://caskroom.io/) are installed and will get us taken care of from the command line:

```
$ brew cask install virtualbox
$ vboxmanage --version
> 4.3.12r93733

$ brew cask install vagrant
$ vagrant --version
> Vagrant 1.6.3
```

Once that is done run the following commands to install [Docker](http://docker.com/).

```
$ curl https://raw.githubusercontent.com/noplay/docker-osx/1.1.1/docker-osx > /usr/local/bin/docker-osx
$ chmod +x /usr/local/bin/docker-osx
$ docker-osx vagrant up --provision --provider virtualbox
$ docker --version
> Docker version 1.1.1, build bd609d2
```

Now we'll need [fig](fig.sh) to facilitate running the development environment. This too is a breeze. For OSX, run the following commands or check out the installation guide on [fig.sh](http://fig.sh).

```
$ curl -L https://github.com/docker/fig/releases/download/0.5.2/darwin > /usr/local/bin/fig
$ chmod +x /usr/local/bin/fig
$ fig --version
> fig 0.5.2
```

Great. You should be able to run Samantha now. Let's give that a shot by running `fig up` on our machine. On OSX, you'll need to enable the `docker-osx shell` first in order to enable docker running in a virtualmachine.

```

$ docker-osx shell
$ fig up
```

The above commands will first download a virtualmachine that docker will be ran in, and then download all the container parts needed to run the application. This is mostly a one time deal. Once that is finished, you should be able to travel to [http://localdocker:5000/](http://localdocker:5000/) in your browser to see the application.

Cheers!