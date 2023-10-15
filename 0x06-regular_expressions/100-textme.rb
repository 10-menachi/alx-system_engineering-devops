#!/usr/bin/env ruby

#This script outputs [SENDER],[RECEIVER],[FLAGS] from a text file

puts ARGV[0].scan(/(?<=from:|to:|flags:)[^\]]*/).join(",")