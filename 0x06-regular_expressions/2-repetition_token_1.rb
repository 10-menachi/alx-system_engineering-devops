#!/usr/bin/env ruby
# The regular expression must match hbtn whereby the letter t can be present zero or one times.
puts ARGV[0].scan(/hb?tn/).join