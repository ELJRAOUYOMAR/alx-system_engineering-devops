# installs puppet-lint package(flask)

package {'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
