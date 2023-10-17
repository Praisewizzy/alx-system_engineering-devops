ncreases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the nginx config file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart nginx
exec { 'restart-nginx':
  command => 'sudo service nginx restart',
  path    => ['/usr/local/bin/', '/bin/', '/usr/bin/'],
}
