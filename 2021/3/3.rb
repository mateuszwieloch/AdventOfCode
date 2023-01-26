lines = File.readlines("3.in").map(&:strip)

gamma = ""  # most common bit
epsilon = ""  # least common bit
0.upto(lines[0].size-1) do |bit|
  zeros = 0
  ones = 0

  lines.each do |line|
    if line[bit] == "0"
      zeros += 1
    else
      ones += 1
    end
  end

  if zeros > ones
    gamma += "0"
    epsilon += "1"
  else
    gamma += "1"
    epsilon += "0"
  end
end
puts gamma.to_i(2) * epsilon.to_i(2)


# Task 2
bit = 0
remaining_lines = lines.clone
until remaining_lines.size == 1
  zeros = 0
  ones = 0

  remaining_lines.each do |line|
    if line[bit] == "0"
      zeros += 1
    else
      ones += 1
    end
  end

  if zeros > ones
    remaining_lines.filter! { |x| x[bit] == "0" }
  else
    remaining_lines.filter! { |x| x[bit] == "1" }
  end
  bit += 1
end
oxygen_level = remaining_lines[0].to_i(2)

bit = 0
remaining_lines = lines.clone
until remaining_lines.size == 1
  zeros = 0
  ones = 0

  remaining_lines.each do |line|
    if line[bit] == "0"
      zeros += 1
    else
      ones += 1
    end
  end

  if zeros <= ones
    remaining_lines.filter! { |x| x[bit] == "0" }
  else
    remaining_lines.filter! { |x| x[bit] == "1" }
  end
  bit += 1
end
co2_level = remaining_lines[0].to_i(2)

puts oxygen_level * co2_level
