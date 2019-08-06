# create temp file
file { 'temporary file':
  ensure  => 'present',
  path    => '/tmp/holberton',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
}