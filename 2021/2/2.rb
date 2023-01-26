lines = File.readlines("2.in")

hor = 0
depth = 0
lines.map(&:chomp).each do |line|
  dir, dist = line.split
  dist = dist.to_i
  hor += dist   if dir == "forward"
  depth -= dist if dir == "up"
  depth += dist if dir == "down"
end
puts hor*depth


# Task 2
aim = 0
hor = 0
depth = 0
lines.map(&:chomp).each do |line|
  dir, dist = line.split
  dist = dist.to_i

  aim += dist if dir == "down"
  aim -= dist if dir == "up"

  if dir == "forward"
    hor += dist
    depth += aim * dist
  end
end
puts hor*depth
