Samantha. An RSS reader built with practical Domain-Driven-Design.

#### Installation

If you're using OSX, then you'll need to install [Virtualbox](https://www.virtualbox.org/wiki/Downloads) & [Vagrant](http://www.vagrantup.com/downloads.html); Docker uses Linux-specific kernal features, so this is a must for Mac users.

You'll then need [docker](docker.com) to run the provided containers. Luckily, this is easy to install. For OSX, run the following commands or check out the installation guide on [docker.com](http://docker.com).

```
$ curl https://raw.githubusercontent.com/noplay/docker-osx/1.1.1/docker-osx > /usr/local/bin/docker-osx
$ chmod +x /usr/local/bin/docker-osx
$ docker-osx shell
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

The above commands will first download a virtualmachine that docker will be ran in, and then download all the container parts needed to run the application. This is mostly a one time deal. Once that is finished, you should be able to travel to http://localdocker:5000/ in your browser to see the application.

Cheers!