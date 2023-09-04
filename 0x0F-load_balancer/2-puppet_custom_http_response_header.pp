# Use Puppet to automate the task of creating a custom HTTP header response.

package { 'nginx':
    ensure   => 'installed',
    provider => 'apt',
}

exec {'100 allow nginx':
    command => '/usr/sbin/ufw allow "Nginx HTTP"'
}

exec { 'http header':
    command => '/usr/bin/sed -i "s/http {/http {\n\tadd_header X-Served-By $(hostname);/" /etc/nginx/nginx.conf',
}

exec { 'run':
  command => '/usr/sbin/service nginx restart',
}
