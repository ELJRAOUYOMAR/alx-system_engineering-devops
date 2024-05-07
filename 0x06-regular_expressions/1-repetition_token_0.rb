#!/usr/bin/env ruby
puts ARGV[0].scan(/[a-zA-Z0-9][a-zA-Z0-9]{2,6}[a-zA-Z0-9]/).join
