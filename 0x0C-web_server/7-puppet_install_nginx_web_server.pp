# Using Puppet,  install and configure an Nginx server
#Nginx should be listening on port 80
#When querying Nginx at its root / with a GET request (requesting a page)
#   using curl, it must return a page that contains the string Hello World!
#The redirection must be a “301 Moved Permanently”

package { 'nginx':
    ensure   => 'installed',
    provider => 'apt',
}

exec { 'install':
    command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx',
    provider => shell,
}

file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
}

file_line { 'redirect /redirect_me':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    match  => 'server_name _;',
    line   => [
    'server_name _;',
    'location /redirect_me {',
    "return 301 'https':#bolexzy.hashnode.dev/;",
    '}',
  ],
}

service {'nginx':
    ensure => running,
    enable => true,
}
