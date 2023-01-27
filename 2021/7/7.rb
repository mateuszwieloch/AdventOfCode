positions = File.read("7.in").chomp.split(",").map(&:to_i)
positions.sort!
align_to = positions[positions.size / 2]
fuel = 0
positions.each { |p| fuel += (align_to-p).abs }
puts "Fuel needed: #{fuel}"


# Task 2
positions = File.read("7.in").chomp.split(",").map(&:to_i)
min, max = positions.minmax

minfuel = 999_999_999_999_999

min.upto(max) do |i|
  fuel = 0
  positions.each do |p|
    dist = (p-i).abs
    fuel += dist*(1+dist)/2
  end
  minfuel = fuel if fuel < minfuel
end

puts minfuel
