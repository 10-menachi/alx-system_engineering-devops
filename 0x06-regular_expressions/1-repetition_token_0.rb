#!/usr/bin/env ruby
# The regular expression must match hbtn whereby the letter t is repeated at least 2 times and at most 5 times
puts ARGV[0].scan(/hb{2,5}tn/).join
