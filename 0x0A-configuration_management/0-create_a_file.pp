# create temp file
file { 'temporary file':
     path    => '/tmp/holberton',
     ensure  => 'present',
     mode    => '0744',
     group   => 'www-data',
     owner   => 'www-data',
     content => 'I love Puppet',
     }