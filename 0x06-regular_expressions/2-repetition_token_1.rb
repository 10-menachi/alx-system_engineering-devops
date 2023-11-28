#!/usr/bin/env ruby
# The regular expression must match hbtn whereby
# there is either b or t between `h` and `n` in the string.
puts ARGV[0].scan(/hb?tn/).join