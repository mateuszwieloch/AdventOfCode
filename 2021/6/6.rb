fish = File.read("6.in").chomp.split(",").map(&:to_i)
fish_grouped = fish.tally
fish_grouped.default = 0
256.times do |day|
  new_fish = fish_grouped[0]
  1.upto(8) do |i|
    fish_grouped[i-1] = fish_grouped[i]
  end
  fish_grouped[6] += new_fish
  fish_grouped[8] = new_fish
  if day == 79 || day == 255
    puts "Flock size after #{day+1} days: #{fish_grouped.values.sum}"
  end
end
