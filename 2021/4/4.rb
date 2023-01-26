class Board
  def initialize
    @rows = []
    @cols = Array.new(5) { Set.new }
  end

  def add_row(row)
    @rows << row.to_set
    row.each_with_index do |el, idx|
      @cols[idx] << el
    end
  end

  def remove_guess(guess)
    @rows.each { |r| r.delete(guess) }
    @cols.each { |c| c.delete(guess) }
  end

  def bingo?
    @rows.any?(&:empty?) or @cols.any?(&:empty?)
  end

  def sum_nums
    @rows.map(&:sum).sum
  end
end

input_file = File.open("4.in")
guesses = input_file.readline.chomp.split(",").map(&:to_i)
boards = []
while input_file.gets
  boards << Board.new
  5.times do
    row = input_file.readline.chomp.split.map(&:to_i)
    boards.last.add_row row
  end
end
input_file.close

guess = nil
done = false
until done
  guess = guesses.shift
  puts "Guess: #{guess}"
  boards.each do |board|
    board.remove_guess(guess)
    if board.bingo?
      puts board.sum_nums * guess
      done = true
      break
    end
  end
end


# Task 2
input_file = File.open("4.in")
guesses = input_file.readline.chomp.split(",").map(&:to_i)
boards = []
while input_file.gets
  boards << Board.new
  5.times do
    row = input_file.readline.chomp.split.map(&:to_i)
    boards.last.add_row row
  end
end
input_file.close


guess = nil
done = false
while boards.size > 1
  guess = guesses.shift
  puts "Guess: #{guess}"
  boards.each { |b| b.remove_guess(guess) }
  boards.reject!(&:bingo?)
end
board = boards.first
until board.bingo?
  guess = guesses.shift
  board.remove_guess(guess)
end
puts boards.first.sum_nums * guess
