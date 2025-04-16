---
title: 【Tech】 Nginx tutorial
category: unknown
tags: technology
comments: true
date: 2015-04-30 00:00:00
---


# Overview

nginx [engine x] is __an HTTP and reverse proxy server__, a mail proxy server, and a generic TCP proxy server. 

For a long time, it has been running on many heavily loaded Russian sites, and recently, Netflix, Wordpress.com. 

Ref: [nginx](http://nginx.org/en/)

__nginx has one master process and several worker processes__. The main purpose of the master process is to read and evaluate configuration, and maintain worker processes. Worker processes do actual processing of requests. 

# Basics

## start nginx

    nginx

## stop nginx

    nginx -s signal

signal: 

1. stop — fast shutdown

1. quit — graceful shutdown

1. reload — reloading the configuration file

1. reopen — reopening the log files

## List of running nginx process

    ps -ax | grep nginx

# config file： nginx.conf

__nginx.conf__

By default, the configuration file is placed in __/etc/nginx__. (If not, check /usr/local/nginx/conf, or /usr/local/etc/nginx.)

## first part

```
	user www-data;
	worker_processes 4;
	pid /run/nginx.pid;
	
	events {
		worker_connections 768;
		# multi_accept on;
	}
```

1. user

	Defines which Linux system user will own and run the Nginx server. Most Debian-based distributions use www-data

	In case you run two simultaneous web servers, or need another program’s user to have control over Nginx, you can play with it.

1. worker_process

	Defines how many threads, or simultaneous instances, of Nginx to run. 

1. pid

	Defines where Nginx will write its master process ID, or PID. 
	
	> On my machine, the file /run/nginx.pid store a single number 724. 

## http part

```
	http {
	
		##
		# Basic Settings
		##
	
		sendfile on;
		tcp_nopush on;
		tcp_nodelay on;
		keepalive_timeout 65;
		types_hash_max_size 2048;
		# server_tokens off;
	
		# server_names_hash_bucket_size 64;
		# server_name_in_redirect off;
	
		include /etc/nginx/mime.types;
		default_type application/octet-stream;
	
		##
		# Logging Settings
		##
	
		access_log /var/log/nginx/access.log;
		error_log /var/log/nginx/error.log;
	
		##
		# Gzip Settings
		##
	
		gzip on;
		gzip_disable "msie6";
	
		# gzip_vary on;
		# gzip_proxied any;
		# gzip_comp_level 6;
		# gzip_buffers 16 8k;
		# gzip_http_version 1.1;
		# gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;
	
		##
		# nginx-naxsi config
		##
		# Uncomment it if you installed nginx-naxsi
		##
	
		#include /etc/nginx/naxsi_core.rules;
	
		##
		# nginx-passenger config
		##
		# Uncomment it if you installed nginx-passenger
		##
		
		#passenger_root /usr;
		#passenger_ruby /usr/bin/ruby;
	
		##
		# Virtual Host Configs
		##
	
		include /etc/nginx/conf.d/*.conf;
		include /etc/nginx/sites-enabled/*;
	}
```

Note: The HTTP block of the nginx.conf file contains the statement include __/etc/nginx/sites-enabled/*;__. This allows for server block configurations to be loaded in from separate files found in __the sites-enabled sub-directory__. 

Usually these are __symlinks to files stored in /etc/nginx/sites-available/__. By using symlinks you can quickly enable or disable a virtual server while preserving its configuration file. 

# config file for sites

## sites-available

__/etc/nginx/sites-available/default__ is a template provided for you. 

```
	server {
	        listen 80 default_server;
	        listen [::]:80 default_server ipv6only=on;
	
	        root /usr/share/nginx/html;
	        index index.html index.htm;
	
	        # Make site accessible from http://localhost/
	        server_name localhost;
	
	        location / {
	                # First attempt to serve request as file, then
	                # as directory, then fall back to displaying a 404.
	                try_files $uri $uri/ /index.html;
	                # Uncomment to enable naxsi on this location
	                # include /etc/nginx/naxsi.rules
	        }
	}
```

__Do not modify this file__. Generally, you’ll want to make a separate file with its own server block for each virtual domain on your server.  So do: 

    cp /etc/nginx/sites-available/default /etc/nginx/sites-available/example.com

## listen directive

```
	listen 80 default_server;
	listen [::]:80 default_server ipv6only=on;
```

The argument __default_server__ means this virtual host will answer requests on port 80 that don’t match any other virtual host’s listen statement. 

The second statement listens over IPv6 and behaves in the same way.

```
	listen     127.0.0.1:80;
	listen     localhost:80;
```

Note: localhost is conventionally set as the hostname for 127.0.0.1 in /etc/hosts.

```
	listen     80;
	listen     *:80;
```

This will listen on all domains and IP addresses on port 80. __listen 80;__ is equivalent to __listen *:80;__

```
	listen     12.34.56.77:80;
	listen     12.34.56.78:80;
	listen     12.34.56.79:80;       
	listen     12.34.56.79:8080;   
```    

This will listen on multiple IP/port. 

## server_name directive

Common:

	server_name   example.com;

Or

	server_name   example.com www.example.com;

Now this:

```
	server_name   *.example.com;
	server_name   .example.com;
```

will listen to all subdomains of example.com, including www.example.com, foo.example.com, etc. __Both equivalent__.

	server_name   "";

If you set server_name to the empty quote set (”“), Nginx will process __all requests that either__ do not have a hostname, __or__ that have an unspecified hostname, such as requests for the IP address itself.

## location directive

__location__ setting lets you configure how Nginx will respond to requests for resources within the server.

eg. 

```
	location / { } 
	location /images/ { } 
	location /blog/ { } 
	location /planet/ { } 
	location /planet/blog/ { }
```

The location can set actual path in the file system (that is under /etc/nginx/ folder). Or we can also set __proxy_pass__ directive. 

Ref 1: [nginx Beginner’s Guide](http://nginx.org/en/docs/beginners_guide.html)


Ref 2: [Basic Nginx Configuration by Linode](https://www.linode.com/docs/websites/nginx/basic-nginx-configuration#location-root-and-index)
