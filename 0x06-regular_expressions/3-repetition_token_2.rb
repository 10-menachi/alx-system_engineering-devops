#!/usr/bin/env ruby
# The regular expression must match hbtn whereby the letter t can be present zero or more times.
puts ARGV[0].scan(/hbt+n/).join