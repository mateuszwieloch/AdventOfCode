nums = File.readlines("./1example.in").map(&:chomp).map(&:to_i)

# Task 1
result = 0
nums.each_cons(2) do |a, b|
  result += 1 if b > a
end
puts result

# Task 2
result = 0
prev = nums[0..2].sum
nums.each_cons(3) do |window|
  result += 1 if window.sum > prev
  prev = window.sum
end
puts result
