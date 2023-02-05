def task1(nums)
  s = nums.to_set
  nums.each do |n|
    return n*(2020-n) if s.include?(2020-n)
  end
  -1
end

nums = File.readlines("1.in").map(&:to_i)
puts "Task 1 result: #{task1(nums)}"

def task2(nums)
  s = nums.to_set
  nums.combination(2) do |a, b|
    return a*b*(2020-a-b) if s.include?(2020-a-b)
  end
  -1
end
puts "Task 2 result: #{task2(nums)}"
